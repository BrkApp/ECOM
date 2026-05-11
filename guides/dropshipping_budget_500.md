# GUIDE DROPSHIPPING — Budget de depart 500 EUR
**Cible :** femmes 45-70, FR, Meta Ads
**Honnetete :** 500 EUR c'est tendu. C'est faisable, mais zero erreur.
**Realisme :** sur 10 personnes qui demarrent a 500 EUR, 2-3 sortent rentables. Les autres apprennent.

---

## 💰 BREAKDOWN BUDGET 500 EUR (a respecter strictement)

| Poste | Cout | Notes |
|-------|-----:|-------|
| Shopify (3 mois a 1 EUR) | 3 EUR | trial 3 jours puis 1 EUR/mois 3 mois |
| Nom de domaine .fr (Namecheap) | 10 EUR | .com a eviter au debut, plus cher |
| Theme Shopify | 0 EUR | **Dawn (gratuit)** suffit largement |
| App ReConvert (upsell) | 0 EUR | plan gratuit OK <50 commandes |
| Klaviyo email | 0 EUR | gratuit jusqu'a 250 contacts |
| Loox reviews | 0 EUR | plan gratuit 14j puis basique 10 EUR/mois (active apres ventes) |
| 1 echantillon fournisseur | 15 EUR | OBLIGATOIRE - jamais lancer sans tester |
| UGC stock (3 videos) | 60 EUR | Fiverr 20 EUR/video ou BillionAires |
| Photos produit (toi-meme) | 0 EUR | smartphone + lumiere fenetre |
| Logo (Canva gratuit ou Looka) | 0 EUR | pas d'agence, pas de 200 EUR de design |
| **TOTAL SETUP** | **88 EUR** | |
| **Budget ADS test** | **400 EUR** | |
| Reserve (frais imprevus) | 12 EUR | retour, expedition, etc. |
| **TOTAL** | **500 EUR** | |

> Si tu depasses 100 EUR de setup → **STOP**. T'as deja perdu sur l'execution. Tout poste au-dela de cette liste est du superflu.

---

## ⚠️ LA REALITE DU COMPTE ADS NEUF

Meta Ads sur un compte neuf + Pixel neuf = **learning phase brutale**.
Tu vas spend les 100 premiers EUR sans aucune vente. C'est normal. Le Pixel a besoin de 5-10 events pour calibrer.

**Implication :** tu dois avoir un produit a marge >= 25 EUR/commande, sinon meme en learning tu te crames.

**Conseil :** ne panique pas avant J5 si ROAS = 0.

---

## 🎯 STRATEGIE BUDGET 500 EUR : "ONE PRODUCT, ONE SHOT"

### Phase 1 — Selection produit (J1-J2, 0 EUR)
- Lance `python3 tools/score_products.py` sur 5 candidats
- Garde **1 seul produit** Money Score >= 8.5
- **Critere supplementaire dropship :** COGS AliExpress/CJ <= 8 EUR
- Verifie en Ad Library : >=10 advertisers actifs FR + 3 ads >120 jours

### Phase 2 — Validation eco (J2, 0 EUR)
- `python3 tools/roas_calculator.py`
- Reglages adaptes dropship :
  - prix de vente : **3 a 5x le COGS** (ex : COGS 7 EUR → vendre 35 EUR)
  - shipping cost : **4-6 EUR** (CJ standard FR)
  - taux retour : **8%** (dropship = plus de retours qu'une marque)
- **Verifie : CPA cible >= 15 EUR** (sinon impossible sur Meta 2026)

### Phase 3 — Setup (J3-J4, ~88 EUR)
- Suis `guides/setup_a_z.md` **sections 2 a 6**
- IMPORTANT dropship : commande l'echantillon en **express** (10 EUR de + mais tu attends 5j au lieu de 15j)

### Phase 4 — Creatives stock (J5, 60 EUR)
- 3 videos UGC stock differentes :
  - **Fiverr** : recherche "UGC ad french woman" — filtre 4.9+ etoiles
  - **BillionAires** ou **Insense** : librairies UGC abonnement
- Si tu as l'aise camera : filme toi-meme avec ta mere/tante/voisine 50+ comme actrice
- Brief : utilise `python3 tools/ugc_brief_generator.py`

### Phase 5 — Lancement Meta Ads (J6, budget 400 EUR sur 10-12 jours)

**Setup adapte budget 500 EUR :**
```
CAMPAGNE Test01 — Sales Objective — CBO 30 EUR/jour

  ADSET 1 : Advantage+ Audience (broad)
    Femmes 45-65, France
    Placements : Advantage+
    Creatives : 3 videos UGC

  (UN SEUL ADSET — pas 3 — budget trop faible pour diversifier)
```

**Pourquoi 1 seul adset :**
- 30 EUR/j sur 3 adsets = 10 EUR par adset = **trop faible pour sortir du learning**
- 30 EUR/j sur 1 adset broad = Meta optimise efficacement
- Tu testes les **creatives** dedans (3 videos), c'est ca qui compte

### Phase 6 — Decisions (J7 a J12)

Utilise chaque matin :
```bash
python3 tools/ads_dashboard_analyzer.py --target-roas 2.9 --target-cpa 17.28
```

**Adaptations seuils budget 500 EUR :**
- KILL une creative si elle a depense >= 30 EUR sans 1 vente
- KILL la campagne entiere si J5 sans 2 ventes (probleme produit/landing/angle)
- KEEP des que ROAS J3-J5 >= 1.5 (le back-end Klaviyo te rentabilise)
- SCALE timide : passe 30 → 45 EUR/j seulement si ROAS J5 >= 2.5

---

## 🛒 FOURNISSEURS DROPSHIP — RANKING 2026

| Fournisseur | Pour quoi | Delai FR | Tarif | Note |
|------------|-----------|---------|-------|------|
| **CJ Dropshipping** | tout sauf cosmetique | 8-12j | meilleur prix Chine | top 1 |
| **Zendrop** | beauty / gadgets | 8-14j | un peu + cher que CJ | bonne app Shopify |
| **AliExpress Choice** | demarrage rapide | 7-15j | OK mais qualite variable | a quitter apres 100 ventes |
| **Spocket** | produits Europe | 3-7j | + cher mais NPS top | si tu veux scaler |
| **Wiio / HyperSKU** | apres 100+ commandes/mois | 5-9j | agent prive, super prix | next level |

### Setup minimum CJ Dropshipping
1. Compte gratuit sur cjdropshipping.com
2. Connect Shopify app
3. Cherche ton produit, demande "Sourcing" si pas trouve
4. Active **"CJPacket Sensitive"** ou **"YunExpress"** pour FR (tracking + rapide)
5. Negocie a partir de 50 commandes : email a ton account manager

---

## 🚨 PIEGES TYPIQUES DROPSHIP (qui tuent les debutants)

### 1. Produit en image "trop beau"
La photo AliExpress est retouchee. Ce que tu recois est moche. **Commande TOUJOURS l'echantillon.**

### 2. Delais caches
Aliexpress dit "10-20 jours". En vrai : 15-25 jours France. Le client 45+ ne va PAS attendre 3 semaines = chargeback = compte Stripe gele.
→ **Utilise CJ ou Spocket avec entrepot EU.**

### 3. Compte Stripe gele a la 1re grosse vente
Tu fais 500 EUR en 1 jour avec un compte tout neuf → Stripe gele tes fonds 90 jours.
→ Active **PayPal en parallele** + appelle Stripe avant de scaler.

### 4. Compte Meta banni pour "low-quality"
Plaintes clients > 1% = ban Meta a vie.
→ Fais un SAV reactif (12h max). Reponds aux DMs. Rembourse vite.

### 5. Pas de TVA → 5000 EUR de CA et URSSAF te tombe dessus
Statut auto-entrepreneur OBLIGATOIRE des le 1er euro (~25 min sur autoentrepreneur.urssaf.fr).
TVA non applicable < 36 800 EUR/an (regime micro).

### 6. AOV trop faible
Vendre un produit a 25 EUR avec CPA 20 EUR = mort.
→ **Bundle obligatoire** ou **upsell ReConvert** post-achat pour monter l'AOV a 45+ EUR.

---

## ✅ CHECKLIST PRODUITS COMPATIBLES DROPSHIP + 45+

Verifie chaque produit candidat sur ces criteres :

- [ ] **COGS <= 8 EUR** (sinon marge dropship insuffisante)
- [ ] **Poids < 500g** (sinon shipping casse la marge)
- [ ] **Pas fragile** (verre, ceramique = retours casses)
- [ ] **Pas alimentaire / cosmetique** au debut (regulation FR + douane)
- [ ] **Pas electrique** (CE, garantie, retours techniques)
- [ ] **Couleur/taille standardisee** (eviter "rouge/bleu/jaune + S/M/L" = nightmare stock)
- [ ] **Prix de vente raisonnable >= 25 EUR** (sinon AOV trop faible)
- [ ] **Ad Library : 10+ advertisers actifs FR**
- [ ] **3+ ads tournant depuis 90+ jours en FR**
- [ ] **Probleme emotionnel clair** (cf STRATEGY_FEMMES_45PLUS.md)

**Top 5 produits dropship-friendly de la strategy file pour budget 500 EUR :**
1. Patchs anti-douleur dos/genoux (#1) — COGS 3-5 EUR, vendre 24.90
2. Patchs yeux collagene (#12) — COGS 2-4 EUR, vendre 19.90 (bundle 3)
3. Correcteur posture (#3) — COGS 5-7 EUR, vendre 34.90
4. Brosse anti-cheveux blancs (#15) — COGS 3-4 EUR, vendre 22.90
5. Tisane sommeil (#23) — attention reglementation, OK si non-medicalise

> **Eviter avec 500 EUR** : sneakers (#4) et appareils massage (#10) — COGS > 15 EUR.
> **Eviter aussi** : complements alimentaires (#9, #23 sans precaution) — risque legal.

---

## 📊 SCENARIO REALISTE 500 EUR (a quoi t'attendre)

### Scenario A — Echec rapide (60% des cas)
```
J1-J5 : spend 150 EUR, 0 vente → produit ou angle defaillant
J6    : KILL, reset, change de produit
Tu as appris : un produit valide, un mauvais.
Tu as encore 350 EUR. Tu retentes 1 fois.
```

### Scenario B — Test moyen (25% des cas)
```
J1-J5 : spend 150 EUR, 2 ventes, ROAS 1.0
J6-J10: spend 200 EUR, 6 ventes, ROAS 1.5
Total : 350 EUR depenses, 8 ventes a 35 EUR = 280 EUR CA → perte 70 EUR
Mais : tu as 8 clientes dans Klaviyo + des datas Pixel.
Tu retentes avec un meilleur creative ou un bundle pour passer ROAS 2x+.
```

### Scenario C — Hit (15% des cas)
```
J1-J5 : ROAS 2.5, tu scales prudemment
J6-J12 : 400 EUR spend cumule, 25 ventes, 875 EUR CA, profit ~200 EUR
Tu reinvestis : passe a 60 EUR/j, prends un UGC vrai a 100 EUR
Mois 2 : tu fais 5-10K EUR de CA.
```

**Le but du budget 500 EUR n'est PAS d'etre rentable du 1er coup.**
Le but est de **trouver le couple produit+angle qui marche** pour pouvoir y mettre 5000 EUR derriere ensuite.

---

## 🎯 PLAN D'ACTION 14 JOURS (CONDENSE 500 EUR)

```
J1  : choix produit + scoring + Ad Library check
J2  : roas_calculator + verification economique
J3  : commande echantillon CJ (express, ~15 EUR)
J4  : Shopify + domaine + Stripe + PayPal
J5  : landing page (theme Dawn) + Klaviyo flows
J6  : reception echantillon - test perso. KO ? on change.
J7  : commande 3 UGC stock Fiverr (60 EUR)
J8  : Meta BM + Pixel + Domain Verif
J9  : reception UGC. Edit sous-titres sur CapCut.
J10 : LANCE - 30 EUR/j CBO broad Advantage+
J11-J14: analyze quotidien, decisions, iterations
```

---

## 🧠 MINDSET BUDGET LIMITE

1. **Tu paries sur 1 produit.** Pas de plan B parallele. Concentration totale.
2. **Tu n'as pas le droit a une erreur sur les fondamentaux** : echantillon non commande, Pixel mal installe, Klaviyo zappe → mort.
3. **Tu apprends, tu ne gagnes pas (encore).** Le but du 1er run = data + experience.
4. **Si tu cremes les 500 EUR sans rien apprendre = vrai echec.** Si tu cremes 500 EUR mais que tu sais pourquoi = etape franchie.
5. **Quand tu retentes, on monte le budget.** 1000 EUR au 2e essai, 2000 EUR au 3e — avec ce que tu auras appris.

---

## 🚀 AVANT DE LANCER : LA QUESTION HONNETE

**Es-tu pret a perdre les 500 EUR ?** Si la reponse est non, **n'investis pas**. Ce business demande de la marge psychologique pour ne pas paniquer a J3 quand 90 EUR sont depenses sans vente.

Si oui : tu as un kit complet pour avoir 3x plus de chances que la moyenne. Lance.
