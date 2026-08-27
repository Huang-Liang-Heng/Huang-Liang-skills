# Project Type：Data Analysis

## Model 重点

业务/研究问题、关键指标、分析单位、最终需要支持的判断与正式产出。

## State 重点

当前可用数据范围、关键 schema/质量状态、canonical analysis-ready data、当前结论与仍未解决的数据问题。

## Architecture 重点

```text
source → ingest/clean → validate → analysis-ready → analysis → formal output
```

大型数据默认先读 schema、索引、元信息，不直接整库加载。
