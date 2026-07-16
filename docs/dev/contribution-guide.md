# 文档仓库重构说明与贡献指南

---

## 一、背景概述

### 1.1 当前状况

RuyiSDK 文档仓库 (`ruyisdk/docs`) 采用**分支即部署**的方式：
- **`zh` 分支**：直接关联线上官网文档，任何提交都会实时影响生产环境
- 文档历经多次迭代，存在结构不够清晰、目录层次杂乱、部分内容过时等问题，亟需一次整体性重构

### 1.2 重构的挑战

| 问题 | 说明 |
|------|------|
| 影响面大 | 重构涉及目录调整、文件移动、内容重写，几乎触及每个角落 |
| 不能影响线上 | `zh` 分支正在被其他开发者持续使用（新增功能说明、使用指南等） |
| 审校周期长 | 大规模变动需要逐页审核，合入过程不能仓促 |

### 1.3 解决方案：双分支并行开发

```
zh 分支（生产环境） ←—— 日常维护、新功能文档
        ↑
        │ 最终合并
        │
restructure-zh 分支 ←—— 文档重构专项工作（不受生产环境影响）
```

- **`restructure-zh`**：专门用于文档重构，所有结构改动在此分支完成
- **`zh`**：保持不变，继续接收日常文档更新
- 重构完成后，将 `restructure-zh` 一次性合入 `zh`，平滑上线

---

## 二、行动方案概览

### 2.1 阶段划分

| 阶段 | 任务 | 负责人 |
|------|------|--------|
| 阶段一 | 确立新目录结构、模板规范、迁移方案 | 核心团队 |
| 阶段二 | 多人并行在 `restructure-zh` 上各自负责不同模块的重构 | 全体贡献者 |
| 阶段三 | 整合审校，修复链接、格式等问题 | 核心团队 |
| 阶段四 | 合并 `restructure-zh` → `zh`，灰度验证后上线 | 分支管理员 |

### 2.2 协同方式

- 重构贡献者均基于 `restructure-zh` 分支提交 PR
- 其他开发人员继续向 `zh` 分支提交日常文档更新
- 两套 PR 互不干扰，各自审校合入

---

## 三、贡献者指南

### 3.1 前置准备

#### 步骤一：Fork 主仓库

1. 访问 https://github.com/ruyisdk/docs
2. 点击右上角 **Fork** 按钮
3. Fork 到你的个人 GitHub 账户下

#### 步骤二：克隆并配置远程仓库

```bash
# Clone 主仓库（开源社区标准做法）
git clone https://github.com/ruyisdk/docs.git
cd docs

# 添加你的个人 fork 作为远程仓库
git remote add personal https://github.com/your-username/docs.git

# 确认远程仓库配置
git remote -v
# 应显示：
# origin    https://github.com/ruyisdk/docs.git (fetch)
# origin    https://github.com/ruyisdk/docs.git (push)
# personal  https://github.com/your-username/docs.git (fetch)
# personal  https://github.com/your-username/docs.git (push)
```

> **说明**：本文档采用开源社区最主流的做法——`origin` 指向主仓库，个人 fork 命名为 `personal`。你也可以根据自己的习惯调整命名，操作本质不变。

---

### 3.2 核心规则 ⚠️

> **每次贡献必须新建一个独立的个人特性分支，严禁直接在 `restructure-zh` 上提交。**

**原因**：
- 避免多个 PR 之间互相包含对方的提交
- 每个 PR 只关注一个独立模块，便于审校
- 如果某次修改被拒绝或需要返工，不影响其他工作

---

### 3.3 标准工作流程

#### 步骤一：同步主仓库最新代码

> ⚠️ **在创建新特性分支之前，必须先同步主仓库的最新代码，确保工作基于最新版本。**

```bash
# 切换到 restructure-zh 分支
git checkout restructure-zh

# 拉取主仓库最新代码
git fetch origin restructure-zh
git reset --hard origin/restructure-zh
```

#### 步骤二：创建个人特性分支

```bash
git checkout -b refactor/your-module-name
```

**分支命名规范**：

| 前缀 | 用途 | 示例 |
|------|------|------|
| `refactor/` | 重构已有内容 | `refactor/quickstart` |
| `feat/` | 新增文档模块 | `feat/advanced-usage` |
| `fix/` | 修复内容错误 | `fix/broken-links` |
| `chore/` | 杂项调整（格式、索引等） | `chore/update-toc` |

#### 步骤三：进行文档重构工作

在个人分支上完成文档修改、移动、重写等工作。

#### 步骤四：提交变更

```bash
# 查看修改状态
git status

# 添加变更
git add .

# 提交（必须包含 -s 签名，通过 DCO 检查）；commit message 强烈推荐使用英语；
git commit -s -m "<type>(<scope>): <subject>"
```

**提交信息格式**：

```
<type>(<scope>): <subject>

- type: refactor | feat | fix | chore
- scope: 影响的模块，如 quickstart, api, install
- subject: 简短说明做了什么
```

示例：
```bash
git commit -s -m "refactor(quickstart): restructure directory and add env setup section"
git commit -s -m "feat(api): add RuyiSDK interface documentation"
git commit -s -m "fix(install): correct package name in installation guide"
git commit -s -m "feat(api): 补充接口说明"  # 不推荐，没有使用英语
```

> **关于 `-s` 参数**：`git commit -s` 会在提交信息末尾自动添加 `Signed-off-by: Name <email>`，这是 DCO（Developer Certificate of Origin）检查的门禁要求。**每个提交都必须包含此签名，否则 PR CI 检查将无法通过。**
> commit message 强烈推荐使用英语；

#### 步骤五：提交 PR 前再次同步主仓库

> 在你工作期间，主仓库可能有新的合入，提交 PR 前务必再次同步，避免冲突。

```bash
# 拉取主仓库最新代码
git fetch origin restructure-zh

# 切回个人分支，进行 rebase
git checkout refactor/your-module-name
git rebase origin/restructure-zh
```

**遇到冲突的解决步骤**：
```bash
# 1. 查看冲突文件
git status

# 2. 手动编辑冲突文件，解决冲突
# 3. 标记为已解决
git add .

# 4. 继续 rebase
git rebase --continue

# 5. 重复直到 rebase 完成
```

#### 步骤六：推送到个人 Fork

```bash
# 首次推送该分支（-u 建立本地与远程分支的关联）
git push -u personal refactor/your-module-name

# 后续推送可直接使用
git push personal refactor/your-module-name
```

> **注意**：如果 rebase 后推送，需要使用强制推送：
> ```bash
> git push -f personal refactor/your-module-name
> ```

#### 步骤七：创建 Pull Request

1. 访问你的 Fork 仓库：`https://github.com/your-username/docs`
2. 页面会自动提示刚推送的分支，点击 **Compare & pull request**
3. 或手动点击 **Pull requests** → **New pull request**
4. 设置 PR 参数：
   - **base repository**：`ruyisdk/docs`
   - **base branch**：`restructure-zh`
   - **head repository**：`your-username/docs`
   - **head branch**：`refactor/your-module-name`
5. 填写 PR 标题和描述（参考下方模板）
6. 确认 DCO 检查通过后，等待审校

**PR 描述模板**：
```markdown
## 重构内容
简要说明本次重构涉及的范围

## 变更说明
- 修改了哪些文件
- 调整了哪些结构
- 新增/删除了哪些内容

## 影响范围
说明本次变更影响的文档页面

## 检查清单
- [ ] 所有链接有效
- [ ] 格式正确
- [ ] 内容准确
```

#### 步骤八：PR 合入后的清理

```bash
# 切换到 restructure-zh
git checkout restructure-zh

# 拉取最新代码（包含刚合入的 PR）
git fetch origin restructure-zh
git reset --hard origin/restructure-zh

# 删除本地特性分支
git branch -d refactor/your-module-name

# 删除个人 Fork 上的远程分支（可选）
git push personal --delete refactor/your-module-name
```

---

### 3.4 PR 修改与更新

当 PR 收到审校意见需要修改时：

```bash
# 切回 PR 对应的分支
git checkout refactor/your-module-name

# 进行修改
# ... 修改文件 ...

# 提交修改
git add .
git commit -s -m "fix: Modified according to review comments"

# 推送到个人 fork（PR 会自动更新）
git push personal refactor/your-module-name
```

如果主仓库在你修改期间有新提交：

```bash
# 同步主仓库最新代码
git fetch origin restructure-zh
git rebase origin/restructure-zh

# 解决冲突后强制推送
git push -f personal refactor/your-module-name
```

---

### 3.5 多 PR 并行开发

```bash
# PR #1：模块 A
git checkout restructure-zh
git reset --hard origin/restructure-zh
git checkout -b refactor/module-a
# ... 工作 ...
git push -u personal refactor/module-a

# PR #2：模块 B（完全独立，互不影响）
git checkout restructure-zh
git reset --hard origin/restructure-zh
git checkout -b refactor/module-b
# ... 工作 ...
git push -u personal refactor/module-b
```

---

### 3.6 注意事项汇总

| 事项 | 说明 |
|------|------|
| ✅ 每次新建分支 | 不要复用旧分支，确保每个 PR 干净独立 |
| ✅ 提交前先同步 | 创建分支前和提交 PR 前，都要同步主仓库最新代码 |
| ✅ 使用 `-s` 签名 | 每个 commit 必须包含 `Signed-off-by`，通过 DCO 检查 |
| ✅ 提交粒度适中 | 一个 PR 不要太大，便于 review（建议 < 500 行变动） |
| ✅ 描述清楚 | PR 中说明改了什么、为什么改、影响哪些页面 |
| ✅ 检查链接 | 移动文件后记得更新相关引用链接 |
| ❌ 不要直接 push 到主仓库 | 所有变更走 PR |
| ❌ 不要在 restructure-zh 上直接提交 | 统一用 PR 合入 |
| ❌ 不要用同一个分支提交多个 PR | 避免提交污染 |

---

## 四、分支管理员：合并 restructure-zh 到 zh

当 `restructure-zh` 重构工作全部完成后，需要将其合并回 `zh` 分支。由于差异可能很大，建议按以下步骤平滑完成。

### 4.1 准备工作

```bash
# 确保本地有所有分支最新状态
git checkout restructure-zh
git pull origin restructure-zh
git checkout zh
git pull origin zh
```

### 4.2 备份 zh 分支

```bash
git checkout zh
git checkout -b zh-backup-$(date +%Y%m%d)
git push origin zh-backup-$(date +%Y%m%d)
git checkout zh
```

### 4.3 创建合并预览分支（可选但推荐）

```bash
git checkout -b preview-merge-zh-restructure
git merge restructure-zh --no-ff
# 检查合并结果、文档构建是否正常
```

### 4.4 执行合并

```bash
# 切换到 zh 分支
git checkout zh
git pull origin zh

# 执行合并
git merge restructure-zh --no-ff -m "merge: 合并 restructure-zh 文档重构成果"
```

**解决冲突**（如有）：
```bash
# 查看冲突文件
git status

# 手动解决冲突后
git add .
git commit -m "merge: 解决 restructure-zh 合并冲突"
```

### 4.5 验证文档构建

```bash
# 本地构建验证（根据项目实际构建命令）
npm run build   # 或 docsify serve、mkdocs build 等
```

确保：
- 所有页面正常生成
- 链接无 404
- 样式正常

### 4.6 推送并上线

```bash
# 推送到远程
git push origin zh

# 触发部署（根据项目实际部署方式）
# 建议先在预发布环境验证，确认无误后再部署生产
```

### 4.7 紧急回滚方案

如果合并后发现问题：

```bash
# 方式一：回滚到合并前的 commit
git checkout zh
git reset --hard <合并前的commit-hash>
git push --force origin zh

# 方式二：使用备份分支恢复
git checkout zh
git reset --hard zh-backup-YYYYMMDD
git push --force origin zh
```

---

## 五、命令速查表

| 操作 | 命令 |
|------|------|
| 同步主仓库最新 | `git fetch origin restructure-zh && git reset --hard origin/restructure-zh` |
| 创建新分支 | `git checkout -b refactor/xxx` |
| 提交（含 DCO 签名） | `git add . && git commit -s -m "refactor(xxx): 描述"` |
| rebase 同步 | `git fetch origin restructure-zh && git rebase origin/restructure-zh` |
| 首次推送到个人 fork | `git push -u personal refactor/xxx` |
| 后续推送 | `git push personal refactor/xxx` |
| 强制推送 | `git push -f personal refactor/xxx` |
| 清理本地分支 | `git branch -d refactor/xxx` |
| 清理远程分支 | `git push personal --delete refactor/xxx` |

---

## 六、参考链接

- [RuyiSDK 文档写作规范与检查指南](https://github.com/ruyisdk/docs/pull/146)
- [重构后的 RuyiSDK 产品简介](https://github.com/ruyisdk/docs/pull/142)  
  
- [DCO 检查说明](https://developercertificate.org/)
- [GitHub Fork 工作流](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models#fork-and-pull-model)
- [Git Commit 规范](https://www.conventionalcommits.org/)

---

如有疑问，欢迎随时在 PR 中或社区交流群中提出。
