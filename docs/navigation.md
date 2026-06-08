- [首页 (index.md)](#)

- [1. 认识 RuyiSDK (intro/)](#) 
  - [1.1 产品简介与愿景 (intro/overview.md)](#) 
  - [1.2 平台兼容性 (intro/compat.md)](#)  👈 platform-support -> compat
  - [1.3 隐私策略简述 (intro/privacy.md)](#)  👈 去掉-brief，在intro下即代表简述
  - [1.4 组成架构 (intro/arch.md)](#)  👈 architecture -> arch
  - [1.5 为什么选择 RuyiSDK (intro/why.md)](#)  👈 上下文明确，why即可

- [2. 快速入门 (start/)](#)  👈 quickstart -> start
  - [2.1 零硬件体验：QEMU 上手 (start/qemu.md)](#) 
  - [2.2 硬件实战：开发板初体验 (start/hw.md)](#)  👈 hardware -> hw

- [3. 需求场景 (scenarios/)](#) 
  - [3.1 场景总览 (scenarios/index.md)](#) 
  - [3.2 S1: 镜像加速 (scenarios/s1-mirror.md)](#)  👈 去掉-acceleration
  - [3.3 S2: 开发板上手 (scenarios/s2-board.md)](#)  👈 去掉-setup
  - [3.4 S3: 交叉编译 (scenarios/s3-cross-compile.md)](#) 
  - [3.5 S4: 自定义 Sysroot (scenarios/s4-sysroot.md)](#)  👈 去掉交叉编译环境重复定语
  - [3.6 S5: 远程调试 (scenarios/s5-debug.md)](#)  👈 remote-debug -> debug
  - [3.7 S6: 教学实验 (scenarios/s6-edu.md)](#)  👈 teaching -> edu
  - [3.8 S7: 多设备管理 (scenarios/s7-multi-dev.md)](#)  👈 multi-device -> multi-dev

- [4. 产品详细指南 (products/)](#) 
  - [4.1 Ruyi 包管理器 (products/pkg/)](#)  👈 package-manager -> pkg
    - [4.1.1 安装与配置 (products/pkg/install.md)](#)  👈 installation -> install
    - [4.1.2 命令详解 (products/pkg/cli.md)](#)  👈 commands -> cli
    - [4.1.3 虚拟环境与 Sysroot (products/pkg/venv.md)](#)  👈 去掉-sysroot重复
  - [4.2 RuyiSDK Eclipse 插件 (products/eclipse/)](#)  👈 eclipse-plugin -> eclipse
    - [4.2.1 安装与更新 (products/eclipse/install.md)](#) 
    - [4.2.2 创建项目 (products/eclipse/project.md)](#)  👈 project-creation -> project
    - [4.2.3 编译与调试 (products/eclipse/debug.md)](#)  👈 去掉编译冗余，保留核心动作
  - [4.3 RuyiSDK VSCode 插件 (products/vscode/)](#)  👈 vscode-plugin -> vscode
    - [4.3.1 安装与更新 (products/vscode/install.md)](#) 
    - [4.3.2 功能与使用 (products/vscode/usage.md)](#)  👈 features -> usage
  - [4.4 RuyiSDK 基础组件 (products/comp/)](#)  👈 components -> comp
    - [4.4.1 组件概览 (products/comp/overview.md)](#) 
    - [4.4.2 GCC 工具链 (products/comp/gcc.md)](#) 
    - [4.4.3 LLVM/Clang 工具链 (products/comp/llvm.md)](#) 
    - [4.4.4 QEMU 模拟器 (products/comp/qemu.md)](#) 
    - [4.4.5 未来路线图 (products/comp/roadmap.md)](#) 

- [5. 社区与贡献 (community/)](#) 
  - [5.1 社区简介 (community/overview.md)](#) 
  - [5.2 核心仓库与 Maintainer (community/repos.md)](#) 
  - [5.3 贡献指南 (community/contributing.md)](#)  👈 去掉-guidelines

- [6. 玩转 RISC-V 开发板 (boards/)](#) 
  - [6.1 选型指南 (boards/selection.md)](#)  👈 去掉开发板、避坑等定语
  - [6.2 系统支持矩阵 (boards/matrix.md)](#)  👈 os-matrix -> matrix
  - [6.3 镜像烧录指南 (boards/flashing.md)](#) 
  - [6.4 应用示例索引 (boards/examples.md)](#) 
  - [6.5 开发板场景实战 (boards/specific/)](#) 
    - [烧录实战：Milk-V Duo (boards/specific/duo-flash.md)](#)  👈 milkv-duo-flashing -> duo-flash
    - [编译实战：Milk-V Duo (boards/specific/duo-compile.md)](#)  👈 milkv-duo-cross-compile -> duo-compile
    - [调试实战：LicheePi 4A (boards/specific/lp4a-debug.md)](#)  👈 licheepi-4a-debugging -> lp4a-debug (LP4A是社区对该板子的通用简称)

- [7. 学习资源 (learn/)](#)  👈 resources -> learn (更强调学习动作)
  - [7.1 嵌入式裸机开发 (learn/bare-metal.md)](#) 
  - [7.2 Linux 应用开发 (learn/linux-app.md)](#) 
  - [7.3 操作系统内核实验 (learn/kernel.md)](#)  👈 os-kernel -> kernel
  - [7.4 教学实验与公开课 (learn/courses.md)](#)  👈 teaching-labs -> courses

- [8. 常见问题与故障排除 (faq/)](#) 
  - [8.1 常见问题 (faq/index.md)](#)
  - [8.2 安装与配置问题 (faq/qa-install.md)](#)  👈 按主题命名，比qa1-xxx更易懂
  - [8.3 编译与调试问题 (faq/qa-debug.md)](#) 

- [9. 法律信息 (legal/)](#) 
  - [9.1 开源许可声明 (legal/licenses.md)](#) 
  - [9.2 商标政策 (legal/trademarks.md)](#) 
  - [9.3 隐私政策 (legal/privacy.md)](#)  👈 去掉-policy完整版后缀，目录已是legal
