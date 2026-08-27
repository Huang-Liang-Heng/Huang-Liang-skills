# State：PROJECT_STATE.md 规则

`PROJECT_STATE.md` 是“此时此刻什么是真的”的短快照，不是历史日志，也不重复 Project Model。

## 必须回答

1. 当前阶段/里程碑是什么？
2. 现在已经成立了哪些能力、结论或状态？
3. 当前 canonical 正式入口/数据/知识源/交付物/结果是什么？
4. 哪些事项仍需人决定？
5. 主要 blocker / uncertainty 是什么？
6. 下一个 milestone 达到什么状态才算完成？

## Semantic State

优先写：

> 用户现在可以完成购买 → 填资料 → 形成待匹配订单。

而不是：

> 新增 11 个页面，修改 24 个文件。

研究中优先写：

> 主规格与事件研究已形成一致结果，当前识别瓶颈是 IV 排除限制。

而不是：

> 新跑了 8 张表。

## 更新条件

- 当前能力/结论发生实质变化；
- canonical 晋升/替换；
- open decision / blocker / uncertainty 改变；
- milestone 改变。

局部重构、格式、命名、无语义差异的文件变更不更新。

## Canonical

- 同类尽量一个 canonical；无法确定写 `UNKNOWN`。
- 最近修改、文件名带 final/v2 都不是 canonical 证据。
- 历史由 Git / archive /外部版本系统承担。

## 与 Handoff

State = 大状态；Handoff = 某个任务做到哪一步、从哪里继续。不要互相复制。
