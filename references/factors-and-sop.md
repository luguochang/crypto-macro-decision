# Factors And SOP

## Purpose

This reference defines the broad factor map and standard operating procedure for objective crypto futures decisions. Use it to avoid one-factor analysis and to force a full scan before recommending long, short, hold, close, switch, or no trade.

## Factor Map

Default asset universe:

- Core: BTC, ETH, SOL.
- Non-core tokens, equity-linked perps, meme coins, unlock trades, and special products only when the user explicitly asks.

### 1. Macro Liquidity

Track:

- Fed policy path: FOMC, dot plot, Powell press conference, Fed speakers.
- FedWatch/OIS/SOFR futures: market-implied rate path, next-meeting hike/cut/hold odds, and year-end implied policy rate.
- U.S. 2Y/10Y yields and 10Y real yield.
- DXY: dollar strength.
- Treasury issuance, TGA, RRP, bank reserves, QT/QE when relevant.

Interpretation:

- Falling real yields + falling DXY + easing Fed expectations = supportive for BTC.
- Rising real yields + stronger DXY + more hawkish Fed path = pressure on crypto, especially altcoins.
- Rate-cut odds rising because inflation cools is generally bullish; rate-cut odds rising because recession/credit stress is not automatically bullish.

### 2. Inflation And Growth

Track:

- CPI and core CPI.
- PPI and core/final demand components.
- PCE and core PCE.
- NFP, unemployment rate, initial claims.
- Oil, gasoline, shipping/geopolitical energy risk.
- Consensus expectations, prior values, actual values, and revisions.

Interpretation:

- Headline inflation from energy can fade if oil reverses.
- Core inflation persistence matters more for Fed policy.
- Strong employment can delay cuts; very weak employment can create recession risk.
- The market trades the surprise: actual vs consensus plus the reaction in yields, DXY, VIX, and Nasdaq.

### 3. Expectations And Surprise

Track before each scheduled data event:

- Release time and timezone.
- Consensus estimate.
- Prior reading and revisions.
- Whisper/market positioning if reputable.
- FedWatch/OIS change before and after the release.
- Immediate reaction in 2Y yield, 10Y yield, real yield, DXY, VIX, Nasdaq, BTC.

Interpretation:

- Hot inflation + yields up + DXY up = bearish for BTC/ETH/SOL.
- Cool inflation + yields down + DXY down = supportive.
- Weak growth data can be bullish only if it increases easing expectations without triggering recession/liquidity stress.
- If data is known in advance as consensus, the trade setup comes from positioning and surprise, not the existence of the event.

### 4. Risk Appetite

Track:

- VIX and, if available, MOVE.
- Nasdaq/QQQ, S&P 500, high-beta growth, AI/tech.
- Credit spreads.
- Market breadth.
- Cross-asset reactions after major news.

Interpretation:

- VIX under 20 and falling supports risk repair, but does not guarantee altcoin strength.
- VIX above 25 with rising yields is a warning for liquidation pressure.

### 5. Crypto Funding And Flow

Track:

- BTC ETF total net flows, not one-fund flows.
- Stablecoin supply.
- Exchange inflow/outflow, especially after unlocks.
- BTC dominance and total altcoin market cap.
- Spot volume and order-book depth.

Interpretation:

- ETF total inflow supports BTC only if large enough and persistent.
- Stablecoin expansion suggests more dry powder.
- Exchange inflow after unlocks can convert potential supply into actual sell pressure.

### 6. Derivatives Positioning

Track:

- Funding rate.
- Open interest.
- Long/short ratio if available.
- Liquidation heatmaps.
- Mark price vs last price.
- Index price vs last price.
- Order-book depth and bid/ask gaps.

Interpretation:

- Price up + funding negative/flat = healthier long continuation; shorts may be trapped.
- Price up + funding extreme positive + OI rising = crowded long risk.
- Price down + OI rising + funding positive = trapped longs; potential cascade.

### 7. Asset-Specific Events

Track:

- BTC: ETF flows, dominance, miner/treasury flows, options expiry, macro sensitivity.
- ETH: ETF/staking/regulatory developments, ETH/BTC trend, on-chain fees, L2 activity.
- SOL: SOL/BTC and SOL/ETH relative strength, ecosystem flows, chain stability, major unlocks only if relevant.
- Non-core assets: unlocks, upgrades, listings, chain outages, TVL/stablecoin/DEX volume only when explicitly requested.

Interpretation:

- Single-token events rarely overpower macro risk-off.
- Good news in weak liquidity can become exit liquidity.
- Special event products require premium/discount and rule analysis, not simple narrative trading.

## Standard Operating Procedure

1. State current user position.
2. Pull live exchange data for BTC/ETH/SOL, plus user-held instrument.
3. Pull macro, consensus expectations, FedWatch/rate path, and breaking-event data.
4. Read active event pool and active decision context only.
5. Classify regime: risk-on, risk-off, event-compressed, or surprise repricing.
6. Score BTC first, then ETH/SOL or user-held asset.
7. Compare asset strength:
   - BTC vs ETH/SOL.
   - ETH/BTC and SOL/BTC.
   - User-requested non-core asset vs BTC/ETH/SOL only when needed.
8. Decide one action:
   - Hold existing long.
   - Close long.
   - Switch product.
   - Flip short.
   - No trade.
9. Give stop, target, invalidation event, and next check time.
10. Append to decision pool.

## Scoring Guide

Use subjective scoring unless a backtest exists.

| Score | Meaning |
|---:|---|
| +6 to +10 | Strong long regime |
| +3 to +5 | Tactical long |
| -2 to +2 | No strong edge / event compression |
| -3 to -5 | Tactical short |
| -6 to -10 | Strong short / liquidation risk |

Probability wording:

- 52%-55%: slight edge.
- 56%-62%: actionable edge with stop.
- 63%-70%: strong setup, still invalidatable.
- Above 70%: avoid unless backed by very clear evidence.

Always label as subjective probability unless backtested.
