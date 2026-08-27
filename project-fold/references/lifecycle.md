# Lifecycle：探索、晋升、同步与清理

## 成熟度

```text
scratch → experiment → candidate → canonical
```

不要求每个状态都有目录；关键是未确认产物不能伪装成正式资产。

## Promotion

进入正式区前至少满足：用途明确、任务要求的验证已完成、不依赖未知临时路径、输入输出可说明。若改变 canonical 或 semantic state，同步对应 State/Architecture/Context。

## Semantic Sync

任务后依次问：

1. 项目目标/模型/边界是否改变？
2. 现在是否有新的能力/结论变成真的？
3. canonical / milestone / blocker / open decision 是否改变？
4. AI 下次应该读取的路线是否改变？
5. 稳定依赖/provenance 是否改变？
6. 是否有需要长期保留的决策原因？
7. 是否留下未完成任务需要 handoff？

没有实质变化就不要制造管理文档更新。

## 清理

优先：归位 → 标记 → 归档 → 确认后删除。未知文件不自动删除；正式资产不得依赖 workspace/scratch。

## Notes 克制

`notes/` 是给人可回看的高价值 rationale，不是 AI 日志桶。只有当“为什么这样决定/偏离”在未来仍有价值时才新增 note。

单条 note 优先保持：**Decision / Reason / Impact / Evidence（按需）**。执行流水、文件清单、普通调试过程放 Git、logs、handoff 或工具输出，不进入 notes。
