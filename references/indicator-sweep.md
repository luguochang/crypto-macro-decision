# Indicator Sweep

Use this concise sweep before any live BTC/ETH/SOL futures decision. Do not explain every item in the final answer; surface only signals that change the action, probability, target, stop, or next check time.

## 12-Point Sweep

| Area | Indicator | Check | Trade Use |
|---|---|---|---|
| Price anchor | BTC 1H/4H structure | Reclaim/break key levels, higher high/lower low | Do not long ETH/SOL against weak BTC |
| Relative strength | ETH/BTC, SOL/BTC, SOL/ETH | Stronger or weaker than BTC | Choose BTC when majors lag |
| Derivatives | Funding rate | Flat/negative vs extreme positive/negative | Avoid crowded side; negative funding + rising price can squeeze shorts |
| Derivatives | Open interest | Price up/down with OI up/down | Detect fresh leverage, short covering, or trapped longs |
| Derivatives | Long/short + taker buy/sell | Crowd leaning one way? | Penalize trades that chase a crowded side |
| Liquidation risk | Liquidation heatmap / obvious stop clusters | Nearest large clusters above/below | Set invalidation away from obvious sweep zones |
| Options | BTC/ETH max pain + expiry OI | Weekly/monthly expiry pressure | Beware pinning or volatility release near expiry |
| Flows | BTC ETF total net flow | Total inflow/outflow, not one fund | Persistent inflow supports BTC; outflow weakens rallies |
| Liquidity | Stablecoin supply / exchange dry powder | Expanding or contracting | Expansion supports risk appetite; contraction lowers dip-buying power |
| Sentiment | Fear & Greed Index | Extreme fear/greed and change vs prior day/week | Contrarian input only; not a standalone signal |
| Cycle/on-chain | MVRV, NUPL, SOPR if available | Profit/loss regime and realized selling | Useful for cycle context, weaker for intraday entries |
| Macro bridge | FedWatch, 2Y/10Y, real yield, DXY, VIX, oil | Direction after latest data/news | Macro confirmation can override crypto-only signals |

## Source Routes

- Day1Global BTC model as checklist inspiration, not a live data source: `star23/Day1Global-Skills`.
- OKX public API for BTC/ETH/SOL price, funding, OI, mark/index, candles, books.
- CoinGlass for funding heatmap, OI, liquidation heatmap, long/short, taker flow, options/max pain.
- Farside or equivalent for BTC ETF total net flows.
- DefiLlama for stablecoin supply and DeFi liquidity context.
- Alternative.me Fear & Greed API for sentiment.
- Glassnode/CryptoQuant/LookIntoBitcoin-style sources for MVRV/NUPL/SOPR when accessible.
- CME FedWatch, Treasury/FRED/Cboe and reputable market data for rate path, yields, VIX, DXY, oil.

## Minimal Final Signal Rule

After scanning, classify each bucket as `bullish / bearish / neutral / unavailable`. If 3+ high-quality buckets conflict, lower confidence and prefer `no trade` or tighter invalidation. If BTC structure, macro bridge, and derivatives all align, allow a clearer long/short call.
