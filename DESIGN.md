# Visual Design Plan — "Who's Better?"

Research-backed design direction for a swipe-based A-vs-B comparison game targeting a Gen Z / IG-TikTok-YT Shorts audience (roughly ages 10-20).

## 1. Why visuals matter more than usual here

This app has almost no functional depth — the entire product IS the visual/interaction feel. Retention and shares live or die on how satisfying a single swipe feels, and how good the end-of-session result card looks as a screenshot. Design isn't decoration for this app, it's the core mechanic.

## 2. Research Summary

### Gen Z UI trends (2026)
- Gen Z favors **emotion and stimulation over minimalism** — bold color, energetic layouts, "tactile maximalism" (rich visuals, elements that look touchable/pressable).
- **Dark mode is the default surface**, not a toggle option — build the primary theme dark, with a light mode as secondary.
- **Motion communicates, it's not decoration** — micro-interactions (card tilt, button press states, haptic-style feedback) make the app feel alive and responsive.
- Visual-first content beats text — players process images far faster than copy, so lean on photos/flags/logos over labels.
- Social integration and instant share are expected as core features, not bolted-on afterthoughts.
- Retro-digital touches (Y2K chrome, glitch, pixelation) read as authentic/native to this generation if used as accents.

Sources: [Wildnet Edge](https://www.wildnetedge.com/blogs/how-gen-z-ui-ux-is-shaping-the-future-of-mobile-design), [Aufait UX — Tactile Maximalism](https://www.aufaitux.com/blog/tactile-maximalism-gen-z-ui/), [Muzli — Mobile App Design Trends 2026](https://muz.li/blog/whats-changing-in-mobile-app-design-ui-patterns-that-matter-in-2026/)

### Swipe-interaction design (Tinder-model best practices)
- Visual hierarchy: the card image should dominate the screen — nothing competes with it for attention.
- **Consistency is what makes swipe apps feel effortless** — same card shape, same button placement, same animation curve every single round.
- Must be **thumb-first**: swipe targets and any buttons live in the bottom two-thirds of the screen, one-handed reachable.
- 60fps is non-negotiable on the swipe/card transition — perceived jank kills the "addictive" feeling this app depends on.
- Each swipe should function as a **micro-decision with instant reward** — the % reveal is that reward, so it should animate in immediately, not after a delay.

Sources: [Medium — Tinder's UX/UI magic](https://medium.com/design-bootcamp/tinders-ux-ui-magic-crafting-connections-and-viral-engagement-1bbb0596c104), [Purrweb — Dating App UI/UX tips](https://www.purrweb.com/blog/tips-to-create-a-successful-dating-app-ui-and-ux/)

### Comparable product: The Higher/Lower Game
- Proven format already has traction with football/NBA/celebrity categories under one shared game shell — validates the multi-category direction.
- Keeps the **end screen minimal** — the score/result is the hero, everything else is stripped back so the result is what gets remembered and shared.
- Leaderboards and score-sharing are the retention/virality loop, not extra content.

Source: [DesignRush — Higher/Lower Game inspiration](https://www.designrush.com/best-designs/websites/the-higher-lower-game), [higherorlowergame.com](https://www.higherorlowergame.com/)

### Color psychology for this age group
- Save **saturated/neon accent colors for reward moments** (the % reveal, a share-card generation) — keep the base UI calmer so the payoff pops.
- Neon-on-dark ("cyberpunk-lite") palettes read as current and youth-coded for 2026, more than pastel or primary-color palettes (those skew younger/kids' apps).
- Team/country colors (flags, club crests) already provide built-in color variety per round — the app chrome around them should stay neutral (near-black background, white/gray text) so player colors don't clash.

Sources: [Vibeberry — Color Psychology in Interactive Gaming](https://vibeberry.io/blog/color-psychology-in-interactive-gaming-design), [A3logics — Color Psychology in Mobile App Design](https://www.a3logics.com/blog/color-psychology-in-mobile-app-development-design/)

## 3. Design Direction

**Aesthetic**: Dark-mode-first, neon accent, sports-card energy. Think TikTok LIVE overlay meets FIFA Ultimate Team card pack opening — bold, punchy, a little chaotic, never corporate.

### Palette
- Background: near-black (`#0B0B0F`) — makes photos and colors pop, matches dark-mode-default expectation
- Primary accent: electric green or hot pink/magenta (pick one as brand color) — reserved for the winning card highlight and CTA elements
- Secondary accent: electric blue or yellow — used for the % bar fill and share-card generation moment
- Text: off-white (`#F5F5F7`), muted gray (`#8A8A93`) for secondary text/counts
- Flags/crests/photos provide the "chaotic" color variety per round — app chrome stays neutral so it never clashes

### Typography
- One bold, condensed display font for player names and the % numbers (big, poster-like, screenshot-worthy) — e.g. a heavy grotesk like Clash Display, Neue Machina, or Inter Black as a free fallback
- Numbers (percentages) should be the single largest element on screen after the swipe — they're the "reward" and the most shareable data point

### Motion / Micro-interactions
- Card tilts and scales slightly under thumb during swipe drag (physical, tactile feel)
- Winning card "snaps" and glows/pulses in accent color on selection
- % bar fills with an animated count-up (0 → final %) over ~400-600ms, not an instant snap — this is the dopamine beat
- Losing card fades/shrinks slightly, doesn't just vanish
- Haptic tap on swipe release (native app) or a snappy sound-effect sting (web) reinforces the "reward" moment

### Result / Share Card
- Treated as its own designed artifact, not a UI screen — vertical 9:16 aspect ratio built specifically for IG Stories/TikTok/Shorts reposting
- Big bold headline stat ("You're in the 6% minority"), player photos, app logo/watermark small in corner
- Auto-generated client-side (canvas/html-to-image), one-tap export — friction here directly kills the share loop

### Sound (optional but recommended)
- Short, punchy UI sting on swipe (0.2-0.3s) — TikTok-native apps train users to expect audio feedback
- Mute-by-default with an easy toggle (many will play with sound off in public/school)

## 4. What to explicitly avoid
- Pastel/soft "kids app" palettes — reads too young for this audience, undercuts the competitive/rivalry tone
- Long onboarding, tutorials, or explainer text — show, don't tell; first swipe should happen in under 5 seconds
- Static, non-animated % reveal — the animation IS the reward, skipping it flattens the whole loop
- Cluttered stat overlays (leave deep stats/analytics out of MVP visuals entirely — this is a vibes/rivalry game, not a stats app)

## 5. Open Design Decisions
1. Pick one accent color as the true "brand" color (green vs pink vs blue) — recommend testing with target-age users if possible
2. Native app (richer haptics/animation control) vs mobile web (faster to ship, no app-store gate) — affects how much motion polish is realistically achievable in MVP
3. Sound on by default or off by default — off is safer for a "kids in class/quiet spaces" audience
