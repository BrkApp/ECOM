# 🎯 ECOM Toolkit — Meta Ads / Femmes 45+

Boite a outils complete pour lancer un business e-commerce rentable sur Meta Ads,
cible : **femmes 45-70 ans francophones**.

> Tu pars de zero ? Lis [`guides/setup_a_z.md`](guides/setup_a_z.md) en premier.
> **Budget serre (500 EUR) + dropshipping ?** → [`guides/dropshipping_budget_500.md`](guides/dropshipping_budget_500.md)
> **One-shot 500 EUR sur patchs anti-douleur dos ?** → [`guides/playbook_patch_dos_500eur.md`](guides/playbook_patch_dos_500eur.md)
> **Recurrent MRR 500 EUR (subscription collagene 45+) ?** → [`guides/playbook_subscription_collagene_500eur.md`](guides/playbook_subscription_collagene_500eur.md) ⭐ recommande pour profil "no-code + patience + recurrent"

---

## 🗂 Structure du repo

```
ECOM/
├── STRATEGY_FEMMES_45PLUS.md      → strategie produits + angles + scaling
├── README.md                       → ce fichier
├── guides/
│   ├── setup_a_z.md                            → setup complet A a Z (1500 EUR+)
│   ├── dropshipping_budget_500.md              → dropship one-shot 500 EUR
│   ├── playbook_patch_dos_500eur.md            → playbook patchs dos 500 EUR
│   └── playbook_subscription_collagene_500eur.md → MRR collagene 500 EUR (recommande recurrent)
├── tools/                          → scripts Python (zero dependance)
│   ├── roas_calculator.py          → calcule ton CPA max & ROAS break-even
│   ├── ad_library_scraper.py       → trouve les ads winners sur Meta
│   ├── score_products.py           → scorer + classer tes idees produits
│   ├── ugc_brief_generator.py      → genere les briefs de tournage
│   └── ads_dashboard_analyzer.py   → analyse quotidienne des campagnes
└── templates/
    ├── product_scorecard.csv       → tableau de scoring produits
    ├── klaviyo_flows_45plus.md     → sequences email/SMS pretes a copier
    ├── ads_dashboard.csv           → suivi quotidien campagnes
    └── sample_brief_patch.md       → exemple de brief UGC genere
```

---

## ⚡ Demarrage rapide

### Pre-requis
- Python 3.8+ (deja installe sur Mac/Linux)
- Aucune dependance externe — tout est en stdlib

### Cas 1 — Tu cherches encore ton produit
```bash
# 1) lance la recherche d'angle/winners
python3 tools/ad_library_scraper.py url "patch dos chaleur" --country FR

# 2) remplis templates/product_scorecard.csv avec tes candidats
# 3) classe-les
python3 tools/score_products.py
```

### Cas 2 — Tu as un produit, tu veux savoir s'il est rentable
```bash
python3 tools/roas_calculator.py
# remplis interactivement : prix, COGS, shipping, etc.
# tu obtiens : CPA max, ROAS break-even, budget de test recommande
```

### Cas 3 — Tu veux brifer une creatrice UGC
```bash
python3 tools/ugc_brief_generator.py \
    --product "Creme lifting peptides" \
    --price 49.90 \
    --angle jeunesse \
    --out mon_brief.md
```
Angles disponibles : `douleur`, `jeunesse`, `energie`, `confort`, `apparence`.

### Cas 4 — Tu as lance des ads, tu veux le verdict du jour
```bash
# 1) remplis templates/ads_dashboard.csv avec les chiffres du jour
# 2) analyse
python3 tools/ads_dashboard_analyzer.py --target-roas 2.9 --target-cpa 17.28
```
Verdicts auto : `SCALE` / `KEEP` / `WATCH` / `KILL` / `WAIT`.

---

## 🎯 Workflow type (semaine 1)

```
Lundi    : scoring produits (3 candidats) + roas_calculator sur le top 1
Mardi    : commande echantillon fournisseur + setup Shopify
Mercredi : landing page + Klaviyo Welcome/Cart flows
Jeudi    : brief UGC + commande creatrice
Vendredi : Meta Business Manager + Pixel + Domain Verif
Weekend  : finition landing + test parcours complet
Lundi+1  : lancement campagne, dashboard quotidien des le J1
```

---

## 📐 Les regles non-negociables

1. **Toujours** calculer le ROAS break-even AVANT de lancer
2. **Toujours** verifier 10+ advertisers actifs en Ad Library (sinon = pas de marche)
3. **Toujours** commander 1 echantillon avant de scaler
4. **Toujours** activer Klaviyo Welcome + Abandoned Cart en J1
5. **Jamais** scaler un adset avant 48h de spend significatif
6. **Jamais** modifier plus de 3 trucs/jour sur une campagne (casse le learning)

---

## 🤝 Iteration

Tous les outils sont scriptes en Python stdlib pour rester portables.
N'hesite pas a forker / modifier les ponderations dans `score_products.py`
ou les seuils dans `ads_dashboard_analyzer.py` selon ce que tu apprends.

Bon scaling.
