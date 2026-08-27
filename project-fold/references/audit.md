# Audit：Project Fold 交付前审计

Project Fold audit 审查项目认知一致性、canonical、组织、provenance 与可运行性；不替代领域专业审计。

## A. Meaning / Control

- [ ] PROJECT_MODEL 与实际目标/产品/研究设计一致。
- [ ] Scope / non-goals 没有被执行过程静默改变。
- [ ] Human Control Points / Open Decisions 没有被 AI 未经说明地替代决定。

## B. Current Truth

- [ ] PROJECT_STATE 只描述当前真相，不是历史流水账。
- [ ] Canonical 正式入口、数据/知识源、交付物和结果明确。
- [ ] UNKNOWN / blocker / uncertainty 被显式记录。

## C. Context Routing

- [ ] PROJECT_CONTEXT 的 Default Load 和 Task Routes 仍有效。
- [ ] Asset Map 指向真实、稳定的位置。
- [ ] 不存在多个文档重复维护同一事实。
- [ ] AI 不需要为了常见任务全项目扫描。

## D. Flow / Provenance

- [ ] 关键正式产物可反查生成入口和关键输入。
- [ ] 正式资产不依赖 workspace/scratch 或未知临时文件。
- [ ] 远程/手工步骤明确。
- [ ] Orphans 被列出，不静默忽略。

## E. Verification

能安全运行时，实际执行 canonical entrypoint、最小 smoke test 或相应验证，并保留可检查证据。不要以“应该可以”代替实际验证。

## F. Domain Boundary

发现统计识别、因果推断、业务合规、安全、内容正确性等专业问题时，报告并转交相应审计；Project Fold 不伪装解决。
