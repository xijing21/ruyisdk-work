## RISC-V 开发板厂商

| 厂商名称 | 企业类型 | 企业简介 | 产品系列 | RISC-V产品系列和主要开发板型号 |
| :--- | :--- | :--- | :--- | :--- |
| **Milk-V (群芯闪耀)** | 开发板研发 | 近两年非常活跃的RISC-V开发板厂商，产品线覆盖从入门级到服务器级。 | Mars、Pioneer、Jupiter、Megrez | **Mars** (JH-7110)、**Pioneer** (SG2042)、**Jupiter** (SpacemiT K1)、**Jupiter2** (SpacemiT K3)、**Megrez** (EIC7700X)。 |
| **Sipeed（矽速科技）** | 开发板研发 | 国内开源硬件团队，长期运营“荔枝派”系列开发板，致力于AIoT生态建设，提供核心板、模组和垂直解决方案。 | 荔枝派系列、Maix系列 | **LicheePi 4A**：基于TH1520（4×C910@1.85GHz）的高性能RISC-V Linux SBC。另有LicheeRV、LicheeConsole 4A、LicheeBook 4A等。 |
| **香蕉派社区 (Banana Pi)** | 开发板研发 | 长期运营BananaPi系列开源开发板，面向全球开发者社区，产品线覆盖ARM/RISC-V开发板、单板计算机等。 | Banana Pi系列开发板 | **BPI-CANMV-K230D-Zero**（与嘉楠合作）、**BPI-F3**（基于SpacemiT K1）。最新推出了基于SpacemiT K1的**BPI-CM6**系统级模块（SoM），兼容树莓派CM4/CM5的底板。 |
| **香橙派 (Orange Pi)** | 开发板研发 | 知名开源硬件品牌，产品线覆盖ARM开发板、工控板等。 | Orange Pi系列 | **Orange Pi RV**：基于赛昉科技JH-7110的RISC-V开发板。 |
| **飞凌嵌入式 (Forlinx)** | 开发板研发 | 嵌入式产品供应商，提供核心板、开发板等。 | 工业级核心板/开发板 | **OK153-S12 / FET153-S核心板**：基于全志T153（4×Cortex-A7 + 64位RISC-V MCU）。 |
| **嘉楠科技 (Canaan)** | 有自己的芯片 | 高性能ASIC芯片设计公司，区块链+AI双主线，已推出多代AI芯片和区块链计算设备。 | 勘智K系列AI芯片 | **K230、K230D**：基于新32位（RV64ILP32）的AIoT量产芯片。合作推出了**BPI-CANMV-K230D-Zero**开发板。 |
| **赛昉科技 (StarFive)** | 有自己的芯片 | RISC-V处理器IP和芯片供应商，推出“惊鸿”系列AI视觉处理SoC。 | 惊鸿系列SoC及开发板 | **VisionFive 2 / VisionFive 2 Lite** (JH-7110/JH-7110S)：类树莓派规格的RISC-V单板计算机。与BeagleBoard等合作的**BeagleV**。 |
| **进迭时空 (SpacemiT)** | 有自己的芯片 | RISC-V处理器芯片厂商，提供高性能RISC-V SoC，其芯片被多家开发板厂商采用。 | 高性能RISC-V SoC | **K1**：8核X60 RISC-V处理器，被用于Banana Pi BPI-F3/CM6、Milk-V Jupiter、MUSE Book等。**K3**：RVA23合规的8核X100 RISC-V AI SoC，搭载于Milk-V Jupiter2。 |
| **南京沁恒微电子 (WCH)** | 有自己的芯片 | 成立于2004年，专注于连接技术和MCU内核研究，基于自研收发器PHY和处理器IP的全栈研发模式，提供以太网、蓝牙无线、USB和PCI类等接口芯片及全栈MCU。产品以“WCH”品牌在开发者中拥有极高知名度。 | 青稞系列RISC-V MCU | **CH32V系列**：包括CH32V103、CH32V203、CH32V307、CH32V407等通用MCU；**CH58X系列**：低功耗蓝牙无线MCU；**CH32X系列**：特色应用MCU；**CH32L系列**：低功耗MCU。配套开发板丰富，如CH32V307评估板、CH585评估板、CH32L103开发板等。 |
| **华创微 (HC Semi)** | 有自己的芯片 | 中国电子科技集团第十四研究所下属企业，近期在RISC-V处理器和AI芯片上取得突破。 | 高性能处理器、AI芯片 | 2026年2月发布了面向边缘计算的高性能RISC-V处理器及首颗AI芯片，已完成流片和测试。 |

### 厂商开发工具与资源现状

| 厂商名称 | 开发工具与资源现状 |
| :--- | :--- |
| **Milk-V (群芯闪耀)** | 其软件生态与社区联系紧密，多款产品（如Pioneer、Meles）得到了**RevyOS**等社区操作系统的官方支持。对于使用SpacemiT芯片的Jupiter系列，则与芯片原厂的Bianbu OS生态协同。 |
| **Sipeed（矽速科技）** | 拥有**详细的官方Wiki**（`wiki.sipeed.com`），提供从硬件资料、系统镜像烧录到软件开发的全套文档。其TH1520系列（如LicheePi 4A）的软件生态与**RevyOS**（由RuyiSDK团队维护）深度绑定，社区中也有大量基于该平台的实践分享，例如“从零构建Linux操作系统”的教程。 |
| **嘉楠科技 (Canaan)** | 主要为K230系列提供**完善的SDK和开发者文档**。官网设有“嘉楠开发者”专栏，持续更新技术方案和应用教程，例如《K230 Linux免编译升级包》、《RTOS系统Sensor ISP标定保姆级教程》等，帮助开发者快速上手。 |
| **飞凌嵌入式 (Forlinx)** | 作为方案提供商，主要提供**完善的BSP（板级支持包）和硬件开发资料**，帮助客户快速进行产品二次开发，强调**长期供货保障和工业级稳定性**。 |
| **赛昉科技 (StarFive)** | 提供较为**完整的软件资源**。其GitHub仓库（`github.com/starfive-tech`）中包含了Linux内核、U-Boot、Vicuna BIOS等源码。官方文档站点（`doc-en.rvspace.org`）提供详细的开发指南。同时，也为VisionFive系列提供了**Python GPIO库** (`VisionFive.gpio`)，方便开发者进行外设控制，其使用方法与树莓派的`RPi.GPIO`类似。 |
| **进迭时空 (SpacemiT)** | 为其芯片提供**Bianbu OS**（一个基于Ubuntu的发行版）作为官方操作系统，并持续迭代以优化硬件性能和软件体验。其软件栈对RISC-V向量扩展等特性有针对性支持。 |
| **南京沁恒微电子 (WCH)** | **工具链极其完善，自成体系**。自主研发**MounRiver Studio (MRS)** 集成开发环境，已迭代多年并推出基于VSCode的MRS2版本，支持Windows/Linux/macOS。提供**WCH-Link**调试下载器，支持在线调试和下载。拥有丰富的**应用示例、专题培训视频、技术文档和大学计划教材**，生态非常成熟。**合作难点**：其产品体系高度完整、自闭环，开发者在其生态内可完成全部开发工作，RuyiSDK目前能提供的互补价值尚不明显，需深入挖掘结合点（如高端Linux开发板支持、特定行业解决方案）。 |


### 2026年上市RISC-V开发板/设备信息（含内部消息）🚀 

| 厂商名称 | 2026年上市RISC-V开发板/设备型号 | 预计上市时间 | 芯片型号 | 产品简介/信息来源 |
| :--- | :--- | :--- | :--- | :--- |
| **Milk-V (群芯闪耀)** | **Titan** | **已开售** (2026年1月) | UltraRISC **UR-DP1000** (八核) | 高性能mini-ITX主板，支持PCIe Gen4 x16插槽可扩展显卡，最高64GB DDR4 ECC内存，预装Ubuntu，适合桌面级开发与服务器应用。 |
| **Milk-V** | **Jupiter2 系列** (SBC / NX SoM / Dev Kit) | **已公布**，计划2026年上市 | 进迭时空 (SpacemiT) **K3** | 全球首批基于RVA23合规RISC-V芯片K3的开发板。SBC形态配备**10GbE SFP+**万兆高速接口，性能强劲。 |
| **Banana Pi (香蕉派社区)** | **BPI-CM6** 系统级模块 | **已公布** (2026年1月) | 进迭时空 (SpacemiT) **K1** | 兼容树莓派CM4/CM5底板引脚，内置8GB LPDDR4和16GB eMMC，便于现有树莓派用户迁移至RISC-V平台。 |
| **Banana Pi (香蕉派社区)** | **BPI-RV2** | **已公布** (FOSDEM 2026亮相) | Siflower **SF21H8898** | 基于新芯片平台的RISC-V单板计算机，具体规格待进一步披露。 |
| **Orange Pi (香橙派)** | **Orange Pi RV2** | **已公布** (FOSDEM 2026亮相) | Ky **X1** | 新一代RISC-V开发板，具体规格待进一步披露。 |
| **Orange Pi (香橙派)** | **Orange Pi R2S** | **已公布** (FOSDEM 2026亮相) | Ky **X1** | 与RV2同期亮相的新品，具体规格待进一步披露。 |
| **南京沁恒微电子 (WCH)** | **CH32H417系列**及配套评估板 | **已发布** (2026年3月官网展示) | 青稞RISC-V5F+V3F双核 | 超高速USB3.0双核互联型MCU，主频400MHz+150MHz，提供5Gbps超高速USB3.0、百兆以太网PHY等，适于高性能图像传感和数据采集应用。 |
| **飞凌嵌入式 (Forlinx)** | **OK153-S12 Mini 开发板** | **已上市** (2026年1月) | 全志 (Allwinner) **T153** | 基于全志T153工业级处理器，4×Cortex-A7 + 独立RISC-V MCU异构架构，面向工业控制场景。 |
| **华创微 (HC Semi)** | **高性能RISC-V处理器**及**AI芯片**相关开发平台 | **芯片已流片** (2026年2月发布)，开发板待公布 | 华创微自研 | 已完成面向边缘计算的高性能处理器和首颗AI芯片的流片测试，后续预计会推出配套的开发板或解决方案。 |
| **DeepComputing** | **DC-ROMA RISC-V Mainboard III** | **已公布** (预购即将开启) | 进迭时空 (SpacemiT) **K3** | 为Framework Laptop 13设计的RISC-V主板，支持RVA23，8核CPU最高2.5GHz，30 TOPS NPU，可选16/32GB LPDDR5内存。 |
| **Aitver** | **ESP32-C3 0.42英寸OLED开发板** | **已上市** (2026年3月) | 乐鑫 (Espressif) **ESP32-C3** | 微型RISC-V MCU开发板，集成0.42英寸OLED显示屏（72×40像素），支持Wi-Fi 4和蓝牙5.0，售价约4.99美元。 |

补充说明：
1. **Milk-V Titan**是高性能桌面级RISC-V主板的代表，其PCIe Gen4 x16插槽支持主流显卡扩展，是RISC-V进入桌面应用的重要产品。
2. **DeepComputing DC-ROMA Mainboard III**延续了其与Framework合作的开源笔记本路线，基于K3芯片的RVA23支持和30 TOPS NPU使其在AI开发方面具有优势。
3. **Banana Pi BPI-RV2**和**Orange Pi RV2/R2S**是在FOSDEM 2026上亮相的新品，目前公开信息有限，但已确认将采用Siflower和Ky的新款RISC-V芯片。

