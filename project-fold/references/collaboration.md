# Collaboration：人机协同与控制权

## 人类默认阅读面

人类日常只需：

1. `PROJECT_MODEL.md`：项目怎么理解；
2. `PROJECT_STATE.md`：现在什么是真的；
3. `notes/`：重要决策/偏离为什么发生。

其余文档不应要求人为了“跟上 AI”而持续阅读。

## AI 默认阅读面

AI 通过 `PROJECT_CONTEXT.md` 路由，再按需读 Model/State、Architecture、Handoff、正式资产与证据。

## 三档控制

### AI Autonomous

局部、可逆、不改变目标/外部行为/研究含义的实现决策。

### AI Execute + Human Aware

规格已明确，AI 可执行；若完成后使某项能力/结论“变成真的”，必须在 State/最终汇报体现 semantic delta。

### Human Control

AI 不得静默决定：

- 目标或 scope；
- 核心用户行为/产品规则；
- 研究问题、识别策略、关键假设与结论表述；
- 重大成本、隐私、安全或不可逆风险；
- 多方案存在实质 trade-off 的选择。

这些进入 `PROJECT_MODEL.md` 的 Human Control Points（稳定类）或 `PROJECT_STATE.md` 的 Open Decisions（当前类）。

## 减少认知负担

减少的是无价值负担，不是人类判断本身：AI 可隐藏日志、文件遍历和机械细节，但不能隐藏会改变决策的约束、不确定性和 trade-off。

## Open Decision 生命周期

- 尚未决定的具体问题 → `PROJECT_STATE.md → Open Decisions`。
- 决定完成后 → 从 Open Decisions 移除。
- 若决定改变稳定目标/流程/scope/control boundary → 同步 `PROJECT_MODEL.md`。
- 若“为什么这样决定”未来仍可能被质疑或复用 → 写一条精炼 `notes/`；否则不额外留文档。
