# 📊 RuyiSDK 统计数据详细说明

最后更新时间：2026年5月7日 | 数据来源：各渠道统计系统每日自动同步

## RuyiSDK 分发渠道说明

- [RuyiSDK 官方软件源](https://fast-mirror.isrc.ac.cn/ruyisdk/)  在RuyiSDK项目语境下,`RuyiSDK 官方软件源`同`ISCAS 镜像源`(RuyiSDK项目由ISCAS发起，托管在ISCAS镜像源);

- RuyiSDK 包管理器分发渠道
  * [PyPI 应用市场](https://pypi.org/project/ruyi/) ：执行 `pip install ruyi` 安装
  * [GitHub Releases](https://github.com/ruyisdk/ruyi/releases/) ：构建好的不同架构二进制包，兼容多个Linux发行版
  * [ISCAS 镜像源](https://mirror.iscas.ac.cn/ruyisdk/ruyi/) ：构建好的不同架构二进制包，兼容多个Linux发行版
  * Linux 发行版:
    * Fedora
    * RevyOS
    * Arch Linux
    * openRuyi
    * openEuler

* RuyiSDK VSCode Extension 分发渠道
  * [Open VSX](https://open-vsx.org/extension/RuyiSDK/ruyisdk-vscode-extension) ：VSCodium Extensions 中搜索 `RuyiSDK`关键字查询 安装 RuyiSDK 插件
  * [Visual Studio Marketplace](https://marketplace.visualstudio.com/manage/publishers/RuyiSDK) ：VS Code Extensions 中搜索 `RuyiSDK`关键字查询 安装 RuyiSDK 插件
  * [GitHub Releases](https://github.com/ruyisdk/ruyisdk-vscode-extension/releases/) ：手动下载 VSIX 文件安装
  * [ISCAS 镜像源](https://mirror.iscas.ac.cn/ruyisdk/ide/plugins/vscode/) ：手动下载 VSIX 文件安装

* RuyiSDK Eclipse Plugins 分发渠道
  * [Eclipse Marketplace](https://marketplace.eclipse.org/content/ruyisdk#metrics) ：Eclipse Marketplace 中搜索 `RuyiSDK`关键字查询 安装 RuyiSDK 插件
  * [GitHub Releases](https://github.com/ruyisdk/ruyisdk-eclipse-plugins/releases/) ： 手动下载 ZIP 包安装
  * [ISCAS 镜像源](https://mirror.iscas.ac.cn/ruyisdk/ide/plugins/eclipse/) ： 手动下载 ZIP 包安装

---

## RuyiSDK 统计页面统计数据说明

以下说明对应 RuyiSDK 官网统计面板中的 6 项核心指标。为保障数据口径清晰，分别列出了统计范围、排除渠道及注意事项。

### 1. RuyiSDK 组件包下载量

**定义：** 通过 RuyiSDK 官方软件源分发的所有二进制组件包（`ruyisdk/dist`目录下）的累计下载次数。

**包含组件：** GNU 编译工具链、LLVM 编译工具链、QEMU 模拟器、调试器、性能分析工具等。

**统计方式：** 软件源服务器日志聚合，~~每次 `ruyi install` 或系统包管理器（apt/yum）成功拉取包即计数一次(应该只有软件源日志统计数据？)~~。

> ⚠️ **注意：** 同一组件不同版本、不同架构分别计数；不代表独立用户数。仅统计软件源渠道，不包含 GitHub Releases 等。

### 2. RuyiSDK 遥测设备数

**定义：** 在用户明确授权“允许上报匿名设备信息”的前提下，RuyiSDK 包管理器向[后端](https://github.com/ruyisdk/ruyi-backend) `ruyi-backend` 上报的唯一设备标识符（UUID）的去重数量。

**UUID 生命周期：** 每个设备环境（操作系统实例）首次运行 `ruyi` 时生成并持久化。重装操作系统、更换硬盘或刷写整机镜像后，原 UUID 丢失，新环境会生成新 UUID，可能重复计数。

**隐私保护：** 不上报任何个人身份信息、IP 地址、地理位置；仅用于产品推广效果的大致参考。

> 📌 **局限性：** ~~未授权上报的设备不可知(现在是默认会上报？)；~~ 同一物理设备因重装系统可能产生多个 UUID。

### 3. RuyiSDK 文档下载量

**定义：** 通过 RuyiSDK 软件源分发的文档资源（PDF、HTML 包、Markdown 打包文件等）的下载次数。

**文档类型：** 峰会/研讨会演示文稿、RVI 标准规范文档、RuyiSDK 用户手册、技术白皮书、最佳实践指南等。

**统计方式：** 软件源服务器日志，按文件下载请求计数。

### 4. RuyiSDK 包管理器下载量

**定义：** Ruyi 包管理器工具（命令行程序 `ruyi`）在各分发渠道的累计下载次数。

**渠道明细（三渠道汇总）：**
- RuyiSDK 软件源（`https://fast-mirror.isrc.ac.cn/ruyisdk/ruyi/`下载的ruyi多架构多版本的累计下载量）
- GitHub Releases（发布页预编译二进制压缩包）
- PyPI（`pip install ruyi`）

> 📌 不包括通过源码编译安装的用户；不同渠道同一用户可能重复下载。

### 5. RuyiSDK VS Code 插件下载量

**定义：** RuyiSDK 配套的 Visual Studio Code 插件的累计下载次数。**本统计不包含以下两个市场的下载量：** Open VSX Registry 和 Visual Studio Marketplace。

**包含渠道：**
- RuyiSDK 软件源（离线插件包）
- GitHub Releases

> 📌 如需查看 Open VSX 或 Visual Studio Marketplace 的数据，请分别访问对应市场页面。当前数字仅反映内部渠道分发情况。

### 6. RuyiSDK Eclipse 组件下载量

**定义：** RuyiSDK 提供的 Eclipse IDE 定制包及插件的累计下载次数。**本统计不包含 Eclipse Marketplace 市场的下载量。**

**包含内容：**
- 预集成的 Eclipse IDE for RuyiSDK（含 RISC-V 开发插件）
- 独立插件（可安装到现有 Eclipse）

**统计渠道：** RuyiSDK 软件源、GitHub Releases。

> 📌 Eclipse Marketplace 市场数据未纳入本指标，如需查询请访问 Eclipse Marketplace 官方页面。

---

### 📌 整体说明
- “不含某市场”表示该市场的下载量未被加总到当前显示的数字中，主要受限数据接口限制，需要前往应用市场页面查看具体数据。
- 如有疑问或需要原始日志数据，请联系 RuyiSDK 运营团队： contact@ruyisdk.cn



---

*RuyiSDK 团队维护 · 本说明文档随统计口径调整不定期更新*
