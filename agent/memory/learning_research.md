# 主流学习产品调研

调研日期：2026-07-20

## 研究范围

产品：本地单页自主学习课程  
受众：中文零基础学习者  
目标：四周内完成 6 个阶段和一套工程判断先修包  
观察维度：课程入口、内容组织、短学习单元、练习、反馈、进度、复习和项目应用

## 产品模式

### Coursera

观察：

- 强调学习目标、教学材料和评估活动之间的对齐。
- Guided Projects 使用短时、任务导向、分步骤指导，并在项目后安排测验。
- 建议把课程拆成可达成目标和稳定学习时间。

用于本项目：

- 每篇文章必须说明学习目标和对应验收。
- 原文阅读之后立即进入项目任务或回忆题。

来源：

- https://www.coursera.org/campus/guided-projects
- https://blog.coursera.org/courseras-commitment-to-learning-how-we-support-skill-development/
- https://www.coursera.org/articles/how-do-online-courses-work

### Khan Academy

观察：

- 以 Skill、Unit、Course 的 Mastery 表示掌握程度。
- 测验和挑战会改变能力等级，并推荐需要复习的课程。
- 进度可直接定位到具体技能练习。

用于本项目：

- 不把浏览文章计为全部学习成果。
- “继续学习”定位第一项未完成文章、测验或产出。

来源：

- https://support.khanacademy.org/hc/en-us/articles/115002552631--Beta-What-is-Unit-Mastery-
- https://support.khanacademy.org/hc/en-us/articles/18735142028045-Update-New-mastery-progress-visualization-on-Course-and-Unit-pages

### Codecademy

观察：

- Path 把 Lesson、Quiz、Project 组织成清晰里程碑。
- 项目从高指导 Practice Project 逐步过渡到低指导 Challenge Project 和独立 Portfolio Project。
- 提示和错误反馈留在项目上下文中，减少切换。

用于本项目：

- 零基础阶段先提供完成示例，再要求自己的项目产出。
- 提示词、阅读问题和练习保留在同一阶段。

来源：

- https://help.codecademy.com/hc/en-us/articles/220453248-Picking-Your-Learning-Path
- https://www.codecademy.com/resources/blog/which-type-of-project-is-right-for-me/
- https://www.codecademy.com/resources/blog/portfolio-projects-in-career-paths

### DataCamp

观察：

- 核心是 Assess → Learn → Practice → Apply 的循环。
- 课程使用短内容和紧邻练习，项目负责迁移到真实问题。
- 可通过短评估跳过已掌握内容。

用于本项目：

- 每阶段加入即时回忆和真实案例产出。
- 后续可增加前测，让有经验的学习者跳过部分导读。

来源：

- https://www.datacamp.com/blog/online-learning-and-pedagogy-at-datacamp
- https://support.datacamp.com/hc/en-us/articles/33815612139799-What-Does-It-Mean-to-Skip-a-Course-on-DataCamp

### Duolingo

观察：

- 当前学习位置始终明确，用户可回到已完成内容复习。
- 长单元被切为更短、更聚焦的 Mini-units，并尽快在真实情境中使用新内容。
- 错题和旧内容通过个性化练习与间隔重复重新出现。

用于本项目：

- 继续学习必须指向唯一下一步。
- 一次只呈现当前文章导读和练习，不要求连续阅读所有文章。
- 后续增加跨阶段复习。

来源：

- https://blog.duolingo.com/how-to-review-lessons-on-duolingo/
- https://blog.duolingo.com/intermediate-mini-units/
- https://blog.duolingo.com/spaced-repetition-for-learning/

### freeCodeCamp

观察：

- 模块由 Theory、Workshop、Lab、Review、Quiz 组成。
- 课程通过逐步构建项目教授概念，并以认证项目检验综合应用。
- 较长认证被拆为更小、可获得成果的阶段。

用于本项目：

- 每阶段都必须留下可独立检查的文档。
- 结课成果由六阶段文档逐步累积，而不是最后从零开始。

来源：

- https://contribute.freecodecamp.org/how-to-work-on-coding-challenges/
- https://contribute.freecodecamp.org/curriculum-file-structure/

## 学习科学补充

### 1. 认知负荷与工作记忆

研究结论：

- 学习者处理陌生信息时，工作记忆容量有限；信息需要先在工作记忆中组织，再进入长期记忆。
- 无关材料、过多新概念和缺少结构的任务会占用有限容量，降低学习与迁移。
- 教学应减少无关加工，把复杂内容分块，并在建立基础结构后再组合任务。

课程应用：

- 每章只安排 5 个递进核心概念。
- 先给概念关系和导读，再让学员进入长文章。
- 文章通过抽屉阅读，避免主线、问题和产出位置丢失。

来源：

- https://link.springer.com/article/10.1007/s10648-019-09465-5

### 2. 读前问题与注意定向

研究结论：

- 在学习材料前提出问题，可以让学习者主动形成预测，并把注意力指向与答案相关的信息。
- 读前问题不是用来淘汰不会的人；学习者必须在后续材料中有机会找到、修正和理解答案。

课程应用：

- 每章开头先给一道真实情境判断，不要求答对。
- 学员先记录直觉，读完后再比较自己改变了什么。

来源：

- https://link.springer.com/article/10.1007/s10648-023-09814-5

### 3. 检索练习与元认知

研究结论：

- 从记忆中主动取回答案，比重复阅读更有利于长期保持和灵活迁移。
- 反馈会增强检索练习效果。
- 学习者经常把“读起来熟悉”误判成掌握，并低估自我测试的价值。

课程应用：

- 每章阅读后立即完成情境回忆题并获得反馈。
- 提醒学员先回忆再核对，不能先重读。

来源：

- https://pubmed.ncbi.nlm.nih.gov/20951630/
- https://pubmed.ncbi.nlm.nih.gov/19358016/

### 4. 完成示例与新手指导

研究结论：

- 零基础学习者面对陌生任务时，完成示例能减少无效试错，把注意力放在步骤和理由上。
- 指导程度需要随先验知识变化：新手受益于更多辅助，经验增加后应逐步减少辅助。

课程应用：

- 每章先拆一个“预约管理平台”的完成示例，再让学员迁移到自己的项目。
- 后续项目任务不直接给完整答案，只保留结构、验收标准和提示词。

来源：

- https://pubmed.ncbi.nlm.nih.gov/34458621/
- https://www.sciencedirect.com/science/article/pii/S0959475225000660

### 5. 自我解释与生成效应

研究结论：

- 学习者解释“为什么这一步成立”，有助于建立概念之间的联系并支持后续问题解决。
- 自己生成信息通常比单纯阅读更容易记住。

课程应用：

- 每篇必读文章都要求学员用自己的话解释一个新情境。
- 每章完成示例后安排 60 秒自我解释，必须包含判断、理由和证据。

来源：

- https://doi.org/10.1207/s15516709cog1302_1
- https://pubmed.ncbi.nlm.nih.gov/17645161/

### 6. 反馈、间隔与迁移

研究结论：

- 反馈整体上对学习有中等程度正向作用，但效果取决于是否提供了可用于修正的信息。
- 把复习分散到不同时间，比一次集中完成更有利于保持；学习时的顺利不等于延迟后的保留。

课程应用：

- 测验反馈不只说对错，还要指回需要修正的判断。
- 每章末尾安排 24 至 48 小时后的无资料回忆或桌面演练。

来源：

- https://pubmed.ncbi.nlm.nih.gov/32038429/
- https://pubmed.ncbi.nlm.nih.gov/28676769/
- https://pubmed.ncbi.nlm.nih.gov/37615780/

### 7. ICAP：从阅读走向生成与对话

研究结论：

- 学习活动可以分为被动、主动、建构和互动四类；仅阅读或点选的学习深度通常低于自己生成解释、比较方案和与他人或助教展开有依据的讨论。
- “做了操作”不等于深度学习，关键是学习者是否产生了超出材料原句的新推理。

课程应用：

- 读前判断、引导练习和自我解释都要求学习者生成内容，并保存在本地。
- AI 助教必须等学员先尝试，再追问理由、证据和迁移，不能直接代答。

来源：

- https://doi.org/10.1080/00461520.2014.965823

### 8. 教学支架与渐隐

研究结论：

- 计算机化支架整体上能改善学习结果；对新手而言，结构化提示、部分完成任务和及时反馈能降低无效搜索。
- 随着能力提高，提示应逐步减少，避免学员只会照抄范例。

课程应用：

- 每章采用“完整示例 → 补全引导练习 → 独立项目产出”的渐隐顺序。
- 六个阶段各提供一份结构化模板，但评分仍要求学员补充自己项目的证据和边界。

来源：

- https://pubmed.ncbi.nlm.nih.gov/28344365/
- https://pubmed.ncbi.nlm.nih.gov/35095238/

### 9. 建构性对齐与掌握标准

研究结论：

- 学习目标、学习活动和测评需要指向同一种可观察表现。
- 掌握学习不能只看是否完成材料，还需要明确标准、纠错机会和再次验证。

课程应用：

- 先修课把目标限定为解释、拆解、验证、安全判断和迁移，并用五维 0/1/2 量规验收。
- 生产可用产品的目标必须由真实数据库、部署、监控、备份和恢复证据验收，不能由文章测验替代。

来源：

- https://doi.org/10.1007/BF00138871
- https://journals.sagepub.com/doi/abs/10.2190/FG7X-7Q9V-JX8M-RDJP

用于本项目的结论：文章摘要不能替代回忆，回忆不能替代应用，应用还需要验收证据。

## 最终用户动线

1. 首次进入：理解课程结果和边界。
2. 完成准备：选案例、准备 AI 工具和学习目录。
3. 查看文档地图：知道每阶段读什么、产出什么。
4. 点击继续：直接进入第一项未完成任务。
5. 先回答章首问题：记录直觉，不要求答对。
6. 只建立 5 个核心概念：先获得理解文章所需的结构。
7. 展开文章导读：按阅读前判断、论证地图、类比和误区定位重点。
8. 阅读中文精读摘要：先建立论点结构；需要完整论证、数字、方法、引用或边界条件时，再打开英文来源定位证据。
9. 勾选文章任务：确认已完成读后自我解释。
10. 完成即时回忆：正确后计入掌握进度。
11. 查看完成示例：理解可接受产出的形状。
12. 补全引导练习：在部分结构上完成第一次迁移。
13. 完成 60 秒自我解释：说清判断、理由和证据。
14. 完成自己的项目文档：留下可检查证据。
15. 按五维量规验收：不足处修改后再进入下一阶段。
16. 24 至 48 小时后不看笔记复习并记录完成。
17. 结课复核：将六阶段产出装订成工程判断包。
18. 进入正式产品课：按八个动手里程碑完成数据库到运维的真实产品。
