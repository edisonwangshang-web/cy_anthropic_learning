# Agent 控制系统

这个目录用于让不同 AI Agent 在多次会话、不同工具和不同模型之间稳定接手项目。

## 组成

- `feature_list.md`：项目能力清单及状态。
- `memory/`：长期事实、决策、进度、研究和文章映射。
- `roles/`：不同角色的输入、工作方式和交付标准。
- `templates/`：新增课程单元、任务和决策时使用的固定结构。

## 使用方式

开始任务时：

1. 阅读根目录 `AGENTS.md` 和 `MEMORY.md`。
2. 阅读 `docs/architecture.md` 和 `memory/progress.md`，确认目录边界与当前完成度。
3. 选择一个或多个角色文件。
4. 从 `feature_list.md` 中确认影响的能力。
5. 修改后运行 `python3 scripts/validate_project.py` 和 `node scripts/check-js-syntax.mjs`。
6. 更新进度和决策记忆。

## 记忆规则

- 只记录未来 Agent 继续工作所需的稳定事实。
- 不保存密钥、账号、私人数据或无关聊天内容。
- 决策必须记录“为什么”，不能只记录“做了什么”。
- 已过时内容应明确标记为“已替代”，不要静默删除决策历史。
- `MEMORY.md` 保持短小；细节放在 `memory/` 中。
