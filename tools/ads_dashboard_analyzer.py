#!/usr/bin/env python3
"""
Daily Ads Dashboard Analyzer
============================

Lit templates/ads_dashboard.csv et applique les regles de decision
automatiques d'un media buyer expert.

Usage :
    python3 tools/ads_dashboard_analyzer.py
    python3 tools/ads_dashboard_analyzer.py --target-roas 2.5 --in templates/ads_dashboard.csv

REGLES (par adset / par jour) :
    KILL  si CPM > 25 EUR ET CTR < 0.8% ET 0 ventes (apres >=24h spend)
    KILL  si depense >= 2x CPA cible ET 0 ventes
    KILL  si ROAS J3+ < 0.5 x target
    WATCH si ROAS entre 0.5x et 1.0x target
    KEEP  si ROAS >= target
    SCALE si ROAS >= 1.2x target ET 3+ ventes (duplique +50% budget)

Le script reecrit la colonne verdict_auto.
"""

from __future__ import annotations
import argparse
import csv
from pathlib import Path


def f(v, d=0.0):
    try:
        return float(str(v).replace(",", ".").strip())
    except (ValueError, AttributeError):
        return d


def i(v, d=0):
    try:
        return int(float(str(v).replace(",", ".").strip()))
    except (ValueError, AttributeError):
        return d


def verdict(row: dict, target_roas: float, target_cpa: float) -> str:
    spend = f(row.get("spend_eur"))
    purchases = i(row.get("purchases"))
    roas = f(row.get("roas"))
    cpm = f(row.get("cpm_eur"))
    ctr = f(row.get("ctr_pct"))
    day_n = i(row.get("day_n"), 1)

    if day_n <= 1 and spend < target_cpa:
        return "WAIT"

    # KILL conditions
    if cpm > 25 and ctr < 0.8 and purchases == 0 and spend >= target_cpa * 0.5:
        return "KILL"
    if spend >= target_cpa * 2 and purchases == 0:
        return "KILL"
    if day_n >= 3 and roas < target_roas * 0.5:
        return "KILL"

    # SCALE conditions
    if roas >= target_roas * 1.2 and purchases >= 3:
        return "SCALE"

    # KEEP
    if roas >= target_roas:
        return "KEEP"

    # WATCH
    if roas >= target_roas * 0.5:
        return "WATCH"

    return "WATCH"


def color_for(v: str) -> str:
    return {
        "KILL": "1;31",
        "WATCH": "1;33",
        "KEEP": "1;32",
        "SCALE": "1;36",
        "WAIT": "0;37",
    }.get(v, "0")


def colorize(s: str, code: str) -> str:
    return f"\033[{code}m{s}\033[0m"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="inp", default="templates/ads_dashboard.csv")
    p.add_argument("--out", default="templates/ads_dashboard_analyzed.csv")
    p.add_argument("--target-roas", type=float, default=2.5,
                   help="ROAS cible (sortie du roas_calculator.py)")
    p.add_argument("--target-cpa", type=float, default=20.0,
                   help="CPA cible en EUR (sortie du roas_calculator.py)")
    args = p.parse_args()

    src = Path(args.inp)
    if not src.exists():
        print(f"Fichier introuvable : {src}")
        return 1

    with src.open() as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        fns = list(reader.fieldnames or [])

    if "verdict_auto" not in fns:
        fns.append("verdict_auto")

    for row in rows:
        row["verdict_auto"] = verdict(row, args.target_roas, args.target_cpa)

    rows.sort(key=lambda r: f(r.get("roas")), reverse=True)

    with Path(args.out).open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fns)
        w.writeheader()
        w.writerows(rows)

    print()
    print(f"  Target ROAS : {args.target_roas} | Target CPA : {args.target_cpa:.2f} EUR")
    print()
    print(f"  {'CAMPAGNE/ADSET':<35} {'SPEND':>8} {'ROAS':>6} {'CPA':>7} {'CTR':>6}  VERDICT")
    print("  " + "-" * 85)
    for r in rows:
        name = f"{r.get('adset_name', '')[:33]:<35}"
        v = r["verdict_auto"]
        line = (
            f"  {name} "
            f"{f(r.get('spend_eur')):>7.2f}E "
            f"{f(r.get('roas')):>5.2f}x "
            f"{f(r.get('cpa_eur')):>6.2f}E "
            f"{f(r.get('ctr_pct')):>5.2f}%"
        )
        print(line + "  " + colorize(v, color_for(v)))
    print()

    counts = {}
    for r in rows:
        counts[r["verdict_auto"]] = counts.get(r["verdict_auto"], 0) + 1
    summary = "  " + "   ".join(f"{k}: {v}" for k, v in sorted(counts.items()))
    print(summary)
    print()
    print(f"  Resultat ecrit : {args.out}")
    print()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
