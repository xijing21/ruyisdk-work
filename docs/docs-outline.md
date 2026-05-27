- [快速入门](./quickstart.md)
- [开篇必读](./index)
  - [产品介绍](./gs/introduction.md)
  - [平台支持情况/兼容性](./gs/platform-support.md)
  - 法律信息
    - [隐私政策](./gs/privacyPolicy.md)
    - 知识产权与DCO

- [Ruyi 包管理器](./rpm/)
  > rpm: RISC-V Package Manager
  - [功能概览](./rpm/index.md)：对照ruyi -h 中的子命令和功能，进行介绍
  - [安装](./rpm/install.md)
  - [管理 Ruyi 软件包](./rpm/pkg.md)
  - [使用集成功能](./rpm/intergration.md)
  - [个性化配置与管理](./rpm/config.md)：各种自定义路径、自定义配置等；如安装路径、软件源设置、遥测模式设置等
  - [更多](./rpm/misc.md)

- [RuyiSDK VSCode 插件](./vsc/)
  - [功能概览](./vsc/index.md)
  - [安装](./vsc/install.md)
  - [管理Ruyi软件包](./vsc/pkg.md)
  - [虚拟环境](./vsc/venv.md)
  - [新闻（News）与状态栏](./vsc/news.md)
  - [源码包提取](./vsc/extract.md)
  - [构建](./vsc/build.md)
  - [集成开发案例](./vsc/caselist.md)

- [RuyiSDK Eclipse 插件](./ecl/)
  - [功能概览](./ecl/index.md)
  - [安装](./ecl/install.md)
  - [管理Ruyi软件包](./ecl/pkg.md)
  - [虚拟环境](./ecl/venv.md)
  - [新闻（News）与状态栏](./ecl/news.md)
  - [源码包提取](./ecl/extract.md)
  - [构建](./ecl/build.md)
  - [集成开发案例](./ecl/caselist.md)
    
- [开发板使用案例](./board/)：链接到 board-docs 网站去
  - [QEMU]
      - 使用 QEMU 和 LLVM
  - [Milk-V Duo](./board/milkv-duo/):设备对应文件名同packages-index中entity；
      - dd 方式刷写开发板 (以 MilkV Duo 为例)
      - 使用厂商发布的二进制工具链构建 (以 MilkV Duo 为例)
      - 构建 milkv-duo-examples 示例程序
      - Milkv Duo : 使用 riscv64-unknown-linux-musl-bin 工具链编译、运行、调试
  - [Licheepi 4A](./board/licp4a/)
        - 以 fastboot 方式刷写开发板 (以 Licheepi 4A 为例)
        - 使用 Ruyi 编译环境构建 (以 Licheepi 4A 为例)
  - [K230D](./board/k230d/)
    - [Canaan K230D 使用说明](./case/k230d/)



