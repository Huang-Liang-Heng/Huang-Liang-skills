# Structure：固定控制层 + 可变正式资产层

## 原则

Project Fold 统一的是**认知协议**，不是软件/科研/数据项目的物理目录。已有稳定结构优先保留。

## 固定控制层

非平凡长期项目通常使用：

```text
PROJECT_MODEL.md
PROJECT_STATE.md
PROJECT_CONTEXT.md
notes/
```

按需增加：

```text
ARCHITECTURE.md
.handoff/
workspace/
README.md
CLAUDE.md
```

## 正式资产层

由场景决定，不强制统一。例如：

### Software

```text
src/
tests/
docs/
assets/
```

### Research / Econometrics

```text
inputs/
scripts/
outputs/
paper/
```

### Data Analysis

```text
raw/ or inputs/
interim/
processed/
analysis/
outputs/
```

### Framework / Presentation / Design

```text
references/
materials/
components/
deliverables/
```

这些只是示例；已有项目不要为匹配示例而迁移。

## Workspace

探索区可选：

```text
workspace/human/
workspace/ai/
```

分离的是探索过程，不是正式项目。确认后的正式资产回到共享正式区。

## 规模

- small：核心控制文档可合并/省略；只创建实际有用的文件。
- standard：Model + State + Context + notes，其他按需。
- large：建议再有 Architecture、handoff、workspace，并在 Context 中维护专门 routes。
