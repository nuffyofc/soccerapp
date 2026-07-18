# Strategy — Competitive Analysis, Virality, Algorithm & Monetization

Companion to [PLAN.md](PLAN.md) and [DESIGN.md](DESIGN.md).

## 1. Competitive Analysis

### Direct comparables

**"Would You Rather?" apps (Live Polls, Viral Game)**
- Live Polls has 6M+ votes logged and runs limited-time themed packs — notably a **"Football 2026" pack**, confirming sports-specific packs work as a content strategy, not just generic party-question content.
- Viral Game (5M+ downloads) positions itself as a social network built entirely around the vote-then-compare loop, and lets users submit their own questions — community content extends the app's lifespan past what the founding team can hand-curate.
- **Takeaway**: the "pick one, then see the crowd's answer" loop alone is a proven, multi-million-download mechanic even with zero stats/skill layer. Validates this app's core loop as sufficient on its own.

**GOAT Debate / Vote The Goat**
- "Vote The Goat" runs live, continuously-updating GOAT rankings across sports, blending fan votes with stats/titles/cultural impact — shows demand for an always-live, never-"finished" ranking rather than a static list.
- The Messi vs Ronaldo GOAT debate is one of the most durable recurring viral topics on TikTok across years — a strong signal that soccer rivalry content specifically (not just sports content generally) has outsized organic reach in short-form video.
- **Takeaway**: lean harder into the Messi/Ronaldo-style rivalry framing in matchup selection, and treat "live, ever-updating" numbers as a feature to advertise, not just a backend detail.

**FIFA Rivals / stats-heavy football apps**
- These compete on data depth (careers, stats databases) — a different, more effortful product than this app is going for. **Confirms the right MVP lane is "no stats, pure vibes/preference"** — competing on data depth would mean competing with EA's resources, which is not winnable for an MVP.

### Positioning
This app should sit in the white space between "Would You Rather" (broad, low-effort, not sports-specific) and "Vote The Goat" (sports-specific, stats-heavy) — a **soccer/World Cup-first, zero-stats, pure-preference swipe game** with best-in-class shareable result cards. None of the comparables reviewed combine swipe-native UX (Tinder-style gesture) with sports preference polling — that combination is the differentiation.

Sources: [Would You Rather? Live Polls](https://apps.apple.com/us/app/would-you-rather-live-polls/id1352732673), [Would You Rather? Viral Game](https://apps.apple.com/us/app/would-you-rather-viral-game/id1011788068), [Vote The Goat 2026](https://www.vote-the-goat.com/), [Goat Debate App](https://apps.apple.com/us/app/goat-debate/id6752636742), [FIFA Rivals](https://apps.apple.com/us/app/fifa-rivals-mobile-soccer/id6746578704)

## 2. Virality Plan

Three loops, ranked by expected impact:

1. **Share-card loop (primary)**: every session ends in an auto-generated, vertical, watermarked result card built specifically for IG Stories/TikTok/YT Shorts reposting. This is the actual user-acquisition channel — treat the share button's conversion rate as the single most important growth metric in the product, above session length or DAU.
2. **Rivalry-content loop**: matchups modeled on proven durable viral topics (Messi vs Ronaldo-style) get surfaced preferentially, especially early in a session, to maximize the odds any given session produces a screenshot-worthy or comment-bait result.
3. **Hot Debates leaderboard (MVP)**: a read-only screen of today's closest-split matchups sitewide — see [PLAN.md](PLAN.md#mvp-feature-hot-debates-leaderboard). Costs nothing extra to build (reuses pairing-algorithm data) and doubles as a re-open/discovery trigger and a competitive/social hook without needing accounts or a friend graph.
4. **Community-submission loop (post-MVP, borrowed from Viral Game)**: once there's a real user base, let users propose matchups or new player pool entries. Keeps content fresh without founder-team curation bottleneck, and gives power users a reason to return.

**Distribution-specific tactics**:
- Design the share card at native aspect ratio for the target platform (9:16), not a generic square export — friction/format-mismatch kills repost rate.
- Timestamp/tournament-tie the content ("World Cup 2026 Edition") so it rides existing search and hashtag traffic rather than competing as a generic sports app.
- Keep a "your friend picked X, you picked Y" comparison mode on the roadmap (post-MVP) — direct friend-to-friend comparison is a stronger share trigger than a solo result, but adds account/identity complexity not worth taking on for MVP.

## 3. Algorithm Plan

### Goal
Two jobs: (1) pick which two players to show next, (2) compute and display the % split. Keep both simple for MVP — no ML needed.

### Pairing algorithm (MVP → v1.1)
**MVP (launch)**: weighted random pairing, avoiding repeat pairings within a session, with a **hand-tagged "rivalry" boost** — a small curated list of high-interest pairs (e.g. Messi/Ronaldo, England/Argentina rivals) gets 3-5x the sampling weight of a random pair. This requires zero live data and is enough to launch with strong content on day one.

**v1.1 (once vote volume exists)**: switch to **data-driven close-split surfacing** — once a pair has enough votes (e.g. n≥30), compute how close the split is to 50/50 and boost sampling weight for pairs in the 40-60% band. This is what actually produces "wait, WHAT, that's not right" reactions that drive shares, and it improves automatically as vote data accumulates — no manual curation needed at scale.

**Underlying rating layer (optional, v1.2+)**: maintain a lightweight **Elo-style rating per player**, updated on every vote (win = rating gain scaled by opponent's rating, per standard Elo). This isn't shown to users directly in MVP, but powers two future features cheaply: a "power rankings" leaderboard screen, and smarter pairing (match similarly-rated players more often, since close-rated pairs are more likely to produce close splits without needing accumulated vote history first). Standard Elo/pairwise-comparison approach — well-established for exactly this kind of "which of two is preferred" ranking problem.

### % display algorithm
- Store votes as `votes(pair_key, winner_id, count)` where `pair_key` normalizes (min_id, max_id) so A-vs-B and B-vs-A accumulate into the same row.
- % shown = `winner_count / total_count_for_pair * 100`, rounded to nearest whole number.
- **Cold-start handling**: for a brand-new pair with <10 votes, either (a) don't show a rivalry-tagged pair until it clears a minimum vote threshold, or (b) show "Be the first to decide!" instead of a misleading percentage from 1-2 votes. Recommend (b) for MVP — it's simpler and turns low sample size into a feature ("you're an early voter") rather than a bug.

Source: [Building a Multiplayer Elo Rating System](https://gautamnarula.com/rating/), [Toxic Algorithms: Elo Rating & Dating Apps](https://feministscientist.substack.com/p/toxic-algorithms-elo-rating-and-dating)

## 4. Paywall Placement Plan

### Core principle from research
Don't paywall on first open — users chose a free app deliberately, and a wall at open kills trust immediately. The highest-converting placement is generally **during or immediately after onboarding**, once the user has had at least one taste of the core loop, because motivation is highest right after install and a free trial makes upgrading feel low-risk. Paywalls also convert best when placed **around a core feature moment**, not as a random interstitial.

### Recommended placement for this app
1. **Do not paywall the core swipe/vote/% loop at all, ever.** That loop is the entire viral engine — gating it kills the share loop this app depends on to grow. Free, unlimited swiping should be the permanent free tier.
2. **First paywall touchpoint: end of first session, at the share-card screen** — not blocking the free/basic share card (that must stay free, it's the growth engine), but offering a **premium share-card style/frame/animated version** as a soft upsell. Low-friction, doesn't block anything the user came for.
3. **Second touchpoint: after ~3-5 completed sessions**, once the user has demonstrated real engagement (this is the "high engagement moment" the research flags as ideal timing) — offer a subscription unlocking:
   - Extra categories (NBA, CS2, actors) beyond a free-tier limit (e.g. soccer free, others behind paywall)
   - Personal stats/history ("your pick history", "your taste profile")
   - Ad-free experience, if ads are used in the free tier for extra revenue
   - Priority/exclusive rivalry packs (e.g. early access to new tournament-tie-in content)
4. **Never gate**: the swipe mechanic itself, the % reveal, or the basic share card — these three are the growth loop and must stay frictionless and free indefinitely.

### Suggested model
Freemium with a light subscription (not one-time IAP) — recurring category/content packs suit this app's format (new tournaments, new sports) better than a single unlock purchase. Consider a free trial on first subscription prompt, since trial offers measurably lift conversion at the onboarding-adjacent moment.

### Sequencing for actual MVP
Given this is still pre-launch, **ship with zero paywall** — the priority is proving the swipe+share loop drives organic growth at all. Introduce the first paywall (soft share-card upsell) only once there's real usage data to test against, and the multi-category paywall only once Phase 2 categories actually exist. Building monetization before the growth loop is validated is the main risk to avoid here.

Sources: [RevenueCat — Optimizing Paywall Placement](https://www.revenuecat.com/blog/growth/paywall-placement), [Adapty — How to Design a Paywall](https://adapty.io/blog/how-to-design-a-paywall-for-a-mobile-app/), [Adapty — Freemium Monetization Strategies](https://adapty.io/blog/freemium-app-monetization-strategies/)

## Open Decisions
1. Confirm rivalry-pair seed list for MVP launch (needs manual curation — who are the 15-20 must-have matchups on day one?)
2. Ads in free tier or subscription-only monetization (affects paywall touchpoint #3 design)
3. Minimum vote threshold for showing real percentages vs "Be the first to decide!" placeholder
