#!/usr/bin/env python3
"""
ROAS / Break-even Calculator — Meta Ads Edition
================================================

A faire AVANT chaque lancement produit. Te dit :
  - ton CPA max acceptable
  - ton ROAS break-even
  - ta marge nette par commande
  - le budget de test recommande

Usage :
    python3 roas_calculator.py

Tu peux aussi le scripter avec --no-prompt et passer des arguments.
"""

from __future__ import annotations
import argparse
import sys
from dataclasses import dataclass


@dataclass
class ProductEconomics:
    sale_price: float        # prix de vente TTC affiche sur la landing
    cogs: float              # cout produit (Aliexpress, fournisseur, etc.)
    shipping_cost: float     # cout d'expedition que TU paies
    shipping_charged: float  # frais de port que tu factures au client (0 si offerts)
    payment_fees_pct: float  # % frais CB/PayPal (Stripe FR ~ 1.5%, PayPal ~ 3.5%)
    vat_pct: float           # TVA applicable (20% France si assujetti)
    return_rate_pct: float   # taux de retour estime (3-8% en moyenne)
    target_margin_pct: float # marge nette visee (apres tout)

    @property
    def revenue_ht(self) -> float:
        gross = self.sale_price + self.shipping_charged
        return gross / (1 + self.vat_pct / 100)

    @property
    def payment_fees(self) -> float:
        return (self.sale_price + self.shipping_charged) * self.payment_fees_pct / 100

    @property
    def cost_per_order(self) -> float:
        # cout total hors pub par commande
        base = self.cogs + self.shipping_cost + self.payment_fees
        # provision retours
        return_loss = base * self.return_rate_pct / 100
        return base + return_loss

    @property
    def gross_profit_before_ads(self) -> float:
        return self.revenue_ht - self.cost_per_order

    @property
    def break_even_cpa(self) -> float:
        """CPA maximum pour ne PAS perdre d'argent (marge = 0)."""
        return self.gross_profit_before_ads

    @property
    def target_cpa(self) -> float:
        """CPA cible pour tenir la marge nette visee."""
        target_profit = self.revenue_ht * self.target_margin_pct / 100
        return self.gross_profit_before_ads - target_profit

    @property
    def break_even_roas(self) -> float:
        if self.break_even_cpa <= 0:
            return float("inf")
        return self.sale_price / self.break_even_cpa

    @property
    def target_roas(self) -> float:
        if self.target_cpa <= 0:
            return float("inf")
        return self.sale_price / self.target_cpa


def recommend_test_budget(eco: ProductEconomics) -> dict:
    """
    Regle media buyer : budget de test = 3x CPA cible minimum par adset.
    On lance 3 adsets en CBO, donc total = 9x CPA cible.
    """
    per_adset = max(eco.target_cpa * 3, 20)  # plancher 20 EUR/jour
    cbo_daily = per_adset * 3
    return {
        "per_adset_daily_eur": round(per_adset, 2),
        "cbo_daily_eur": round(cbo_daily, 2),
        "test_phase_3_days_eur": round(cbo_daily * 3, 2),
        "kill_criteria": (
            "Si apres 2 jours : CPM > 25 EUR ET CTR < 0.8% ET 0 vente -> kill creative."
        ),
        "scale_criteria": (
            "Si ROAS J3 >= target ROAS x 1.2 -> duplique le winning adset +50% budget toutes les 48h."
        ),
    }


def color(s: str, code: str) -> str:
    return f"\033[{code}m{s}\033[0m"


def print_report(eco: ProductEconomics) -> None:
    print()
    print(color("=" * 60, "1;36"))
    print(color("  ROAS / BREAK-EVEN REPORT", "1;36"))
    print(color("=" * 60, "1;36"))
    print()
    print(f"  Prix de vente TTC         : {eco.sale_price:>8.2f} EUR")
    print(f"  + Frais de port factures  : {eco.shipping_charged:>8.2f} EUR")
    print(f"  - TVA ({eco.vat_pct:.0f}%)             : -{(eco.sale_price + eco.shipping_charged) - eco.revenue_ht:>7.2f} EUR")
    print(f"  = CA HT par commande      : {eco.revenue_ht:>8.2f} EUR")
    print()
    print(f"  COGS produit              : {eco.cogs:>8.2f} EUR")
    print(f"  Cout shipping reel        : {eco.shipping_cost:>8.2f} EUR")
    print(f"  Frais paiement ({eco.payment_fees_pct:.1f}%)     : {eco.payment_fees:>8.2f} EUR")
    print(f"  Provision retours ({eco.return_rate_pct:.0f}%)    : {(eco.cost_per_order - eco.cogs - eco.shipping_cost - eco.payment_fees):>8.2f} EUR")
    print(f"  = Cout total / commande   : {eco.cost_per_order:>8.2f} EUR")
    print()
    print(color("  -- MARGES --", "1;33"))
    print(f"  Profit brut avant pub     : {eco.gross_profit_before_ads:>8.2f} EUR")
    print()
    print(color("  -- CPA / ROAS --", "1;33"))
    be_cpa_color = "1;32" if eco.break_even_cpa > 0 else "1;31"
    print(color(f"  CPA break-even            : {eco.break_even_cpa:>8.2f} EUR", be_cpa_color))
    print(color(f"  ROAS break-even           : {eco.break_even_roas:>8.2f} x", be_cpa_color))
    print()
    tg_cpa_color = "1;32" if eco.target_cpa > 0 else "1;31"
    print(color(f"  CPA cible (marge {eco.target_margin_pct:.0f}%)    : {eco.target_cpa:>8.2f} EUR", tg_cpa_color))
    print(color(f"  ROAS cible                : {eco.target_roas:>8.2f} x", tg_cpa_color))
    print()

    if eco.target_cpa < 5:
        print(color("  WARNING : CPA cible < 5 EUR. Tres difficile sur Meta en 2026.", "1;31"))
        print(color("            Augmente le prix, baisse le COGS, ou trouve un produit + cher.", "1;31"))
        print()
    elif eco.target_cpa > 30:
        print(color("  EXCELLENT : CPA cible > 30 EUR. Audience 45+ tres atteignable.", "1;32"))
        print()

    rec = recommend_test_budget(eco)
    print(color("  -- BUDGET DE TEST RECOMMANDE --", "1;33"))
    print(f"  Par adset / jour          : {rec['per_adset_daily_eur']} EUR")
    print(f"  CBO total / jour (3 ads)  : {rec['cbo_daily_eur']} EUR")
    print(f"  Phase test 3 jours        : {rec['test_phase_3_days_eur']} EUR")
    print()
    print(color("  Regles de decision :", "1;33"))
    print(f"    KILL  : {rec['kill_criteria']}")
    print(f"    SCALE : {rec['scale_criteria']}")
    print()
    print(color("=" * 60, "1;36"))
    print()


def prompt_float(label: str, default: float) -> float:
    raw = input(f"  {label} [{default}] : ").strip()
    if not raw:
        return default
    try:
        return float(raw.replace(",", "."))
    except ValueError:
        print("    valeur invalide, on garde le defaut.")
        return default


def interactive() -> ProductEconomics:
    print()
    print(color("ROAS Calculator - rentre tes chiffres (Enter = defaut)", "1;36"))
    print()
    return ProductEconomics(
        sale_price=prompt_float("Prix de vente TTC (EUR)", 49.90),
        cogs=prompt_float("COGS produit (EUR)", 8.0),
        shipping_cost=prompt_float("Cout shipping reel (EUR)", 4.0),
        shipping_charged=prompt_float("Frais de port factures au client (EUR)", 0.0),
        payment_fees_pct=prompt_float("Frais paiement (%)", 2.5),
        vat_pct=prompt_float("TVA (%)", 20.0),
        return_rate_pct=prompt_float("Taux de retour estime (%)", 5.0),
        target_margin_pct=prompt_float("Marge nette visee (%)", 25.0),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="ROAS / break-even calculator")
    parser.add_argument("--sale-price", type=float)
    parser.add_argument("--cogs", type=float)
    parser.add_argument("--shipping-cost", type=float, default=4.0)
    parser.add_argument("--shipping-charged", type=float, default=0.0)
    parser.add_argument("--payment-fees", type=float, default=2.5)
    parser.add_argument("--vat", type=float, default=20.0)
    parser.add_argument("--return-rate", type=float, default=5.0)
    parser.add_argument("--target-margin", type=float, default=25.0)
    args = parser.parse_args()

    if args.sale_price is not None and args.cogs is not None:
        eco = ProductEconomics(
            sale_price=args.sale_price,
            cogs=args.cogs,
            shipping_cost=args.shipping_cost,
            shipping_charged=args.shipping_charged,
            payment_fees_pct=args.payment_fees,
            vat_pct=args.vat,
            return_rate_pct=args.return_rate,
            target_margin_pct=args.target_margin,
        )
    else:
        eco = interactive()

    print_report(eco)
    return 0


if __name__ == "__main__":
    sys.exit(main())
