# Crypto Macro Decision Skill

一个面向 Codex 的加密货币宏观交易决策 skill，默认聚焦 BTC、ETH、SOL，通过实时行情、衍生品结构、宏观预期、突发事件和复盘记录，输出更可执行的合约交易判断。

> Status: experimental research workflow. This project is not financial advice.

## What It Does

这个 skill 不是普通行情评论模板，而是一套可迁移的交易决策流程。它会强制分析：

- BTC / ETH / SOL 的实时价格、资金费率、未平仓合约、标记价、指数价和 K 线结构。
- FOMC、CPI、PPI、PCE、非农、FedWatch 降息/加息预期等宏观因素。
- 地缘冲突、油价、美元指数、美债收益率、VIX、纳指等跨市场风险偏好。
- ETF 资金流、稳定币供应、期权交割、爆仓热力图、多空拥挤度。
- 当前事件池和历史决策池，避免遗漏关键事件，也避免被旧判断锚定。

最终目标是让 Codex 在用户询问加密货币合约操作时，不只给“可能上涨也可能下跌”的宽泛结论，而是输出一个主操作：

- `hold long`
- `close long`
- `flip short`
- `hold short`
- `close short`
- `switch product`
- `no trade`

每次交易建议都应包含主观概率、目标、止损/失效位、事件风险、改变判断的条件和下一次检查时间。

## Why It Exists

加密货币尤其是合约市场很容易被单一叙事误导。常见错误包括：

- 只看新闻标题，不看市场是否已经提前定价。
- 只看 CPI / PCE 数字，不看市场预期和实际值的差异。
- 只看 BTC 价格，不看资金费率、OI、爆仓区和订单簿。
- 只看某个币的利好，不看它相对 BTC / ETH / SOL 是否走弱。
- 只记得上一次判断，后续不复盘，也不修正模型。

这个 skill 的设计目标是把这些问题压进一个固定流程：先查事实，再看预期差，再判断市场反应，最后给出可验证的交易动作。

## Default Asset Universe

默认关注：

- `BTC-USDT-SWAP`
- `ETH-USDT-SWAP`
- `SOL-USDT-SWAP`

非核心资产、meme、解锁币、股票映射合约、特殊事件产品默认不分析。只有用户明确点名时，才进入专项分析，避免噪音污染主判断。

## Repository Layout

```text
crypto-macro-decision/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── data-sources.md
│   ├── decision-pool.md
│   ├── event-pool.md
│   ├── exchange-derivatives.md
│   ├── factors-and-sop.md
│   ├── indicator-sweep.md
│   └── templates.md
└── scripts/
    ├── append_decision.py
    ├── append_event.py
    └── okx_snapshot.py
```

## Key Files

| File | Purpose |
|---|---|
| `SKILL.md` | Codex skill 入口，定义触发条件、核心流程和输出格式。 |
| `references/data-sources.md` | 数据源、API、Web Search 路线和来源优先级。 |
| `references/event-pool.md` | 活跃事件池，用于跟踪未来事件和突发风险。 |
| `references/decision-pool.md` | 决策池，用于记录仓位上下文和交易复盘。 |
| `references/factors-and-sop.md` | 宏观、预期差、衍生品、情绪和品种强弱分析 SOP。 |
| `references/indicator-sweep.md` | 每次交易前的精简指标扫描清单，避免遗漏核心信号。 |
| `references/exchange-derivatives.md` | 合约市场检查清单：资金费率、OI、标记价、订单簿等。 |
| `references/templates.md` | 事件记录、决策记录和实时回答模板。 |
| `scripts/okx_snapshot.py` | 拉取 OKX 合约行情、资金费率、OI、标记价、K 线和订单簿。 |
| `scripts/append_event.py` | 向事件池追加结构化事件记录。 |
| `scripts/append_decision.py` | 向决策池追加结构化交易决策。 |

## Installation

把仓库放到 Codex skills 目录下：

```bash
mkdir -p ~/.codex/skills
git clone <your-repo-url> ~/.codex/skills/crypto-macro-decision
```

如果你已经在本地维护这个目录，可以直接把仓库内容同步到：

```text
~/.codex/skills/crypto-macro-decision
```

## Requirements

- Codex skill runtime.
- Python 3.
- Network access for exchange APIs and live web search.
- No OKX API key is required for the bundled public-market snapshot script.

## Quick Start

验证 skill 结构：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/crypto-macro-decision
```

抓取默认 BTC / ETH / SOL 的 OKX 合约快照：

```bash
python3 ~/.codex/skills/crypto-macro-decision/scripts/okx_snapshot.py
```

包含 1H / 4H K 线：

```bash
python3 ~/.codex/skills/crypto-macro-decision/scripts/okx_snapshot.py --candles
```

包含订单簿：

```bash
python3 ~/.codex/skills/crypto-macro-decision/scripts/okx_snapshot.py --books
```

指定其他交易对：

```bash
python3 ~/.codex/skills/crypto-macro-decision/scripts/okx_snapshot.py BTC-USDT-SWAP ETH-USDT-SWAP
```

## Example Prompts

可以在 Codex 中这样问：

```text
根据当前 BTC/ETH/SOL 实时价格、宏观事件和衍生品结构，给我一个本周合约胜率最高的主操作。
```

```text
我现在持有 BTC 多单，帮我重新检索事件池和最新宏观，判断继续持有、平仓还是反手。
```

```text
FOMC 前后 BTC 合约怎么处理？看一下 FedWatch、油价、VIX、美债收益率和资金费率。
```

```text
复盘上一条决策，记录 24h / 72h 结果，并更新决策池。
```

## Decision Output Format

实时交易回答应尽量遵循：

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

## Live Search Policy

任何实时市场判断都不能只依赖历史记忆。必须刷新：

- 交易所实时数据：OKX 或用户实际交易所。
- 宏观预期：CME FedWatch、FOMC、CPI、PPI、PCE、NFP consensus。
- 跨市场风险：VIX、DXY、美债收益率、实际利率、WTI / Brent、Nasdaq。
- 突发事件：Reuters、AP、Bloomberg、CNBC 等可靠来源。
- 加密结构：ETF flows、funding、OI、long/short ratio、liquidation heatmap、options expiry。

地缘和油价类事件至少需要两个可靠来源确认。未确认新闻只能作为低置信度风险，不能当作已落地事实。

## Event Pool And Decision Pool

事件池和决策池是这个 skill 的核心，但它们不能无限膨胀到影响判断。

维护规则：

- 每次交易决策只读活跃事件和当前仓位上下文。
- CPI、PPI、PCE、非农、FOMC、期权交割这类重复事件写成规则，临近窗口再展开。
- 已过期事件移动到历史区，只保留可复盘结论。
- 决策池保留当前仓位和最近关键决策，更早记录应归档。
- 每次交易建议后补充 24h、72h、7d 复盘。

## Risk Disclaimer

This repository is for research, workflow design, and decision logging only. It does not provide financial, investment, legal, tax, or trading advice.

Crypto futures are high-risk products. Leverage can cause rapid liquidation even when the medium-term direction is correct. Any probability in this skill is subjective unless explicitly backed by a validated backtest.

Users are responsible for their own trading decisions, position sizing, leverage, risk control, and compliance with local laws.

## Contributing

Useful contributions include:

- Better public data-source integrations.
- More robust macro consensus collection.
- ETF flow, VIX, yields, DXY, oil and FedWatch helper scripts.
- Decision-pool review tooling.
- Cleaner event-pool archival workflow.
- More rigorous historical validation and backtesting.

Before changing `SKILL.md`, keep it concise. Put detailed reference material under `references/` and deterministic utilities under `scripts/`.
