# RuyiSDK 包管理器自动化发版与测试流程优化——初步想法
## 一、 当前发布流程现状
当前 `ruyi` 包管理器的发布与测试流程呈现出“核心构建发版高度自动化，质量保障与分发推广高度人工化”的特点。
### 1. 当前流程图
```mermaid
flowchart TD
    subgraph 代码开发与提交
    Dev[开发者编写代码] --> PR[提交 Pull Request]
    end
    subgraph CI自动化测试与构建
    PR -->|自动触发| CI_Lint[CI: Lint检查 + 单元测试 + 集成测试]
    CI_Lint -->|通过| Merge[合入主分支]
    Merge -->|修改版本号| AutoTag[auto-tag.yml: 自动打 Tag]
    AutoTag -->|触发Tag| ReleaseBuild[CI: 多平台 Dist 构建]
    ReleaseBuild -->|自动| Release[自动创建 GitHub Release]
    ReleaseBuild -->|自动| PyPI[自动上传 PyPI]
    end
    subgraph 人工测试与评估
    Release --> ManualTest[测试人员: 根据日志人工整理/执行测试]
    ManualTest --> ManualReport[测试人员: 手工撰写 Gitee Markdown 测试报告]
    ManualReport --> ManualReview[测试团队: 人工评审报告并决定是否发布]
    end
    subgraph 人工分发与推广
    ManualReview -->|确认发布| ManualDist[人工: 多渠道同步包]
    ManualReview -->|确认发布| ManualNotify[人工: 撰写发版文章及新闻推送]
    end
    classDef auto fill:#d4edda,stroke:#28a745;
    classDef manual fill:#f8d7da,stroke:#dc3545;
    class CI_Lint,AutoTag,ReleaseBuild,Release,PyPI auto;
    class ManualTest,ManualReport,ManualReview,ManualDist,ManualNotify manual;
```
### 2. 流程描述与自动化程度说明
*   **全自动化环节（绿色）**：
    *   **代码静态检查与测试执行**：PR 提交后，自动触发 Lint 检查、单元测试和集成测试。
    *   **版本打标与产物构建**：版本号变更后，自动打 Tag，并针对 Linux/Windows/macOS 多平台构建可执行文件。
    *   **基础渠道发版**：自动创建 GitHub Release 页面，并将 Wheel 包发布至 PyPI。
*   **纯人工环节（红色）**：
    *   **测试报告生成与评审**：CI 运行仅输出日志，测试人员需手动从日志中摘取结果，人工撰写 Gitee 测试报告，并进行人工评审。
    *   **多渠道分发与通知推广**：发版包的多渠道同步（如镜像站）、发版通知文章撰写及新闻推广均由人工完成。
---
## 二、 优化后的发布流程（全链路自动化方案）
针对现状中的人工瓶颈，设计以下全链路自动化优化方案，通过引入结构化测试产物、AI内容生成与审批门禁，实现“测试-报告-评审-分发-推广”的闭环自动化。
### 1. 优化后流程图
```mermaid
flowchart LR
    subgraph 触发与测试层
    T1[pyproject.toml 版本号变更] --> A1[auto-tag 自动打 tag]
    A1 --> A2[ci.yml: 执行单测+集成测试]
    A2 --> A3[package-ci: 多发行版矩阵测试]
    A3 --> A4[自动上传 JUnit XML 结构化产物]
    end
    subgraph 报告与裁决层
    A4 --> B1[CI: report-generator 聚合 JUnit+Issues]
    B1 --> B2[AI 辅助生成 Gitee 风格 Markdown 报告]
    B2 --> B3[自动提交至 Gitee ruyisdk-test 仓库]
    B3 --> C1{人工/团队 Review 测试报告}
    C1 -->|通过| C2[GitHub Environment 审批门禁<br/>标记可发布]
    C1 -->|不通过| C3[打回修复]
    end
    subgraph 分发与推广层
    C2 --> D1[自动上传 PyPI]
    C2 --> D2[自动更新 GitHub Release]
    C2 --> D3[自动同步至镜像站 mirror.iscas]
    D1 & D2 & D3 --> E1[AI 生成发版文章<br/>基于 changelog+测试摘要]
    E1 --> E2[自动触发邮件/IM webhook 推送]
    end
    classDef auto fill:#d4edda,stroke:#28a745;
    classDef manual fill:#f8d7da,stroke:#dc3545;
    classDef ai fill:#cce5ff,stroke:#007bff;
    class A1,A2,A3,A4,B1,B2,B3,D1,D2,D3,E2 auto;
    class C1,C2 manual;
    class E1 ai;
```
### 2. 方案核心价值
*   **测试报告自动化**：释放测试人员约 60-70% 的报告撰写工作量，测试结果实时归档。
*   **分发与推广自动化**：包分发与发版新闻推送实现无人值守。
*   **AI 赋能切入点**：AI 接入测试日志生成缺陷草案，接入 Changelog 生成发版新闻，降低运营与测试双重成本。
---
## 三、 优化方案存在的问题及后续进一步优化策略
尽管上述全链路自动化方案解决了“执行后”的流程断点，但在“执行前”和“需求源头”仍存在深层次问题，需在后续规划中进一步优化：
### 问题1：新特性支持与新功能的测试用例覆盖滞后
**问题剖析**：
自动化流程极大地保障了**回归测试**的效率，但面临新特性覆盖的问题。如果发版修改的代码引入了新功能，而开发者未同步补充单元测试和集成测试用例，现有的 CI 流水线依然会“绿灯”通过，导致发版质量存在盲区。
**后续优化方案**：
*   **流程约束**：建立 PR 模板，要求提交新功能 PR 时，必须勾选或关联对应的测试用例更新（哪怕只是测试用例骨架）。
*   **AI 赋能测试左移**：引入 AI 工具，基于 PR 的 diff 代码变动，自动生成单元测试用例草案供开发者参考和完善，降低编写测试用例的门槛。


### 问题2：发版依据缺失及测试与研发割裂
**问题剖析**：
当前流程中，代码修改的前置需求依据相对缺失。受既往“小步快跑”的发版策略影响，实际操作演变成了“滞后测试”模式：先打 Release，再根据 changelog 分析是否需要新增测试用例，人工测试通过后才算完成发版。这种模式导致测试用例开发与代码研发割裂，拉长了有效验证周期。
**策略调整共识**：
经沟通评估，“固定发版时间频率”本质是一种管理策略，而非项目刚需，是可以协商调整的。只要能向用户明确传达“下个版本解决什么问题”以及“大致的发布时间范围”，并尽量保障内容和质量，即可满足用户期待。因此，发版约束可从“固定频率”转向“发布计划与质量驱动”。
**后续优化方案（轻量级落地版）**：
基于上述策略调整，无需引入重型项目管理流程，通过以下易操作的机制即可实现测试与研发的同步：
1.  **轻量化发布计划管理（基于 GitHub Milestone）**：
    利用 GitHub 现有的 Milestone 功能管理发布计划。每个 Milestone 代表一个待发版本，明确纳入需解决的 Issue，并标注大致的时间范围（如“预计X月上旬”）。当 Milestone 内规划的核心 Issue 均已开发完成并合并时，即视为满足发版条件。
2.  **PR 级别的测试左移卡点**：
    将测试用例的开发从“发版后”提前至“代码开发时”。制定合入规范：**涉及新功能或缺陷修复的 PR，必须同步提交或关联对应的测试用例（单测或 ruyi-pytest 提交）**。未附带测试用例的新特性 PR 不予合入。这样在发版触发自动化测试时，CI 能够直接覆盖最新特性，彻底消除人工事后补测环节。
3.  **AI 辅助计划跟踪与内容生成**：
    利用 AI 赋能运营，定期读取 Milestone 下的 Issue 完成状态。当进度达到发版阈值时，AI 自动汇总已完成的 Issue 生成 Changelog 草案及发版预告（包含版本内容和大致时间），推送到内部沟通渠道，以极低的人力成本弥补原流程中“计划文档缺失”的问题，使发版过程更具确定性和透明度。

