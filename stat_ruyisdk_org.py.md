### stat_ruyisdk_org.py 使用说明
#### 脚本目的
为了统计 github/ruyisdk 下的 Forks 、Stars 、 Watchers、Issues 、 PRs、 Contributors 等各项能够反应社区活跃度的统计数据。

#### 统计结果
```
# Repositories工作表
| RepoName       | Forks | Stars | Watchers | Issues | PRs |

# Summary工作表
| TotalRepos | TotalForks | TotalStars | TotalWatchers | TotalIssues | TotalPRs | TotalContributors | StatTime | AllContributors |

```

#### 运行说明（Linux下）
1. 获取your_token_here
2. 配置系统环境变量：export GITHUB_TOKEN=your_token_here
3. 运行脚本：python3 stat_ruyisdk_org.py

#### 运行结果
python3 stat_ruyisdk_org.py
=== 开始统计 ===

[1/3] 获取组织贡献者列表...
找到 47 位组织贡献者

[2/3] 获取仓库列表...
共找到 43 个仓库

[3/3] 处理仓库统计...
  [1/43] 处理: wechat-articles
  [2/43] 处理: revyos
  [3/43] 处理: ruyici
  [4/43] 处理: llvm-project
  [5/43] 处理: riscv-gcc
  [6/43] 处理: riscv-binutils
  [7/43] 处理: docs
  [8/43] 处理: ruyibuild
  [9/43] 处理: riscv-glibc
  [10/43] 处理: riscv-gnu-toolchain
  [11/43] 处理: openwrt-th1520
  [12/43] 处理: dynamorio
  [13/43] 处理: LuaJIT
  [14/43] 处理: ruyisdk-base
  [15/43] 处理: ruyi
  [16/43] 处理: ruyisdk
  [17/43] 处理: demo
  [18/43] 处理: doc4test
  [19/43] 处理: pmd
  [20/43] 处理: ruyisdk-website
  [21/43] 处理: packages-index
  [22/43] 处理: riscv-gnu-toolchain-rv64ilp32
  [23/43] 处理: qemu
  [24/43] 处理: k230-rv64ilp32-linux-kernel
  [25/43] 处理: k230-rv64ilp32-opensbi
  [26/43] 处理: k230-rv64ilp32-u-boot
  [27/43] 处理: mkimg-k230-rv64ilp32
  [28/43] 处理: support-matrix
  [29/43] 处理: ruyisdk-vscode-extension
  [30/43] 处理: linux-xuantie-kernel
  [31/43] 处理: linux-xuantie-kernel-test
  [32/43] 处理: ruyi-backend
  [33/43] 处理: openwrt-eic770x
  [34/43] 处理: k230_linux_sdk
  [35/43] 处理: jdk
  [36/43] 处理: jdk11u
  [37/43] 处理: ruyisdk-xda
  [38/43] 处理: .github
  [39/43] 处理: meta-kendryte-k230
  [40/43] 处理: ruyisdk-overlay
  [41/43] 处理: ruyi-packaging
  [42/43] 处理: ruyisdk-eclipse-packages
  [43/43] 处理: ruyisdk-eclipse-plugins

=== 统计完成 ===
结果已保存到: github_stats_ruyisdk_20250618_175227.xlsx

汇总统计:
{
  "TotalRepos": 43,
  "TotalForks": 168,
  "TotalStars": 155,
  "TotalWatchers": 155,
  "TotalIssues": 434,
  "TotalPRs": 1373,
  "TotalContributors": 47,
  "StatTime": "20250618_175227",
  "AllContributors": "255doesnotexist, Arielfoever, ChunyuLiao, Cyl18, Estherrzhang, FIFCC, Gekyume777, KevinMX, KotorinMinami, Pagerd, RevySR, Sebastianhayashi, Sharelter, Tianyu-Fu, U2FsdGVkX1, Viki1888, YunxiangLuo, abing1991, aisuneko, brsf11, cxjjxc, guoren83, imkiva, infiWang, jamesbeyond, ksco, lazyparser, leeyong5866, luke-8-pro, menghong0522, minghq, nekorouter, panglars, pz9115, qjivy, semiyd, stydxm, trdthg, weilinfox, wychlw, xen0n, xianbing99, xijing21, xingmingjie, yjd01941629, yunxiangluo2023, zxy502"
}


### 获取 GitHub Token 的步骤

1. **登录 GitHub 账户**
   - 访问 [GitHub 官网](https://github.com) 并登录

2. **进入 Token 设置页面**
   - 点击右上角头像 → "Settings"
   - 左侧菜单选择 "Developer settings"
   - 选择 "Personal access tokens" → "Tokens (classic)"

3. **创建新 Token**
   - 点击 "Generate new token" → "Generate new token (classic)"
   - 输入描述（如 "Repo Stats Tool"）
   - 选择过期时间（建议选 "No expiration" 或长期有效期）

4. **设置权限（Scopes）**
   勾选以下权限：
   - `repo` (全选)
   - `read:org`
   - `read:user`

5. **生成 Token**
   - 滚动到页面底部点击 "Generate token"
   - **重要**：立即复制生成的 token（关闭页面后将无法再次查看）
