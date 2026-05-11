# SETUP A-Z — De zero a ta premiere vente Meta Ads
**Public :** quelqu'un qui n'a rien (pas de Shopify, pas de Meta Business, pas de fournisseur).
**Duree :** 7 a 10 jours.
**Budget initial minimum :** 800 a 1500 EUR (300-500 setup + 500-1000 ads test).

---

## ORDRE D'EXECUTION

```
J1-J2  : choisir produit + valider rentabilite           (gratuit)
J3     : Shopify + nom de domaine + Stripe/PayPal        (~50 EUR)
J4     : fournisseur + import produit                    (~50-200 EUR commande test)
J5     : landing page + emails Klaviyo                   (gratuit)
J6     : Meta Business Manager + Pixel + Domain Verif    (gratuit)
J7     : brief UGC + tournage rapide ou stock UGC        (50-150 EUR par UGC)
J8     : 1re campagne Meta Ads                           (test 150 EUR/j x 3 jours)
J9-J10 : ajustements
```

---

## 1) CHOISIR UN PRODUIT (J1)

### Recherche
- Ouvre `STRATEGY_FEMMES_45PLUS.md` (a la racine) → liste de 25 produits ranges
- Pour chaque produit qui t'attire, ouvre la Meta Ad Library :
  ```bash
  python3 tools/ad_library_scraper.py url "patch dos chaleur" --country FR
  ```
- Verifie : **>=10 advertisers actifs** + au moins **3 ads >180 jours** = produit valide

### Validation
- Remplis `templates/product_scorecard.csv` avec 3-5 candidats
- Lance :
  ```bash
  python3 tools/score_products.py
  ```
- Garde ceux avec Money Score >= 8.5 → ce sont tes Quick Wins

### Validation eco
```bash
python3 tools/roas_calculator.py
```
Si CPA cible < 10 EUR → produit trop bon marche, change.
Si ROAS cible > 4x → tu vas galerer, change.
**Sweet spot 45+ : CPA cible 15-25 EUR, ROAS cible 2.2-3.0x.**

---

## 2) SHOPIFY (J3)

### Comptes a creer
1. **Shopify** : trial 3 jours puis 1 EUR/mois 3 mois → shopify.com
2. **Nom de domaine** : achete sur Namecheap ou OVH (~10 EUR/an). Nom court, .fr ou .com.
3. **Stripe FR** : stripe.com → comptes pro acceptes en 24h
4. **PayPal Business** : paypal.com/business → essentiel pour +15% conversion sur 45+

### Theme Shopify recommande
- **Dawn** (gratuit, suffit largement pour debuter)
- Police LISIBLE : Inter 18px / titre 28px. Pas de fontaisies cursives.
- Boutons CTA contraste fort. Texte noir sur fond clair.

### Apps Shopify minimum
| App | Usage | Cout |
|-----|-------|------|
| Klaviyo Email | flows email/SMS | gratuit < 250 contacts |
| ReConvert | upsell post-achat | 5 EUR/mois |
| Loox ou Judge.me | reviews photos | 10-20 EUR/mois |
| TrackingMore | suivi colis | gratuit a 9 EUR/mois |

### Mentions legales (NON NEGOCIABLE en FR)
- CGV
- Mentions legales (nom, SIRET, adresse)
- Politique de confidentialite RGPD
- Politique de retours (mets en avant la garantie 30j)
- → templates gratuits chez ShopifyFR ou copie d'un concurrent serieux

---

## 3) FOURNISSEUR (J4)

### Options (par ordre de qualite)
1. **Marque FR / locale** (Etsy, Ankorstore, salons) : meilleur, mais cher et lent
2. **Fournisseur dropship FR / EU** : Spocket (Europe), Ankorstore wholesale
3. **CJ Dropshipping** : meilleur compromis qualite/prix Chine, livraison 8-12j
4. **Zendrop** : similaire CJ, interface plus simple
5. **AliExpress direct** : OK pour tester 1 mois, mais delais 15-25j → mauvais NPS

### Regle d'or
- **COMMANDE 1 EXEMPLAIRE** chez toi AVANT de lancer une ad
- Verifie qualite + packaging + delai reel
- Si le produit est moisi → tu vas crouler sous les retours et Meta ban ton compte pour mauvais feedback

### Prix
- Negocie a partir de 50 commandes : -10 a -20%
- A partir de 200 commandes/mois : agent en Chine via Honest Fulphilment / NextSmartShip

---

## 4) LANDING PAGE (J5)

### Structure obligatoire (45+ specifique)
```
1. HERO : photo produit + headline + sous-headline + CTA
2. BARRE DE TRUST : "Livraison offerte | Garantie 30j | SAV FR" en GROS
3. 3 BENEFICES (icones + texte court)
4. AVANT/APRES ou DEMO produit (image ou GIF)
5. TEMOIGNAGES (3 minimum, avec photos de femmes 50+)
6. COMMENT CA MARCHE (3 etapes max)
7. FAQ (8-10 questions courtes)
8. GARANTIE expliquee en detail
9. SECTION "Qui sommes-nous" (rassure)
10. CTA FINAL
```

### Regles 45+
- Texte 16-18px, **interligne 1.6**
- Couleurs douces (pas de neon, pas de degrades agressifs)
- Photo de la fondatrice en bas de page = +20% conversion
- Telephone visible en haut a droite (rassure meme sans l'utiliser)
- Bouton CTA : "Commander - 49.90 EUR" (PAS "Acheter maintenant")

### Themes/builders rapides
- **GemPages** ou **Replo** : drag-drop pour Shopify
- **Booster** : theme deja optimise conversion

---

## 5) EMAILS / SMS (J5)

Suis `templates/klaviyo_flows_45plus.md`.
Mets en route en priorite :
1. Welcome Flow
2. Abandoned Cart Flow
3. Post-Purchase Flow

Les 3 autres viendront apres les premieres ventes.

---

## 6) META BUSINESS MANAGER (J6)

### Etapes
1. Va sur business.facebook.com → cree un Business Manager
2. Ajoute ta page Facebook (cree-la si besoin, nom = nom de marque)
3. Ajoute ton compte Instagram (cree-le, connecte a la page FB)
4. Cree un **compte publicitaire** (Ad Account) en EUR
5. Active **2FA** sur ton compte perso + ajoute une 2e methode de paiement (carte de secours)

### Pixel Meta
- Settings → Data Sources → Pixels → Create Pixel
- Connecte le Pixel a Shopify : Shopify Admin → Online Store → Preferences → Facebook Pixel ID
- Active **Conversions API** Shopify (gratuit, Shopify le fait nativement) → essentiel pour ne pas perdre 30% des conversions a cause d'iOS

### Domain Verification (NON NEGOCIABLE)
- Settings → Brand Safety → Domains → ajoute ton-domaine.fr
- Verifie via meta-tag HTML ou DNS
- Sans ca → impossible de configurer les events optimises

### Aggregated Event Measurement
- Events Manager → ton Pixel → Aggregated Event Measurement
- Range tes events : 1) Purchase, 2) InitiateCheckout, 3) AddToCart, 4) ViewContent, ...

---

## 7) META AD LIBRARY API TOKEN (optionnel mais ultra utile)

Pour utiliser `python3 tools/ad_library_scraper.py search ...` :

1. developers.facebook.com → Mes Apps → Cree App → Business
2. Ajoute le produit "Ad Library API"
3. Verification identite (CNI scan, ~24h)
4. Generate Token (long-lived, 60 jours)
5. Configure :
   ```bash
   export META_AD_LIBRARY_TOKEN="EAAB...."
   ```
   (ajoute la ligne dans ton ~/.zshrc ou ~/.bashrc pour persister)

---

## 8) CREATIVES (J7)

### Option A — UGC sur mesure (best ROAS mais 100-300 EUR)
- Genere ton brief :
  ```bash
  python3 tools/ugc_brief_generator.py
  ```
- Recrute une creatrice 45+ sur :
  - Backstage.com (France)
  - TikTok Creator Marketplace
  - Groupes Facebook "UGC creators France"
- Negocie 80-150 EUR pour 3 hooks + 1 video complete

### Option B — Stock UGC (rapide mais moins performant)
- BillionAires, Insense, Loom-UGC : librairies UGC achetables
- 30-50 EUR par video

### Option C — Toi-meme (si tu es a l'aise camera)
- Smartphone vertical 9:16
- Lumiere naturelle fenetre
- 25-30s max
- Sous-titres dans CapCut (gratuit)

---

## 9) PREMIERE CAMPAGNE META (J8)

### Structure
```
CAMPAGNE "Test01-CBO"
  Objectif       : Sales (Purchase)
  Budget         : CBO 150 EUR / jour
  Optimisation   : Highest Volume
  Bid strategy   : Auto

  ADSET 1 : Advantage+ (broad)
    Audience  : Femmes 45-65, France, Advantage+ Targeting
    Placements: Advantage+ Placements
    Creatives : 3 videos UGC (Hook1, Hook2, Hook3)

  ADSET 2 : Interets 1
    Audience  : Femmes 45-65, France, Interets [Menopause, Jardinage, Damart]
    Creatives : meme 3 videos

  ADSET 3 : Interets 2
    Audience  : Femmes 50-70, France, Interets [Croisieres, Stephane Plaza, Thalasso]
    Creatives : meme 3 videos
```

### Compte a respecter
- **Pas plus de 3 modifs/jour** sur la campagne → sinon tu casses la learning phase
- **48h minimum** avant de juger un adset
- Track dans `templates/ads_dashboard.csv` chaque jour
- Lance `python3 tools/ads_dashboard_analyzer.py` chaque matin

---

## 10) REGLES D'OR DU MEDIA BUYER (afficher au mur)

1. **Ne juge jamais avant 48h** de spend significatif (>=2x ton CPA cible)
2. **Le creative gagne, pas l'audience** : 80% de ton temps doit aller a tester des creatives
3. **Tue vite ce qui ne marche pas** mais **scale lentement** ce qui marche (+50% tous les 2 jours)
4. **Le back-end (email/SMS) fait la rentabilite** : pas de Klaviyo = pas de business
5. **Compte Meta = ton actif n°1** : 2FA, paiement double, pas de claims agressifs
6. **Le client 45+ est plus loyal que rentable a court terme** : LTV >> ROAS J0
7. **Si ROAS J0 = 1.5x et tu as un flow Klaviyo → tu es rentable**. Ne panique pas a 2.0x.

---

## CHECKLIST DE LANCEMENT (a cocher avant la 1re ad)

- [ ] Produit recu et teste personnellement
- [ ] ROAS cible calcule et viable (>= 2.0x)
- [ ] Domaine achete et connecte a Shopify
- [ ] Stripe + PayPal actives
- [ ] Mentions legales en place
- [ ] Landing page testee mobile (90% du traffic FB Ads = mobile)
- [ ] Pixel Meta installe et test event reussi
- [ ] Conversions API active
- [ ] Domain verification OK
- [ ] Klaviyo : Welcome + Abandoned Cart en route
- [ ] 3 creatives UGC differentes en stock
- [ ] 1500 EUR budget reserve pour le test
- [ ] Tu as bloque 1h/jour pour analyser le dashboard

→ Si tout est coche : LANCE.
