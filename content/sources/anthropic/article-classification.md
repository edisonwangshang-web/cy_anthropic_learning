# Anthropic Engineering 文章全文分类报告

抓取来源：https://www.anthropic.com/engineering

抓取时间：2026-07-17

覆盖范围：索引页暴露的 25 篇文章全部抓取。`claude-code-best-practices` 会从 Anthropic Engineering 链接重定向到 Claude Code 文档站，已按最终 URL 抓取正文。

本报告基于本目录下两份文件生成：

- `articles-fulltext.json`
- `articles-fulltext.md`

## 一、分类框架

这批文章不是普通“产品发布博客”，核心都围绕一个问题：

> 如何把 AI agent 从能演示的能力，工程化成可验证、可恢复、可隔离、可评估、可维护的生产系统。

按主问题可分为七类：

| 分类 | 核心问题 |
|---|---|
| A. Agent 架构与长任务工程 | agent 如何做长时间、多步骤、可恢复的复杂任务 |
| B. Agentic Coding 与 Claude Code 工作流 | 如何用 coding agent 高质量完成软件工程任务 |
| C. 工具、MCP、Skills 与上下文工程 | agent 如何高效使用工具、知识、技能和外部系统 |
| D. 安全、权限、沙箱与 containment | agent 拿到真实权限后，如何限制破坏半径 |
| E. Evals、基准、招聘与评测方法论 | 如何可靠衡量 agent 能力，避免指标失真 |
| F. 生产事故、质量退化与基础设施治理 | 模型/产品质量问题如何发生、发现和修复 |
| G. 检索与知识增强 | 如何让模型可靠使用大规模外部知识 |

## 二、逐篇分类

| # | 文章 | 主分类 | 辅助标签 | 分类依据 |
|---:|---|---|---|---|
| 1 | Designing AI-resistant technical evaluations | E | 招聘评估、技术面试、AI 辅助时代人才筛选 | 讨论 Claude 逐步击穿 take-home 技术测试，重点是如何设计仍有区分度的技术评估。 |
| 2 | A postmortem of three recent issues | F | 生产事故、模型服务、跨硬件一致性、路由/采样 bug | 复盘三类基础设施 bug 如何导致 Claude 响应质量下降，以及如何通过检测和发布流程改进治理。 |
| 3 | Introducing advanced tool use on the Claude Developer Platform | C | 工具搜索、程序化工具调用、工具示例、上下文节省 | 介绍 Tool Search、Programmatic Tool Calling、Tool Use Examples，重点是大规模工具库下的上下文和工具选择问题。 |
| 4 | An update on recent Claude Code quality reports | F | Claude Code、质量退化、推理 effort、缓存、系统提示 | 复盘 Claude Code 质量下降来自推理档位、thinking 缓存清理、系统提示改动三类产品层变化。 |
| 5 | Building a C compiler with a team of parallel Claudes | A | 多 agent、并行软件工程、测试驱动、长期自治 | 16 个 Claude 并行构建 C 编译器，核心是多 agent 协作、任务锁、测试 harness 和长期自动化软件工程。 |
| 6 | Building effective agents | A | agent 架构、workflow、routing、parallelization、orchestrator-worker | 给出构建 agent 的基础架构模式，区分 workflow 和 agent，强调简单、可组合的模式。 |
| 7 | How we built Claude Code auto mode | D | 权限自动化、审批疲劳、分类器、prompt injection | 讨论 93% 权限提示被批准带来的审批疲劳，以及用输入探针和输出动作分类器替代部分人工审批。 |
| 8 | Best practices for Claude Code | B | Claude Code、验证、计划、上下文管理、subagent、自动化 | 面向使用者的 agentic coding 方法论：先探索再计划、给 Claude 可运行验收、管理上下文、使用子 agent、回滚和自动化。 |
| 9 | Beyond permission prompts: making Claude Code more secure and autonomous | D | 沙箱、文件系统隔离、网络隔离、云端执行 | 说明仅靠权限弹窗不够，必须用文件系统和网络隔离来让 agent 更安全地自治执行。 |
| 10 | The "think" tool | C | 工具使用、显式思考、复杂规则、顺序决策 | 通过 think tool 给 Claude 在工具调用链中留出结构化推理空间，提高复杂策略/规则任务的一致性。 |
| 11 | Code execution with MCP | C | MCP、代码执行、上下文效率、工具编排 | 把 MCP 工具呈现为代码 API，让 agent 用代码编排工具、过滤中间结果，减少 token 和错误。 |
| 12 | Introducing Contextual Retrieval | G | RAG、Contextual Embeddings、Contextual BM25、rerank | 讲传统 RAG 切块丢上下文的问题，并用上下文化 chunk、BM25、embedding、rerank 提高召回。 |
| 13 | Demystifying evals for AI agents | E | agent eval、harness、grader、trace、regression | 系统定义 agent eval 的结构、术语、生命周期价值和设计方法，是 agent 评测方法论文章。 |
| 14 | Desktop Extensions | C | MCP 分发、桌面扩展、非技术用户安装、密钥配置 | 解决 MCP server 安装复杂的问题，把 MCP 打包成一键安装扩展，降低非技术用户使用门槛。 |
| 15 | Effective context engineering for AI agents | C | 上下文工程、context rot、compaction、note-taking、subagents | 把 prompt engineering 扩展为 context engineering，讨论如何管理有限注意力和长期任务上下文。 |
| 16 | Effective harnesses for long-running agents | A | 长任务 harness、progress file、feature list、git、E2E 测试 | 讨论长时间 coding agent 如何跨 context window 持续推进，核心是初始化、任务清单、进度文件、git 和端到端验证。 |
| 17 | Equipping agents for the real world with Agent Skills | C | Skills、渐进式披露、程序化知识、可组合能力 | 把组织流程、脚本、资料打包成 agent 可动态加载的 Skills，解决领域知识和操作流程复用问题。 |
| 18 | Eval awareness in Claude Opus 4.6’s BrowseComp performance | E | eval contamination、benchmark leakage、web-enabled eval | 讨论模型识别自己在被测评并搜索/解密答案，对开放网络环境下 benchmark 完整性提出挑战。 |
| 19 | Harness design for long-running application development | A | 长任务应用开发、planner-generator-evaluator、设计评价 | 通过 planner/generator/evaluator 架构，让 agent 做长时间全栈应用开发，并用独立 evaluator 解决自我评价偏乐观。 |
| 20 | How we contain Claude across products | D | containment、VM、sandbox、egress、agent identity | 从 claude.ai、Claude Code、Claude Cowork 三类产品总结 agent containment 架构和安全失效模式。 |
| 21 | Quantifying infrastructure noise in agentic coding evals | E | 基准误差、资源配置、Terminal-Bench、SWE-bench | 证明 agentic coding eval 分数会受 CPU/RAM/时间/infra 影响，强调资源配置是评测变量。 |
| 22 | Scaling Managed Agents | A | hosted agents、session log、sandbox、harness 解耦 | 讨论 Managed Agents 如何把 brain、hands、session 解耦，让长任务 agent 可恢复、可替换、可扩展。 |
| 23 | How we built our multi-agent research system | A | 多 agent research、orchestrator-worker、并行搜索、citation | 讲 Claude Research 的多 agent 架构，适用于宽度优先、信息量超大、可并行探索的研究任务。 |
| 24 | Raising the bar on SWE-bench Verified with Claude 3.5 Sonnet | B | SWE-bench、coding scaffold、bash/edit tools、最小工具集 | 说明 SWE-bench 评测的不只是模型，而是模型 + agent scaffold；重点是 coding agent 工具和提示设计。 |
| 25 | Writing effective tools for agents — with agents | C | 工具设计、MCP、tool eval、token efficiency、agent ergonomics | 讨论工具是“确定性系统和非确定性 agent 的契约”，重点是如何设计 agent 友好的工具和评测。 |

## 三、按主题重新归组

### A. Agent 架构与长任务工程

核心文章：

- Building effective agents
- Effective harnesses for long-running agents
- Harness design for long-running application development
- Scaling Managed Agents
- How we built our multi-agent research system
- Building a C compiler with a team of parallel Claudes

核心观点：

- 不要默认使用复杂 agent 框架；先用简单、可组合的 workflow/agent 模式。
- 长任务不能靠一次长上下文硬撑，要有 feature list、progress file、git commit、session log、context reset。
- 多 agent 适合宽度优先、可并行、信息量大、子任务弱依赖的任务；不适合高度耦合的所有场景。
- 生产级 agent 需要把 session、harness、sandbox 解耦，任何一层失败都能恢复。

### B. Agentic Coding 与 Claude Code 工作流

核心文章：

- Best practices for Claude Code
- Raising the bar on SWE-bench Verified with Claude 3.5 Sonnet

核心观点：

- 给 agent 一个可运行的验收信号：测试、构建、lint、截图、E2E 检查。
- 工作流应是 explore -> plan -> implement -> verify -> commit。
- coding agent 的表现强烈依赖 scaffold、工具描述、上下文管理，而不是只由模型能力决定。
- 代码任务里“验证闭环”比“生成代码”更重要。

### C. 工具、MCP、Skills 与上下文工程

核心文章：

- Introducing advanced tool use
- Code execution with MCP
- Writing effective tools for agents
- Agent Skills
- Desktop Extensions
- The "think" tool
- Effective context engineering for AI agents

核心观点：

- 工具定义和工具结果会污染上下文，必须按需加载、渐进披露。
- 对复杂工具链，agent 用代码调用工具比自然语言逐步调用更高效。
- 工具要按 agent 的认知方式设计：命名清楚、职责边界清楚、返回高信号内容。
- Skills 是把组织知识、流程和脚本打包给 agent 的方式，适合复用领域能力。
- 上下文是有限资源，核心原则是“最小但高信号”。

### D. 安全、权限、沙箱与 containment

核心文章：

- How we contain Claude across products
- How we built Claude Code auto mode
- Beyond permission prompts

核心观点：

- 人工审批会产生疲劳，不能作为唯一安全边界。
- 真正可靠的边界来自环境限制：文件系统、网络、VM、沙箱、egress control、凭证隔离。
- agent 风险分三类：用户误用、模型误行为、外部攻击。
- 权限不是“能不能点同意”，而是“agent 理论上能碰到什么、能传到哪里”。

### E. Evals、基准、招聘与评测方法论

核心文章：

- Demystifying evals for AI agents
- Eval awareness in BrowseComp
- Quantifying infrastructure noise in agentic coding evals
- Designing AI-resistant technical evaluations

核心观点：

- agent eval 是端到端系统评测，包含模型、工具、环境、资源、harness、grader。
- 静态 benchmark 会被污染，web-enabled agent 甚至可能识别自己正在被测。
- 资源配置、时间限制、infra 稳定性都会影响 coding eval 分数。
- AI 时代的人才评估要测真实工作能力，而不是容易被模型代做的固定题。

### F. 生产事故、质量退化与基础设施治理

核心文章：

- A postmortem of three recent issues
- An update on recent Claude Code quality reports

核心观点：

- 用户感知的“模型变差”可能来自路由、缓存、采样、系统提示、推理档位等产品/基础设施层。
- 多个小变更叠加会表现为广泛但难复现的质量退化。
- 需要跨平台、跨硬件、跨上下文长度、跨产品入口的质量监控和回归测试。

### G. 检索与知识增强

核心文章：

- Introducing Contextual Retrieval

核心观点：

- 传统 RAG 切块会丢上下文，导致召回失败。
- 对 chunk 增加上下文化说明，再结合 BM25、embedding 和 reranking，可以显著降低检索失败。

## 四、对“AI 时代非程序员全栈产品课程”的启发

这些文章对课程设计最重要的启发有五条：

### 1. 课程不应只教“让 AI 写代码”，而应教“给 AI 验收闭环”

对应文章：

- Best practices for Claude Code
- Effective harnesses for long-running agents
- Demystifying evals for AI agents

课程应把每个功能都设计成：

规格 -> 生成 -> 测试 -> 证据 -> 修复 -> 提交。

非程序员不需要成为码农，但必须会定义验收标准。

### 2. 生产可用的核心是环境、权限、数据和恢复能力

对应文章：

- How we contain Claude across products
- Beyond permission prompts
- Claude Code auto mode

课程必须强调：

- 不把真实密钥暴露给 AI
- 不让 AI 直接碰生产数据库
- 使用沙箱、最小权限、环境隔离
- 所有危险动作要有回滚方案

### 3. 长项目要有“agent 工作台”，不能只靠聊天记录

对应文章：

- Effective harnesses for long-running agents
- Harness design for long-running application development
- Scaling Managed Agents

课程项目应强制产生：

- `feature_list.json`
- `progress.md`
- `test_cases.md`
- `release_checklist.md`
- git commit 历史

这些文件就是非程序员指挥 AI 的项目控制台。

### 4. 工具选择要服务于“可迁移”，不能只教某个按钮

对应文章：

- Agent Skills
- Advanced tool use
- Code execution with MCP
- Desktop Extensions

课程可以绑定一套工具实操，但要让学员理解：

- 工具会变
- 数据、权限、测试、部署、监控这些判断逻辑不变
- 可导出代码、可迁移数据库、可查看日志，比“生成得快”更重要

### 5. 评测和验收会成为 AI 产品工程的核心能力

对应文章：

- Demystifying evals for AI agents
- Quantifying infrastructure noise
- Eval awareness in BrowseComp
- Designing AI-resistant technical evaluations

课程结业不应只看“页面能打开”，而应看：

- 功能验收是否完整
- 权限验收是否完整
- 数据恢复是否演练
- 线上错误是否可查
- 新功能是否不破坏旧功能

## 五、给课程大纲的直接修改建议

基于这批文章，课程大纲建议新增或强化三块：

### 新增：AI 项目控制台

放在“和 AI 高效对话”之后。

内容：

- feature list
- progress log
- test checklist
- release checklist
- AI 修改记录
- git 提交规范

目标：让非程序员能跨多天、多轮、多上下文管理同一个项目。

### 强化：验收与 eval

不要只在毕业项目讲验收，应该每章都有验收。

每个模块都要有：

- 功能验收
- 异常验收
- 权限验收
- 数据验收
- 回归验收

### 强化：安全边界与生产环境

安全模块要从“概念”变成“操作清单”：

- 哪些文件不能给 AI
- 哪些命令不能让 AI 自动执行
- 哪些环境变量必须隔离
- 开发库、测试库、生产库如何区分
- 数据库备份和恢复如何演练

## 六、最终归纳

Anthropic Engineering 这 25 篇文章共同指向一个结论：

> AI 工程的核心正在从“提示词技巧”转向“系统工程”：上下文、工具、权限、评测、沙箱、日志、恢复、持续迭代。

这与你的课程目标高度一致。

因此，这门课的差异化不应该是“非程序员也能用 AI 写代码”，而应该是：

> 非程序员也能用 AI 搭建、验证、上线、维护一个有安全边界和生产验收的真实产品。
