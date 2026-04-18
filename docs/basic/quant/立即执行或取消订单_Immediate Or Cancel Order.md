![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# 什么是 IOC 订单？
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)
立即执行或取消订单（IOC）是一种买入或卖出证券的订单，该订单会立即执行全部或部分，然后取消任何未完成的部分。IOC 订单是几种“持续时间”或有效期订单中的一种，投资者可以利用它来指定订单在市场上保持活跃的时间以及在什么条件下取消订单。

其他常用的持续时间订单类型包括全量成交或取消（FOK）、全部或无（AON）和有效期至取消（GTC）。大多数在线交易平台允许手动下 IOC 订单或将其编入自动交易策略中。

### 关键要点

- 立即执行或取消（IOC）订单试图立即执行并取消任何未成交的部分。
- IOC 订单只需部分成交，可以被指定为限价单或市价单。
- IOC 是一种持续时间订单类型，其他类型包括全量成交或取消（FOK）、全部或无（AON）和有效期至取消（GTC）。

## IOC 如何运作

投资者可以根据其特定的执行需求提交“限价”或“市价”立即执行或取消订单（IOC）。IOC 限价单在特定价格下输入，而 IOC 市价单则不附带价格，并以买入的最佳报价和卖出的最佳出价进行交易。

IOC 订单与其他持续时间订单的不同之处在于，它们只需部分成交，而 FOK 和 AON 订单则必须完全成交或被取消。GTC 订单在市场上被执行或被客户取消之前保持活跃，尽管大多数经纪商会在30到90天之间取消它们。

## 何时使用 IOC 订单

投资者通常在提交大额订单时使用 IOC 订单，以避免以不同价格成交。IOC 订单会自动取消任何未立即成交的部分。假设一位交易者下达了一个 IOC 订单，以购买 5,000 股国际商业机器公司（IBM）的股票。任何未立即购买的 5,000 股部分会被自动取消。那些在一天内交易多只股票的人可能使用 IOC 订单来减少在收盘时忘记取消订单的风险。

**提示：** IOC 订单帮助投资者限制风险，加快执行，并通过提供更大的灵活性来改善价格。

## 示例

假设一位投资者下达了一个 IOC 市价单，以购买 1,000 股苹果公司（AAPL）的股票。订单簿显示 2,000 股的出价为 170.95 美元，500 股的卖盘为 171.00 美元。该订单会立即以出价价格（171 美元）成交 500 股，并取消未成交的 500 股部分。

再假设另一位投资者在市场开放时下达了一份 IOC 限价单，想以 169 美元购买 1,000 股苹果股票，此时股票的卖价为 170 美元。由于标准普尔 500 指数在下午略微下降，一位卖家以 169 美元的价格报价 700 股 AAPL。然而，由于该订单在当天早些时候未能成交，因此 IOC 订单会被立即取消。

## 使用 IOC 的好处

IOC 限价单可以在快速波动或流动性不足的市场中防止不良成交。另一方面，IOC 市价单确保在需求强劲的股票中实现全部或部分成交。

## IOC 如何影响市价单或限价单？

市价单是在最佳可得价格下买卖股票的订单，并将被立即执行。限价单是在特定价格或更好价格下买卖股票的订单。市价单和限价单可能包含时间限制和其他交易指令，如 IOC。[1]

## 对市场交易者来说，有效期是什么意思？

交易者在下单时使用有效期指令，以指明订单在执行或过期之前将保持活动的时间。

## 结论

立即执行或取消订单（IOC）是一种买入或卖出证券的订单，该订单会立即执行全部或部分，然后取消任何未成交的部分，结合有效期指令。IOC 限价单在快速波动的市场中保护投资者，而 IOC 市价单在需求高涨的强劲市场中确保了全部或部分成交。

## 参考文献

[1] U.S. Securities and Exchange Commission. "[Understanding Order Types](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14)."

## IOC订单的执行机制详解

### 订单生命周期

IOC订单从提交到完成的生命周期极短，通常在微秒级别完成：

1. **提交**：订单进入交易所撮合引擎
2. **匹配**：引擎扫描对手方订单簿，寻找可成交的价格
3. **部分成交**：执行所有可匹配的数量
4. **取消残余**：未成交部分立即被取消，不留在订单簿中

### IOC与其他时效指令的数学对比

设订单总量为 $Q$，可即时成交量为 $Q_a$（取决于订单簿深度），则各类订单的成交量 $Q_f$ 为：

| 订单类型 | 成交量 $Q_f$ | 条件 |
|---------|-------------|------|
| IOC | $\min(Q, Q_a)$ | 部分成交即可 |
| FOK | $Q$ 或 $0$ | $Q_a \geq Q$ 时全部成交，否则全部取消 |
| AON | $Q$ 或 $0$ | 与FOK类似，但可等待 |
| GTC | 累计至 $Q$ | 可跨日持续有效 |
| Day | $\leq Q$ | 当日有效 |

IOC订单的**成交率**（Fill Rate）定义为：

$$\text{Fill Rate} = \frac{Q_f}{Q} = \frac{\min(Q, Q_a)}{Q}$$

### 执行成本分析

IOC限价单的隐含成本来自两部分：

$$\text{Total Cost} = \underbrace{(P_{limit} - P_{mid}) \cdot Q_f}_{\text{价差成本}} + \underbrace{P_{mid} \cdot (Q - Q_f)}_{\text{机会成本的名义值}}$$

其中机会成本的实际大小取决于未成交部分后续的价格走势。

## 详细交易实例

**案例一：IOC限价单在快速市场中的应用**

假设标的股票AAPL当前订单簿：

- 买一：$170.90 × 800股
- 卖一：$171.00 × 300股
- 卖二：$171.05 × 500股
- 卖三：$171.10 × 1,200股

交易者提交IOC限价买单：1,000股 @ $171.05

**执行过程**：
1. 以$171.00成交300股（吃掉卖一）
2. 以$171.05成交500股（吃掉卖二）
3. 总成交800股，剩余200股被取消
4. 加权均价：$(300 \times 171.00 + 500 \times 171.05) / 800 = \$171.031$

**如果使用常规限价单**（$171.05，不带IOC）：
- 同样成交800股，但剩余200股会挂在$171.05的买方，等待后续成交
- 风险：如果价格反转下跌，这200股可能在更不利的时间成交

**案例二：IOC市价单在流动性探测中的应用**

机构投资者需买入50,000股，但不希望暴露全部需求。使用IOC市价单进行流动性探测：

| 时间 | IOC订单量 | 成交量 | 成交均价 | 订单簿反应 |
|------|----------|--------|---------|----------|
| 10:00:01 | 2,000 | 2,000 | $50.02 | 卖方挂单减少 |
| 10:00:15 | 3,000 | 2,500 | $50.05 | 价差扩大至$0.08 |
| 10:00:30 | 2,000 | 1,800 | $50.04 | 新卖方挂单进入 |
| 10:01:00 | 3,000 | 3,000 | $50.03 | 流动性恢复 |

通过IOC订单，交易者可以在不泄露全部需求的情况下逐步积累头寸。

## 量化应用

```python
import numpy as np
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum

class OrderType(Enum):
    IOC = "IOC"
    FOK = "FOK"
    GTC = "GTC"
    DAY = "DAY"

@dataclass
class PriceLevel:
    price: float
    quantity: int

@dataclass
class ExecutionReport:
    order_type: str
    side: str
    requested_qty: int
    filled_qty: int
    cancelled_qty: int
    avg_price: Optional[float]
    fills: List[dict]
    fill_rate: float

class IOCOrderSimulator:
    """IOC订单模拟器，支持多种订单类型对比"""
    
    def __init__(self, bid_levels: List[PriceLevel], 
                 ask_levels: List[PriceLevel]):
        self.bids = sorted(bid_levels, key=lambda x: x.price, reverse=True)
        self.asks = sorted(ask_levels, key=lambda x: x.price)
    
    def execute_order(self, side: str, quantity: int, 
                      limit_price: Optional[float] = None,
                      order_type: OrderType = OrderType.IOC) -> ExecutionReport:
        """
        执行订单
        
        Parameters:
            side: 'buy' or 'sell'
            quantity: 订单数量
            limit_price: 限价（None=市价单）
            order_type: 订单类型
        """
        if side == 'buy':
            levels = [PriceLevel(a.price, a.quantity) for a in self.asks]
        else:
            levels = [PriceLevel(b.price, b.quantity) for b in self.bids]
        
        fills = []
        remaining = quantity
        
        for level in levels:
            # 检查限价约束
            if limit_price is not None:
                if side == 'buy' and level.price > limit_price:
                    break
                if side == 'sell' and level.price < limit_price:
                    break
            
            fill_qty = min(remaining, level.quantity)
            fills.append({'price': level.price, 'qty': fill_qty})
            remaining -= fill_qty
            
            if remaining <= 0:
                break
        
        total_filled = quantity - remaining
        
        # 根据订单类型决定最终结果
        if order_type == OrderType.FOK:
            if total_filled < quantity:
                # FOK：不能全部成交则全部取消
                return ExecutionReport(
                    order_type="FOK", side=side,
                    requested_qty=quantity, filled_qty=0,
                    cancelled_qty=quantity, avg_price=None,
                    fills=[], fill_rate=0.0
                )
        
        elif order_type == OrderType.IOC:
            # IOC：部分成交，剩余取消
            pass  # 默认行为
        
        avg_price = (sum(f['price'] * f['qty'] for f in fills) / total_filled 
                     if total_filled > 0 else None)
        
        return ExecutionReport(
            order_type=order_type.value, side=side,
            requested_qty=quantity, filled_qty=total_filled,
            cancelled_qty=remaining, 
            avg_price=round(avg_price, 4) if avg_price else None,
            fills=fills,
            fill_rate=round(total_filled / quantity, 4)
        )
    
    def compare_order_types(self, side: str, quantity: int, 
                            limit_price: float) -> dict:
        """对比不同订单类型的执行结果"""
        results = {}
        for ot in [OrderType.IOC, OrderType.FOK]:
            report = self.execute_order(side, quantity, limit_price, ot)
            results[ot.value] = {
                'filled': report.filled_qty,
                'cancelled': report.cancelled_qty,
                'avg_price': report.avg_price,
                'fill_rate': f"{report.fill_rate:.1%}"
            }
        return results
    
    def optimal_ioc_strategy(self, side: str, total_qty: int, 
                              max_slices: int = 10, 
                              delay_recovery: float = 0.7) -> dict:
        """
        优化IOC订单的分批执行策略
        
        Parameters:
            total_qty: 需要成交的总量
            max_slices: 最大分批次数
            delay_recovery: 每次IOC后流动性恢复比例
        """
        filled_total = 0
        total_cost = 0
        slice_results = []
        
        remaining = total_qty
        
        for i in range(max_slices):
            if remaining <= 0:
                break
            
            # 动态确定本次IOC数量（越接近后期越激进）
            urgency = (i + 1) / max_slices
            slice_qty = min(
                int(remaining * (0.2 + 0.3 * urgency)),
                remaining
            )
            slice_qty = max(slice_qty, 100)
            
            # 执行IOC
            report = self.execute_order(side, slice_qty, order_type=OrderType.IOC)
            
            filled_total += report.filled_qty
            if report.avg_price:
                total_cost += report.avg_price * report.filled_qty
            remaining -= report.filled_qty
            
            slice_results.append({
                'slice': i + 1,
                'requested': slice_qty,
                'filled': report.filled_qty,
                'avg_price': report.avg_price
            })
            
            # 模拟流动性部分恢复
            for level in self.asks if side == 'buy' else self.bids:
                level.quantity = int(level.quantity * delay_recovery) + 50
        
        avg_cost = total_cost / filled_total if filled_total > 0 else None
        
        return {
            'total_requested': total_qty,
            'total_filled': filled_total,
            'fill_rate': f"{filled_total/total_qty:.1%}",
            'avg_cost': round(avg_cost, 4) if avg_cost else None,
            'n_slices': len(slice_results),
            'slices': slice_results
        }


# 使用示例
bid_levels = [
    PriceLevel(170.90, 800), PriceLevel(170.85, 1500),
    PriceLevel(170.80, 2000), PriceLevel(170.75, 3000)
]
ask_levels = [
    PriceLevel(171.00, 300), PriceLevel(171.05, 500),
    PriceLevel(171.10, 1200), PriceLevel(171.15, 2000)
]

sim = IOCOrderSimulator(bid_levels, ask_levels)

# 1. IOC限价买单
print("=== IOC限价买单 (1000股 @ $171.05) ===")
report = sim.execute_order('buy', 1000, limit_price=171.05, order_type=OrderType.IOC)
print(f"成交: {report.filled_qty}股, 取消: {report.cancelled_qty}股")
print(f"均价: ${report.avg_price}, 成交率: {report.fill_rate:.1%}")
print(f"成交明细: {report.fills}")

# 2. 对比IOC vs FOK
print("\n=== IOC vs FOK 对比 (1000股 @ $171.05) ===")
sim2 = IOCOrderSimulator(bid_levels, ask_levels)  # 重置
comparison = sim2.compare_order_types('buy', 1000, 171.05)
for ot, res in comparison.items():
    print(f"{ot}: 成交{res['filled']}股, 均价={res['avg_price']}, "
          f"成交率={res['fill_rate']}")

# 3. IOC分批执行策略
print("\n=== IOC分批执行 (5000股) ===")
sim3 = IOCOrderSimulator(bid_levels, ask_levels)
strategy = sim3.optimal_ioc_strategy('buy', 5000, max_slices=8)
print(f"总成交: {strategy['total_filled']}/{strategy['total_requested']} "
      f"({strategy['fill_rate']})")
print(f"均价: ${strategy['avg_cost']}")
for s in strategy['slices']:
    print(f"  第{s['slice']}批: 请求{s['requested']}股, "
          f"成交{s['filled']}股 @ ${s['avg_price']}")
```

## IOC订单的策略应用场景

1. **流动性探测（Pinging）**：高频交易者使用小额IOC订单测试暗池或其他交易场所的隐藏流动性。通过快速发送和取消IOC订单，可以在不暴露交易意图的情况下探测市场深度。

2. **最优执行算法中的IOC组件**：TWAP、VWAP等执行算法在需要激进成交时，会将子订单设置为IOC类型。例如，当算法落后于预定进度时，切换为IOC市价单以追赶进度。

3. **跨市场套利**：当同一证券在多个交易所上市时，套利者使用IOC订单在一个交易所快速成交，同时在另一个交易所执行反向交易，锁定价差。IOC的即时取消特性确保不会因延迟而产生单腿风险。

4. **风险管理**：当需要紧急减持风险头寸时（如突发利空消息），IOC市价单确保立即执行最大可能数量，同时避免在流动性枯竭时留下未成交的挂单。

## 关于LLMQuant
LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。