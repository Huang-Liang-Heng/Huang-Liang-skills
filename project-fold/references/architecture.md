# Architecture：稳定依赖与 Provenance

`ARCHITECTURE.md` 主要服务 AI 和需要深挖的人。它回答“正式资产怎样连接”，不重复目标、当前状态或历史原因。

## 何时需要

- 多组件/多服务；
- 多数据链或多语言 pipeline；
- 正式结果需要多步生成；
- 存在远程/手工/外部断点；
- 每次进入项目都要重新推断依赖关系。

## 最小内容

1. Canonical entrypoints；
2. Input/trigger → transformation/mechanism → formal artifact/outcome；
3. 关键组件依赖；
4. 正式产物 provenance；
5. 外部/手工步骤；
6. 已知 breakpoints/orphans。

## 更新条件

只有稳定依赖、正式产物来源、canonical pipeline 或外部断点变化时更新。任务进度不写这里。
