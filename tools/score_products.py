#!/usr/bin/env python3
"""
Product Scoring Engine
======================

Lit templates/product_scorecard.csv, calcule le Money Score, classe les produits
en : QUICK WIN / SCALING PLAY / TEST / SKIP, et reecrit le CSV avec le verdict.

Usage :
    python3 tools/score_products.py
    python3 tools/score_products.py --in mes_produits.csv --out scored.csv

Ponderation Money Score (sur 10) :
    emotional_intensity   x 0.20
    facebook_ads_fit      x 0.25
    purchase_impulse      x 0.20
    profit_potential      x 0.20
    (10 - competition)    x 0.15

Bonus traction :
    +0.3 si ad_library_winners_count >= 10
    +0.5 si running_days_max >= 180 (winner confirme)
    +0.2 si supplier_price_eur * 3 <= sale_price_eur (marge x3+)
"""

from __future__ import annotations
import argparse
import csv
from pathlib import Path


def to_float(v: str, default: float = 0.0) -> float:
    try:
        return float(str(v).replace(",", ".").strip())
    except (ValueError, AttributeError):
        return default


def to_int(v: str, default: int = 0) -> int:
    try:
        return int(float(str(v).replace(",", ".").strip()))
    except (ValueError, AttributeError):
        return default


def score_row(row: dict) -> tuple[float, str]:
    ei = to_float(row.get("emotional_intensity_0_10"))
    fb = to_float(row.get("facebook_ads_fit_0_10"))
    pi = to_float(row.get("purchase_impulse_0_10"))
    co = to_float(row.get("competition_level_0_10"))
    pp = to_float(row.get("profit_potential_0_10"))

    base = (
        ei * 0.20
        + fb * 0.25
        + pi * 0.20
        + pp * 0.20
        + (10 - co) * 0.15
    )

    bonus = 0.0
    winners = to_int(row.get("ad_library_winners_count"))
    if winners >= 10:
        bonus += 0.3
    days = to_int(row.get("running_days_max"))
    if days >= 180:
        bonus += 0.5

    sale = to_float(row.get("sale_price_eur"))
    supplier = to_float(row.get("supplier_price_eur"))
    if supplier > 0 and sale >= supplier * 3:
        bonus += 0.2

    score = min(10.0, base + bonus)

    if score >= 8.5 and pi >= 8 and co <= 7:
        verdict = "QUICK WIN"
    elif score >= 8.0 and pp >= 8:
        verdict = "SCALING PLAY"
    elif score >= 7.0:
        verdict = "TEST"
    else:
        verdict = "SKIP"

    return round(score, 2), verdict


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="inp", default="templates/product_scorecard.csv")
    p.add_argument("--out", default="templates/product_scorecard_scored.csv")
    args = p.parse_args()

    src = Path(args.inp)
    if not src.exists():
        print(f"Fichier introuvable : {src}")
        return 1

    with src.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    for col in ("money_score", "verdict"):
        if col not in fieldnames:
            fieldnames.append(col)

    for row in rows:
        score, verdict = score_row(row)
        row["money_score"] = f"{score:.2f}"
        row["verdict"] = verdict

    rows.sort(key=lambda r: to_float(r["money_score"]), reverse=True)

    with Path(args.out).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    print()
    print(f"  {len(rows)} produits scores -> {args.out}")
    print()
    print(f"  {'PRODUIT':<45} {'SCORE':>6}  VERDICT")
    print("  " + "-" * 75)
    for r in rows:
        name = r.get("product_name", "")[:43]
        print(f"  {name:<45} {r['money_score']:>6}  {r['verdict']}")
    print()
    quick = sum(1 for r in rows if r["verdict"] == "QUICK WIN")
    scale = sum(1 for r in rows if r["verdict"] == "SCALING PLAY")
    test = sum(1 for r in rows if r["verdict"] == "TEST")
    skip = sum(1 for r in rows if r["verdict"] == "SKIP")
    print(f"  Quick Wins : {quick}   Scaling : {scale}   Test : {test}   Skip : {skip}")
    print()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
