# 🎯 PLAYBOOK — Patchs anti-douleur dos
**Mode :** One-shot 500 EUR. Pas de 2e budget derriere. Execution chirurgicale.
**Date :** 2026-05-11

> Ce document est ton manuel d'execution. Suis-le pas a pas, dans l'ordre.
> Chaque ecart augmente tes chances d'echec.

---

## 🧠 POURQUOI CE PRODUIT EST UN BON CHOIX POUR TOI

### Forces (ce qui joue pour toi)
1. **Marche valide a 100%** : Nooro, Kailo, NuriaMD tournent depuis 2-3 ans avec 6 chiffres/jour de spend.
2. **Audience parfaite** : 70%+ des femmes 50+ ont mal au dos chronique. C'est universel.
3. **Achat impulsif** : douleur active = decision rapide. Pas de reflexion 3 jours.
4. **COGS tres bas** : 2-4 EUR la unite chez CJ. Marges enormes.
5. **AOV facile a monter** : bundle de 3/5/10 patchs = AOV 45-80 EUR sans effort.
6. **Faible friction sur la creative** : avant/apres "main sur le dos / sourire" = simple a filmer.

### Risques (ce que tu dois savoir)
1. **Competition feroce** : tu dois te differencier sur l'angle, pas le produit.
2. **Claim medical = ban Meta** : interdit de dire "guerit", "remplace medicament", "soigne".
3. **Saisonnalite** : pics en hiver (douleurs amplifiees) + rentree (post-vacances jardinage). Mai 2026 = OK mais pas le meilleur.
4. **Qualite chinoise variable** : 1 fournisseur sur 3 envoie du moisi. **Echantillon non-negociable.**

---

## 📦 ETAPE 1 — TROUVER LE BON FOURNISSEUR (J1)

### Recherche CJ Dropshipping (recommande)
1. Va sur cjdropshipping.com → cree un compte gratuit
2. Recherche : **"back pain patch"** ou **"heat patch back"** ou **"magnet pain relief patch"**
3. Filtre :
   - Warehouse : **CN ou US (livre vers EU)** ou idealement **CZ/PL** (entrepot Europe = delai 5-8j au lieu de 10-15j)
   - Reviews fournisseur : 4.6+ etoiles minimum
   - Sold quantity : >1000 (preuve de volume)

### 3 sous-types possibles (choisis-en UN)
| Type | COGS approx | Differenciation | Prix de vente conseille |
|------|------------:|-----------------|------------------------:|
| **Patch chauffant adhesif** | 0.30 EUR/unite | "chaleur 8h sans pile" | bundle 10 a 29.90 EUR |
| **Patch magnetique adhesif** | 0.50 EUR/unite | "aimants therapeutiques" | bundle 10 a 34.90 EUR |
| **Patch a base de plantes (menthol/poivre)** | 0.60 EUR/unite | "ingredients naturels" | bundle 10 a 32.90 EUR |

> **Mon choix pour toi :** patch chauffant adhesif. Le plus visuel ("sensation de chaleur immediate" = promesse simple), le moins risque cote claims medicaux.

### Commande echantillon (~15 EUR avec express)
- Commande **2 boites** (1 pour tester sur toi/proche, 1 pour les photos)
- Choisis l'expedition la plus rapide (CJPacket Sensitive EU ou YunExpress EU)
- Tu dois avoir le produit en main avant J7

---

## 💰 ETAPE 2 — PRICING & BUNDLE STRATEGY (J2)

### Le bundle obligatoire (sans ca tu ne survis pas a Meta)

**Page produit Shopify proposera 3 options :**
```
┌─────────────────────────────────────────────────────────┐
│  OPTION 1 : 1 boite de 10 patchs                        │
│             24.90 EUR                                    │
│                                                          │
│  OPTION 2 : 2 boites de 10 patchs  ← MOST POPULAR       │
│             39.90 EUR (au lieu de 49.80)                 │
│             "Conseillee par nos clientes"                │
│                                                          │
│  OPTION 3 : 4 boites de 10 patchs  ← BEST VALUE         │
│             64.90 EUR (au lieu de 99.60)                 │
│             "Cure complete 4 mois - LIVRAISON OFFERTE"   │
└─────────────────────────────────────────────────────────┘
```

### Calcul rentabilite (avec COGS unitaire 0.40 EUR, soit 4 EUR/boite)

| Bundle | Prix vente | COGS | Shipping | Frais paiement | **Profit brut** |
|--------|-----------:|-----:|---------:|--------------:|----------------:|
| 1 boite | 24.90 | 4 | 4 | 0.60 | **16.30 EUR** |
| 2 boites | 39.90 | 8 | 4.50 | 1.00 | **26.40 EUR** |
| 4 boites | 64.90 | 16 | 5.50 | 1.60 | **41.80 EUR** |

→ **CPA cible : 18-22 EUR.** Atteignable sur audience 45+ broad.

### Lance le calcul precis avec tes vrais chiffres
```bash
python3 tools/roas_calculator.py --sale-price 39.90 --cogs 8 --shipping-cost 4.50
```

---

## 🎨 ETAPE 3 — POSITIONNEMENT & MARQUE (J2)

### Le piege : pas de marque generique
"Patch dos" sans marque = perdu dans 50 concurrents. Donne un nom.

### Suggestions de noms (cherche dispo .fr)
- **Lumea** (douceur, lumiere — passe-partout)
- **Renaitre** (emotionnel, evoque retrouver son corps)
- **Caliae** (chaleur en latin, pro)
- **Soleva** (chaleur du soleil)
- **Belva** (belle + bien-etre)

> Choisis-en un que le **.fr est libre** (verifie sur namecheap.com). 10 EUR/an.

### Promesse de marque (a repeter sur tout)
*"Le soulagement, sans medicaments, sans ordonnance, sans rendez-vous."*

---

## 🎬 ETAPE 4 — CREATIVES (J5-J7)

### Strategie creative (1 angle, 3 hooks)

**Angle gagnant :** *Storytelling kine / decouverte tardive*

Pourquoi cet angle ? Il marche depuis 3 ans, il n'est PAS sature comme l'angle "avant/apres", et il transforme l'audience 45+ en spectatrice empathique.

### Brief UGC (genere automatiquement)
```bash
python3 tools/ugc_brief_generator.py \
    --product "Patch chauffant anti-douleur dos" \
    --price 39.90 \
    --angle douleur \
    --out brief_patch_lumea.md
```

### Les 3 hooks a faire tourner par la creatrice
1. *"Ma kine m'a dit : 'Si vous aviez su ca plus tot, on n'en serait pas la.'"*
2. *"J'ai 62 ans. Je remonte les courses au 3e etage sans grimacer. Premiere fois en 5 ans."*
3. *"Mon mari a remarque que je dormais sans bouger. Ca faisait des mois que je me reveillais 3 fois."*

### Option A — UGC stock Fiverr (60 EUR, recommande)
- Va sur fiverr.com
- Cherche : **"french UGC mature woman product review"** OU **"french UGC ad over 40"**
- Filtre : Level 2+ sellers, 4.9+ etoiles, livraison 4j
- Brief :
  - Demande **3 versions** avec hooks differents (cf ci-dessus)
  - 25-30s vertical 9:16
  - Sous-titres en dur
  - Voix-off claire
- Cout total : 50-80 EUR

### Option B — Toi-meme avec un proche 50+
- Maman, tante, voisine, amie...
- Smartphone vertical 9:16, lumiere fenetre (le matin idealement)
- Cap Cut pour sous-titres (gratuit, mobile)
- Filme 3 versions avec hooks differents
- **Cout : 0 EUR.** Mais demande de l'aise.

> Si tu doutes : option A. Le risque de cramer ton budget ads sur un UGC mediocre fait toi-meme > 60 EUR de Fiverr.

---

## 🛍 ETAPE 5 — LANDING PAGE (J5)

### Structure exacte (a copier section par section)

```markdown
SECTION 1 — HERO (above the fold)
─────────────────────────────────────
H1 : "Le soulagement, sans medicaments"
H2 : "Patchs chauffants Lumea - 8h de chaleur ciblee"
[Photo produit pose sur dos d'une femme 50+]
[Bouton : VOIR LES PACKS - 39,90 EUR]
Barre de trust juste en dessous :
  ✓ Livraison offerte des 39 EUR
  ✓ Garantie satisfait ou rembourse 30 jours
  ✓ SAV francais (numero affiche)

SECTION 2 — DOULEUR (empathie)
─────────────────────────────────────
"Vous vous reveillez avec le dos bloque.
Vous evitez de soulever votre petit-enfant.
Vous comptez les heures jusqu'a la prochaine douleur."

Vous n'etes pas seule. 67% des femmes apres 50 ans
vivent avec une douleur lombaire quotidienne.

SECTION 3 — SOLUTION
─────────────────────────────────────
"Et si la solution etait dans un patch ?"

Lumea diffuse une chaleur reguliere de 50-55 C
pendant 8 heures, ciblant precisement les muscles
contractes.

[GIF : la chaleur visible sur le patch]

3 BENEFICES (icones + 1 phrase chaque)
  🌡️  Chaleur durable 8h
  ✋  Adhesif doux, ne tire pas la peau
  👜  Discret sous les vetements

SECTION 4 — COMMENT CA MARCHE
─────────────────────────────────────
1. Retirer le film protecteur
2. Coller sur la zone douloureuse
3. Sentir la chaleur en 60 secondes

SECTION 5 — TEMOIGNAGES (3 minimum)
─────────────────────────────────────
Photo de femme 55-65 + texte 4-5 lignes
"Marie, 58 ans, Lyon" - "J'avais essaye 5 cremes...
Lumea c'est le 1er truc qui tient ses promesses."

(2 autres temoignages similaires - utilise photos
de banque d'images type Pexels avec des 50+)

SECTION 6 — LES PACKS (le coeur)
─────────────────────────────────────
[3 cartes pricing comme decrit en section 2]
Bouton "MOST POPULAR" sur le bundle 2 boites.
Logos paiement (CB Visa, Mastercard, PayPal) sous le pack.

SECTION 7 — FAQ
─────────────────────────────────────
Q: Combien de temps pour ressentir la chaleur ?
R: 60 secondes apres application.

Q: Est-ce que ca colle bien sous les vetements ?
R: Oui, l'adhesif est concu pour rester 8-12h.

Q: Quel est le delai de livraison ?
R: 5 a 10 jours en France metropolitaine.

Q: Que faire si ca ne fonctionne pas sur moi ?
R: Renvoyez les patchs non utilises dans les 30 jours,
remboursement integral.

Q: Y a-t-il des contre-indications ?
R: A eviter sur peau lesee, en cas de grossesse,
et pour les personnes portant un pacemaker.

(5 autres FAQ courantes)

SECTION 8 — GARANTIE (rassure)
─────────────────────────────────────
Encadre vert avec icone bouclier :
"GARANTIE 30 JOURS - SATISFAITE OU REMBOURSEE
Sans condition. Sans questions. Sans negociation."

SECTION 9 — QUI SOMMES-NOUS
─────────────────────────────────────
Mini-photo + paragraphe court :
"Lumea est une marque francaise..."
(meme si tu es seule, ca rassure)

SECTION 10 — CTA FINAL
─────────────────────────────────────
"Reprenez votre vie en main."
[Bouton : COMMANDER MAINTENANT]
```

### Apps Shopify a installer
- **Loox** ou **Judge.me** : reviews (gratuit < 50 reviews)
- **ReConvert** : upsell post-achat (ajouter 1 boite a -50% sur thank-you page)
- **Frequently Bought Together** (gratuit) : suggere bundle au panier

---

## 📧 ETAPE 6 — KLAVIYO (J5)

Suis exactement `templates/klaviyo_flows_45plus.md`. Active en priorite :
1. **Welcome Flow** (4 emails)
2. **Abandoned Cart Flow** (3 emails + 1 SMS)
3. **Post-Purchase Flow** (5 emails)

Ces 3 flows valent **20-30% de ton CA**. Sans eux, tu vas perdre 100 EUR sur l'abandon de panier que Klaviyo aurait recupere.

---

## 🚀 ETAPE 7 — LANCEMENT META (J10)

### Setup campagne
```
CAMPAGNE : Lumea-Test01-CBO
Objectif : Sales (Purchase)
Budget : CBO 30 EUR/jour
Optimisation : Highest Volume

  ADSET unique : "Broad-Femmes-45-65"
  Audience : Femmes 45-65, France
  Detailed Targeting : (laisser vide → Advantage+ Audience)
  Placements : Advantage+ Placements
  Creatives : 3 videos UGC differentes (Hook1, Hook2, Hook3)
```

### Pourquoi UNE seule campagne, UN seul adset
- Budget 30 EUR/j = trop faible pour diversifier
- Meta a besoin de 5-10 conversions pour sortir de la learning phase
- Le test se fait sur les **creatives** (les 3 videos), pas les audiences

### Compliance Meta (a respecter ABSOLUMENT)
- Aucune photo de zoom sur une douleur (interdit)
- Aucun claim type "soulage l'arthrose", "remplace anti-inflammatoires"
- Utilise "pour celles qui veulent...", "retrouver le confort..."
- Si Meta rejette ton ad : modifie la phrase litigieuse, ne re-lance pas le meme texte

---

## 📊 ETAPE 8 — ARBRE DE DECISION JOUR PAR JOUR

```
J10 (lancement) - Spend 30 EUR
└─ Resultats normaux a J1 : 0-1 vente, CPM 5-15 EUR, CTR 0.8-1.5%
   → CONTINUE. Tout est normal.

J11 - Spend cumule 60 EUR
└─ 0 vente, CTR < 0.8% → PROBLEME CREATIVE
   └─ Action : remplace la creative la plus weak par une 4e (refais hook differemment)
└─ 0 vente, CTR > 1.2% mais 0 ATC → PROBLEME LANDING
   └─ Action : verifie temps de chargement mobile (PageSpeed Insights)
                verifie bouton CTA visible
                ajoute paypal si pas deja fait
└─ 0 vente, CTR > 1.2%, ATC mais 0 checkout → PROBLEME PRIX/CONFIANCE
   └─ Action : ajoute "Livraison offerte" plus visible
                renforce la garantie 30j
└─ 1-2 ventes → CONTINUE sans toucher

J12 - Spend cumule 90 EUR
└─ 0 vente cumule → KILL IMMEDIAT, change de produit OU de creative
   └─ Tu as 410 EUR restants. Decide : abandonner ou relancer avec nouveau angle.
└─ 1 vente, ROAS 0.4 → CONTINUE encore 2 jours pour confirmer learning
└─ 2+ ventes, ROAS >= 1.2 → CONTINUE sans toucher

J13-J14 - Spend cumule 120-150 EUR
└─ ROAS J3 cumule >= 1.5 → JACKPOT, tu peux scaler doucement
   └─ Action : passe le budget 30 → 45 EUR/j (jamais +50% d'un coup)
└─ ROAS 0.8-1.5 → ZONE GRISE
   └─ Si tu as Klaviyo qui tourne, tu es probablement BE → CONTINUE
   └─ Sinon → ameliore le back-end avant de scaler
└─ ROAS < 0.5 → KILL

J15-J20 - Si tu es toujours en course
└─ ROAS stable 1.5+ → scale a 45 puis 60 EUR/j
└─ Tu commences a generer du cash : pre-commande plus de stock chez CJ
└─ Plante 1 nouveau hook UGC chaque semaine pour maintenir le CTR

JOUR D'OR : ROAS atteint 2.5x avant J15
└─ Tu as un winner. Tes 500 EUR ont rapporte la formule.
└─ Reinvestis 100% du profit dans le scaling, pas dans des nouveaux gadgets.
```

---

## 🎯 SEUILS DE KILL ABSOLUS

| Indicateur | Seuil | Action |
|------------|-------|--------|
| Spend 90 EUR, 0 vente | KILL absolu | change creative + landing |
| Spend 200 EUR cumule, 0 vente | KILL produit | passe a un autre produit |
| Spend 150 EUR, ROAS < 0.3 | KILL | landing ou prix defaillant |
| 3 plaintes clients en 1 semaine | KILL marketing | retravaille les claims |

---

## 💡 LES 5 LEVIERS POUR MAXIMISER TES CHANCES (sans cash supplementaire)

### 1. Bundle 2 boites en MOST POPULAR
Force par defaut le AOV a 39.90 EUR au lieu de 24.90. **+60% de CA pour 0 effort.**

### 2. ReConvert upsell "1 boite a -50%" sur thank-you page
Taux d'acceptation moyen : 18%. Sur 50 ventes : +9 ventes additionnelles a 12 EUR. **+100 EUR profit/mois.**

### 3. SMS dans le flow Abandoned Cart
Recupere 15-20% des paniers abandonnes. Sur 100 paniers abandonnes, +15 ventes recuperees = 600 EUR.

### 4. Photos de marque "vraie" (pas Aliexpress)
Demande a 2 amies 50+ de te preter 30 min : photos avec ton echantillon. Visuel pro = +20% conversion.

### 5. Coupon "WELCOME10" dans la popup Klaviyo
Capture 12-25% des visiteurs en email. Tu pourras leur revendre en email gratuitement.

---

## ❌ CE QUE TU NE DOIS PAS FAIRE

- ❌ Tester 3 produits en parallele (tu n'en as pas les moyens)
- ❌ Acheter une formation "dropshipping" a 297 EUR (tout est dans ce repo)
- ❌ Payer 200 EUR un UGC creator influencer "premium"
- ❌ Lancer sans avoir teste le produit toi-meme
- ❌ Lancer sans Klaviyo configure (Cart Abandonment minimum)
- ❌ Modifier ta campagne Meta tous les jours (casse la learning phase)
- ❌ Paniquer a J2 a 0 vente (c'est normal sur compte neuf)
- ❌ Augmenter le budget avant 5 jours stables ROAS positif

---

## ✅ CHECKLIST AVANT LANCEMENT (J9 - veille du go)

- [ ] Echantillon recu, **teste sur ton dos a toi**, qualite OK
- [ ] CJ Dropshipping connecte a Shopify, fulfillment auto active
- [ ] 3 bundles configures dans Shopify avec photos perso
- [ ] Landing page testee mobile, temps de chargement < 3s
- [ ] Klaviyo : Welcome + Cart + Post-Purchase actifs
- [ ] Popup -10% configuree
- [ ] Stripe + PayPal actifs et testes avec une vraie carte
- [ ] Pixel Meta installe + Conversions API active
- [ ] Domain Verification OK dans Meta Business Manager
- [ ] 3 creatives UGC pretes (verticales 1080x1920, sous-titres en dur)
- [ ] CGV / Mentions legales / Politique retours visibles en footer
- [ ] Compte Stripe a un solde 0 (jamais de retrait avant 30j de vie)
- [ ] Numero de telephone SAV visible en haut de la landing
- [ ] Tu as bloque 1h/jour pendant 14 jours pour le monitoring
- [ ] Tu acceptes psychologiquement de perdre 500 EUR

---

## 📞 SI TU AS UN DOUTE A UN MOMENT

Reviens dans le repo, ouvre le bon outil :
- Pas sur de ton prix ? → `python3 tools/roas_calculator.py`
- Pas sur d'une creative ? → `python3 tools/ugc_brief_generator.py`
- Pas sur d'une campagne ? → `python3 tools/ads_dashboard_analyzer.py`
- Tu veux scorer une autre piste produit en backup ? → `python3 tools/score_products.py`

---

## 🎬 TON PROCHAIN PAS (LITTERALEMENT MAINTENANT)

1. Ouvre **cjdropshipping.com** dans un nouvel onglet
2. Cree un compte (5 min)
3. Cherche "**back pain heat patch**"
4. Trouve 1 fournisseur avec :
   - 1000+ ventes
   - 4.6+ etoiles
   - Entrepot EU (CZ ou PL)
5. **Commande 2 boites en express** (~15 EUR)
6. Reviens ici demain pour la suite (setup Shopify)

Tu as 7 jours avant le lancement. La machine est en marche.
