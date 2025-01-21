![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# TradingAgents：多智能体LLM金融交易框架
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

## 摘要
近年来，依托大语言模型（LLM）推动的多智能体（multi-agent）协作在自动化决策与问题求解方面取得了显著进展。然而，在金融领域，大多数研究仍然局限于单一智能体处理具体交易任务，或利用多智能体框架独立搜集数据，尚未充分模拟现实交易公司内部“分工—协作”式的团队动态。本篇提出的“TradingAgents”框架，借鉴了专业交易公司的组织结构，打造了基于LLM的多智能体团队，包括从事基本面研究、情绪分析、技术分析以及不同风险偏好交易的多种角色；框架还设置了多空观点研究员（Bull和Bear研究员）来平衡市场观点，并配备风险管理团队进行敞口监控。在此系统下，交易智能体通过综合团队争论及历史数据进行决策，模拟真实世界协作式的交易环境。实验结果表明，与基准模型相比，该框架在累积收益、夏普比率以及最大回撤等指标上都有显著提升，证明了多智能体LLM在金融交易应用中的潜力。


![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2025/01/18/1737234033648-6cf5f1c2-7345-437d-9fb8-96ed84ee3156.png)


## 引言
大语言模型（LLMs）与自主智能体（autonomous agents）结合，已在许多领域展现出类人化的决策与工作流程复刻能力（参见Park et al. [2023]; Havrilla et al. [2024]; Talebirad and Nadiri [2023]; Tang et al. [2024]）。它通过给语言智能体配置各种“工具”并允许其与其他智能体协作，将复杂问题拆分为多个细化子任务，从而提高问题求解能力。金融市场作为一个高度复杂的系统，包含公司基本面、市场情绪、技术指标及宏观事件等多维度因素，正是这种多智能体系统可充分发挥的应用场景。

传统量化交易系统通常依赖纯量化模型，难以全面刻画多维度影响因素；而LLM对自然语言数据的高效处理能力，使其特别适用于新闻、财报与社交媒体等文字类信息分析。此外，深度学习驱动的黑箱式交易策略可解释性往往不足，而多智能体LLM框架能够通过透明的推理过程及证据链条提供更高的可解释性（Li et al. [2023a]; Wang et al. [2024b]; Yu et al. [2024]）。

尽管如此，当前将LLM应用于金融及交易领域的框架仍面临两大瓶颈：

1. **难以真实模拟交易公司的组织结构**  
   大多数多智能体金融应用只关注狭义任务（Li et al. [2023a]; Wang et al. [2024b]; Yu et al. [2024]），并未对真实交易公司中团队协作、流程管控等组织结构加以模拟，难以有效复刻现实中成熟的交易运作模式。

2. **通信接口低效**  
   许多系统仅依赖自然语言消息记录（如聊天历史）或无结构的信息池进行决策（Park et al. [2023]; Qian et al. [2024]），当对话轮数变多时，信息的丢失或“串线效应”就越明显，导致智能体难以在长时间跨度内保持一致的上下文与逻辑关系（尤其在动态金融环境下）。

针对上述挑战，本文提出了一套新的多智能体交易系统。首先，我们通过模拟专业交易公司多角色、多层级协作来提升决策过程的真实度与专业度：包括基本面分析师、情绪/新闻分析师、技术分析师及多空立场研究员等，协同完成动态决策；同时还有风险管理团队对敞口进行监控，及时控制下行风险。其次，我们在通信层面采用“结构化报告+自然语言争论”混合机制，保证信息在决策传递阶段的严谨与简洁，又能通过自然语言对复杂问题进行多轮探讨。

我们通过在历史金融数据集上的回测实验对该框架进行验证，与多种基准策略进行比较，借助累计收益、夏普比率及最大回撤等指标衡量交易表现，实验结果证明本框架在交易表现及风险控制方面具备显著优势。

---

## 相关研究

### LLM用作金融助手
在金融领域，研究者通过在金融语料上对大模型进行微调（fine-tuning），或干脆从头训练金融专用LLM，以满足专业语境下的财务分析、信息检索及辅助决策需求。

> **微调LLM（Fine-Tuned LLMs for Finance）：**  
> 例如PIXIU (FinMA)（Xie et al. [2023]）、FinGPT（Yang, Liu, and Wang [2023]）及Instruct-FinGPT（Zhang, Yang, and Liu [2023]）等，这些模型在大量金融领域指令或数据上进行微调，显著提升了金融情境下的分类或问答性能。某些场景下，这些模型甚至优于BloombergGPT（Wu et al. [2023]）。但在更偏向生成式任务上，与GPT-4等通用大模型相比仍可能稍有差距。

> **从头训练金融LLM（Finance LLMs Trained from Scratch）：**  
> 这类模型如BloombergGPT（Wu et al. [2023]）、XuanYuan 2.0（Zhang, Yang, and Xu [2023]）和Fin-T5（Lu et al. [2023]）等，通过在海量通用数据和专用金融文本上联合预训练，以提高对金融领域术语和任务的理解深度。这些模型在金融情感分类或摘要等任务上往往优于同等规模的通用模型，但在与GPT-3或PaLM（Chowdhery et al. [2022]）等封闭源大型模型对比时，可能存在规模上的限制。

总的来说，针对金融领域的LLM能在特定任务上取得优异效果，体现出“领域适配（domain adaptation）”的重要性。而构建更大规模或更高质量的金融专用数据集，是进一步提升这类模型性能的核心途径。


![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/01/18/1737234055721-e826d91a-41f6-4004-88af-b45fd0810e12.png)

> 图1：TradingAgents整体框架组织结构示意。I. 分析师团队并行采集市场信息；II. 研究团队对数据展开争论与评估；III. 交易员综合研究意见做出交易决策；IV. 风险管理团队监控风险暴露；V. 基金经理最终审批并执行交易。

### LLM用作交易员
此类工作将LLM视为直接交易执行的智能体，通过整合新闻、财报以及股价等外部数据进行自动化买卖决策。主要可分为三类：基于新闻的、基于推理的及基于强化学习的代理。

> **基于新闻的交易代理（News-Driven Agents）：**  
> 将新闻和宏观经济事件嵌入到LLM输入中，用于预测股价走势。相关研究表明，无论是GPT-3.5、GPT-4等闭源模型，还是Qwen（Bai et al. [2023]）、Baichuan（Yang et al. [2023]）等开源模型，都能够根据新闻情感评分执行多空策略（Lopez-Lira and Tang [2023]），并可通过微调（如FinGPT、OPT等）提升在特定金融领域的表现（Zhang et al. [2024a]; Kirtac and Germano [2024]）。

> **基于推理的交易代理（Reasoning-Driven Agents）：**  
> 在交易决策中强化模型的反思（reflection）与争论（debate）机制。如FinMem（Yu et al. [2023]）和FinAgent（Zhang et al. [2024b]）会在多模态数据上分层记忆提取，然后再进行技术指标分析来支持更准确的交易判断（Ji et al. [2023]）。另一些针对多智能体争辩机制的研究（Xing [2024]；TradingGPT (Li et al. [2023b]))则通过不同角色的LLM互相质疑，从而提升决策的合理性与稳健性。

> **基于强化学习的交易代理（Reinforcement Learning-Driven Agents）：**  
> 使用回测收益作为奖励信号对LLM进行强化学习。例如SEP（Koa et al. [2024]）利用带记忆与反思机制的RL来持续优化模型预测；也有工作将LLM生成的词向量与股市特征结合，通过PPO等算法训练交易策略（Ding et al. [2023]; Schulman et al. [2017]）。

### LLM用作Alpha因子挖掘
LLM还可用于产生Alpha因子，而非直接执行交易。比如QuantAgent（Wang et al. [2023]）采用双循环（inner-loop/outer-loop）架构，让“writer代理”基于“trader代理”的想法生成脚本，并由“judge代理”反馈，最后再在真实市场中回测并迭代完善。AlphaGPT（Wang et al. [2023]）也提出了人类在环（human-in-the-loop）的Alpha因子挖掘流程。此类研究证明，利用LLM生成并优化交易策略或因子，在实践中具有可行性与高效性。

---

## TradingAgents：角色细分
通过为LLM智能体设定明确的角色与目标，可将庞大复杂的交易流程拆解为可控子任务。金融交易最适合此类模式：在现实中，交易公司本身就有多种专家团队协同作战。TradingAgents正是借鉴了这一思路，将七种角色分配到模拟的“交易公司”中：包括基本面分析师（Fundamentals Analyst）、情绪分析师（Sentiment Analyst）、新闻分析师（News Analyst）、技术分析师（Technical Analyst）、研究员（Researcher）、交易员（Trader）及风险经理（Risk Manager）。

### 分析师团队
分析师团队（见图2）由以下四类代理组成，各司其职，覆盖市场信息的方方面面：

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2025/01/18/1737234079367-1d92b86f-c1fd-4858-8dcb-5d7a835d4a1e.png)

> 图2：TradingAgents的分析师团队示意

- **基本面分析师（Fundamental Analyst）**  
  通过分析财报、收益报告、内部交易等数据来评估公司内在价值，判断股票是否被低估或高估，为长期投资提供参考。

- **情绪分析师（Sentiment Analyst）**  
  关注社交媒体、舆情打分以及公司内部情绪等公众信息，预测短期投资者行为可能对股价带来的影响。

- **新闻分析师（News Analyst）**  
  追踪宏观经济指标、重大新闻及公司事件，识别对市场有潜在影响的突发消息或政策变化，为把握行情拐点提供依据。

- **技术分析师（Technical Analyst）**  
  计算MACD、RSI等技术指标，分析价量关系和价格形态，用于判断买卖时机和趋势走势。

上述分析师团队的输出形成对市场全方位的解读，为后续研究团队提供可靠信息输入。

### 研究团队
研究团队（见图3）主要负责对分析师团队提供的数据进行批判性评估，并以多空两个不同视角展开多轮辩论：


![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2025/01/18/1737234106063-b227bc1d-70c2-4211-aba2-73df9df02669.png)

> 图3：TradingAgents研究团队：多头视角与空头视角

- **多头研究员（Bullish Researchers）**  
  强调积极面与增长空间，为看多策略提供支撑性论据。

- **空头研究员（Bearish Researchers）**  
  着重揭示潜在风险与消极信号，为避免盲目入场提供“对立”观点。

通过这种辩证方式，研究团队能就市场风险与收益做出平衡性结论，为交易员提供更全面的策略建议。

### 交易员代理
交易员代理（见图4）在汇总分析师团队与研究团队意见后，结合量化数据与情感信息等多维输入，做出具体买卖决策：


![](https://fastly.jsdelivr.net/gh/bucketio/img17@main/2025/01/18/1737234120399-46e853de-cc49-471c-9956-21ccb91edba6.png)

> 图4：TradingAgents的交易员决策流程

- **评估分析师及研究员的建议**  
- **决定交易时机与规模**  
- **执行买卖指令**  
- **动态调整持仓**

作为直接面对市场的角色，交易员需要平衡潜在收益与风险，并快速应对市场变化。

### 风险管理团队
风险管理团队（见图5）实时跟踪交易组合的风险敞口，并确保交易活动符合事先设定的风险参数和合规要求：


![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/01/18/1737234141836-9af89d93-289e-4021-9b3b-c51a0f6f1537.png)

> 图5：TradingAgents风险管理及基金经理审批流程

- **评估市场波动、流动性、对手方风险等**  
- **执行风险缓释策略，如止损或头寸分散**  
- **向交易员提供风险反馈，并提出调整建议**  
- **确保整体组合与公司风险偏好相匹配**

通过上述多角色的协同，TradingAgents可在仿真环境中执行类似现实交易公司内部严谨、高度分工的决策流程。所有智能体均采用ReAct（Yao et al. [2023]）提示框架，在共享的环境状态下配合行动，并在需要时开展内部争论或调用工具，确保决策动态与灵活性。

---

## TradingAgents：代理工作流程

### 通信协议
目前大多数LLM多智能体框架仍只采用自然语言消息作为唯一的通信方式（Fatouros et al. [2024b]; Li et al. [2023a]; Yang et al. [2024]; Yang, Yue, and He [2023]）。但对金融交易这类需要长周期规划且信息维度复杂的任务来说，纯自然语言的“连续对话”往往容易出现“串线”或遗失关键信息（Hong et al. [2024]）。

为此，我们借鉴MetaGPT等框架的思路，引入**结构化通信协议**：通过清晰定义的格式传递报告，保证只有与本角色相关的信息被读取与处理，并在生成报告后记录到共享状态。这种方式可减少多余消息，也降低信息在多轮对话中的变形风险。

### 代理交互类型
与以往依赖大量自然语言聊天的交易框架不同，TradingAgents主要通过**结构化文档**与**简要的自然语言对话**来协作：

- **结构化报告**：  
  - 分析师团队：各自生成简明扼要的研究报告，包含关键指标、结论与建议。  
  - 交易员：阅读分析师报告后给出明确的交易信号与理由，再交由风险管理团队审核。  

- **自然语言讨论**：  
  - 研究团队：多空研究员查阅全局状态和分析报告后进行n轮对话，然后由一个“主持人”代理做归纳，给出最终观点并记录。  
  - 风险管理团队：针对交易员决策，按照不同风险偏好（激进、中性、保守）做n轮辩论，最后由主持人整理并提出修改意见。  
  - 基金经理：审阅风险管理团队的讨论，决定是否执行并写回最终决策。

### 底层LLM模型
为兼顾任务的复杂度与速度需求，我们在框架中混合使用不同LLM：  
- **“快思”模型（如`gpt-4o-mini`、`gpt-4o`）**：高效处理摘要、数据检索或表格转文字等低深度任务。  
- **“深思”模型（如`o1-preview`）**：擅长进行多轮推理、决策与长文本报告撰写等高深度任务。  

具体而言：  
- 分析师节点大多需要深度推理的能力，以生成扎实的分析结果；  
- 研究员与交易员也依赖深度推理模型来确保决策质量；  
- 工具与API的调用会交由相对轻量的模型，提升效率。  

通过灵活更换不同LLM，TradingAgents可以在无需GPU、仅使用API服务的模式下运行，也方便将来接入更强的推理模型或金融领域专用模型以进一步提升表现。

---

## 实验

### 回测
我们使用多资产、多模态的股票数据对框架进行回测，包括Apple、Nvidia、Microsoft、Meta、Google等公司，具体数据来源包含：

- **历史股价**：2024年1月1日至2024年3月29日的开盘价、最高价、最低价、收盘价、交易量等。  
- **新闻数据**：来自Bloomberg、Yahoo、EODHD、FinnHub、Reddit等多源的每日新闻，涵盖宏观经济与公司事件。  
- **社交媒体与情绪**：Reddit、X/Twitter等社交平台的帖子及由辅助LLM计算的情绪打分。  
- **内部交易与情绪**：公司内部交易信息和公开文件。  
- **财务报表**：公司定期发布的季度与年报。  
- **公司概况及历史**：第三方提供的简介与历史财务信息。  
- **技术指标**：MACD、RSI、布林带等共60种常见技术指标。

### 模拟设置
回测区间为2024年1月1日至2024年3月29日。TradingAgents在每日只读取当日及之前的数据，不使用未来信息（防止“前视偏差”）。根据分析后给出的买卖或持仓决策，我们在模拟环境中执行相应的指令，并记录每日的收益与风险指标。

### 基准模型
对比的基准策略包括：

- **Buy and Hold**：平均买入并持有全部选定股票，不做任何操作。  
- **MACD策略**：基于MACD线与信号线交叉点生成买卖信号。  
- **KDJ + RSI策略**：结合KDJ与RSI指标判断超买超卖区间进行交易。  
- **ZMR（Zero Mean Reversion）**：基于价格相对某基准线的偏离及回归信号下单。  
- **SMA（Simple Moving Average）**：利用长短期均线交叉进行买入或卖出。

### 评估指标
我们选用以下常用指标衡量策略的风险与收益：

1. **累计收益（Cumulative Return，CR）**  

$$
\text{CR} = \left(\frac{V_{\text{end}} - V_{\text{start}}}{V_{\text{start}}}\right)\times 100\%
$$
其中 $V_{\text{end}}$ 为回测结束时的组合价值，$V_{\text{start}}$ 为回测初始组合价值。

2. **年化收益（Annualized Return，AR）** 

$$
\text{AR} = \left(\left(\frac{V_{\text{end}}}{V_{\text{start}}}\right)^{\frac{1}{N}} - 1\right)\times 100\%
$$

其中 $N$ 为年数（本次回测约为3个月，可按比例折算成年化）。

3. **夏普比率（Sharpe Ratio，SR）**  

$$
\text{SR} = \frac{\bar{R} - R_{f}}{\sigma}
$$
4. **最大回撤（Maximum Drawdown，MDD）**  

$$
\text{MDD} = \max_{t \in [0,T]} \Bigl(\frac{\text{Peak}_t - \text{Trough}_t}{\text{Peak}_t}\Bigr)\times 100\%
$$

反映在回测期间，组合价值从峰值回落至谷底的最大跌幅。


## 结果与分析

### 性能对比

下面的表1展示了TradingAgents与多种基准策略在苹果（AAPL）、谷歌（GOOGL）、亚马逊（AMZN）等股票上的表现。我们可以看到，TradingAgents在各指标上均有明显优势。

**表1：** 各方法在四项评估指标上的表现对比。加粗的数值表示统计指标最优，最后一行的improvement展示了TradingAgents相对于次优基准的提升幅度。

| Categories | Models | **AAPL** |     | **GOOGL** |     | **AMZN** |
| --- | --- | --- | --- | --- | --- | --- |
| CR%↑ | ARR%↑ | SR↑ | MDD%↓ |  | CR%↑ | ARR%↑ | SR↑ | MDD%↓ |  | CR%↑ | ARR%↑ | SR↑ | MDD%↓ |
| 市场 | B&H | -5.23 | -5.09 | -1.29 | 11.90 |  | 7.78 | 8.09 | 1.35 | 13.04 |  | 17.1 | 17.6 | 3.53 | 3.80 |
| 规则 | MACD | -1.49 | -1.48 | -0.81 | 4.53 |  | 6.20 | 6.26 | 2.31 | 1.22 |  | - | - | - | - |
| 基 | KDJ&RSI | 2.05 | 2.07 | 1.64 | 1.09 |  | 0.4 | 0.4 | 0.02 | 1.58 |  | -0.77 | -0.76 | -2.25 | 1.08 |
| 础 | ZMR | 0.57 | 0.57 | 0.17 | 0.86 |  | -0.58 | 0.58 | 2.12 | 2.34 |  | -0.77 | -0.77 | -2.45 | 0.82 |
| 策 | SMA | -3.2 | -2.97 | -1.72 | 3.67 |  | 6.23 | 6.43 | 2.12 | 2.34 |  | 11.01 | 11.6 | 2.22 | 3.97 |
| 略 | TradingAgents | **26.62** | **30.5** | **8.21** | **0.91** |  | **24.36** | **27.58** | **6.39** | **1.69** |  | **23.21** | **24.90** | **5.60** | **2.11** |
|      | Improvement(%) | +24.57 | +28.43 | +6.57 | - |  | +16.58 | +19.49 | +4.26 | - |  | +6.10 | +7.30 | +2.07 | - |

#### 累计收益与年化收益
在**表1**及下图中，TradingAgents在三只股票上均获得了**至少23.21%的累计收益**以及**24.90%的年化收益**，比其他基准方法高出**6.1%以上**。尤其是波动较大的AAPL，在短短不到三个月能取得**超过26%**的收益，而许多传统技术指标策略此时则表现相对疲软。


![](https://fastly.jsdelivr.net/gh/bucketio/img8@main/2025/01/18/1737234726980-6d6ef67a-ac90-4fae-9780-eb6017ad9f78.png)

> (a) AAPL的累计收益(CR)对比


![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2025/01/18/1737234738834-2023dd7d-baab-464e-9938-14ef7d78b3b7.png)

> (b) TradingAgents在AAPL的具体交易点示例  
> 绿色/红色箭头分别表示做多/做空的时机

#### 夏普比率
TradingAgents在夏普比率上也表现突出：在AAPL、GOOGL、AMZN上的夏普比率均达到**5.60以上**，比次优策略高**至少2.07**。这说明在同等波动或风险下，TradingAgents能够获得更高的超额收益，具有更好的风险收益平衡。

#### 最大回撤
规则类策略在控制风险上通常有一定优势，但其收益普遍不高。而TradingAgents通过多智能体争论尤其是风险管理团队的调控，一方面捕捉到了市场主要机会，另一方面最大回撤也能控制在2左右，没有陷入过度冒险的境地。

#### 可解释性
相比目前大多数深度学习交易模型是“黑箱”决策，LLM多智能体具备更高可解释性：其操作与理由可用自然语言输出，不仅便于交易员理解与调试，还能根据决策过程提供针对性调整。我们在附录中列举了TradingAgents某一天的完整日志，包括它如何调用工具、推理、执行决策等过程，可见其透明度远胜于一般的深度神经网络交易策略。

### 讨论
实验结果显示：通过角色分工、相互争论与协同决策，TradingAgents能够显著提升交易绩效。一方面，多数据源与专家视角的互补有助于交易员做出更全面的判断；另一方面，风险管理团队可及时对策略进行限制与调优，保证在把握收益的同时避免严重回撤。此外，多智能体之间以自然语言方式记录的推理过程，也使得策略具备良好的可解释性与可审计性，这在金融实务中尤为关键。

---

## 结论
本文提出的TradingAgents框架，模拟了一个类似真实交易公司的多角色、多层级协同环境：每个LLM智能体专门负责分析某一维度或承担特定职责，通过多轮对话与结构化报告进行信息交换和决策，最终实现自动化股票交易。在回测实验中，TradingAgents在累积收益、夏普比率及最大回撤等关键指标上均显著超越了多种基准。  
未来，我们计划在实盘环境中部署该框架，进一步扩充角色种类与任务范围，并结合实时数据处理能力，以增强TradingAgents对瞬息万变金融市场的适应性。



如需获得完整教程和超详细代码！欢迎扫描下方二维码加入**LLMQuant知识星球**。


![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/01/18/1737234806568-9b7760a0-ea4c-4d12-a60c-b537ebdfe1d5.JPG)



## 关于LLMQuant

LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。欢迎加入**知识星球**获取**内部资料**。
