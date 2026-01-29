# RuyiSDK 系统兼容性

## RuyiSDK 系统支持计划
RuyiSDK 初期主要支持linux发行版。MacOS、Win 暂缓支持。

Linux发行版支持主要策略：
* 主流的Linux发行版
* 有LTS版本的，支持最新的 2 个 LTS版本；
* 没有 LTS 版本的，支持最新的 1个版本（或者广泛应用的）；

支持计划和支持策略详见：https://ruyisdk.org/docs/Other/platform-support 

## RuyiSDK 核心组件对主流 Linux Distribution 支持情况
### RuyiSDK 核心组件范围
* RuyiSDK 包管理器（ruyi）：最核心的基础工具，目前兼容性验证最齐全；
* RuyiSDK VSCodium（VSCode）插件（ruyisdk-vscode-extension）：依赖Linux发行版对 VSCodium/VSCode 支持情况；插件尽可能的调研和支持这些被广泛应用的Distros中的VSCodium/VSCode 版本；
* RuyiSDK Eclipse 插件（ruyisdk-eclipse-plugins）：依赖Linux发行版对 Eclipse 支持情况；插件尽可能的调研和支持这些被广泛应用的Distros中的Eclipse 版本；
* GNU Toolchain
* LLVM Toolchain
* Qemu

### 支持程度定义
RuyiSDK 核心组件在 Linux Distribution中的支持状态定义为如下几种状态：
* 未验证
* 不支持
* 单独打包(验证技术支持可行性），可单独下载rpm/deb包到系统进行安装
* 包加入发行版社区官方仓库
* 包进入发行版构建系统软件包列表（或者说进入官方软件源）
* 包成为镜像预装软件(主流OS一般不容易，厂商/定制OS相对容易协商)

### 支持程度一览表
https://docs.qq.com/sheet/DUFdWd3NYcFJQandH?tab=BB08J2 
