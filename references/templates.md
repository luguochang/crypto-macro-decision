# Templates

## Event Entry Template

```markdown
### YYYY-MM-DD HH:mm TZ - Event Name

- Category:
- Status: upcoming / active / past / breaking / resolved
- Source:
- Confidence: high / medium / low
- Assets affected:
- Why it matters:
- Consensus / expected:
- Actual / confirmed:
- Surprise vs expected:
- Bullish path:
- Bearish path:
- What to monitor:
- Next update time:
```

## Decision Entry Template

```markdown
### YYYY-MM-DD HH:mm TZ - Short Decision Title

- User position:
- Instrument:
- Main action: <exact enum only: open long / open short / hold long / hold short / close long / close short / flip long to short / flip short to long / trigger long / trigger short / no trade>
- Action validity check: single enum / no slash / no conditional main action
- Horizon:
- Last / mark / index price + timestamp/source/freshness:
- 1H / 4H candle timestamp:
- Order book timestamp/depth:
- Funding / OI timestamp:
- Data quality:
- Unavailable / stale data:
- Consensus / expected macro data:
- Actual / market reaction if released:
- Primary signal vote:
  - BTC structure:
  - Macro bridge:
  - Derivatives:
- Decision ladder result:
- No-trade / trigger boundary:
- Event compression matrix:
- Existing-position rule:
- Hard blocks:
- Soft downgrades:
- EV / RR gate:
- Scorecard:
  - BTC structure and momentum:
  - Macro bridge:
  - Derivatives:
  - Spot/ETF/stablecoin flows:
  - Asset relative strength:
  - Inflation/growth surprise:
  - Technical confirmation / execution quality:
  - Event risk / time compression:
  - Priced-in adjustment:
  - Crowding adjustment:
  - Auxiliary sentiment/on-chain/options:
  - Total:
- Entry trigger:
- Trigger type: orderable / recheck-only / not applicable
- Stop price:
- Targets:
  - T1:
  - T2:
- Risk/reward:
- Position size class:
- Subjective probability:
- Confidence cap reason:
- Event risk:
- Priced-in audit:
- Crowding audit:
- Why not the opposite:
  - For long: why not short.
  - For short: why not long.
  - For no trade: why not long / why not short / closer trigger.
  - For close: why not hold / why not flip.
  - For hold: why not close / why not flip.
- Reasons ranked:
  1.
  2.
  3.
- What changes the decision:
- Sources:
- Decision-pool update: append / do not append / append after user confirms position
- Next review time:

Review:
- 24h result:
- 72h result:
- 7d result:
- Error category:
- Model adjustment:
```

## Live Answer Template

```text
Main action: <exact enum only: open long / open short / hold long / hold short / close long / close short / flip long to short / flip short to long / trigger long / trigger short / no trade>
Action validity check: single enum / no slash / no conditional main action
Instrument:
Horizon:
Last / mark / index price + timestamp/source/freshness:
1H / 4H candle timestamp:
Order book timestamp/depth:
Funding / OI timestamp:
Data quality:
Unavailable / stale data:
Derivatives confirmation:
- Funding:
- OI 1h/4h/24h:
- Long/short:
- Liquidation:
- Taker/CVD:
- Basis:
- Options if relevant:
Cross-exchange conflicts:
Primary signal vote:
Decision ladder result:
No-trade / trigger boundary:
Event compression matrix:
Existing-position rule:
Hard blocks:
Soft downgrades:
EV / RR gate:
Scorecard:
Scorecard total:
Event risk:
Priced-in audit:
Crowding audit:
Subjective probability:
Confidence cap reason:
Entry trigger:
Trigger type: orderable / recheck-only / not applicable
Stop price:
Targets:
- T1:
- T2:
Risk/reward:
Position size class:
Invalidation event/price:
Do-not-hold-through event:
Why this is the highest-probability path:
Why not the opposite:
- For long: why not short.
- For short: why not long.
- For no trade: why not long / why not short / closer trigger.
- For close: why not hold / why not flip.
- For hold: why not close / why not flip.
Sources used:
Decision-pool update: append / do not append / append after user confirms position
What would change the decision:
Next review time:
```

For `no trade`, fill both:

```text
Trigger long:
Trigger short:
```

For `trigger long` or `trigger short`, `Entry trigger` is the actionable trigger. `Trigger type` must be `orderable` only when stop, T1/T2, and RR are valid; otherwise use `recheck-only` and list the data that must refresh before execution. Put the opposite-side trigger or invalidation under `What would change the decision`.

For `no trade` caused by missing critical facts, `Trigger long` and `Trigger short` may be `unavailable until [specific missing facts] refresh`; include the next review time.

The live answer must not end with balanced commentary. Put sources and decision-pool status before the final two fields, then end with `What would change the decision` and `Next review time`.
