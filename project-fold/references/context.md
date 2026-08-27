# Context：PROJECT_CONTEXT.md 与按需加载

## 目标

`PROJECT_CONTEXT.md` 是 AI 的项目总控路由器，不是项目说明书。它让 AI 在大型项目中避免“为了保险把所有文件都读一遍”。

## 固定加载策略

1. 非平凡任务先读 `PROJECT_CONTEXT.md`。
2. 按 Router 读取 `PROJECT_MODEL.md`、`PROJECT_STATE.md`。
3. 再根据任务只读取直接相关的 notes / architecture / handoff / formal assets / evidence。
4. 需要更多上下文时逐层扩展，不递归全目录。

## Router 应包含

- Default Load：通常 Model + State。
- Task → Context Routes：任务类型对应额外文档。
- Project Asset Map：正式代码/数据/知识源/交付物/测试/探索区的位置。
- Document Responsibility：每个核心文档的唯一职责、读者和更新触发。
- Project-specific Routes：大型项目中的专门加载路线。

## 何时更新

只有以下变化才更新 Router：

- 新增/废弃重要文档；
- 正式资产根目录或 canonical 入口拓扑变化；
- 某类任务应该读取的文档发生变化；
- 文档职责发生冲突或重新分配。

不要因为普通文件新增就更新。

## 冲突处理

若 Model / State / Context / Architecture / 实际资产冲突：

1. 不猜哪一个正确；
2. 找证据与最近有效决策；
3. 明确冲突；
4. 修复单一事实源，再让其他文件仅引用它。
