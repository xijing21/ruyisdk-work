## **一、国内RISC-V芯片及开发板厂商/企业**

### （1）CPU核心/IP研发生产厂商

| 厂商| 简介| 官网| 文档/社区| 备注/扩展指令集/特点|
| -------- | --------- | --------- | -------- | --------- |
| 芯来科技              | 全系列RISC-V处理器IP及解决方案，低功耗到高性能| https://www.nucleisys.com/ | https://docs.nucleisys.com/ | 自研Xxldsp、Xxlcz扩展指令集，提升代码密度和性能；新增UX1030H，支持RVA23虚拟化/安全隔离，高并发  |
| 沁恒微电子            | MCU及USB/接口芯片厂商，有RISC-V MCU产品线| https://www.wch.cn/| https://www.wch.cn/bbs/| CH32V系列，开源RISC-V内核；青稞RISC-V系列，2025生态大会获奖|
| 阿里巴巴平头哥        | 玄铁系列IP，AIoT/高性能计算| https://www.t-head.cn/| https://occ.t-head.cn/| 玄铁C906/C910/C930等，生态成熟；玄铁C930服务器级已交付，RISE唯一中国董事会成员|
| 睿思芯科（RISC-Mind） | 高端RISC-V处理器IP与SoC方案，创始团队源自伯克利RISC-V原创组 | https://www.terapines.com/ | -| 高性能RISC-V服务器CPU，面向边缘计算与数据中心；2025发布“灵羽”处理器，中国首款全自研服务器芯片 |
| 中科昊芯              | RISC-V DSP(数字信号处理器)| https://www.haocore.com/   | -| HX2000系列，工业控制/新能源/汽车电子|
| 奕斯伟（ESWIN）       | 芯片/方案/生态，车载工业| https://www.eswin.com/     | -| EIC7702X AI芯片，2025加入RISE|
| 进迭时空（SpacemiT）  | 高性能RISC-V芯片/整机| https://www.spacemit.com/  | -| VitalStone V100 64核服务器芯片，12nm工艺|
| 匠芯创（ArtInChip）   | 工业控制SoC，多媒体AI| https://artinchip.com/     | -| 2025峰会展示工业应用SoC|
| Andes Technology | 台湾RISC-V IP厂商，推出AE350等高性能处理器；高性能IP，AX45MP多核 | https://www.andestech.com/| AndesCore系列，面向AIoT、车载；与BrainChip合作AI|

### （2）物理芯片制造/量产厂商

| 厂商| 简介| 官网| 文档/社区/售卖| 备注/扩展指令集/特点|
| ------- | --------- | -------- | ---------- | ---------- |
| 全志科技           | 智能终端SoC芯片厂商，量产多款RISC-V芯片，与阿里平头哥深度合作| https://www.allwinnertech.com/| https://bbs.aw-ol.com/| D1系列，AIoT/车载；D1系列，面向智能家居、工业互联、车载等|
| 嘉楠科技           | 区块链及AI芯片厂商，推出全球首款RISC-V Vector1.0商用量产芯片K230| https://canaan.io/| https://developer.canaan-creative.com/ | K230支持AI计算，面向边缘AI场景|
| 算能科技（Sophgo） | AI芯片与服务器芯片厂商，推出64核RISC-V服务器芯片| https://www.sophgo.com/| -| 面向高性能计算、AI加速、云端推理等；SG2044 64核服务器升级版，主线Linux 6.16 |
| 兆易创新           | 国内MCU龙头，量产全球首款RISC-V内核32位通用MCU（GD32V系列）| https://www.gigadevice.com/| -| 工业控制、家电、物联网等应用；全球首款RISC-V 32位通用MCU                    |
| 中科蓝讯           | 无线音频SoC厂商，90%收入来自RISC-V架构芯片| https://www.bluetrum.com/| -| AB32VG1等，面向TWS耳机、智能音箱等|
| 乐鑫科技           | Wi-Fi/Bluetooth MCU；Wi-Fi MCU芯片全球市占率超30%，ESP32-C系列均采用RISC-V架构 | https://www.espressif.com/| https://docs.espressif.com/| ESP32-C3/C6/C5/H2，支持AI语音、低功耗物联网；ESP32-C系列，PSA-L2安全认证    |
| 瑞芯微             | 消费电子与AIoT芯片厂商，已量产RISC-V架构产品| https://www.rock-chips.com/| -| 边缘AI、多媒体、智能终端|
| 泰凌微             | 低功耗无线物联网芯片厂商，多款BLE芯片采用RISC-V架构| [https://www.telink-semi.com/](https://www.telink-semi.com/) || TLSR9系列，支持多协议并行、AI语音处理|
| 博流智能           | 物联网WiFi/蓝牙芯片厂商，BL602/BL702等支持RISC-V| https://www.bouffalolab.com/| -| BL602/702；面向智能家居、可穿戴、智能音箱等|
| 紫光国微           | 安全芯片/MCU；安全芯片与特种IC厂商，加入中国RISC-V联盟，布局RISC-V MCU| https://www.ungroup.com/| -| 汽车电子/车规、金融安全、工业控制|

### （3）开发板/整机制造厂商

| 厂商| 简介| 典型产品      | 官网/社区| 备注/典型产品|
| --------- | ---------------- | ------------- | ----------- | -------------- |
| MilkV（群星闪耀） | RISC-V开发板厂商，推出MilkV Duo等| MilkV Duo| https://milkv.io/[https://community.milkv.io/](https://community.milkv.io/) ||
| StarFive赛昉科技  | RISC-V生态领导者，推出VisionFive开发板| VisionFive    | https://www.starfivetech.com/   https://rvspace.org/zh/home            | 昉·星光、昉·天枢，面向AI、边缘计算、教育开发 |
| Sipeed矽速科技  | 开发板与芯片厂商，Lichee Pi系列支持RISC-V| Lichee Pi系列 | https://sipeed.com/| 边缘AI/IoT|
| 进迭时空        | 高性能RISC-V芯片与整机制造商|| [https://www.spacemit.com/](https://www.spacemit.com/)| 高性能边缘计算、智能机器人|
| OrangePi       | 开源单板计算机厂商，部分型号支持RISC-V| Orange Pi RV  | https://www.orangepi.org/| Orange Pi RV，面向教育与开发者|
| BeagleBoard    | 国际知名开源硬件社区，推出BeagleV等RISC-V开发板 | BeagleV-Ahead | https://www.beagleboard.org/| BeagleV-Ahead，TI与SiFive合作|

### （4）软件平台及生态支持

| 厂商/组织          | 简介                                 | 官网                       | 备注/典型产品                    |
| ------------------ | ------------------------------------ | -------------------------- | -------------------------------- |
| 兆松科技           | 高性能RISC-V和AI基础架构软件平台     | https://www.terapines.com/ | 编译器、指令优化、AI软件栈       |
| 奕斯伟             | 芯片与方案、硅材料、生态链开发等板块 | https://www.eswin.com/     | RISC-V生态链开发、车载与工业芯片 |
| RIOS Lab           | 国际RISC-V开源实验室，推动生态建设   | https://www.rioslab.org/   | 开源IP、大学合作、开源社区       |
| Antmicro           | 嵌入式系统与RISC-V开源方案服务商     | https://antmicro.com/      | FPGA实现、系统定制、嵌入式软件   |
| 北京开源芯片研究院 |                                      | https://www.bosc.ac.cn/    | 万众一芯项目，2025大赛主办       |

---

## **二、国际RISC-V芯片及开发板厂商/企业**

| 公司| 简介| 官网| 备注/典型产品|
| ------------ | --------- | ----------- | ---------- |
| SiFive| RISC-V商业化先驱，推出U74、E系列等IP| https://www.sifive.com/| HiFive开发板、U74多核IP、面向边缘计算；P870核心，RVA23支持    |
| Microchip| FPGA与MCU厂商，支持RISC-V内核| [https://www.microchip.com/](https://www.microchip.com/) | PolarFire SoC、FPGA开发板|
| Tenstorrent| AI高性能RISC-V CPU| https://tenstorrent.com/| Ascalon RISC-V CPU，AI训练推理；Ascalon内核，SPEC INT领先Zen5 |
| NVIDIA| GPU厂商，部分GPU控制内核采用RISC-V| https://www.nvidia.com/| CUDA向RISC-V移植中|
| Qualcomm| 移动芯片龙头，布局RISC-V MCU与IoT芯片| https://www.qualcomm.com/| QCC74xM RISC-V模块|
| Intel            | 推出10亿美元RISC-V生态基金| https://www.intel.com/| 生态投资、FPGA加速|
| Mobileye         | 自动驾驶芯片厂商，加入RISC-V国际基金会| https://www.mobileye.com/| 车规RISC-V芯片布局|
| Ventana Micro    | 数据中心芯片let| https://www.ventanamicro.com/| Veyron V2 192核|
| Codasip          | RISC-V处理器IP与定制化工具链提供商| https://www.codasip.com/| 支持专用指令集扩展，面向AI、通信等领域|
| Ventana Micro    | 高性能RISC-V服务器芯片研发商| https://www.ventanamicro.com/| 面向云计算与数据中心，强调能效比|
| Esperanto        | 高能效RISC-V多核AI芯片公司| https://www.esperantotech.com/| 面向边缘AI与语音处理|
| Veedra           | RISC-V安全处理器与IP供应商| https://www.veedra.com/| 面向物联网与车规级安全应用|
| GreenWaves       | 超低功耗RISC-V AI芯片厂商| https://www.greenwaves-technologies.com/| GAP系列，面向音频与传感器融合处理|
| Akeana           | RISC-V IP供应商| -| Premier成员|
| Rivos            | 数据中心/AI服务器| https://www.rivosinc.com/| 2025融资加速|
| AheadComputing   | 前Intel团队，64位高性能CPU| -| 2025种子轮2150万美元，针对AI瓶颈|

---

## **三、全球RISC-V生态联盟与组织**

| 组织/联盟| 简介| 官网| 备注/特点|
| ----------- | ------------ | ----------- | --------------- |
| RISC-V International(RVI)          | 全球RISC-V标准制定与生态推广核心组织；全球标准制定，4500+成员 | https://riscv.org/| 中国12家Premier成员，RVA23 Profile已批准；|
| RIOS Lab                           | 国际RISC-V开源实验室，推动生态建设| https://www.rioslab.org/      | 开源IP、大学合作、开源社区|
| 中国开放指令生态(RISC-V)联盟(CRVA) | 国内RISC-V生态核心联盟，推动产学研结合| https://crva.ac.cn/sy         | 300+成员，包括阿里、华为、中科院等|
| 中国RISC-V产业联盟(CRVIC)          | 产业链上下游协同创新组织| http://www.crvic.org/sy       | 涵盖芯片设计、软件工具、整机应用等|
| RDI聚力联盟                        | 聚焦RISC-V数字基础设施生态创新| https://www.rdi-alliance.org/ | 联合成都、上海等地创新中心，推动产业落地|
| RISE项目（Linux基金会欧洲）        | 软件生态加速，20+成员| https://riseproject.dev/      | 2025与Yocto深度合作，Python/Golang优化|
| Quintauris                         | 高通/博世/英飞凌等合资，汽车/IoT| https://www.quintauris.com/   | 2025推出RT-Europa实时Profile，与Andes/Lauterbach合作 |
| DARE项目（欧洲EuroHPC）            | 2.4亿欧元HPC/AI RISC-V处理器开发| https://eurohpc-ju.europa.eu/ | 38家机构，2025启动|

---

## **四、开源项目与社区资源**

| 项目/社区| 简介| 资源地址| 备注/特点|
| ---- | --------- | -------------- | ----------- |
| 香山（Xiangshan） | 中科院计算所开源高性能RISC-V处理器核 | https://github.com/OpenXiangShan/XiangShan   | 支持多核，面向高性能计算；2025商业化预期，“南湖”14nm版本 |
| RISC-V Mini       | 极简RISC-V处理器实现，教学与入门利器 | https://github.com/ucb-bar/riscv-mini        | 200行Verilog代码，适合学习                                 |
| Ventus GPGPU      | 清华大学开源RISC-V Vector GPGPU项目  | https://github.com/THU-LAM-Ventus/Ventus     | 包含ISA、编译器、验证工具链                                |
| Rocket Chip       | Chisel构建的RISC-V SoC生成器         | https://github.com/chipsalliance/rocket-chip | 支持灵活定制，教学与科研常用                               |
| OpenHW Group      | 开源RISC-V IP核与验证平台            | https://www.openhwgroup.org/                 | CORE-V系列商用IP，面向商用与工业应用                       |

---

## **五、RISE RISC-V软件生态计划**

RISE（RISC-V Software Ecosystem）是由Linux基金会欧洲托管、RISC-V International支持的全球性软件生态加速计划，旨在推动RISC-V在移动、消费电子、数据中心、汽车等领域的软件成熟与商业化。

RISE创始董事会成员（2023年启动）

| 公司               | 简介/角色                | 官网                | 备注/特点                    |
| ------------------ | ---------------------- | ------------------- | ---------------------------- |
| 谷歌（Google）     | 推动Android对RISC-V的官方支持                  | https://www.google.com/       | AOSP已纳入RISC-V适配         |
| 英特尔（Intel）    | 推动RISC-V软件工具链和开源生态建设             | https://www.intel.com/        | 投资10亿美元RISC-V生态基金   |
| 平头哥（阿里）     | 中国大陆唯一董事会成员，推动玄铁系列RISC-V生态 | https://www.t-head.cn/        | 玄铁C906/C910/C930，全栈适配 |
| 三星（Samsung）    | 推动RISC-V在移动与消费电子领域的应用           | https://www.samsung.com/      | 多款芯片采用RISC-V架构       |
| 联发科（MediaTek） | 推动RISC-V在通信与IoT芯片的应用                | https://www.mediatek.com/     | 天玑系列探索RISC-V           |
| 英伟达（NVIDIA）   | GPU控制内核全面转向RISC-V，已量产30亿颗        | https://www.nvidia.com/       | NV-RISCV32/64/Vector系列     |
| 高通（Qualcomm）   | 布局RISC-V在移动与物联网芯片                   | https://www.qualcomm.com/     | QCC74xM RISC-V模块           |
| Andes Technology   | 高性能RISC-V IP厂商                            | https://www.andestech.com/    | AE350系列                    |
| Imagination        | GPU与AI加速器厂商，推动RISC-V生态              | https://www.imgtec.com/       | 支持RISC-V扩展               |
| Red Hat            | 推动Linux发行版对RISC-V的适配                  | https://www.redhat.com/       | Fedora、RHEL等支持RISC-V     |
| Rivos              | 高性能RISC-V服务器芯片与系统厂商               | https://www.rivosinc.com/     | 面向数据中心与AI             |
| SiFive             | RISC-V商业化先驱，提供IP核与开发板             | https://www.sifive.com/       | HiFive、U74多核IP            |
| Ventana Micro      | 高性能RISC-V服务器芯片研发商                   | https://www.ventanamicro.com/ | Veyron V2 192核服务器CPU     |

---

## **六、高校/科研机构（部分）**

| 机构/项目          | 简介                                                   | 官网/资源                    | 备注/特点                                     |
| ------------------ | ------------------------------------------------------ | ---------------------------- | --------------------------------------------- |
| 中科院计算所       | 开源高性能RISC-V处理器“香山”项目，推动学术与产业结合 | https://www.ict.ac.cn/       | “雁栖湖”“南湖”版本，分别基于28nm/14nm工艺 |
| 清华大学           | 开源GPGPU“乘影(Ventus)”项目，支持RISC-V Vector扩展   | https://www.tsinghua.edu.cn/ | 涵盖ISA、硬件架构、编译器、仿真器、验证工具等 |
| UC Berkeley        | RISC-V原创项目组，持续推动开源架构标准化               | https://www.berkeley.edu/    | 发起RISC-V ISA，开源“RISC-V Mini”教学处理器 |
| 电子科技大学       | RISC-V芯片设计、工具链开发，参与多项RISC-V生态建设     | https://www.uestc.edu.cn/    | 产学研合作，推动RISC-V教育与科研              |
| 上海交通大学       | 开展RISC-V架构研究，支持开源EDA工具链开发              | https://www.sjtu.edu.cn/     | 与企业合作，推动RISC-V在工业与AI场景应用      |
| 北京开源芯片研究院 | 万众一芯/大赛                                          | https://www.bosc.ac.cn/      |                                               |

---

## **七、生态合作伙伴（代表性企业）**

华为（鸿蒙R 2025中国峰会）、腾讯、比亚迪、中兴等深度适配。

| 企业   | 简介                                             | 官网                     | 备注/特点                        |
| ------ | ------------------------------------------------ | ------------------------ | -------------------------------- |
| 华为   | 鸿蒙系统深度适配RISC-V，参与RISC-V国际基金会     | https://www.huawei.com/  | 面向消费电子与工业控制           |
| 中兴   | 积极参与RISC-V生态建设，布局RISC-V芯片与通信设备 | https://www.zte.com.cn/  | 推动RISC-V在5G、物联网等领域应用 |
| 比亚迪 | 车规级RISC-V芯片应用，联合平头哥等推进智能座舱   | https://www.byd.com/     | 推动RISC-V在汽车电子领域落地     |
| 腾讯   | 云计算与AI领域探索RISC-V应用                     | https://www.tencent.com/ | 支持RISC-V在云服务器与AI推理场景 |

---

## **八、补充国际RISC-V生态组织与计划**

| 组织/计划       | 简介                                            | 官网                              | 备注/特点                            |
| --------------- | ----------------------------------------------- | --------------------------------- | ------------------------------------ |
| DARE（欧洲）    | EuroHPC联合体启动，开发多款数据中心级RISC-V芯片 | https://www.eurohpc-ju.europa.eu/ | 包括通用处理器、矢量加速器、AI处理器 |
| Quintauris      | 高通、博世、英飞凌、恩智浦、北欧半导体合资成立  | https://www.quintauris.com/       | 加速RISC-V在全球汽车与IoT领域商业化  |
| RISC-V 专利联盟 | 中国9大芯片巨头联合成立，推动专利互不诉讼生态   | https://www.crvaic.org/           | 包括芯原、平头哥、赛昉科技等         |
