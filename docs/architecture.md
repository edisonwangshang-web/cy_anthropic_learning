# 项目架构

## 目标

本项目同时包含可运行课程、课程设计、来源档案、学习材料和 Agent 治理。架构的首要目标是让这些内容各自拥有单一职责，避免学员页面、研究数据和维护记忆互相耦合。

## 分层

| 层 | 目录 | 职责 | 可以依赖 |
|---|---|---|---|
| 学习应用 | `course/` | 学员打开、阅读、练习和记录进度 | `materials/`、公开来源链接 |
| 课程内容 | `content/curriculum/` | 正式课程大纲、教育审查和课程设计依据 | `content/sources/` |
| 来源证据 | `content/sources/anthropic/` | 英文全文、分类和抓取校验 | 不依赖学习应用 |
| 学习材料 | `materials/` | 可下载工作区、阶段模板和案例 | 不依赖项目治理 |
| 项目文档 | `docs/` | 架构说明和视觉参考 | 可引用各层路径 |
| Agent 治理 | `agent/`、`AGENTS.md`、`MEMORY.md` | 决策、进度、角色和跨会话记忆 | 可读取所有层 |
| 自动化 | `scripts/` | 结构校验、脚本语法检查和资料打包 | 可读取所有层 |

依赖方向必须从学习应用指向稳定材料，或从治理和自动化读取其他层。来源档案不能反向依赖页面实现。

## 学习应用

`course/` 是唯一可运行成品目录：

```text
course/
├── index.html
├── articles/
│   ├── classification.html
│   └── reader.html
└── assets/
    ├── course.css
    ├── course.js
    ├── classification.css
    ├── classification.js
    ├── reader.css
    └── reader.js
```

HTML 只负责语义结构，CSS 只负责呈现，JavaScript 只负责本地状态和交互。页面仍可通过 `file://` 直接打开，不引入构建工具或远程运行时。

## 稳定入口

- `index.html` 是仓库和 GitHub Pages 的稳定入口。
- `Anthropic工程博客学习路径课程.html` 保留为历史入口。
- `anthropic-engineering-crawl/` 中的两个 HTML 保留为历史文章入口。

兼容入口只做跳转，不复制课程实现。URL 中的文章锚点会被保留。

## 内容与证据

- `content/curriculum/` 保存“教什么、为什么这样教”。
- `content/sources/anthropic/` 保存“原文说了什么、抓取是否完整”。
- 中文精读摘要属于学习应用的一部分，但必须链接回英文来源；它不能替代来源证据。

## 学习材料

`materials/learner-workspace/` 是压缩包的唯一来源。不得直接手工修改 ZIP 后再回填目录。

打包命令：

```bash
python3 scripts/package_materials.py
```

压缩包内以 `learner-workspace/` 为根目录，文件列表必须与源目录一致。

## 变更规则

### 新增或更新文章

必须同时检查：

1. `content/sources/anthropic/` 中的全文和分类证据。
2. `course/assets/reader.js` 中的精读摘要和英文链接。
3. `course/articles/classification.html` 中的分类入口。
4. `course/index.html` 中的必读、选读和阶段映射。
5. `agent/memory/article_stage_map.md`。
6. `scripts/validate_project.py` 的数量和链接约束。

### 修改学习阶段

必须同时更新页面、阶段模板、评分量规、文章映射、项目记忆和验证规则。

### 调整目录

必须保留稳定入口，修正全部相对链接，并让校验器同时检查 `href` 与 `src`。

## 完成标准

每次架构或内容变更至少执行：

```bash
python3 scripts/validate_project.py
node scripts/check-js-syntax.mjs
git status -sb
```

校验通过只能证明结构、链接和脚本语法正确；桌面、手机、键盘和视觉表现仍需要浏览器验证。
