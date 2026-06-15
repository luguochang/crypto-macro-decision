# Data Sources

Use primary or near-primary sources where possible. For unstable market facts, always refresh by web search or API.

## Exchange And Crypto

OKX public APIs:

- Ticker: `https://www.okx.com/api/v5/market/ticker?instId={INST_ID}`
- Candles: `https://www.okx.com/api/v5/market/candles?instId={INST_ID}&bar=1H&limit=48`
- Funding: `https://www.okx.com/api/v5/public/funding-rate?instId={INST_ID}`
- Open interest: `https://www.okx.com/api/v5/public/open-interest?instId={INST_ID}`
- Mark price: `https://www.okx.com/api/v5/public/mark-price?instType=SWAP&instId={INST_ID}`
- Index ticker: `https://www.okx.com/api/v5/market/index-tickers?instId={INDEX_ID}`
- Books: `https://www.okx.com/api/v5/market/books?instId={INST_ID}&sz=10`

Common instruments:

- `BTC-USDT-SWAP`
- `ETH-USDT-SWAP`
- `SOL-USDT-SWAP`

Only pull non-core instruments when the user explicitly asks for them.

Flows and derivatives:

- Farside BTC ETF flows: `https://farside.co.uk/btc/`
- CoinGlass: liquidation, long/short, options max pain.
- Deribit: options expiry policy and BTC/ETH options data.
- DefiLlama: stablecoin supply, TVL, unlock references.
- Tokenomist / TokenTrack / CoinMarketCal: token unlocks and events only for explicitly requested non-core tokens. Cross-check; do not trust one source.

## Macro

Official:

- Federal Reserve FOMC calendar: `https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm`
- Federal Reserve H.15 rates: `https://www.federalreserve.gov/releases/h15/`
- BLS CPI: `https://www.bls.gov/news.release/cpi.nr0.htm`
- BLS PPI: `https://www.bls.gov/news.release/ppi.nr0.htm`
- BLS Employment Situation: `https://www.bls.gov/news.release/empsit.htm`
- BEA PCE and release schedule: `https://www.bea.gov/news/schedule`
- U.S. Treasury rates: `https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics`
- FRED 10Y real yield: `https://fred.stlouisfed.org/series/DFII10`

Market:

- Cboe VIX: `https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv`
- CME FedWatch: `https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html`
- DXY, WTI, Brent, Nasdaq/QQQ: use reputable market data.
- MacroMicro / Investing / Trading Economics / Econoday: consensus expectations when official sources provide release schedules but not market consensus. Cross-check if possible.

News:

- Reuters, AP, Bloomberg, CNBC for breaking geopolitical and macro news.
- For geopolitics, use at least two independent reputable sources before treating a claim as confirmed.
- Use recency and timestamps. News about war, oil, sanctions, central banks, and IPOs changes quickly.

## Mandatory Live Search Sweep

For any live trade call, run a targeted sweep instead of relying on one search result. Use the relevant lanes below and prefer recency filters when available.

### Breaking Geopolitics / Oil

Use when there is war, ceasefire, sanctions, Strait of Hormuz, Israel/Iran, U.S./Iran, Russia/Ukraine, Red Sea, or oil-shipping risk.

- `Reuters Iran ceasefire agreement Strait of Hormuz oil today`
- `AP Iran ceasefire agreement oil markets today`
- `Bloomberg Iran ceasefire oil Strait Hormuz markets today`
- `CNBC oil prices Iran ceasefire risk assets today`
- `WTI Brent crude today Iran ceasefire`

Decision use:

- Confirmed ceasefire or shipping reopening usually reduces oil-risk premium.
- Lower oil reduces inflation fear, supports rate-cut expectations, and can support BTC/ETH/SOL if yields/DXY confirm.
- Failed ceasefire, sanctions, or shipping disruption raises oil and can pressure crypto through inflation and risk-off channels.

### Fed / Rates / Data Expectations

Use before CPI/PPI/PCE/NFP/FOMC or when yields move sharply.

- `CME FedWatch rate cut probability today`
- `June 2026 FOMC dot plot Powell preview consensus`
- `US CPI consensus forecast next release core CPI`
- `US PPI consensus forecast next release`
- `US PCE consensus forecast next release core PCE`
- `US nonfarm payrolls consensus forecast next release unemployment wage growth`
- `Treasury yield 2 year 10 year real yield today`

Decision use:

- Record consensus, prior value, actual value when released, and immediate market reaction.
- Trade the surprise versus consensus, not the headline alone.
- If actual data is not released yet, classify the market as pre-event positioning.

### Crypto Market Structure

Use for BTC/ETH/SOL futures decisions.

- `BTC ETF flows Farside latest`
- `Bitcoin Ethereum Solana funding open interest liquidation heatmap today`
- `BTC ETH SOL long short ratio CoinGlass today`
- `Deribit BTC ETH options expiry max pain current week`
- `stablecoin supply crypto market DefiLlama latest`

Decision use:

- BTC is the direction anchor.
- ETH/SOL longs require relative strength versus BTC plus non-crowded funding/OI.
- A crowded long setup can be bearish even with good news.

## Targeted Search Queries

Use targeted queries:

- `Reuters Bitcoin oil Iran FOMC today`
- `FOMC June 2026 dot plot Powell press conference`
- `BTC ETF flows Farside June 2026`
- `CPI PPI PCE release date official`
- `{asset} token unlock date source Tokenomist DefiLlama` only when user asks for that asset.

## Source Priority

1. Official source / exchange API.
2. Reputable market data.
3. Professional aggregator.
4. Reuters/AP/Bloomberg style news.
5. Social media only as sentiment, never as confirmed fact.
