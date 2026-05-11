#!/usr/bin/env python3
"""
UGC Creative Brief Generator
============================

Genere un brief tournage Markdown pret a envoyer a une creatrice UGC 45+.
Calibre pour Meta Ads, audience femmes 45-70.

Usage interactif :
    python3 tools/ugc_brief_generator.py

Usage scripte :
    python3 tools/ugc_brief_generator.py \
        --product "Patch anti-douleur dos" \
        --price 29.90 \
        --angle "douleur" \
        --out brief_patch.md
"""

from __future__ import annotations
import argparse
import datetime as dt
from pathlib import Path


ANGLES = {
    "douleur": {
        "pain": "douleurs chroniques (dos, genoux, articulations)",
        "hooks": [
            "Ma kine m'a dit : 'Si vous aviez su ca plus tot...'",
            "J'ai arrete les anti-inflammatoires en 4 jours.",
            "62 ans, je marche enfin sans grimacer.",
        ],
        "shots": [
            "Plan 0-2s : visage de la creatrice, grimace de douleur, main sur la zone.",
            "Plan 2-5s : voix-off + texte 'Ca a change ma vie' grosse police.",
            "Plan 5-10s : demo produit pose / utilisation (close-up).",
            "Plan 10-20s : temoignage face camera, 1 phrase claire.",
            "Plan 20-25s : retour visage detendu, sourire, levee de poids.",
            "Plan 25-30s : CTA 'Disponible aujourd'hui sur [marque].fr'",
        ],
    },
    "jeunesse": {
        "pain": "rides, paupieres tombantes, peau qui se relache",
        "hooks": [
            "Effet en 2 minutes - camera qui ne ment pas.",
            "Ma fille m'a demande si j'avais fait du Botox.",
            "A 58 ans, c'est la 1re fois que je vois une difference.",
        ],
        "shots": [
            "Plan 0-2s : visage NU sans maquillage, lumiere naturelle, close-up rides.",
            "Plan 2-4s : application produit time-lapse cote A du visage.",
            "Plan 4-8s : avant/apres SPLIT SCREEN cote A vs cote B.",
            "Plan 8-15s : voix-off raconte la decouverte du produit.",
            "Plan 15-22s : temoignage face camera, regard direct.",
            "Plan 22-28s : 2e application + sourire confiant.",
            "Plan 28-30s : CTA 'Lien dans la bio' / 'Cliquez ici'.",
        ],
    },
    "energie": {
        "pain": "fatigue, manque d'energie, humeur en baisse",
        "hooks": [
            "Je me reveille avant le reveil maintenant.",
            "Ma petite-fille n'arrive plus a me suivre.",
            "Plus de coup de barre a 15h.",
        ],
        "shots": [
            "Plan 0-2s : reveil difficile, baillements, fatigue.",
            "Plan 2-5s : prise du produit avec cafe / petit-dej.",
            "Plan 5-12s : journee active - jardin, courses, balade.",
            "Plan 12-20s : temoignage 'avant je...' face camera.",
            "Plan 20-25s : retour energique en fin de journee.",
            "Plan 25-30s : CTA.",
        ],
    },
    "confort": {
        "pain": "inconfort au quotidien (pieds, vetements, sommeil)",
        "hooks": [
            "J'ai marche 8h hier. Zero douleur. A 62 ans.",
            "Premiere nuit complete depuis 3 ans.",
            "Comme marcher sur un nuage.",
        ],
        "shots": [
            "Plan 0-2s : la creatrice montre l'inconfort (frotte pieds, masse dos).",
            "Plan 2-6s : demo produit + mise en place.",
            "Plan 6-15s : scene de vie reelle (marche, sieste, journee).",
            "Plan 15-22s : temoignage detaille.",
            "Plan 22-28s : comparatif visuel (gros plan).",
            "Plan 28-30s : CTA.",
        ],
    },
    "apparence": {
        "pain": "perte de confiance face au miroir, photos ratees",
        "hooks": [
            "Je me suis vue de profil sur une photo... j'ai pleure.",
            "Comme si j'avais 20 ans de moins - sans chirurgie.",
            "Mon mari m'a redit 'tu es belle' apres 15 ans.",
        ],
        "shots": [
            "Plan 0-2s : creatrice devant miroir, regard critique.",
            "Plan 2-5s : decouverte produit.",
            "Plan 5-12s : essai / application + reactions.",
            "Plan 12-20s : essayage tenue / sortie avec amies.",
            "Plan 20-28s : temoignage emotionnel.",
            "Plan 28-30s : CTA.",
        ],
    },
}

DEFAULT_ANGLE = "douleur"


def render_brief(
    product: str,
    price: float,
    angle: str,
    target: str,
    extra_notes: str = "",
) -> str:
    angle = angle.lower().strip()
    a = ANGLES.get(angle, ANGLES[DEFAULT_ANGLE])
    today = dt.date.today().isoformat()

    hooks_md = "\n".join(f"  {i+1}. \"{h}\"" for i, h in enumerate(a["hooks"]))
    shots_md = "\n".join(f"- {s}" for s in a["shots"])

    return f"""# BRIEF UGC — {product}

**Date brief :** {today}
**Produit :** {product}
**Prix de vente :** {price:.2f} EUR
**Angle marketing :** {angle.upper()}
**Audience cible :** {target}

---

## OBJECTIF
Creer une video UGC verticale (9:16) de **25 a 30 secondes** pour Facebook Feed,
Reels et Stories. Sortie : MP4 1080x1920, sans logo de plateforme.

## PROFIL CREATRICE
- Femme, **48-65 ans**
- Apparence naturelle (peu ou pas de maquillage lourd)
- Voix posee, debit lent, francais clair
- Cadre tournage : interieur cosy, lumiere du jour fenetre, ou exterieur calme
- **PAS de fond studio**, on veut "real life"

## DOULEUR / EMOTION A INCARNER
{a['pain']}

## HOOKS POSSIBLES (choisir ou adapter UNE phrase pour le plan d'ouverture)
{hooks_md}

> La phrase doit etre dite **dans les 1,5 premieres secondes**. C'est ce qui stoppe le scroll.

## SCENARIO PLAN PAR PLAN
{shots_md}

## REGLES TECHNIQUES (obligatoires)
- **Format** : vertical 9:16, 1080x1920
- **Duree** : 25-30 secondes max
- **Son** : voix claire, **PAS de musique de fond forte** (couvre la voix)
- **Sous-titres** : a brûler en dur (audience FB regarde sans son)
  - Police grosse, sans-serif, blanc avec contour noir
  - Position : tiers inferieur
- **Pas de filtres** Instagram qui lissent le visage
- **Pas de transitions** flashy : on veut "vrai temoignage"

## A ABSOLUMENT EVITER (compliance Meta + qualite)
- Pas de avant/apres CORPOREL agressif (interdit Meta)
- Pas de "vous avez mal au dos ?" en accusatoire
- Pas de "a votre age" / "vieille"
- Pas de claims medicaux ("guerit", "remplace votre medicament")
- Pas de pression / culpabilisation

## LANGAGE A UTILISER
- "Pour celles qui veulent..."
- "Retrouver..."
- "Profiter de..."
- "Je me sens..."
- "J'ai redecouvert..."

## LIVRABLES ATTENDUS
1. **3 hooks differents** filmes (versions 1, 2, 3) de la 1re phrase + 1er plan
2. **1 video complete** de 25-30s
3. **1 version sans CTA** (pour pouvoir A/B tester des CTA differents en montage)
4. **Rushes bruts** (au cas ou on veut re-monter)

## REMUNERATION & DELAI
- Tarif : (a remplir)
- Delai : 5 jours ouvres apres reception du produit
- Droits : usage publicitaire payant Meta + TikTok pendant 12 mois

## NOTES SUPPLEMENTAIRES
{extra_notes if extra_notes else "(aucune)"}

---

**Contact :** (a remplir)
**Reference brief :** UGC-{today.replace('-', '')}-{angle[:3].upper()}
"""


def prompt(label: str, default: str) -> str:
    raw = input(f"  {label} [{default}] : ").strip()
    return raw or default


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--product")
    p.add_argument("--price", type=float)
    p.add_argument("--angle", choices=list(ANGLES.keys()))
    p.add_argument("--target", default="Femmes 45-70 ans, FR, FB/IG")
    p.add_argument("--notes", default="")
    p.add_argument("--out", help="chemin de sortie .md")
    args = p.parse_args()

    if not args.product:
        print()
        print("Generateur de brief UGC - reponds aux questions :")
        print()
        args.product = prompt("Nom du produit", "Patch anti-douleur dos")
        args.price = float(prompt("Prix TTC", "29.90").replace(",", "."))
        print(f"  Angles dispos : {', '.join(ANGLES.keys())}")
        args.angle = prompt("Angle", "douleur")
        args.target = prompt("Audience cible", args.target)
        args.notes = prompt("Notes supplementaires (entree pour skip)", "")

    md = render_brief(
        product=args.product,
        price=args.price or 0.0,
        angle=args.angle or "douleur",
        target=args.target,
        extra_notes=args.notes,
    )

    if args.out:
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"\nBrief ecrit : {args.out}\n")
    else:
        print()
        print(md)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
