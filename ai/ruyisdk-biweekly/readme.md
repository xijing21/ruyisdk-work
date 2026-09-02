# RuyiSDK双周进展汇报流程自动化改造说明

## 一、背景

### 1.1 为什么要做这件事

RuyiSDK双周进展汇报是团队定期同步各模块开发进度的重要机制。目前整个流程（模板初始化、通知、PR提交与合入、卷首语撰写、进度催办、社区转发）全部由人工完成，重复性劳动占比高，且对执行者的时间精力消耗较大。

### 1.2 当前全人工操作流程

目前每期双周报的完整流程如下：

1. 仓库管理员在双周一手动初始化新的双周模板文件；
2. 在沟通群中通知各模块负责人提交进展；
3. 各模块负责人分别提交PR；
4. 管理员检查并催交PR；
5. 管理员审核并合并PR（技术内容依赖PR Bot检查，人工主要把关格式）；
6. 管理员基于各模组总体情况，总结并添加卷首语；
7. 管理员review：手动删除本期无进展的章节（如QEMU）、typo问题、格式问题等；
8. 管理员在群中通知报告完成，邀请提交者一起再次Review；
9. 管理员或者社区经理人工在RuyiSDK用户社区转发双周报内容。
10. 社区经理在微信群/QQ群等转发双周报告链接。

其中**步骤1、2、4、5**均为高重复性、低创造性劳动，具备自动化改造的基础条件。

### 1.3 基础条件

- 代码仓库托管于GitHub（ruyisdk/wechat-articles），具备GitHub Actions自动化能力；
- 团队成员习惯使用GitHub PR协作流程，对Git操作熟悉；
- PR 提交者为各模组的负责人，基本能够保障技术准确性，专业技术把控比PR审核者更专业。PR审核主要看格式和typo；
- 沟通群计划从微信群迁移至飞书群，飞书开放平台支持Bot与Webhook消息推送；

---

## 二、自动化/半自动化改造设想

针对步骤1、2、4、5，采用 GitHub Actions + 飞书Bot 实现（双周周期可能因节假日调整，故以手动触发 workflow_dispatch 为主）：

1. **模板自动初始化**：管理员在 Actions 页面点击运行，输入日期和期号，自动生成当期双周报文件并推送，同时飞书群通知开始提交；
2. **进度查看**：按需触发，自动汇总近期 PR 与 commit 情况发送到飞书群，提醒未提交的负责人；
3. **PR 自动合入**：负责人提交的 PR 通过链接有效性基础检查后自动合入，失败时自动在 PR 下评论 @作者 说明原因；（基于目前负责人提交的内容质量较高为基础）
4. **卷首语 AI 生成**（规划中）：在个人仓库触发 Action，调用内部 AI 站点生成卷首语草稿，人工审核后使用。（考虑AI内容还是需要人工审核，暂时不太合适直接在ruyisdk主仓库中操作，个人仓库操作更加合适）

> 方案选用 github action 为主要技术手段主要是考虑运行避免依赖其它运行环境，方便长期维护。

## 三、改造实现
### 3.1 Action 清单

```
.github/workflows/
├── init-template.yml      # 双周报模板初始化 + 飞书通知（手动触发）
├── check-progress.yml     # PR/commit 进度汇总 + 飞书催办（手动触发）
├── pr-check.yml           # PR 链接有效性检查（PR 自动触发）
└── automerge.yml          # PR 自动合入 + 失败自动评论（检查完成后自动触发）
```
> 基于 main 分支 `.github/workflows/` ，目前源码已经提交并合入仓库。

### 3.2 各 Action 思路
**① init-template.yml —— 模板初始化（对应人工步骤 1、2）**
- 手动触发，输入两个参数：日期（YYYYMMDD）、期号；
- 读取 `biweekly-template/template.md`，将首行替换为 `# RuyiSDK 双周进展汇报 第 XXX 期 · YYYY 年 MM 月 DD 日`，删除模板中以 `> ` 开头的说明行；
- 生成新文件 `{日期}-ruyisdk-biweekly-{期号}.md`，以 `github-actions[bot]` 身份提交到 main；
- 通过 `secrets.FEISHU_WEBHOOK_URL` 向飞书群推送通知（含文件链接、截止时间周二中午 12:00、模板说明链接）。
**② check-progress.yml —— 进度催办（对应人工步骤 4）**
- 手动触发，输入回看天数（默认 2 天）；
- 用 `gh pr list` 拉取近 N 天所有 PR（标题、状态、作者、链接），用 GitHub API 拉取近 N 天 main 分支的 commit；
- 汇总为报告（含 PR 数、commit 数、明细列表），经 jq 构造 JSON 后推送到飞书群。
**③ pr-check.yml —— PR 链接检查（对应人工步骤 5 的格式把关）**
- 任何 PR 提交/更新时自动触发；
- 对 PR 中 `.md` 文件**新增行**做 diff，提取所有新增的 http/https 链接（去除行尾标点），无新增链接则直接跳过；
- 用 lychee 逐一检查链接可达性（20 秒超时、失败重试 2 次），失败则该检查不通过，PR 无法合入。
**④ automerge.yml —— 自动合入（对应人工步骤 5 的合并操作）**
- 由 "PR Check" 工作流完成后自动触发（`workflow_run` 事件），运行在 main 分支上下文——这是关键设计：fork PR 场景下 `pull_request` 上下文的 secrets 会被 GitHub 剥离，而 `workflow_run` 上下文拥有完整 secrets 与写权限，且不 checkout PR 代码，fork 作者无法触碰任何 token；
- **检查通过** → 用 `AUTO_MERGE_TOKEN`（拥有 Contents/PR 写权限的 fine-grained PAT）执行 `gh pr merge --squash --delete-branch`，PR 自动 squash 合入并删除分支；
- **检查失败/取消** → 用 GITHUB_TOKEN 在该 PR 下自动评论 @作者，说明 link-check 失败、附 Actions 日志链接、提示偶发网络超时可 Re-run、修复 push 后会自动合入。
> 注：notify-on-fail 与 automerge 两个 job 无依赖关系（成功才合并、失败才评论，逻辑互斥），避免一方被 skip 时连带跳过另一方。

---

## 四、使用说明：一个新双周周期的完整操作流程

前置条件：飞书群已配置自定义机器人 Webhook，并存入仓库 Secret `FEISHU_WEBHOOK_URL`（见第五章配置 ②）。

| 步骤 | 操作人 | 操作 | 对应人工流程 |
|---|---|---|---|
| 1 | 管理员 | 双周一，打开仓库 **Actions → Init RuyiSDK Biweekly Template → Run workflow**，输入日期（如 `20260915`）和期号（如 `76`），点击运行 | 步骤 1：初始化模板 |
| 2 | 自动 | Action 自动生成当期双周报文件并推送，飞书群收到开始提交通知（含文件链接与截止时间） | 步骤 2：群通知 |
| 3 | 各模块负责人 | 正常提交 PR（fork 或分支均可，流程与之前完全一致） | 步骤 3：提交 PR |
| 4 | 自动 | 每个 PR 自动触发 link-check；通过则自动 squash 合入并删分支；失败则 PR 下自动评论 @作者 及原因 | 步骤 5：审核+合并 |
| 5 | 管理员 | 截止日前在 **Actions → Check Biweekly Progress → Run workflow**（可输入回看天数），飞书群收到进度汇总，据此催办未提交的负责人 | 步骤 4：催交 |
| 6 | 管理员 | 所有 PR 合入后，人工撰写卷首语、review 删减无进展章节、修 typo（此环节保持人工，保证质量） | 步骤 6、7、8 |
| 7 | 管理员/社区经理 | 双周报定稿后在社区转发（卷首语 AI 生成功能规划中） | 步骤 9、10 |

**日常维护注意**：
- PR 作者收到失败评论后，若判断为网络偶发，直接在 Actions 里 Re-run link-check 即可，通过后会自动合入；
- 若需**暂停自动合入**（如某期需要人工把关），临时方案是通知大家先不合并、管理员关闭该 PR 的自动合并——长期方案可在 Ruleset 中临时移除 required check；
- automerge 使用 `--squash`，与现有合并习惯一致。

---

## 五、需要管理员协助配置的事项（请按顺序对照操作）

以下 4 项配置**只有组织管理员/Admin 权限能做**，逐项完成后整套自动化即可上线。

### 配置 ①：组织层放开 fine-grained PAT（必做，绕不过）
1. 打开 `https://github.com/organizations/ruyisdk/settings/personal-access-tokens`；
2. 进入 **Settings** 标签页；
3. **Fine-grained personal access tokens** 一项：
   - 选择 **Allow access**；或
   - 选择 **Require administrator approval**（推荐，可控性更好）——若选此项，配置 ② 中创建的 token 需要你再回到 `Personal access tokens → Requests` 标签页点击 **Approve** 一次；
4. 保存。
> 说明：组织仓库中 fine-grained PAT 若未经组织策略放行，即使 token 本身权限正确，API 也会返回 403。此步骤仅组织所有者可见、可操作。

### 配置 ②：创建 PAT 并存入仓库 Secret（合入功能的开关）
1. 由管理员创建 fine-grained PAT（`Settings → Developer settings → Fine-grained tokens → Generate new token`）：
   - **Token name**：`wechat-articles-automerge`
   - **Resource owner**：选 **ruyisdk**
   - **Repository access**：Only select repositories → 勾选 `ruyisdk/wechat-articles`
   - **Permissions**：
     - Repository permissions → **Contents: Read and write**
     - Repository permissions → **Pull requests: Read and write**
   - **Expiration**：建议 1 年，到期前需更新 Secret；
   
2. 若组织策略为 Require approval，回到组织设置批准该 token（见配置 ① 第 3 步）；
3. 打开 `https://github.com/ruyisdk/wechat-articles/settings/secrets/actions`；
4. **New repository secret**：
   - Name：`AUTO_MERGE_TOKEN`（注意名字一样）
   - Value：粘贴刚才生成的 token；
5. （已经配置，无需操作）配置飞书：同一页面再新建一个 Secret：
   - Name：`FEISHU_WEBHOOK_URL`
   - Value：飞书群 → 设置 → 群机器人 → 添加自定义机器人 → 复制的 Webhook 地址。
> 安全性说明：该 PAT 仅限这一个仓库、仅 Contents+PR 两项写权限；automerge 工作流运行在 main 上下文，PR 作者（含 fork）无法读取该 secret。

### 配置 ③：分支 Ruleset 设置 required check（合入的前置闸门）
1. 打开 `https://github.com/ruyisdk/wechat-articles/settings/rules`（若为分支保护，则在 `settings/branches`）；
2. 针对默认分支 `main` 的 Ruleset（新建或编辑）：
   - **Require status checks to pass** → 添加必须通过的检查：**`link-check`**（注意：名称就是 `link-check`，来自 pr-check.yml 的 job）；
   - **Required approvals**：设为 **0**（否则 PR 会卡在等待人工 approve，自动合入无法触发；如希望保留人工复核，可与我们再商定折中方案）；
   - **Allow squash merging**：保持开启（automerge 使用 squash 方式）；
3. 保存并生效。

### 配置 ④：验证（call 我配合）
- Actions → Init RuyiSDK Biweekly Template：已经验证，成功
- 
- PR自动合入：个人仓验证过，官方仓库需要上述组织管理员配置，完成配置后再验证。
   - 用任意测试分支提一个含 `.md` 修改的 PR：
   - PR 的 Checks 中出现 `link-check` 且能跑完 → pr-check.yml 与 Ruleset 生效；
   - link-check 绿后，Actions 列表自动出现 **Automerge** run 且 PR 变为 **Merged**（squash）→ 配置 ①② 生效；
   - 可再提一个故意带失效链接的 PR，验证 PR 下出现自动评论 → notify-on-fail 生效；
> 验证用的测试 PR/文件可 Revert 清理。

<img width="1848" height="1756" alt="image" src="https://github.com/user-attachments/assets/c679dc42-61a4-49b4-9a52-bd059075e317" />

---

**汇总：需要管理员操作的入口共 3 处**:
- 组织 Settings 的 PAT 策略页
  
- 仓库 Settings 的 Secrets 页

- 仓库 Settings 的 Rules 页
 参考：
 <img width="1254" height="2873" alt="image" src="https://github.com/user-attachments/assets/e5bce8f1-39a5-404e-b7bc-185b4631f28d" />

 

自动合入的配置验证可 @ 我一起进行。目前第75期的双周进展还剩余2部分没有提交，计划用于验证。
