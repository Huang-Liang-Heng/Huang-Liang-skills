# Project Fold Skill v3

Project Fold 是一套**目标导向、低认知负担、跨场景的人机项目协作协议**。它不要求软件、科研、数据分析或框架设计采用同一套业务目录；统一的是上层项目认知、当前真相、AI 上下文路由和可追溯关系。

建议安装到：

```text
~/.claude/skills/project-fold/
```

常用命令：

```text
/project-fold init
/project-fold adopt
/project-fold sync
/project-fold audit
```

## 人类日常只需要关注

```text
PROJECT_MODEL.md   # 我们在做什么、系统/研究怎样运行、边界在哪里
PROJECT_STATE.md   # 现在什么是真的、下一步是什么、哪些事待决定
notes/             # 重要决策和偏离为什么发生
```

## AI 的项目入口

```text
PROJECT_CONTEXT.md # AI 总控路由：该任务应该读哪些文档、正式资产在哪里
```

AI 先通过 `PROJECT_CONTEXT.md` 确定上下文，再按需读取 `PROJECT_MODEL.md`、`PROJECT_STATE.md`、`ARCHITECTURE.md`、`.handoff/`、源码、数据、研究说明或其他证据。**不要默认递归加载整个项目。**

## 核心设计

```text
Project Meaning  → PROJECT_MODEL.md
Project Truth    → PROJECT_STATE.md
Context Routing  → PROJECT_CONTEXT.md
Rationale        → notes/
Task Microstate  → .handoff/
Dependencies     → ARCHITECTURE.md (optional)
Evidence         → formal assets / tests / logs / outputs / Git
```

`SKILL.md` 只保留常驻决策协议；详细规范在 `references/` 中按需加载。
