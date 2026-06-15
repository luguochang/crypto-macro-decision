---
name: crypto-macro-decision
description: Use when the user asks for BTC/ETH/SOL crypto macro analysis, futures long/short decisions, event-driven crypto trading, exchange derivatives data, event-pool updates, decision logs, or objective highest-probability crypto operation advice.
---

# Crypto Macro Decision

## Overview

Use this skill to produce objective, event-aware futures decisions for major crypto assets. Default focus is BTC first, then ETH and SOL. Analyze other tokens or special products only when the user explicitly names them.

Always separate facts, inference, and trade action. Always record the decision for later review when the user asks for an actionable market call.

## Required References

Load only what is needed. Keep `SKILL.md` lean; references are conditional.

- `references/event-pool.md`: read active/current events before every live market decision; update breaking events.
- `references/decision-pool.md`: read only active position and recent decisions unless reviewing history.
- `references/factors-and-sop.md`: read for the macro/crypto checklist, consensus expectations, and decision scoring.
- `references/exchange-derivatives.md`: read for funding, OI, liquidation, order book, long/short crowding.
- `references/data-sources.md`: read for APIs, source priority, and web-search query routes.
- `references/templates.md`: read when appending event or decision records.

If the user mentions an existing local research log, read it too. If `/Users/chase/Desktop/codex/self/jiamihuobi/crypto_macro_research_log_2026-06-14.md` exists, use it as supplemental history, not as current market truth.

For context control, read active/current sections first. Do not load or restate long historical archives unless the user asks for review or the current decision depends on a past analog. Recurring monthly events should be maintained as calendar rules and expanded only when they enter the active decision window.

## Non-Negotiable Workflow

1. **Establish position and horizon.**
   - Identify current instrument, side, entry if known, leverage/liquidation risk if known, and whether the user needs a now/next-hour/next-day/FOMC-style decision.
   - If the user already holds a contract, prefer `hold / close / switch / flip` over vague “reduce exposure”.

2. **Refresh live facts.**
   - Crypto prices: use exchange APIs, preferably OKX for BTC/ETH/SOL instruments.
   - Derivatives: funding, open interest, mark price, index price, candles, order book, and liquidation/long-short data when available.
   - Macro: VIX, U.S. yields, real yields, DXY, oil, FedWatch/OIS, CPI/PPI/PCE/NFP consensus and actuals, FOMC calendar.
   - Events: read `event-pool.md`, then run a fresh web-search sweep for breaking macro/geopolitical/crypto events. Search at least official/primary sources plus Reuters/AP-style news when facts are unstable.

3. **Classify the market regime.**
   - Risk-on repair: VIX down, yields/real yields down, oil down, ETF/stablecoin flows improving, BTC reclaiming levels.
   - Risk-off pressure: VIX up, real yields up, DXY up, oil/geopolitical stress up, ETF outflows, BTC breaking structure.
   - Event compression: major FOMC/CPI/PPI/PCE/NFP/options expiry within 24-48h; reduce confidence and emphasize invalidation.
   - Surprise repricing: actual data or breaking news differs from consensus, moving rates/oil/DXY/VIX.

4. **Rank assets by trade quality.**
   - BTC is the direction anchor.
   - ETH and SOL are higher-beta majors; trade them only when they show relative strength and derivatives are not crowded.
   - Non-core tokens/products are excluded by default and analyzed only if explicitly requested.

5. **Produce one main action.**
   - Give the highest-probability action first.
   - Include subjective probability and explicitly label it as non-backtested unless a historical sample exists.
   - Include invalidation price/event, target, and the next time to ask again.
   - Avoid broad ranges as the final answer. Ranges are allowed only as target/stop zones.

6. **Append state when appropriate.**
   - If a decision is made, append to `references/decision-pool.md`.
   - If a new event matters, append to `references/event-pool.md`.
   - Use `references/templates.md` formats.

## Output Format for Trade Calls

Use this structure for actionable requests:

```text
Main action:
Instrument:
Side:
Current price/time/source:
Subjective probability:
Targets:
Stop / invalidation:
Do-not-hold-through event:
Why this is the highest-probability path:
What would change the decision:
Next check time:
Sources used:
Decision-pool update:
```

## Decision Rules

- If BTC is strong and funding is not crowded, prefer BTC long over weaker assets.
- If BTC is weak, avoid ETH/SOL longs unless they show clear independent relative strength.
- If BTC is weak and ETH/SOL are weaker, short only after BTC structure confirms weakness and derivatives are not already extremely crowded.
- If a major event is within 24 hours, distinguish “can hold into target” from “should not hold through event”.
- If funding is extreme positive and OI is rising, do not chase longs blindly.
- If funding is negative while price rises, shorts may be trapped; continuation probability improves.
- If ETF flows are cited, verify the total column, not only IBIT/one-fund flows.
- If consensus macro data is cited, compare actual vs expected and market reaction; the surprise matters more than the headline alone.
- If a ceasefire/oil/geopolitical claim is cited, verify with at least two reputable sources or mark it as unconfirmed.

## Objective Tone Requirements

- Do not preserve old conclusions for consistency. Re-evaluate from latest data.
- State “I do not know” only when key facts cannot be verified; otherwise choose the best-probability action.
- Mark rumors and social-media narratives as low-confidence unless confirmed by primary or reputable news sources.
- Avoid comfort language. The user wants facts, logic, probability, and a usable action.

## Useful Scripts

- `scripts/okx_snapshot.py`: fetch OKX ticker, funding, open interest, mark/index price, candles, and order book for common instruments.
- `scripts/append_decision.py`: append a structured decision entry to `references/decision-pool.md`.
- `scripts/append_event.py`: append a structured event entry to `references/event-pool.md`.

Run scripts with `python3`.
