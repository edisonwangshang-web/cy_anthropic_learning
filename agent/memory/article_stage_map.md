# 文章与阶段映射

总数：25 篇  
必读：12 篇  
选读：13 篇

## 阶段 1：Agent 工程基础

项目产出：AI 产品执行流程图、核心概念说明

| 类型 | 文章 | 课程作用 |
|---|---|---|
| 必读 | Building effective agents | 区分 Workflow 与 Agent，建立最小架构观 |
| 必读 | Effective context engineering for AI agents | 理解上下文有限、按需加载和外部记忆 |
| 选读 | How we built our multi-agent research system | 学习宽任务的多 Agent 并行探索 |

## 阶段 2：AI 编程工作流

项目产出：产品规格、feature list、progress log、验收标准

| 类型 | 文章 | 课程作用 |
|---|---|---|
| 必读 | Best practices for Claude Code | 建立 Explore、Plan、Implement、Verify、Commit 流程 |
| 必读 | Effective harnesses for long-running agents | 学习跨会话进度、功能清单和端到端验证 |
| 选读 | Harness design for long-running application development | 学习 Planner、Generator、Evaluator 分工 |
| 选读 | Building a C compiler with a team of parallel Claudes | 观察多 Agent 任务锁和测试协作 |

## 阶段 3：工具与上下文

项目产出：工具选型表、最小上下文包、数据暴露清单

| 类型 | 文章 | 课程作用 |
|---|---|---|
| 必读 | Writing effective tools for agents - with agents | 把工具设计成 Agent 可理解的操作契约 |
| 必读 | Equipping agents for the real world with Agent Skills | 用渐进式披露封装流程、脚本和资料 |
| 选读 | Introducing advanced tool use | 工具搜索和程序化调用 |
| 选读 | Code execution with MCP | 代码化工具编排与上下文压缩 |
| 选读 | Introducing Contextual Retrieval | RAG 召回、上下文化和重排 |
| 选读 | Desktop Extensions | 降低非技术用户的工具安装门槛 |
| 选读 | The "think" tool | 为复杂工具链提供显式推理空间 |

## 阶段 4：安全与权限

项目产出：三环境隔离图、权限矩阵、安全红线

| 类型 | 文章 | 课程作用 |
|---|---|---|
| 必读 | How we contain Claude across products | 理解多层 Containment、VM、网络出口和身份 |
| 必读 | Beyond permission prompts | 理解审批疲劳及文件和网络沙箱 |
| 选读 | How we built Claude Code auto mode | 学习风险分类器和自动权限判断 |

## 阶段 5：评测与验收

项目产出：测试用例集、验收评分表、证据留存规则

| 类型 | 文章 | 课程作用 |
|---|---|---|
| 必读 | Demystifying evals for AI agents | 建立 Task、Trial、Grader、Trace、Outcome 框架 |
| 必读 | Quantifying infrastructure noise in agentic coding evals | 识别资源和环境带来的评测噪声 |
| 选读 | Designing AI-resistant technical evaluations | AI 辅助时代的人才评估 |
| 选读 | Eval awareness in Claude Opus 4.6's BrowseComp performance | Benchmark 污染和评测意识 |
| 选读 | Raising the bar on SWE-bench Verified | 模型、工具和 Scaffold 的共同影响 |

## 阶段 6：生产治理

项目产出：故障处理手册、事故复盘模板、最小监控要求

| 类型 | 文章 | 课程作用 |
|---|---|---|
| 必读 | A postmortem of three recent issues | 生产质量退化、基础设施 Bug 和发布治理 |
| 必读 | An update on recent Claude Code quality reports | 推理档位、缓存和系统提示带来的产品质量问题 |
| 选读 | Scaling Managed Agents | 长任务运行、会话恢复和 Brain/Hands 解耦 |

## 维护规则

- 页面和本文件的必读/选读状态必须一致。
- 必读文章必须拥有课程内导读和完成状态。
- 选读文章必须说明“什么情况下值得读”。
- 必读和选读文章都必须先进入本地中文精读摘要；摘要保留英文来源核对入口，并明确说明不是逐段或完整翻译。
- 每篇文章只设置一个主学习阶段，避免重复计算进度。
- 若文章跨多个主题，使用分类报告保留辅助标签。
