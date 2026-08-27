# Project Context Router

> **AI 总控文档。** 人类通常无需日常阅读。它只负责告诉 AI：默认读什么、当前任务再读什么、正式资产在哪里。保持短，不复制 Model/State/Notes 的内容。

## 1. Default Load

任何非平凡任务先读取：

1. `PROJECT_MODEL.md`
2. `PROJECT_STATE.md`

不要默认递归读取整个项目。

## 2. Task → Context Routes

| 任务信号 | 额外读取 | 不要默认读取 |
|---|---|---|
| 修改项目目标、scope、业务/研究核心逻辑 | 相关 `notes/`；必要时用户给出的规格 | 全部历史日志 |
| 代码/数据/pipeline/产物依赖 | `ARCHITECTURE.md`（若存在）+ 直接相关正式资产 | 全部 outputs / 全部源码 |
| 继续某个未完成任务 | 对应 `.handoff/handoff-*.md` | 其他 handoff |
| 追溯“为什么这样决定” | 对应 `notes/` | 整个 notes 目录 |
| 验证/审计 | 对应 tests/logs/outputs + provenance | 无关探索文件 |
| 使用/交付说明 | `README.md`（若存在） | 内部实现细节 |

## 3. Project Asset Map

只登记稳定入口/目录，不列每个文件。

- Formal source / implementation：
- Data / knowledge inputs：
- Formal outputs / deliverables：
- Tests / validation：
- Workspace / experiments：
- External / remote systems：

## 4. Document Responsibility

| 文档 | 主要读者 | 唯一职责 | 更新触发 |
|---|---|---|---|
| `PROJECT_MODEL.md` | Human + AI | 稳定目标、模型、scope、human control | 稳定语义改变 |
| `PROJECT_STATE.md` | Human + AI | 当前真相、canonical、决策、blocker、milestone | 当前状态改变 |
| `PROJECT_CONTEXT.md` | AI | 上下文路由、资产地图、文档职责 | 项目文档/资产拓扑改变 |
| `notes/` | Human + AI | 重要决定/偏离/原因 | 需要保留 rationale |
| `ARCHITECTURE.md` | AI + Human on demand | 稳定依赖与 provenance | 依赖关系改变 |
| `.handoff/` | AI | 单次任务短期状态 | 未完成任务需要续接 |
| `README.md` | Human / external | 使用方式与交付说明 | 用户入口改变 |
| Git / logs / tests | AI on demand | 历史与底层证据 | 自动产生/按需验证 |

## 5. Project-specific Routes

只在本项目确实需要时添加。例如：

| 任务 | 读取 |
|---|---|
|  |  |

## 6. Loading Rules

- 先路由，再加载；从最小上下文开始。
- 优先读取直接相关文档/文件，不用“可能有用”为理由扫描整个目录。
- 大文件、数据、历史 output 默认不读取；先看 schema/索引/元信息。
- 同一事实只认一个 source of truth；若冲突，标记并报告，不自行合并成“看似一致”。
