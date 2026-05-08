# 📊 RuyiSDK 统计数据详细说明

## 致读者
欢迎您来到这里，针对官网web展示的统计数据，有些背景和初衷希望您提前了解。

RuyiSDK 软件栈的内容包含了基础软件（如GNU编译工具链、LLVM工具链、QEMU模拟器、V8、openJDK、Go等）和开发工具（RuyiSDK 包管理器、RuyiSDK VS Code IDE插件、RuyiSDK Eclipse IDE插件等）。

其中基础软件部分通过直接贡献到上游的方式进行 RISC-V 架构适配/优化，其分发方式随着根社区，呈现多样化的特点。
开发工具（RuyiSDK 包管理器、RuyiSDK VS Code IDE插件、RuyiSDK Eclipse IDE插件等）部分也是多渠道多平台分发推广，希望给用户提供多样化的更加便捷的安装方式。其中依托在ISCAS镜像站的 RuyiSDK 软件源 是 RuyiSDK 维护的自建渠道。
由于 RuyiSDK 工具均为开源，源代码依托于 Github 平台，因此 Github Release 也是主要的分发渠道。

鉴于 RuyiSDK 软件源 和 Github Release 提供了方便的数据接口，能够比较方便的获取到下载数据，因此在统计数据中这两个渠道的下载量被广泛包含。根据工具的产品语言特性、社区归属等，还有其它分发方式，但是受限于统计数据无法方便接入，因此统计数据未包含。
为了帮助关注统计数据的伙伴们了解我们的统计数据情况，现整理以下说明。
任何时候，我们的统计数据只是为了更好的帮助我们改善产品。且受限于一些客观限制，数据未必非常精准，以参考和改进产品为目的。

渠道涵盖以下产品：

- **RuyiSDK 包管理器**（`ruyi`命令行工具）
- **RuyiSDK VS Code Extension**
- **RuyiSDK Eclipse Plugins**


## RuyiSDK 分发渠道及是否纳入官网统计页面一览

鉴于 RuyiSDK 软件源 和 Github Release 提供了方便的数据接口，能够比较方便的获取到下载数据，因此在统计数据中这两个渠道的下载量被广泛包含。
上架到应用市场的数据需要前往对应应用市场，通过应用市场的给出的信息了解，具体访问链接在文末给出。

| 渠道 | 包管理器 | VS Code插件 | Eclipse插件  | 纳入统计页面 |
| ------------------------- | --- | --- | --- | --- | 
| ISCAS镜像源               | ✅ | ✅ | ✅ | ✅ |
| GitHub Releases           | ✅ | ✅ | ✅ | ✅ |
| PyPI                      | ✅ | ❌ | ❌ | ✅ |
| Linux发行版系统包仓库     | ✅（进展中） | ❌ | ❌ | ❌ |
| Open VSX                  | ❌ | ✅ | ❌ | ❌ |
| Visual Studio Marketplace | ❌ | ✅ | ❌ | ❌ |
| Eclipse Marketplace       | ❌ | ❌ | ✅ | ❌ |
| Eclipse更新站点           | ❌ | ❌ | ✅（进展中） | ❌ |

## RuyiSDK 统计页面统计数据说明

以下说明对应 RuyiSDK 官网统计面板中的 6 项核心指标。为保障数据口径清晰，分别列出了统计范围、排除渠道及注意事项。

### 1. RuyiSDK 组件包下载量

**定义：** 通过RuyiSDK官方软件源分发的所有二进制组件包（`ruyisdk/dist`目录下）的累计下载次数。

**包含组件：** GNU编译工具链、LLVM编译工具链、QEMU模拟器、调试器、性能分析工具等。

**统计方式：** RuyiSDK软件源服务器日志聚合，统计对 `ruyisdk/dist`目录下所有软件包文件的下载请求。

> ⚠️ **注意：** 同一组件不同版本、不同架构分别计数；不代表独立用户数。**仅统计软件源渠道**，不包含GitHub Releases等其他来源。

### 2. RuyiSDK 遥测设备上报数

**定义：** RuyiSDK包管理器向后端 `ruyi-backend`上报的唯一设备标识符（UUID）的去重数量。**默认开启上报**。

**UUID生命周期：** 每个设备环境（操作系统实例）首次运行 `ruyi`时生成并持久化。重装操作系统、更换硬盘或刷写整机镜像后，原UUID丢失，新环境会生成新UUID，可能重复计数。

**隐私保护：** 不上报任何个人身份信息、IP地址、地理位置；仅用于产品推广效果的大致参考。

**上报策略：** 默认开启上报，用户可通过环境变量 `RUYI_TELEMETRY_OPTOUT=1`禁用。

> 📌 **局限性：** 用户可自愿禁用上报；同一物理设备因重装系统可能产生多个UUID。

### 3. RuyiSDK 文档下载量

**定义：** 通过RuyiSDK软件源分发的文档资源（PDF、HTML包、Markdown打包文件等）的下载次数。

**文档类型：** 峰会/研讨会演示文稿、RVI标准规范文档、RuyiSDK用户手册、技术白皮书、最佳实践指南等。

**统计方式：** RuyiSDK软件源服务器日志，按文件下载请求计数。

### 4. RuyiSDK 包管理器下载量

**定义：** Ruyi包管理器工具（命令行程序 `ruyi`）在各分发渠道的累计下载次数。

**渠道明细（三渠道汇总）：**

- ISCAS镜像源（RuyiSDK软件源的 `ruyi/`目录下多架构多版本的累计下载次数）
- GitHub Releases（发布页预编译二进制压缩包）
- PyPI（`pip install ruyi`）

> 📌 不包括从Linux发行版系统包仓库安装的用户；不同渠道同一用户可能重复下载。Linux发行版系统包仓库暂无法统计下载量和安装量，当前重点着力 ruyi 引入到各Linux发行版镜像源相关工作。

### 5. RuyiSDK VS Code 插件下载量

**定义：** RuyiSDK配套的Visual Studio Code插件的累计下载次数。**本统计不包含Open VSX和Visual Studio Marketplace两个市场。**

**包含渠道：**

- ISCAS镜像源（离线插件包，VSIX文件）
- GitHub Releases

> 📌 如需查看Open VSX或Visual Studio Marketplace的数据，请分别访问对应市场页面。当前数字仅反映镜像源和GitHub Releases分发的下载量。

### 6. RuyiSDK Eclipse 组件下载量

**定义：** RuyiSDK提供的Eclipse IDE定制包及插件的累计下载次数。**本统计不包含Eclipse Marketplace市场。**

**包含内容：**

- 预集成的Eclipse IDE for RuyiSDK（含RISC-V开发插件）
- 独立插件（可安装到现有Eclipse）

**包含渠道：**

- ISCAS镜像源（`ruyisdk/ide/`目录下的完整IDE包和插件包）
- GitHub Releases

> 📌 Eclipse Marketplace数据未纳入本指标，如需查询请访问Eclipse Marketplace官方页面。


## RuyiSDK 分发渠道与链接


### RuyiSDK 包管理器分发渠道

- [RuyiSDK 官方软件源 / ISCAS 镜像源](https://fast-mirror.isrc.ac.cn/ruyisdk/)：在RuyiSDK项目语境下，“RuyiSDK 官方软件源”同“ISCAS 镜像源”（RuyiSDK项目由ISCAS发起，托管于ISCAS镜像源）
- [PyPI 应用市场](https://pypi.org/project/ruyi/)：执行 `pip install ruyi` 安装
- [GitHub Releases](https://github.com/ruyisdk/ruyi/releases/)：构建好的不同架构二进制包，兼容多个Linux发行版
- [ISCAS 镜像源（ruyi目录）](https://mirror.iscas.ac.cn/ruyisdk/ruyi/)：构建好的不同架构二进制包，兼容多个Linux发行版
- Linux发行版系统包仓库（进展中）：
  - Fedora 
  - RevyOS
  - Arch Linux
  - openRuyi
  - openEuler
  - ...

### RuyiSDK VS Code Extension 分发渠道

- [Open VSX](https://open-vsx.org/extension/RuyiSDK/ruyisdk-vscode-extension)：在VSCodium Extensions中搜索 `RuyiSDK` 安装
- [Visual Studio Marketplace](https://marketplace.visualstudio.com/manage/publishers/RuyiSDK)：在VS Code Extensions中搜索 `RuyiSDK` 安装
- [GitHub Releases](https://github.com/ruyisdk/ruyisdk-vscode-extension/releases/)：手动下载VSIX文件安装
- [ISCAS 镜像源](https://mirror.iscas.ac.cn/ruyisdk/ide/plugins/vscode/)：手动下载VSIX文件安装

### RuyiSDK Eclipse Plugins 分发渠道

- [Eclipse Marketplace](https://marketplace.eclipse.org/content/ruyisdk#metrics)：在Eclipse Marketplace中搜索 `RuyiSDK` 安装
- [GitHub Releases](https://github.com/ruyisdk/ruyisdk-eclipse-plugins/releases/)：手动下载ZIP包安装
- [ISCAS 镜像源](https://mirror.iscas.ac.cn/ruyisdk/ide/plugins/eclipse/)：手动下载ZIP包安装
- Eclipse更新站点（Update Site）：通过更新站点URL在线安装（进展中）

> 关于Eclipse Marketplace 应用市场统计数据的说明：
> - Eclipse Marketplace 仅为一个中心化的索引，其中不包含任何插件程序。用户在 Eclipse 中更新已安装的插件时将绕过该市场，因此不产生统计数据。
> - Eclipse Marketplace 网站接口可能存在故障，故需要在 Eclipse IDE 内置商店页面中找到 RuyiSDK 插件并手动记录准确的安装次数。并且经观察，更新插件方式安装时 installed 数据将保持不变。

---

*RuyiSDK 团队维护 · 本说明文档随统计口径调整不定期更新 · 最后更新时间：2026年5月8日*
