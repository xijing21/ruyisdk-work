## **一、国内RISC-V生态**

### **(1) CPU IP核心与解决方案厂商**

| 厂商                     | 简介                                                                      | 官网                                                        | 核心产品/特点                                                                                                                                                                                                                             |
| :----------------------- | :------------------------------------------------------------------------ | :---------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **芯来科技**       | 专注于RISC-V处理器IP研发与解决方案，覆盖从低功耗MCU到高性能AIoT的全场景。 | [https://www.nucleisys.com/](https://www.nucleisys.com/)       | **N/X** 系列： 低功耗到高性能应用处理器。`<br>`**UX** 系列： 支持Linux与实时操作系统，UX1030H支持RVA23虚拟化/安全隔离。`<br>`**自研扩展**： Xxldsp、Xxlcz扩展指令集，提升代码密度和性能。                           |
| **阿里巴巴平头哥** | 阿里旗下芯片公司，玄铁系列处理器是国内外生态最成熟的RISC-V IP之一。       | [https://www.t-head.cn/](https://www.t-head.cn/)               | **C906**： 高能效AIoT处理器，广泛应用。`<br>`**C910**： 高性能应用处理器。`<br>`**C920/C930**： 更高性能，支持矢量计算，面向边缘服务器、网络处理。`<br>`**RISE项目** 唯一中国董事会成员，全力推动软件生态。 |
| **赛昉科技**       | 提供从CPU IP到开发板的全栈式解决方案，是RISC-V生态的领导者之一。          | [https://www.starfivetech.com/](https://www.starfivetech.com/) | **昉·天枢**： 高性能处理器IP，支持DDR5/PCIe 5.0，面向PC、数据中心。`<br>`**昉·星光**： 单板计算机，推动开发者生态。                                                                                                       |
| **睿思芯科**       | 创始团队源自UCB RISC-V原创项目组，专注于高端处理器IP与SoC方案。           | [https://www.terapines.com/](https://www.terapines.com/)       | **“灵羽”**： 2025年发布，宣称中国首款全自研服务器级RISC-V芯片。                                                                                                                                                                   |
| **进迭时空**       | 专注于高性能RISC-V芯片与整机解决方案。                                    | [https://www.spacemit.com/](https://www.spacemit.com/)         | **VitalStone V100**： 64核服务器芯片，采用12nm工艺。                                                                                                                                                                                |
| **中科昊芯**       | 专注于RISC-V架构的DSP（数字信号处理器）研发。                             | [https://www.haocore.com/](https://www.haocore.com/)           | **HX2000系列**： 面向工业控制、新能源、汽车电子等实时性要求高的领域。                                                                                                                                                               |
| **奕斯伟**         | 业务覆盖芯片与方案、硅材料、生态链开发。                                  | [https://www.eswin.com/](https://www.eswin.com/)               | **EIC7702X**： AI芯片，2025年加入RISE项目，布局车载与工业市场。                                                                                                                                                                     |
| **匠芯创**         | 专注于工业控制与多媒体AI SoC设计。                                        | [https://artinchip.com/](https://artinchip.com/)               | 在2025 RISC-V峰会展示多款工业应用SoC。                                                                                                                                                                                                    |
| **晶芯科技**       | 新兴的RISC-V CPU IP供应商，致力于提供高性能和可配置的解决方案。           | https://hzt.com.tw/                                        | -                                                                                                                                                                                                                                         |

### **(2) 芯片设计与量产厂商**

| 厂商                 | 简介                                                                  | 官网                                                          | 核心产品/特点                                                                                                     |
| :------------------- | :-------------------------------------------------------------------- | :------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------- |
| **全志科技**   | 老牌智能终端SoC厂商，与平头哥深度合作，量产多款RISC-V芯片。           | [https://www.allwinnertech.com/](https://www.allwinnertech.com/) | **D1系列**： 搭载平头哥C906，面向智能家居、工业互联、车载等市场。                                           |
| **嘉楠科技**   | 区块链及AI芯片厂商，推出全球首款支持RISC-V Vector 1.0的商用量产芯片。 | [https://canaan.io/](https://canaan.io/)                         | **K230**： 多模态边缘AIoT芯片，支持AI计算，面向智慧零售、智能家居等。                                       |
| **算能科技**   | AI芯片与服务器芯片厂商，积极布局RISC-V高性能计算。                    | [https://www.sophgo.com/](https://www.sophgo.com/)               | **SG2042/SG2044**： 64核服务器CPU，已进入主流Linux内核支持。                                                |
| **兆易创新**   | 国内MCU龙头，率先量产全球首款RISC-V内核的32位通用MCU。                | [https://www.gigadevice.com/](https://www.gigadevice.com/)       | **GD32V系列**： 面向工业控制、家电、物联网等，生态成熟。                                                    |
| **乐鑫科技**   | Wi-Fi/Bluetooth MCU全球领导者，ESP32-C系列全面转向RISC-V架构。        | [https://www.espressif.com/](https://www.espressif.com/)         | **ESP32-C3/C5/C6/H2**： 支持Wi-Fi 6、蓝牙5、AI语音，获得PSA安全认证，是物联网领域最成功的RISC-V产品线之一。 |
| **中科蓝讯**   | 无线音频SoC巨头，绝大部分收入来自RISC-V架构芯片。                     | [https://www.bluetrum.com/](https://www.bluetrum.com/)           | **AB32VG1** 等系列，广泛应用于TWS耳机、智能音箱等消费电子领域。                                             |
| **沁恒微电子** | 专注于接口和MCU芯片，其自研的“青稞”RISC-V内核广受欢迎。             | [https://www.wch.cn/](https://www.wch.cn/)                       | **CH32V系列**： 开源内核，性价比高，在2025生态大会上获奖。                                                  |
| **瑞芯微**     | 消费电子与AIoT芯片大厂，已有多款产品采用RISC-V架构。                  | [https://www.rock-chips.com/](https://www.rock-chips.com/)       | 在边缘AI、多媒体处理等领域布局RISC-V。                                                                            |
| **泰凌微电子** | 低功耗无线物联网芯片厂商，多款BLE芯片采用RISC-V内核。                 | [https://www.telink-semi.com/](https://www.telink-semi.com/)     | **TLSR9系列**： 支持多协议并行、AI语音处理。                                                                |
| **博流智能**   | 物联网Wi-Fi/蓝牙SoC厂商。                                             | [https://www.bouffalolab.com/](https://www.bouffalolab.com/)     | **BL602/BL702**： 面向智能家居、可穿戴设备。                                                                |
| **紫光国微**   | 安全芯片与特种IC厂商，已加入中国RISC-V联盟，布局车规级MCU。           | [https://www.ungroup.com/](https://www.ungroup.com/)             | 面向汽车电子、金融安全、工业控制。                                                                                |

### **(3) 开发板与整机制造商**

| 厂商                     | 简介                                                 | 典型产品                   | 官网/社区                                           |
| :----------------------- | :--------------------------------------------------- | :------------------------- | :-------------------------------------------------- |
| **MilkV**          | 专注于RISC-V开发板的创新公司，产品以高性价比著称。   | MilkV Duo, Mars            | [https://milkv.io/](https://milkv.io/)                 |
| **赛昉科技**       | 不仅提供IP，也推出多款高性能开发板。                 | VisionFive 1/2             | [https://rvspace.org/](https://rvspace.org/)           |
| **矽速科技**       | 知名的开源硬件厂商，LicheePi系列支持多种RISC-V芯片。 | Lichee Pi 4A               | [https://sipeed.com/](https://sipeed.com/)             |
| **香山开源处理器** | 中科院计算所的开源项目，也有社区推出的开发板。       | “雁栖湖”、“南湖”评估板 | [GitHub](https://github.com/OpenXiangShan/XiangShan)   |
| **Orange Pi**      | 开源单板计算机厂商，已推出RISC-V架构产品。           | Orange Pi RV               | [https://www.orangepi.org/](https://www.orangepi.org/) |
| **BeagleBoard**    | 国际开源硬件社区，与赛昉等合作推出RISC-V板卡。       | BeagleV-Ahead              | [https://beagleboard.org/](https://beagleboard.org/)   |

### **(4) 软件、工具链与生态服务**

| 厂商/组织                    | 简介                                                       | 官网                                                  | 备注                                 |
| :--------------------------- | :--------------------------------------------------------- | :---------------------------------------------------- | :----------------------------------- |
| **兆松科技**           | 专注于RISC-V和AI基础软件，提供编译器、指令优化和AI软件栈。 | [https://www.terapines.com/](https://www.terapines.com/) | 与睿思芯科关联，提供软硬件一体方案。 |
| **北京开源芯片研究院** | 推动中国开源芯片生态，主办“一生一芯”等人才培养计划。     | [https://www.bosc.ac.cn/](https://www.bosc.ac.cn/)       | “香山”处理器的主要支持单位。       |
| **RIOS Lab**           | 国际RISC-V开源实验室（中美合作），推动开源IP与生态建设。   | [https://www.rioslab.org/](https://www.rioslab.org/)     | 与清华、伯克利等高校紧密合作。       |
| **Antmicro**           | 国际领先的嵌入式系统与开源方案服务商，积极参与中国生态。   | [https://antmicro.com/](https://antmicro.com/)           | 提供FPGA实现、系统定制和软件服务。   |

---

## **二、国际RISC-V生态**

### **(1) 核心IP与芯片厂商**

| 公司                            | 简介                                                     | 官网                                                          | 核心产品/特点                                                                                                                                          |
| :------------------------------ | :------------------------------------------------------- | :------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SiFive**                | RISC-V商业化先驱和生态核心推动者。                       | [https://www.sifive.com/](https://www.sifive.com/)               | **Performance P870**： 高性能CPU IP，支持RVA23。`<br>`**Intelligence X390**： 高性能AI/矢量处理器。`<br>`**HiFive** 开发板系列。 |
| **Andes Technology**      | 亚洲领先的CPU IP公司，RISC-V产品线非常全面。             | [https://www.andestech.com/](https://www.andestech.com/)         | **AndesCore AX45MP**： 高性能多核处理器，支持Linux，面向汽车、网络。`<br>`**RISC-V International** 及 **RISE** 董事会成员。        |
| **Codasip**               | 提供RISC-V处理器IP和定制化工具链，强调“处理器定制”。   | [https://www.codasip.com/](https://www.codasip.com/)             | 支持客户自定义指令，面向AI、通信等专用领域。                                                                                                           |
| **Ventana Micro Systems** | 专注于数据中心级高性能RISC-V CPU Chiplet。               | [https://www.ventanamicro.com/](https://www.ventanamicro.com/)   | **Veyron V2**： 192核服务器CPU，采用Chiplet技术，性能对标ARM Neoverse。`<br>`**RISE** 董事会成员。                                       |
| **Tenstorrent**           | 由Jim Keller领导的AI高性能计算公司，主要采用RISC-V架构。 | [https://tenstorrent.com/](https://tenstorrent.com/)             | **Ascalon** CPU IP，宣称性能领先AMD Zen 5，面向AI训练和推理。                                                                                    |
| **Qualcomm**              | 移动芯片龙头，已大规模量产用于穿戴设备的RISC-V MCU。     | [https://www.qualcomm.com/](https://www.qualcomm.com/)           | **Snapdragon Wear** 平台中的RISC-V MCU，并牵头成立 **Quintauris** 公司。                                                                   |
| **NVIDIA**                | 在其GPU中广泛使用自研的RISC-V内核作为控制器。            | [https://www.nvidia.com/](https://www.nvidia.com/)               | 已量产超30亿颗RISC-V核心，并积极将CUDA生态向RISC-V移植。                                                                                               |
| **Intel**                 | 通过IFS代工服务和生态基金大力支持RISC-V发展。            | [https://www.intel.com/](https://www.intel.com/)                 | 设立10亿美元基金，推动RISC-V在IFS平台上的创新。                                                                                                        |
| **Microchip**             | 提供集成RISC-V硬核的FPGA产品。                           | [https://www.microchip.com/](https://www.microchip.com/)         | **PolarFire SoC FPGA**： 集成5核RISC-V CPU子系统。                                                                                               |
| **Esperanto**             | 研发高能效、大规模多核RISC-V AI加速器。                  | [https://www.esperantotech.com/](https://www.esperantotech.com/) | **ET-SoC-1**： 集成了1000多个RISC-V内核，面向数据中心AI推理。                                                                                    |
| **Rivos**                 | 由苹果前高管创立，专注于数据中心和AI服务器的RISC-V芯片。 | [https://www.rivosinc.com/](https://www.rivosinc.com/)           | 2025年获得新一轮大额融资，加速产品研发。                                                                                                               |
| **AheadComputing**        | 由前Intel团队创立，专注于64位高性能RISC-V CPU。          | -                                                             | 2025年完成2150万美元种子轮融资，旨在解决AI计算瓶颈。                                                                                                   |

---

## **三、全球生态联盟与关键组织**

| 组织/联盟                      | 简介                                                          | 官网                                                        | 备注/特点                                                                                                                                                               |
| :----------------------------- | :------------------------------------------------------------ | :---------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RISC-V International** | 全球RISC-V标准制定与生态推广的核心组织。                      | [https://riscv.org/](https://riscv.org/)                       | 拥有4500多名成员，负责ISA标准、认证和生态建设。**RVA23** 应用处理器规范已批准。                                                                                   |
| **RISE Project**         | 由Linux基金会托管的全球软件生态加速计划。                     | [https://riseproject.dev/](https://riseproject.dev/)           | 核心目标是加速RISC-V在主流操作系统（Android, Linux）、语言（Java, Python, Go）和框架上的成熟度。**董事会成员包括谷歌、英特尔、平头哥、高通、英伟达、Red Hat等**。 |
| **Quintauris**           | 由高通、博世、英飞凌、恩智浦、北欧半导体合资成立。            | [https://www.quintauris.com/](https://www.quintauris.com/)     | 专注于为汽车和物联网提供商业化RISC-V解决方案，2025年推出**RT-Europa** 实时处理器规范。                                                                            |
| **中国RISC-V产业联盟**   | 推动中国RISC-V产业链协同创新与应用落地。                      | [http://www.crvic.org/](http://www.crvic.org/)                 | 涵盖芯片、软件、系统、投资等全产业链。                                                                                                                                  |
| **中国开放指令生态联盟** | 聚焦于开源指令集和开源芯片生态的产学研结合。                  | [https://crva.ac.cn/](https://crva.ac.cn/)                     | 成员包括阿里、华为、中科院等顶尖机构。                                                                                                                                  |
| **RISC-V专利联盟**       | 由中国多家芯片巨头联合成立，旨在构建专利共享和防护体系。      | [https://www.crvaic.org/](https://www.crvaic.org/)             | 初始成员包括芯原、平头哥、赛昉等9家公司，推动专利互不诉讼。                                                                                                             |
| **DARE Project**         | 欧洲EuroHPC联合体资助的大型项目，开发数据中心级RISC-V处理器。 | [https://eurohpc-ju.europa.eu/](https://eurohpc-ju.europa.eu/) | 投资2.4亿欧元，联合38家机构，开发通用CPU、矢量加速器和AI处理器。                                                                                                        |

---

## **四、重点开源项目与社区**

| 项目/社区               | 简介                                                  | 资源地址                                                  | 备注/特点                                                                                                    |
| :---------------------- | :---------------------------------------------------- | :-------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| **香山**          | 中科院计算所开源的高性能RISC-V处理器核。              | [GitHub](https://github.com/OpenXiangShan/XiangShan)         | **“雁栖湖”**（28nm）、**“南湖”**（14nm）版本，性能对标ARM Cortex-A76，2025年进入商业化预期。 |
| **Ventus GPGPU**  | 清华大学开源的支持RISC-V Vector扩展的GPGPU项目。      | [GitHub](https://github.com/THU-LAM-Ventus/Ventus)           | 包含完整的ISA、编译器、仿真器和验证工具链。                                                                  |
| **CORE-V Family** | OpenHW Group主导的开源、工业级验证的RISC-V IP核家族。 | [https://www.openhwgroup.org/](https://www.openhwgroup.org/) | **CV32E40P**、**CVA6** 等，目标是为商用提供高质量的开源IP。                                      |
| **Rocket Chip**   | 基于Chisel构建的RISC-V SoC生成器，源自UCB。           | [GitHub](https://github.com/chipsalliance/rocket-chip)       | 学术研究和原型设计中最常用的平台之一。                                                                       |
| **SWERV**         | Western Digital开源的两款RISC-V核心。                 | [GitHub](https://github.com/chipsalliance/Cores-SweRV)       | **SweRV EH2**（双核）和 **SweRV EL2**，面向嵌入式和控制应用。                                    |

---

## **五、高校与科研机构（核心贡献者）**

| 机构                         | 主要贡献                                                  | 官网                                                      |
| :--------------------------- | :-------------------------------------------------------- | :-------------------------------------------------------- |
| **UC Berkeley**        | RISC-V指令集的发源地，持续引领架构创新和开源实践。        | [https://www.berkeley.edu/](https://www.berkeley.edu/)       |
| **中科院计算所**       | 发起“香山”高性能开源处理器项目，推动产学研用结合。      | [https://www.ict.ac.cn/](https://www.ict.ac.cn/)             |
| **清华大学**           | 发起“乘影”开源GPGPU项目，在计算机体系结构领域贡献突出。 | [https://www.tsinghua.edu.cn/](https://www.tsinghua.edu.cn/) |
| **苏黎世联邦理工学院** | 在RISC-V安全架构、形式化验证等方面做出重要贡献。          | [https://ethz.ch/](https://ethz.ch/)                         |

---
