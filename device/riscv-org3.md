## **一、国内RISC-V芯片及开发板厂商/企业（补充完善版）**

### （1）CPU核心/IP研发生产厂商

| 厂商 | 简介 | 官网 | 文档/社区 | 备注/扩展指令集/特点 |
|------|------|------|-----------|----------------------|
| **芯来科技** | 全系列RISC-V处理器IP及解决方案，低功耗到高性能 | https://www.nucleisys.com/ | https://docs.nucleisys.com/ | N/X/UX系列IP，自研NICE扩展指令集；RVA23虚拟化支持，符合RISC-V International认证 |
| **赛昉科技** | RISC-V处理器IP及整板解决方案提供商 | https://www.starfivetech.com/ | https://doc.rvspace.org/ | 昉·天枢Dubhe系列IP（Dubhe-90/80/70），同时提供VisionFive开发板 |
| **阿里巴巴平头哥** | 玄铁系列IP，AIoT/高性能计算 | https://www.xrvm.cn/ | https://openvela.io/ | 玄铁C906/C910/C920/C930，生态最成熟；RVV 1.0矢量扩展先驱 |
| **睿思芯科** | 高端RISC-V处理器IP与SoC方案，源自伯克利RISC-V原创团队 | https://www.terapines.com/ | - | 高性能服务器级IP，支持CHI互连协议；**据称**2025发布"灵羽"处理器 |
| **中科昊芯** | RISC-V DSP(数字信号处理器) | https://www.haocore.com/ | https://gitee.com/haocore | HX2000系列，CLA并行加速，工业/汽车级应用 |
| **奕斯伟（ESWIN）** | 芯片/方案/生态，车载工业 | https://www.eswin.com/ | - | EIC7700X AI芯片，支持RVV 1.0；**据称**2025年加入RISE联盟 |
| **进迭时空（SpacemiT）** | 高性能RISC-V芯片/IP | https://www.spacemit.com/ | https://github.com/spacemit-tech | VitalStone V100 64核服务器芯片，自研MUSE扩展，12nm工艺 |
| **匠芯创（ArtInChip）** | 工业控制SoC，多媒体AI | https://artinchip.com/ | https://gitee.com/artinchip | D21x/D13x系列，集成GPU与RISC-V，主攻工业HMI |
| **时擎科技** | 基于RISC-V的端侧AI处理引擎 | http://www.timesintelli.com/ | - | TimesFormer智能处理器，DSA架构，智能家居/安防 |
| **香山处理器** | 中科院计算所开源RISC-V处理器项目 | https://xiangshan-doc.cn/ | https://github.com/OpenXiangShan | 开源高性能乱序核，南湖/雁栖湖/昆明湖系列，中国芯粒生态核心 |
| **沁恒微电子** | MCU及USB/接口芯片厂商，RISC-V MCU | https://www.wch.cn/ | https://www.wch.cn/bbs/ | 青稞V4A/V4B内核，CH32V系列，USB特色；**据称**2025生态大会获奖 |
| **Andes Technology** | 台湾RISC-V IP厂商，高性能多核IP | https://www.andestech.com/ | https://www.andestech.com/en/support-download | AndesCore™ AX45MP/AX65，ISO 26262车规认证，与BrainChip合作AI加速 |
| **晶芯科技** | 台湾RISC-V CPU IP供应商，高性能可配置 | https://hzt.com.tw/ | - | 支持自定义指令扩展，AIoT/网络通信应用 |

---

### （2）物理芯片制造/量产厂商

| 厂商 | 简介 | 官网 | 文档/社区/售卖 | 备注/扩展指令集/特点 |
|------|------|------|----------------|----------------------|
| **全志科技** | 智能终端SoC，与平头哥深度合作 | https://www.allwinnertech.com/ | https://bbs.aw-ol.com/ | D1/D1s系列，支持RVV 0.7.1，AIoT/车载/工控 |
| **嘉楠科技** | 区块链及AI芯片，K230为Vector 1.0商用量产芯片 | https://canaan.io/ | https://developer.canaan-creative.com/ | K230/K230D，KPU神经网络加速器，边缘AI |
| **算能科技（Sophgo）** | AI芯片与服务器芯片 | https://www.sophgo.com/ | https://developer.sophgo.com/ | SG2042/SG2044 64核服务器芯片，支持2D/3D图形；**据称**SG2044支持Linux 6.16主线 |
| **兆易创新** | 国内MCU龙头，全球首款RISC-V 32位通用MCU | https://www.gigadevice.com/ | https://www.gigadevice.com.cn/support/ | GD32VF103系列，pin-to-pin兼容ARM，生态成熟 |
| **中科蓝讯** | 无线音频SoC，90%收入来自RISC-V | https://www.bluetrum.com/ | - | AB32VG1，BT889X系列，TWS耳机/音箱，高性价比 |
| **乐鑫科技** | Wi-Fi/Bluetooth MCU，全球市占率超30% | https://www.espressif.com/ | https://docs.espressif.com/ | ESP32-C3/C6/C5/H2，支持Zigbee/Thread/Matter，PSA-L2安全认证 |
| **瑞芯微** | 消费电子与AIoT芯片 | https://www.rock-chips.com/ | https://opensource.rock-chips.com/ | RV1103/RV1106，NPU加持，智能视觉/边缘AI |
| **泰凌微** | 低功耗无线物联网芯片，BLE多协议 | https://www.telink-semi.com/ | https://wiki.telink-semi.cn/ | TLSR9系列，支持Matter/Thread/BLE并行 |
| **博流智能** | 物联网WiFi/蓝牙芯片 | https://www.bouffalolab.com/ | https://github.com/bouffalolab | BL602/BL702/BL808，RISC-V+AI加速，智能家居/可穿戴 |
| **紫光国微** | 安全芯片/MCU，中国RISC-V联盟成员 | https://www.ungroup.com/ | - | 安全MCU，汽车电子/金融安全/工业控制 |
| **国民技术** | 安全芯片与通用MCU，N32系列RISC-V | https://www.nationz.com.cn/ | https://www.nationz.com.cn/support/ | N32系列，安全与低功耗，物联网/工业/家电 |
| **先楫半导体（HPMicro）** | 高性能RISC-V MCU，亚GHz主频 | https://www.hpmicro.com/ | https://hpmicro.com.cn/cn技术支持 | HPM6700/6400/5300/6300，主频达1GHz+，工业控制/新能源 |
| **航顺芯片** | MCU厂商，HK32系列RISC-V | http://www.hangshun-chip.com/ | - | HK32R系列，pin-to-pin兼容M3/M0，低成本替代 |
| **华米科技（Zepp）** | 智能可穿戴设备芯片 | https://www.zepp.com/ | - | 黄山1号/2号/3号，全球首款可穿戴RISC-V芯片 |
| **芯动科技（Innosilicon）** | 高端芯片设计，风华系列GPU+RISC-V | http://www.innosilicon.com.cn/ | - | 风华系列GPU整合RISC-V，图形与AI计算 |

---

### （3）开发板/整机制造厂商

| 厂商 | 简介 | 典型产品 | 官网/社区 | 备注/典型产品 |
|------|------|----------|-----------|---------------|
| **MilkV（群芯闪耀）** | RISC-V开发板新锐， milkv.io社区 | MilkV Duo/Duo S/ pioneer | https://milkv.io/ https://community.milkv.io/ | Duo系列基于Sophgo CV1800B，超低成本Linux板 |
| **赛昉科技（StarFive）** | RISC-V生态领导者，IP+开发板 | VisionFive 2 | https://www.starfivetech.com/ https://rvspace.org/ | JH7110/JH8100芯片，Debian/Ubuntu官方支持 |
| **矽速科技（Sipeed）** | 开发板与AI模组，MaixPy生态 | LicheePi 4A/Cluster | https://sipeed.com/ | 基于玄铁C906，支持AI加速与Cluster集群 |
| **进迭时空（Spacemit）** | 高性能RISC-V整机与开发板 | MUSE V1 Book | https://www.spacemit.com/ | VitalStone V100服务器芯片，笔记本电脑形态 |
| **香橙派（Orange Pi）** | 开源单板计算机 | Orange Pi RV | https://www.orangepi.org/ | 基于赛昉JH7110，支持Android/Linux桌面 |
| **BeagleBoard** | 国际开源硬件社区 | BeagleV-Ahead/Fire | https://www.beagleboard.org/ | 与赛昉/微五合作，BeagleBoard生态 |
| **瑞莎（radxa）** | 开源硬件，RK生态合作伙伴 | ROCK 5系列 | https://radxa.com/ https://forum.radxa.com/ | 基于瑞芯微RK3588，部分RISC-V合作项目 |
| **香蕉派（Banana Pi）** | 开源硬件社区 | BPI-F3 | http://www.banana-pi.org/ | 基于赛昉JH7110，双网口设计，软路由应用 |
