# Exchange Derivatives Checklist

Use this reference whenever the user trades futures/contracts or asks about long/short, liquidation, funding, OI, order book, or “庄家收割”.

## Core Data

For each traded instrument, collect:

- Last price.
- Mark price.
- Index price.
- 24h high/low.
- Funding rate and next funding time.
- Open interest in coin and USD.
- 1H and 4H candles.
- Order book depth near price.
- Long/short ratio and liquidation heatmap if available from external sources.

## Interpretation Rules

### Funding

- Mild positive: normal in an uptrend.
- Extreme positive: crowded longs; beware long squeeze.
- Mild negative while price rises: shorts may be paying; continuation can improve.
- Extreme negative: crowded shorts; beware squeeze up.

### Open Interest

- Price up + OI up: new leverage entering; trend can continue but watch crowding.
- Price up + OI down: short covering; less reliable continuation.
- Price down + OI up: new shorts or trapped longs; watch liquidation.
- Price down + OI down: deleveraging; may stabilize after flush.

### Mark vs Last

- Mark price drives liquidation. Do not rely only on last price.
- If mark is below last for a long position, liquidation risk is worse than the screen may feel.
- For thin event products requested by the user, mark/index stability is central.

### Order Book And “Harvest” Risk

Crypto is semi-transparent:

- Liquidation clusters can be targeted.
- Stop zones near obvious levels can be swept.
- Thin order books amplify wicks.
- Events with high OI and extreme funding attract stop hunts.

Mitigation:

- Do not place stops exactly at obvious round numbers if the user has flexibility.
- Prefer structural invalidation zones over arbitrary tiny stops.
- Do not hold high leverage through major macro events unless explicitly intended.

## Product-Specific Notes

### BTC

BTC is the direction anchor. If funding is not crowded and macro is risk-on, BTC long is usually cleaner than weak altcoin long.

### ETH

ETH is a higher-beta major. Prefer ETH long only when ETH/BTC is stable or rising and funding is not crowded.

### SOL

SOL is a high-beta major. Prefer SOL long only when SOL/BTC and SOL/ETH show relative strength and derivatives are not crowded.

### Non-Core Assets

Analyze token unlocks, special product rules, premium/discount, or chain-specific events only when the user explicitly asks.

## Minimal OKX API Targets

- Ticker: `https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT-SWAP`
- Funding: `https://www.okx.com/api/v5/public/funding-rate?instId=BTC-USDT-SWAP`
- OI: `https://www.okx.com/api/v5/public/open-interest?instId=BTC-USDT-SWAP`
- Candles: `https://www.okx.com/api/v5/market/candles?instId=BTC-USDT-SWAP&bar=1H&limit=48`
- Books: `https://www.okx.com/api/v5/market/books?instId=BTC-USDT-SWAP&sz=10`
- Mark: `https://www.okx.com/api/v5/public/mark-price?instType=SWAP&instId=BTC-USDT-SWAP`
