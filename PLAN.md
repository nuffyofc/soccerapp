# Overall Plan — "Who's Better?"

A swipe-based A-vs-B comparison game. Users pick between two players; the app instantly shows what % of everyone else picked the same one. Built for virality with a Gen Z / IG-TikTok-YT Shorts audience. See [DESIGN.md](DESIGN.md) for the visual design plan.

## Concept
Higher/Lower-style "would you rather" game for World Cup soccer players (MVP), expandable later to NBA, CS2 esports, and movie actors. Not a stats quiz — pure preference polling, with the % result and a shareable result card as the core hook.

## MVP Scope: Player Pool
- World Cup national teams (2026 tournament), ~8-10 marquee countries (Brazil, Argentina, France, England, Portugal, Spain, Germany, etc.)
- Top 6-8 recognizable players per country = ~60-80 players total
- Static JSON dataset, curated for star power/recognizability over tactical accuracy
- Player fields: `id, name, country, photoUrl, flagEmoji`

## Core Loop (Swipe Mechanic)
1. Two player cards shown, full-bleed vertical, mobile-first
2. User swipes left/right (or taps) to pick — instant, no confirmation step
3. Inline result appears immediately: animated % bar showing the split, plus total vote count
4. Auto-advance to next pairing (~1s delay, no button press needed)
5. Pairing algorithm prioritizes **close-split matchups** (45-55% range) once enough votes exist — these are the ones people screenshot and argue about
6. After a fixed session (e.g. 10 rounds), show a **shareable summary card** ("You're in the 6% minority club") with one-tap export to IG Stories/TikTok

## MVP Feature: Hot Debates Leaderboard
A read-only screen showing today's closest-split matchups site-wide (pairs in the 40-60% range, sourced from the same pairing algorithm data — see [STRATEGY.md](STRATEGY.md#3-algorithm-plan)). No accounts, no new data model — reuses existing vote counts. Functions as both a competition hook ("what's everyone arguing about") and a re-open/discovery trigger. Kept deliberately simple for MVP: a ranked list of matchups with their live split %, tappable to jump straight into that specific comparison.

## Virality Mechanics
- Shareable result card is the primary distribution/growth channel — auto-generated, branded, one tap to share
- Minority/majority framing ("Only 6% agree with you") drives ego-driven shares
- Rivalry-first pairing surfaces nationally-loaded or classic matchups early (Messi vs Ronaldo, historic rivalries)
- Zero friction: no login, no loading screen, first swipe within seconds of opening

## Data & Backend
- Table: `votes(player_a_id, player_b_id, winner_id, count)`, normalized pair ordering so A-vs-B and B-vs-A share one row
- Increment on each vote, compute % from the two counts on read
- Backend: Supabase (Postgres + auto REST API) — fastest path to a working backend without hosting custom server code
- Anonymous voting, no auth for MVP

## Screens
1. **Swipe screen**: full-bleed card stack, inline animated % result, auto-advance
2. **Share/summary screen**: end-of-session shareable result card + "play again"
3. **Hot Debates screen**: ranked list of today's closest-split matchups, tappable into that comparison

## Tech Stack
- Frontend: React Native (Expo) if targeting an actual mobile app for app-store discovery — this audience lives in apps, not mobile web. Alternative: mobile-optimized React web app to skip app-store review cycles for MVP speed.
- Backend/DB: Supabase
- Share-card generation: client-side canvas/html-to-image (fast, free, no server rendering needed)
- Hosting (if web): Vercel/Netlify

## Phase 2 (post-validation, not MVP)
- Additional categories: NBA, CS2 esports, movie actors — same swipe/vote/share mechanic, new datasets
- Cross-category discovery (finish soccer deck, get suggested NBA deck)
- **Trivia mode**: quiz questions about players/clubs with correct answers and scoring — a genuinely different game mechanic from the preference-swipe loop, needs its own curated answer-key dataset. Natural fit alongside multi-category expansion (e.g. club trivia next to a club "who's better" deck).
- **Daily crossword**: one crossword puzzle per day per category (soccer terms/player names, later NBA/CS2/movies), Wordle-style daily-ritual mechanic. Needs its own puzzle-generation/curation pipeline and grid-solving UI — distinct enough from the swipe loop that it should be validated as its own feature after the core loop proves out, not bundled into MVP.
- Personal streak tracking across sessions — needs accounts or durable local state, and rewards solo grinding over the share/argue behavior the MVP is optimized for

## Out of Scope for MVP
- Multi-category (ship World Cup soccer only first)
- Trivia mode and daily crossword (see Phase 2 — both are separate game mechanics from the core swipe loop and would roughly double MVP build scope)
- User accounts, streak tracking across sessions, filtering by position/team
- Any "correct answer" or stats-backed scoring in the core loop — that loop is preference polling, not trivia (trivia's correct-answer scoring lives in its own Phase 2 mode)

## Open Questions
1. Native app (Expo/React Native) or mobile web first?
2. Final list of 8-10 countries + player rosters — draft needed
3. Session length: fixed 10 rounds then share card, or endless scroll with periodic share prompts?
4. Brand accent color and sound-on-by-default vs off (see [DESIGN.md](DESIGN.md) open decisions)
