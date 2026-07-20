# 陈婴学习

面向非程序员的 AI 全栈产品课程工程。项目当前包含两条明确分开的学习主线：

1. **工程判断先修课**：已经实现为可离线打开的静态学习应用。
2. **正式全栈产品课**：当前完成课程大纲，后续按数据库、后端、客户端、权限、部署和运维逐步建设。

## 快速开始

直接打开根目录的 `index.html`，或打开：

```text
course/index.html
```

页面不依赖服务端、远程 JavaScript、字体或分析脚本，学习进度只保存在当前浏览器。

## 项目结构

```text
.
├── course/                     # 学员直接使用的静态课程应用
│   ├── index.html
│   ├── articles/              # 分类页与中文精读摘要阅读器
│   └── assets/                # 页面样式和交互脚本
├── content/
│   ├── curriculum/            # 课程大纲与教育审查
│   └── sources/anthropic/     # 原始全文、分类和抓取证据
├── materials/
│   ├── learner-workspace/     # 六阶段可填写模板
│   └── learner-workspace.zip
├── docs/
│   ├── architecture.md        # 架构边界与维护规则
│   └── references/            # 视觉参考资料
├── agent/                     # Agent 角色、记忆、决策和模板
├── scripts/                   # 校验与资料打包脚本
├── AGENTS.md                  # Agent 第一入口
├── MEMORY.md                  # 当前项目状态摘要
└── index.html                 # 稳定入口，跳转到 course/
```

旧课程文件名和旧文章页面路径保留为兼容入口，已有本地书签不会失效。

## 项目校验

```bash
python3 scripts/validate_project.py
node scripts/check-js-syntax.mjs
```

重新生成学员工作区压缩包：

```bash
python3 scripts/package_materials.py
```

## 关键文档

- [项目架构](docs/architecture.md)
- [正式全栈课程大纲](content/curriculum/fullstack-course-outline.zh-CN.md)
- [教育审查与优化报告](content/curriculum/education-audit.zh-CN.md)
- [文章与阶段映射](agent/memory/article_stage_map.md)
- [项目决策记录](agent/memory/decisions.md)

## 维护原则

- `course/` 只放可运行、可交付给学员的页面和资源。
- `content/sources/` 是证据档案，不直接承担教学动线。
- `materials/` 是学员产出模板，不混入项目治理文档。
- `agent/` 和根目录记忆文件服务于后续 Agent 接手，不出现在学员主线。
- 所有路径调整、文章增删和阶段变化必须通过项目校验。
