已根据您提供的链接逐条核实，对上一版的"官方"用词与部分事实做了修正。关键事实修订如下：
**核实结果摘要**
- **Debian**（tracker.debian.org/pkg/ruyi）：`ruyi` 已正式进入 Debian 官方仓库。当前 unstable 与 testing 均为 **0.52.0**，stable-backports（trixie-backports）也已收录 **0.52.0-1~bpo13+1**；上游最新 0.53.0 尚待打包。也就是说 **Debian 13 (trixie) 稳定版需启用 backports 才能安装**，testing (forky) / unstable (sid) 可直接安装。
- **Fedora**（packages.fedoraproject.org/pkgs/ruyi/ruyi/）：包审核已完成（Bug #2399640，2025-10-05 initial import），**已正式进入 Fedora 官方仓库**，Rawhide 当前版本 **0.52.0-1**，Fedora 42/43 等活跃分支均可安装。上一版"审核中未入库"的说法需要更正。
- **Arch Linux**：AUR（aur.archlinux.org/packages/ruyi，当前 0.50.0-1，维护者 weilinfox/lilac）与 archlinuxcn 仓库（github.com/archlinuxcn/repo 下 archlinuxcn/ruyi）均为**社区仓库**，不属于 Arch 官方仓库。
- **Gentoo**：ruyisdk-overlay 由 RuyiSDK 项目（ISCAS）维护，**不是 Gentoo 官方 overlay**；其 README 也明确说明 Gentoo 并非 RuyiSDK 官方支持的发行版。
- **openEuler**：`ruyi` 本体尚未进入 openEuler 官方仓库，目前仅前置依赖包通过社区软件包仓库完成引入，ruyi 引入仍在流程中，暂不应列入"已支持"。
## 修订后的发行版支持情况表
| 系统 | 支持情况 | 版本范围 | 如何安装使用 |
|---|---|---|---|
| Debian 13 (trixie) 稳定版 | 官方支持（需启用 backports） | 0.52.0 | `sudo apt install -t trixie-backports ruyi` |
| Debian testing (forky) / unstable (sid) | 官方支持 | 0.52.0 | `sudo apt install ruyi` |
| Debian 12 (bookworm) 及更早 | 不支持 | — | 改用 RuyiSDK 安装脚本或预编译二进制 |
| Ubuntu 最新开发版 | 官方支持（universe） | 0.51.0 起 | `sudo apt install ruyi` |
| Ubuntu 各 LTS（如 24.04）及旧版 | 不支持 | — | 改用 RuyiSDK 安装脚本或预编译二进制 |
| Fedora 42 及以上 | 官方支持 | 0.52.0 | `sudo dnf install ruyi` |
| openRuyi（如意 OS） | 官方支持 | 随发行版仓库发布 | `sudo dnf install ruyi` |
| Arch Linux | 社区仓库（AUR、archlinuxcn） | 0.50.0 | `yay -S ruyi`，或启用 archlinuxcn 源后 `sudo pacman -S ruyi` |
| Gentoo Linux | RuyiSDK 提供 overlay（非官方） | 随 ruyisdk-overlay 更新 | 添加 ruyisdk-overlay 后 `sudo emerge --ask dev-util/ruyi` |
| openEuler | 引入流程中（前置依赖已通过社区软件包仓库完成引入） | — | 暂用 RuyiSDK 安装脚本或预编译二进制 |
| 其他发行版 | 未收录 | — | 使用 RuyiSDK 安装脚本、预编译二进制或 `pipx install ruyi` |
## 各发行版详细用法（按修订后术语）
### Debian
Debian 13 (trixie) 稳定版用户需先启用 backports，在 `/etc/apt/sources.list` 中添加：
```
deb http://deb.debian.org/debian trixie-backports main
```
然后安装：
```bash
sudo apt update
sudo apt install -t trixie-backports ruyi
```
testing (forky) 与 unstable (sid) 用户可直接安装：
```bash
sudo apt update
sudo apt install ruyi
```
### Ubuntu
仅最新开发版仓库收录（universe），各 LTS 及旧版本仓库中没有该包：
```bash
sudo apt update
sudo apt install ruyi
```
LTS 用户请使用 RuyiSDK 安装脚本或预编译二进制（见文末）。
### Fedora
已正式进入官方仓库，Fedora 42 及以上版本直接安装：
```bash
sudo dnf install ruyi
```
### openRuyi（如意 OS）
官方仓库直接安装：
```bash
sudo dnf install ruyi
```
### Arch Linux（社区仓库）
**方式一：AUR 安装**（当前版本 0.50.0-1，维护者 weilinfox），以 yay 为例、请用普通用户执行：
```bash
yay -S ruyi
```
**方式二：archlinuxcn 社区仓库**（由 lilac 自动构建，版本通常更接近上游）。在 `/etc/pacman.conf` 中添加：
```ini
[archlinuxcn]
Server = https://mirror.iscas.ac.cn/archlinuxcn/$arch
```
然后安装：
```bash
sudo pacman -Sy
sudo pacman -S ruyi
```
### Gentoo Linux（RuyiSDK 提供 overlay）
ruyisdk-overlay 由 RuyiSDK 项目维护，**并非 Gentoo 官方 overlay**；包位于 `dev-util/ruyi`：
```bash
# 1. 安装 eselect-repository 与 git
sudo emerge --ask app-eselect/eselect-repository dev-vcs/git
# 2. 添加 ruyisdk-overlay
sudo eselect repository add ruyisdk git https://github.com/ruyisdk/ruyisdk-overlay.git
# 3. 同步仓库
sudo emaint sync -r ruyisdk
# 4. 接受 testing 关键字（ebuild 标记为测试版）
sudo emerge dev-util/ruyi --autounmask-write --autounmask
sudo dispatch-conf   # 输入 u 接受变更
# 5. 安装
sudo emerge --ask dev-util/ruyi
```
需注意 ruyisdk-overlay README 的提示：RuyiSDK 官方软件源提供的部分二进制包可能依赖较旧 ABI 的库，在 Gentoo 等滚动发行版上或需手动调整。
### openEuler
`ruyi` 本体尚未进入 openEuler 官方仓库，目前仅前置依赖包通过社区软件包仓库完成引入，ruyi 本体的引入仍在流程中。当前建议使用 RuyiSDK 安装脚本或预编译二进制安装。
## 版本验证与滞后提示
发行版渠道的版本通常会晚于上游发布一到数个版本（截至本次核实，上游最新为 0.53.0，Debian/Fedora/AUR 仓库分别为 0.52.0 / 0.52.0 / 0.50.0）。安装后建议执行版本验证：
```bash
ruyi version
```
命令正常打印版本号与 Copyright 信息即安装成功。撰写文档时也可附上以下查询入口，便于读者自行确认仓库中的最新版本：
- Debian: https://tracker.debian.org/pkg/ruyi
- Fedora: https://packages.fedoraproject.org/pkgs/ruyi/ruyi/
- AUR: https://aur.archlinux.org/packages/ruyi
- archlinuxcn: https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/ruyi
- ruyisdk-overlay: https://github.com/ruyisdk/ruyisdk-overlay
## 未收录发行版的替代安装方式
- **安装脚本（推荐）**：自动检测架构并从最近镜像下载最新稳定版至 `/usr/local/bin/ruyi`；
- **预编译二进制**：从 GitHub Releases 或 ISCAS 镜像站下载 `amd64` / `arm64` / `riscv64` 之一，`chmod +x` 后放入 PATH；
- **pip 安装**：`pipx install ruyi`，仅适用于 x86_64 与 arm64；riscv64 架构因部分 Python 依赖缺少预编译 wheel 可能构建失败，官方明确不推荐。
同时建议在表格下方保留原文提示：发行版渠道版本可能滞后于上游发布，安装前确认仓库提供的版本，安装后执行 `ruyi version` 验证。
