#!/usr/bin/env python3
"""
Meta Ad Library Scraper
=======================

Genere des URLs ciblees vers Meta Ad Library + extrait les ads d'une page
publique a partir d'un advertiser ou d'un mot-cle.

DEUX MODES :

  1) URL BUILDER (toujours dispo, zero API)
     Genere des liens pre-remplis vers Ad Library, optimises pour le tracking
     de winners (FR, FB+IG, ads actives).

     python3 ad_library_scraper.py url "patch dos" --country FR
     python3 ad_library_scraper.py url --advertiser "Nooro" --country FR

  2) SCRAPER VIA META GRAPH API (token requis)
     Necessite un token developpeur Meta gratuit + l'app "Ad Library API".
     Voir guides/setup_a_z.md section 7 pour obtenir le token.

     export META_AD_LIBRARY_TOKEN="EAAB..."
     python3 ad_library_scraper.py search "collagene" --country FR --limit 50 --out winners.csv

Le mode 1 marche immediatement, le mode 2 demande 10 min de setup.
"""

from __future__ import annotations
import argparse
import csv
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from typing import Iterable


AD_LIBRARY_BASE = "https://www.facebook.com/ads/library/"
API_BASE = "https://graph.facebook.com/v19.0/ads_archive"


def build_url(
    query: str | None = None,
    advertiser: str | None = None,
    country: str = "FR",
    active_only: bool = True,
) -> str:
    params = {
        "active_status": "active" if active_only else "all",
        "ad_type": "all",
        "country": country,
        "media_type": "all",
    }
    if query:
        params["q"] = query
        params["search_type"] = "keyword_unordered"
    if advertiser:
        params["view_all_page_id"] = ""  # facultatif
        params["search_type"] = "page"
        params["q"] = advertiser
    return AD_LIBRARY_BASE + "?" + urllib.parse.urlencode(params)


def api_search(
    token: str,
    query: str,
    country: str = "FR",
    limit: int = 50,
) -> list[dict]:
    fields = ",".join([
        "id",
        "page_name",
        "page_id",
        "ad_creative_bodies",
        "ad_creative_link_titles",
        "ad_creative_link_descriptions",
        "ad_snapshot_url",
        "ad_delivery_start_time",
        "ad_delivery_stop_time",
        "publisher_platforms",
        "languages",
        "estimated_audience_size",
        "currency",
    ])
    params = {
        "search_terms": query,
        "ad_reached_countries": json.dumps([country]),
        "ad_active_status": "ACTIVE",
        "ad_type": "ALL",
        "fields": fields,
        "limit": str(min(limit, 100)),
        "access_token": token,
    }
    url = API_BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "ecom-toolkit/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data.get("data", [])


def ad_running_days(ad: dict) -> int:
    start = ad.get("ad_delivery_start_time")
    if not start:
        return 0
    try:
        start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
    except ValueError:
        return 0
    end_raw = ad.get("ad_delivery_stop_time")
    end_dt = (
        datetime.fromisoformat(end_raw.replace("Z", "+00:00"))
        if end_raw
        else datetime.now(start_dt.tzinfo)
    )
    return max(0, (end_dt - start_dt).days)


def write_csv(rows: Iterable[dict], path: str) -> int:
    rows = list(rows)
    if not rows:
        print("Aucun resultat.", file=sys.stderr)
        return 0
    cols = [
        "running_days",
        "page_name",
        "id",
        "platforms",
        "body",
        "link_title",
        "ad_delivery_start_time",
        "ad_snapshot_url",
    ]
    enriched = []
    for ad in rows:
        bodies = ad.get("ad_creative_bodies") or []
        titles = ad.get("ad_creative_link_titles") or []
        plats = ad.get("publisher_platforms") or []
        enriched.append({
            "running_days": ad_running_days(ad),
            "page_name": ad.get("page_name", ""),
            "id": ad.get("id", ""),
            "platforms": ",".join(plats),
            "body": (bodies[0] if bodies else "").replace("\n", " ")[:280],
            "link_title": (titles[0] if titles else "")[:140],
            "ad_delivery_start_time": ad.get("ad_delivery_start_time", ""),
            "ad_snapshot_url": ad.get("ad_snapshot_url", ""),
        })
    # tri : winners = ads qui tournent depuis longtemps en haut
    enriched.sort(key=lambda r: r["running_days"], reverse=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(enriched)
    return len(enriched)


def cmd_url(args: argparse.Namespace) -> int:
    url = build_url(
        query=args.query,
        advertiser=args.advertiser,
        country=args.country,
        active_only=not args.include_inactive,
    )
    print()
    print("Ouvre cette URL dans ton navigateur :")
    print()
    print(url)
    print()
    print("Astuce media buyer :")
    print("  - tri par 'plus recente' puis scroll pour voir l'anciennete des ads")
    print("  - ads qui tournent depuis 3+ mois = winners valides")
    print("  - clique 'See Ad Details' pour voir le creative complet")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    token = os.environ.get("META_AD_LIBRARY_TOKEN", "").strip()
    if not token:
        print("ERREUR : variable d'env META_AD_LIBRARY_TOKEN absente.", file=sys.stderr)
        print("Voir guides/setup_a_z.md section 7 pour obtenir un token.", file=sys.stderr)
        return 2
    try:
        ads = api_search(token, args.query, args.country, args.limit)
    except Exception as exc:
        print(f"ERREUR API : {exc}", file=sys.stderr)
        return 3
    count = write_csv(ads, args.out)
    print(f"OK : {count} ads ecrites dans {args.out}")
    print("Ouvre le CSV, regarde la colonne 'running_days' :")
    print("  > 90 jours = winner")
    print("  > 180 jours = jackpot, copie l'angle")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Meta Ad Library helper")
    sub = p.add_subparsers(dest="cmd", required=True)

    url_p = sub.add_parser("url", help="genere une URL Ad Library (zero setup)")
    url_p.add_argument("query", nargs="?")
    url_p.add_argument("--advertiser", help="nom de page exact (mode advertiser)")
    url_p.add_argument("--country", default="FR")
    url_p.add_argument("--include-inactive", action="store_true")
    url_p.set_defaults(func=cmd_url)

    s_p = sub.add_parser("search", help="recherche via Graph API (token requis)")
    s_p.add_argument("query")
    s_p.add_argument("--country", default="FR")
    s_p.add_argument("--limit", type=int, default=50)
    s_p.add_argument("--out", default="winners.csv")
    s_p.set_defaults(func=cmd_search)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
