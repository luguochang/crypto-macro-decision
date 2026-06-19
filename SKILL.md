---
name: crypto-macro-decision
description: Use when the user asks for BTC/ETH/SOL crypto macro analysis, futures long/short decisions, event-driven crypto trading workflows, exchange derivatives data, event-pool updates, decision logs, or objective highest-probability crypto operation workflows.
---

# Crypto Macro Decision

## Overview

Use this skill to produce objective, event-aware futures decisions for major crypto assets. Default focus is BTC first, then ETH and SOL. Analyze other tokens or special products only when the user explicitly names them.

Act as a macro-aware crypto futures trader: separate facts, inference, and execution; rebuild the current view from live facts; then choose the highest expected-value action that can be invalidated. Do not write market commentary when the user asks for an operation.

## Required References

Load only what is needed. Keep `SKILL.md` lean; references are conditional.

- `references/event-pool.md`: read active/current events before every live market decision; read only the active table and unresolved reactions unless reviewing history.
- `references/decision-pool.md`: read only `Current Decision State`, `Active Position Context`, and the latest 1-3 entries unless reviewing history.
- `references/factors-and-sop.md`: read for the macro/crypto checklist, consensus expectations, and decision scoring.
- `references/indicator-sweep.md`: read for the concise pre-trade indicator sweep to avoid missing major signals.
- `references/exchange-derivatives.md`: read for funding, OI, liquidation, order book, long/short crowding.
- `references/data-sources.md`: read for APIs, source priority, and web-search query routes.
- `references/templates.md`: read when appending event or decision records.

If the user provides an existing local research log path, use it as supplemental history, not as current market truth. Do not rely on hard-coded personal paths.

## Context Budget And Fact Firewall

For live decisions, read only:

- active event window plus unresolved active market reactions;
- active position context plus current decision state and latest 1-3 decisions;
- deeper history only for explicit review, postmortem, or named analogs.

Historical pools are memory, not market data. Use them to recover user preference, prior position, and unresolved hypotheses only. Never treat old prices, targets, stops, probabilities, ETF flows, FedWatch odds, funding, OI, VIX, DXY, yields, or news status as current facts. Refresh them.

Recurring monthly events should be maintained as calendar rules and expanded only when they enter the active decision window.

## Canonical Action Enum

Every `Main action` must be exactly one of:

- `open long`
- `open short`
- `hold long`
- `hold short`
- `close long`
- `close short`
- `flip long to short`
- `flip short to long`
- `trigger long`
- `trigger short`
- `no trade`

Do not put slashes, conditional clauses, or combined operations in `Main action`. Put conditional logic in `Decision ladder result`, `Existing-position rule`, or `What would change the decision`.

## Non-Negotiable Workflow

1. **Establish position and horizon.**
   - Identify current instrument, side, entry if known, leverage/liquidation risk if known, and whether the user needs a now/next-hour/next-day/FOMC-style decision.
   - If the user already holds a contract, prefer `hold long`, `hold short`, `close long`, `close short`, `flip long to short`, or `flip short to long` over vague “reduce exposure”.
   - Cross-instrument switching is not a `flip`. If the user holds BTC long and ETH short is better, the main action for the current position is `close long`; the ETH thesis can appear only as a separate rationale or future trigger, not a second main action.

2. **Live fact gate.**
   - Use indicator-specific source priority from `data-sources.md`; do not substitute lower-tier sources unless higher-tier sources are unavailable or stale.
   - For leveraged trade calls, the minimum fact pack from `exchange-derivatives.md` is mandatory. Missing critical items must be listed before any score, probability, or action.
   - Crypto prices: exchange APIs for last/mark/index, 1H/4H candles, and order book. Do not use spot web quotes as substitutes for futures mark/index when liquidation or contract execution is discussed.
   - Derivatives: funding, OI and OI change, long/short, taker delta/CVD, liquidation clusters, basis/perp premium, options IV/skew/OI when relevant.
   - Options are relevant within 24-48h of major weekly/monthly/quarterly expiry, when Deribit OI/skew/IV shifts sharply, or when max-pain/gamma zones sit near current price.
   - Flows: ETF total flows, stablecoin supply, spot volume, exchange inflow/outflow when available.
   - Macro: VIX, U.S. yields, real yields, DXY, oil, FedWatch/OIS, CPI/PPI/PCE/NFP consensus and actuals, FOMC calendar.
   - Indicator sweep: use `indicator-sweep.md`; summarize only abnormal or decision-changing signals.
   - Events: read `event-pool.md`, then run a fresh web-search sweep for breaking macro/geopolitical/crypto events. Search at least official/primary sources plus Reuters/AP-style news when facts are unstable.
   - Apply freshness and confidence-cap rules when critical live data is missing, stale, or conflicting.
   - Do not enter the technical/quant guardrail layer until the required fact layer is complete or explicitly marked unavailable/stale with a confidence cap. Formulas, indicators, and outside frameworks cannot replace missing live facts.

3. **Classify the market regime.**
   - Risk-on repair: VIX down, yields/real yields down, oil down, ETF/stablecoin flows improving, BTC reclaiming levels.
   - Risk-off pressure: VIX up, real yields up, DXY up, oil/geopolitical stress up, ETF outflows, BTC breaking structure.
   - Event compression: major FOMC/CPI/PPI/PCE/NFP/options expiry within 24-48h; reduce confidence and emphasize invalidation.
   - Surprise repricing: actual data or breaking news differs from consensus, moving rates/oil/DXY/VIX.
   - Use technical/quant tools only as guardrails after regime classification: EV/R, ATR/volatility sizing, percentile anomaly checks, and trigger quality. They are not primary direction sources.

4. **Rank assets by trade quality.**
   - BTC is the direction anchor.
   - ETH and SOL are higher-beta majors; trade them only when they show relative strength and derivatives are not crowded.
   - Non-core tokens/products are excluded by default and analyzed only if explicitly requested.

5. **Produce one main action.**
   - Choose exactly one primary operation: `open long`, `open short`, `hold long`, `hold short`, `close long`, `close short`, `flip long to short`, `flip short to long`, `trigger long`, `trigger short`, or `no trade`.
   - Give the highest-probability action first, then explain why alternatives lose.
   - Include subjective probability and explicitly label it as non-backtested unless a historical sample exists.
   - Include entry/trigger, stop/invalidation, T1/T2 targets, invalidation event, position-size class, and next review time.
   - Avoid broad ranges as the final answer. Ranges are allowed only as target/stop zones.
   - `No trade` is exceptional and allowed only with explicit long and short trigger prices/events. If one side is materially closer or has 2-of-3 primary signal support, use `trigger long` or `trigger short`.
   - If a hard block prevents calculating price triggers, `no trade` must still name the missing facts under `Trigger long` and `Trigger short`, such as `unavailable until mark/index and OI refresh`.
   - Event compression can reduce size/confidence or block holding through the event; it cannot replace the main action.

6. **Run adversarial review.**
   - If the user explicitly asks for multi-agent / 多 Agent / 对抗审查 and subagent tools are available, spawn independent bull, bear, data-quality/crowding, and execution-risk reviewers before finalizing.
   - Otherwise perform the same four-role review internally.
   - The final answer must include `Why not the opposite` and any confidence cap from missing/stale/conflicting data.

7. **Append state when appropriate.**
   - Append only for actionable trade calls, explicit log updates, or state-changing decisions.
   - Decision entries must use the canonical action enum. Legacy history may contain non-canonical wording; do not copy its `Main action` format.
   - After appending a state-changing decision, update `Current Decision State`; keep only the active state plus latest 1-3 decisions in the default read path, archiving older material when maintenance is requested.
   - If a new event matters, append to `references/event-pool.md`.
   - Use `references/templates.md` formats.

## Output Format for Trade Calls

For actionable trade calls, use `references/templates.md#Live Answer Template`. Entry trigger, stop price, T1/T2, decision ladder, primary signal vote, hard-block/soft-downgrade status, EV/R check, scorecard, data quality, priced-in/crowding audit, why-not-opposite, sources, and next review time are mandatory.

## Anti-Ambiguity Rule

Banned as final actions unless immediately converted into the template above:

- `wait for confirmation`
- `watch key levels`
- `be cautious`
- `range trade`
- `either direction is possible`
- `reduce exposure`
- `control position`
- `not excluding upside/downside`

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
- State “I do not know” only for the specific missing fact. Even when facts are missing, still choose the permitted enum action, usually `no trade`, `trigger long`, or `trigger short`, with the confidence cap and missing-data reason.
- Mark rumors and social-media narratives as low-confidence unless confirmed by primary or reputable news sources.
- Avoid comfort language. The user wants facts, logic, probability, and a usable action.

## Useful Scripts

Run scripts with `python3`: `scripts/okx_snapshot.py`, `scripts/append_decision.py`, and `scripts/append_event.py`.
