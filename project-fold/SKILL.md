---
name: project-fold
description: >
  目标导向的跨场景项目认知与协作框架。适用于软件、科研、数据分析、论文、框架设计与长期复杂项目。
  用最小文档维持项目目标、当前真相、人类控制点、AI 上下文路由与可追溯执行关系。
  新建/接管项目使用 init/adopt；发生语义状态、canonical、依赖或文档路由变化后使用 sync；重要交付前使用 audit。
argument-hint: "[init|adopt|sync|audit] [可选说明]"
---

# Project Fold

目标：**让人以最小认知负担保持项目控制权，让 AI 只加载当前任务所需上下文。**

## 核心文件

- `PROJECT_MODEL.md`：人类项目心智模型。目标、核心对象/逻辑、能力/产出、边界、人类控制点。
- `PROJECT_STATE.md`：人 + AI 当前真相。现在已成立什么、canonical、未决事项、blocker、下一里程碑。
- `PROJECT_CONTEXT.md`：AI 上下文路由器。规定默认阅读、任务→文档映射、正式资产位置与文档职责。
- `notes/`：给人保留的重要决策、偏离、假设变化与原因。
- `ARCHITECTURE.md`：可选，主要给 AI；记录稳定组件/数据/产物关系与 provenance。
- `.handoff/`：AI 任务级短期状态；不是人类项目总览。

## 不变量

1. **目标导向**：先判断动作是否服务 `PROJECT_MODEL.md`，再执行。
2. **单一事实源**：同一事实只在一个核心文件中维护；其他地方链接，不复制。
3. **人类界面最小化**：默认只要求人读 Model、State、相关 Notes。
4. **AI 按需加载**：先读 `PROJECT_CONTEXT.md`；按其中路由读取 Model/State 与任务相关材料，不递归吞整个项目。
5. **语义优先**：同步首先问“现在什么变成真的”，而不是“改了哪些文件”。
6. **控制权保留**：目标、scope、关键行为/研究假设、重要风险和不可逆 trade-off 不得由 AI 静默决定。
7. **探索与正式分离**：探索可失败；正式资产必须可解释、可验证、可追溯。
8. **最小改动**：适配现有项目，不为模板大规模迁移或创建空目录。

## 模式

### `init`
1. 只读扫描项目与材料，判断目标、场景、规模。
2. 读取 `references/structure.md`、`references/model.md`、`references/context.md`。
3. 创建最小控制层：`PROJECT_MODEL.md`、`PROJECT_STATE.md`、`PROJECT_CONTEXT.md`；需要时创建 `notes/`、`.handoff/`、`workspace/`。
4. 依赖复杂时再创建 `ARCHITECTURE.md`。
5. 不覆盖已有 README、CLAUDE.md 或正式资产。

### `adopt`
1. 先只读，不重排。
2. 建立项目目标/模型、当前 canonical、正式资产和关键依赖的候选图。
3. 读取 `references/model.md`、`references/state.md`、`references/context.md`；复杂依赖再读 `references/architecture.md`。
4. 先建立控制层，再决定是否需要整理物理目录。
5. 不确定项写 `UNKNOWN`，不猜。

### `sync`
默认只检查本次任务及直接依赖。读取 `references/lifecycle.md`；其余按需。

- 目标、核心逻辑、scope、人类控制点改变 → 更新 `PROJECT_MODEL.md`。
- 已成立能力/结论、canonical、open decision、blocker、milestone 改变 → 更新 `PROJECT_STATE.md`。
- 文档职责、正式资产位置、任务→文档路由改变 → 更新 `PROJECT_CONTEXT.md`。
- 稳定依赖/provenance 改变 → 更新 `ARCHITECTURE.md`。
- 重要决策原因/偏离 → 写 `notes/`。
- 未完成的单次任务 → 写 `.handoff/`。
- 没有实质变化 → 不改管理文档。

### `audit`
读取 `references/audit.md`。验证项目模型/状态是否与实际一致、canonical 是否明确、正式资产是否可追溯、AI 路由是否 stale、正式产物是否依赖 workspace，以及可安全执行的 smoke test/验证是否真正运行。

## 人机边界

- **AI 可自主**：局部、可逆、不改变项目语义的实现决策。
- **AI 执行 + 人知情**：已有明确规格但会改变实际能力/结果的事项；完成后汇报 semantic delta。
- **必须由人决定**：改变目标/scope、核心用户行为、关键研究设计/假设、重大成本风险、不可逆方案或存在实质 trade-off 的选择。

## 输出原则

完成工作后优先汇报：

1. **现在什么是真的**；
2. **本次真正改变了什么**；
3. **这对目标意味着什么**；
4. **还需要人决定什么**。

实现细节、文件列表和日志按需展开。详细规则见 `references/output.md`。

## 按需参考

总控与读取：`references/context.md` · 项目模型：`references/model.md` · 状态：`references/state.md` · 目录：`references/structure.md` · 架构：`references/architecture.md` · 生命周期：`references/lifecycle.md` · 人机协同：`references/collaboration.md` · 输出：`references/output.md` · 命名：`references/naming.md` · 审计：`references/audit.md`。

场景规则仅在匹配时读取 `references/project-types/` 下对应文件。
