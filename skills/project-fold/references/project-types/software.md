# Project Type：Software

## Model 重点

- 用户/调用者是谁；
- 核心对象与业务流程；
- 最终系统能力；
- scope / non-goals；
- 会改变用户行为、数据权限、成本/安全的 Human Control Points。

## State 重点

用“现在用户/系统可以完成什么”描述进度，避免以文件数、组件数、代码行数为主状态。

## Architecture 重点

```text
request/event → interface → service/domain → storage/external systems → response/outcome
```

Context 只路由到当前 feature 的相关模块与测试，不默认扫描整个代码库。
