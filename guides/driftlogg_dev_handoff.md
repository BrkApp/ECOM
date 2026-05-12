# DriftLogg — Brief de dev (handoff)

> Document destine a l'instance Claude Code qui developpe DriftLogg.
> Contient : contexte produit, repositionnement strategique, et le backlog
> ordonne en 6 sprints (~15-20 jours dev cumules).

---

## 1. CONTEXTE PRODUIT (rappel court)

- **Nom :** DriftLogg
- **Tagline actuelle :** SaaS qui predit le declin des dependances open source
- **Stack :** Next.js 14 App Router, TypeScript strict, Tailwind CSS, shadcn/ui, Octokit, Vercel KV
- **Etat actuel :** MVP fonctionnel non deploye. Free tool (scan a la demande) operationnel. Waitlist integree.
- **6 signaux analyses :** cadence commits, reactivite issues, fraicheur releases, sante communaute, licence/trust, presence sociale
- **Output :** score 0-100 + niveau de risque

---

## 2. INSIGHTS STRATEGIQUES (a integrer dans tout le travail produit)

### Benchmark concurrentiel synthese
| Concurrent | Couvre vs DriftLogg | Pricing | Faiblesse a exploiter |
|---|---|---|---|
| **OSSF Scorecard** | 4 de nos 6 signaux | gratuit | UX devs-only, pas de digest humain, pas de multi-repo dashboard, pas d'alertes mail |
| **Socket.dev** | focus supply chain attacks (different scope) | freemium / enterprise | n'addresse pas l'abandonment |
| **Snyk Advisor** | health score similaire | **SUNSETTING janvier 2026** | fenetre d'opportunite ENORME |
| **deps.dev (Google)** | API metadata uniquement | gratuit API only | pas d'UI, pas d'alertes |
| **Endor Labs** | reachability + dependency lifecycle | enterprise 5-50K$/an | inabordable < 100 devs |

### Le wedge a defendre dans tout le produit
> **DriftLogg = le remplacant de Snyk Advisor, avec monitoring continu + recommandations d'alternatives.**

3 piliers de differentiation :
1. **Timing** : positionnement explicite comme alternative au Snyk Advisor sunset
2. **UX simple** : onboarding 30s, digest hebdo email/Slack (pas un dashboard a checker)
3. **Alternative recommendation** : quand une dep decline, suggerer 3 remplacements compatibles → **personne d'autre ne le fait, c'est le killer feature**

---

## 3. PRICING (a implementer)

```
FREE
  - 5 repos
  - Scan a la demande
  - Score 0-100 + 6 signaux
  - Mention "Powered by DriftLogg" obligatoire sur les rapports publics

PRO — 29 EUR/mois (tier qui rapporte)
  - 50 repos monitored 24/7
  - Digest hebdo email
  - Slack integration
  - Alertes en temps reel quand un signal vire au rouge
  - Recommandations d'alternatives (killer feature)
  - Historique 6 mois

TEAM — 99 EUR/mois
  - 250 repos
  - Multi-user (5 seats inclus)
  - SBOM export (CycloneDX)
  - Webhooks custom
  - SSO Google

ENTERPRISE — sur devis
  - Volume illimite, SLA, support dedie
```

---

## 4. STACK DECISIONS A PRENDRE

| Besoin | Choix recommande | Alternative | Pourquoi |
|---|---|---|---|
| Auth | **Clerk** | NextAuth + Supabase | Clerk plus rapide a integrer, free tier 10K MAU |
| DB (historique scores) | **Supabase Postgres** ou **Neon** | Vercel KV insuffisant pour time-series | Vercel KV = OK pour cache, pas pour data |
| Email | **Resend** | Postmark | Free tier 3K emails/mois, DX Next.js excellent |
| Crons | **Vercel Cron Jobs** | Trigger.dev, Inngest | natif Vercel, gratuit en Pro |
| Paiements | **Stripe Checkout + Customer Portal** | Lemon Squeezy | standard SaaS, gestion TVA UE |
| Slack | **Webhooks Slack natifs** | Slack App OAuth | webhook URL = setup en 30s cote user |

---

## 5. BACKLOG — 6 SPRINTS ORDONNES

### Sprint 1 — REPOSITIONNEMENT (3 jours)
**But :** capter le trafic Snyk Advisor + rendre le pitch evident.

- [ ] Homepage : nouveau H1 + sous-titre
  - H1 : "Watch your dependencies before they die"
  - H2 : "The Snyk Advisor replacement with continuous monitoring & alternative suggestions"
- [ ] Section "Why DriftLogg vs OSSF Scorecard vs Snyk Advisor" (table comparative honnete)
- [ ] Page `/pricing` avec 3 tiers Free/Pro/Team (cards shadcn/ui)
- [ ] Page `/alternative-to-snyk-advisor` (SEO ciblee)
- [ ] Template dynamique `/package/[ecosystem]/[name]` (SEO long tail : "is faker maintained", "is moment.js dead", etc.)
- [ ] OG image personnalisee par rapport scan (Next.js OG `@vercel/og`)
- [ ] Meta tags + JSON-LD `SoftwareApplication`
- [ ] CTA homepage : "Scan a repo" (gratuit, sans signup pour 1 scan)

**Acceptance :** la homepage refletant le nouveau wedge est en ligne, pricing visible, 1 page SEO live.

---

### Sprint 2 — AUTH + DASHBOARD MULTI-REPO (3-4 jours)
**But :** rendre possible d'avoir un compte payant avec ses repos sauvegardes.

- [ ] Integration **Clerk** (signup email + GitHub OAuth)
- [ ] Migration data : Vercel KV → Supabase Postgres
  - Tables minimales : `users`, `monitored_repos`, `scans`, `signal_snapshots`
- [ ] Page `/dashboard` (auth required)
  - Liste des repos monitores
  - Score actuel + tendance 30j
  - Bouton "Add repo" (input URL GitHub)
  - Bouton "Remove" par repo
- [ ] Page `/dashboard/repo/[id]` (detail repo)
  - Score actuel + 6 signaux detailles
  - Graphique evolution 6 mois (recharts ou tremor)
  - Liste des alternatives suggerees (sera populee Sprint 5)
- [ ] Middleware Next.js : tier gating
  - Free : max 5 repos
  - Pro : max 50 repos
  - Team : max 250 repos
- [ ] Page `/settings` (compte, billing, notifications)

**Acceptance :** un user peut s'inscrire, ajouter 5 repos, voir un dashboard fonctionnel.

---

### Sprint 3 — MONITORING CONTINU + DIGEST EMAIL (3 jours)
**But :** le coeur de la valeur Pro.

- [ ] Vercel Cron job `/api/cron/daily-scan` (1x/jour, 4h UTC)
  - Parcourt tous les `monitored_repos`
  - Re-compute les 6 signaux
  - Persiste un `signal_snapshot` (timestamp + scores)
  - Detecte transitions de risk level (green → yellow → red)
- [ ] Vercel Cron job `/api/cron/weekly-digest` (dimanche 8h UTC)
  - Aggrege par user
  - Genere HTML email (React Email + Resend)
  - Contenu : "Cette semaine sur vos 12 deps : 2 ont decline, 1 alerte critique, voici quoi faire"
- [ ] Email template "Welcome" a la creation de compte
- [ ] Email template "Critical alert" instantane si un repo passe en rouge
- [ ] Page `/settings/notifications` (frequence digest, opt-in/out par event type)

**Acceptance :** un user qui ajoute 5 repos recoit un digest hebdo le dimanche.

---

### Sprint 4 — SLACK INTEGRATION (2 jours)
**But :** ouvrir le marche teams (qui paient + cher).

- [ ] Page `/settings/integrations/slack`
  - Input : webhook URL Slack (saisie manuelle, pas OAuth pour v1)
  - Bouton "Test connection" (envoie un message test)
- [ ] Quand un repo passe en rouge → POST sur webhook avec un payload formate Block Kit
- [ ] Quand digest hebdo → option d'envoi Slack en plus de l'email
- [ ] Documentation in-app "Comment recuperer son webhook Slack" (capture d'ecran)

**Acceptance :** un user peut configurer Slack en 2 min et recevoir une alerte test.

---

### Sprint 5 — ALTERNATIVE RECOMMENDATION (3-5 jours) ← KILLER FEATURE
**But :** le seul vrai differenciateur sur le marche.

#### v1 : approche curated
- [ ] Table `package_alternatives` : `package_id`, `alternative_id`, `category`, `migration_difficulty (1-5)`, `notes`
- [ ] Seed initial : 200 packages les plus populaires npm + 100 PyPI les plus telecharges
  - Mapping manuel pour les categories evidentes (moment.js → date-fns, dayjs, luxon)
- [ ] Page detail repo : section "DriftLogg suggests"
  - 3 alternatives max
  - Score health de l'alternative (calcule par nos signaux)
  - Niveau de difficulte de migration
- [ ] Email digest : inclure les alternatives pour chaque dep en alerte rouge

#### v2 (apres v1 deployee) : approche automatique
- [ ] Utiliser deps.dev API pour identifier packages "similaires" (meme ecosystem, meme categorie keywords)
- [ ] Ranking : popularity + health DriftLogg + activite recente

**Acceptance :** quand un user a moment.js en rouge, il voit "DriftLogg suggests : date-fns (score 92), dayjs (score 88), luxon (score 85)".

---

### Sprint 6 — STRIPE + BILLING (1.5 jour)
**But :** encaisser. Sans ca, rien ne sert.

- [ ] Setup Stripe Products : Pro EUR 29/mo, Team EUR 99/mo
- [ ] Stripe Checkout : redirige depuis `/pricing`
- [ ] Webhook handler `/api/webhooks/stripe` :
  - `checkout.session.completed` → upgrade user tier
  - `customer.subscription.deleted` → downgrade user
  - `invoice.payment_failed` → email + grace period 7 jours
- [ ] Customer Portal Stripe (lien depuis `/settings/billing`)
- [ ] Page `/billing` montre : plan actuel, prochaine facture, lien portal
- [ ] TVA : configurer Stripe Tax pour gestion UE automatique
- [ ] Coupon "EARLY50" : -50% a vie pour les 50 premiers Pro (early adopters)

**Acceptance :** un user clique "Upgrade to Pro" → paie → est upgrade instantanement.

---

## 6. DEPENDANCES / DECISIONS PRODUIT EN COURS

### A trancher avec le founder avant de coder
- [ ] **Domain name final** : driftlogg.com ? driftlogg.io ? .dev ?
- [ ] **Couleurs marque** : actuellement shadcn defaults — garder ou customiser ?
- [ ] **Devise primaire** : EUR (FR) ou USD (marche US plus gros) ? recommande EUR avec localisation USD via geo-IP

### Hors scope MVP (v2)
- Multi-user / seats (Sprint Team plus tard)
- SSO Google (Team feature)
- SBOM export CycloneDX
- API publique pour DriftLogg
- Webhook custom (pour CI/CD integrations type GitHub Action)
- Support GitLab / Bitbucket (npm/PyPI/Go/Maven first via GitHub)

---

## 7. CONTRAINTES TECHNIQUES IMPORTANTES

- **Rate limit GitHub API** : 5000 req/h authentifie. Pour 100 users x 50 repos = 5000 repos scannes/jour. Bien dispatcher avec queue (BullMQ ou simple delay).
- **Vercel Cron** : max 60s per job en Pro. Pour le daily scan : utiliser fan-out pattern (1 cron qui enqueue, plusieurs invocations qui consomment).
- **Resend free** : 3000 emails/mois. Suffit jusqu'a ~750 users actifs (4 emails/mois chacun en moyenne).
- **Supabase free** : 500MB DB, 2GB transfer. OK pour les premiers 200 users.

---

## 8. PRIORITE D'EXECUTION

Si on doit couper, voici l'ordre de priorite par ROI :

```
PRIORITE 1 (bloquant pour vendre)
  Sprint 1 : Repositionnement
  Sprint 2 : Auth + Dashboard
  Sprint 6 : Stripe billing

PRIORITE 2 (essentiel a la valeur Pro)
  Sprint 3 : Monitoring continu + digest email
  Sprint 5 v1 : Alternative recommendation (curated)

PRIORITE 3 (nice to have, ouvre marche team)
  Sprint 4 : Slack
  Sprint 5 v2 : Alternatives automatiques
```

→ Le founder peut commencer outreach **apres Sprint 1+2+3+6**. Sprint 4-5 viennent ensuite mais peuvent etre commercialisees en "coming soon" sans bloquer les ventes.

---

## 9. CHECKLIST DE LANCEMENT (apres Sprint 6)

- [ ] Domain Verification + SSL
- [ ] Robots.txt + sitemap.xml
- [ ] Google Search Console + indexation des pages SEO
- [ ] Plausible Analytics (PostHog si tu veux event tracking)
- [ ] Sentry pour erreur monitoring
- [ ] Tests E2E (Playwright) sur les flows critiques : signup, add repo, scan, upgrade
- [ ] CGV + Politique de confidentialite RGPD
- [ ] Page status (Better Stack ou Instatus)
- [ ] Twitter/X account, LinkedIn page de marque (a remplir manuellement)

---

## 10. ESTIMATION CUMULEE

| Sprint | Effort | Cumul |
|--------|-------:|-------:|
| 1 - Repositionnement | 3j | 3j |
| 2 - Auth + Dashboard | 3-4j | 6-7j |
| 3 - Monitoring + Email | 3j | 9-10j |
| 4 - Slack | 2j | 11-12j |
| 5 - Alternatives v1 | 3-5j | 14-17j |
| 6 - Stripe | 1.5j | **15-18j cumules** |

> Assiste par Claude Code en mode focus, ces 15-18 jours peuvent etre comprimes en 3-4 semaines calendaires en parallele d'un CDI.

---

**Fin de brief.**
Toute question, demander au founder avant d'inventer une decision produit.
