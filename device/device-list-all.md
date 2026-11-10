# 支持的设备清单

## 说明
### 统一命名规则/表达方式
企业/品牌全英文、IP 核用官方英文名、SOC 加企业前缀、开发板完整品牌+型号 

- **Vendor / Brand**：一律使用官方英文拼写（T-Head、SOPHGO、SpacemiT、StarFive、Canaan、ESWIN、SiFive、Allwinner、Sipeed、ISCAS、Milk-V、Banana Pi、Orange Pi、AWOL）。
- **IP Core**：`官方英文核名 + 型号`，如 `XuanTie C910`、`SiFive U74`、`XiangShan Nanhu`、`SpacemiT X60`。
- **SoC**：`Vendor 前缀 + 完整型号`，如 `SOPHGO SG2042`、`SpacemiT K1`、`SiFive FU740-C000`、`Sipeed Zhihe A210`。
- **Board**：`Brand + Model（+ 中文别名）`，社区品牌（Milk-V / Sipeed Lichee / Banana Pi / Orange Pi）保留英文原名；国内笔记本/整机类（Ruyi 系列、MUSE 系列、Nezha D1）采用"英文品牌型号 + 中文别名"三段式。


### 后续同类情况的判断原则
为方便后续维护，给出两条可复用的判据：
1. **是否单列 IP Core**：看它是否构成独立授权型号、是否有独立的微架构/流水线（如 C920 与 C920V2 只是工艺/频率 tune，GCC 中是同一个 `-mcpu=c920` 加不同 tune 参数），是则单列，否则并入。
2. **是否列入 IP Core 清单**：只有当厂商给出官方核型号时才列入（如 XuanTie C910、SiFive U74）；若 SoC 集成的核连官方型号都没有公开，宁可留 "—" 也不臆造名称。Canaan K510 官方产品页只描述为 "dual-core RISC-V architecture CPU"，没有型号，属于这种情况。
3. **混合架构设备 IP Core 列写法**：统一采用 "SpacemiT X100 + A100" 两核并列写法，与 RuyiSDK 官方矩阵口径一致；如需也可拆分为 "SpacemiT X100（CPU）+ SpacemiT A100（AI）"。

## 一、IP 核型号清单（IP Core List）

| id | IP Core（Official English Name + Model） | Vendor |
|---|---|---|
| 1 | XiangShan Nanhu | BOSC / ICT CAS |
| 2 | XuanTie C906 | T-Head / Alibaba |
| 3 | XuanTie C908 | T-Head / Alibaba |
| 4 | XuanTie C910 | T-Head / Alibaba |
| 5 | XuanTie C920 | T-Head / Alibaba |
| 6 | SpacemiT X60 | SpacemiT |
| 7 | SiFive U74 | SiFive |
| 8 | SiFive P550 | SiFive |
| 9 | SpacemiT X100 | SpacemiT |

> 注：
> - Canaan K510 的自研 RISC-V 64 位双核 CPU，官方未给出独立核代号，未收录到该表。
> - XuanTie C920 含 C920V2（SOPHGO SG2044 SoC IP Core） ，XuanTie C920V2 不单独列，并入 C920 条目（gcc/GCC 社区也是把 C920v1/v2 当作同一 IP 的两个 tune 变体处理）。
> - K3 是"同构融合计算"架构，集成 8×X100 高性能计算大核（四发射乱序、RVA23、RVV 1.0、最高 2.4 GHz）+ 8×A100 超宽并行 AI 核（1024-bit RVV 1.0，60 TOPS），二者均为进迭时空自研 RISC-V 核，考虑到目前 RuyiSDK 只验证了 X100 ，暂时只列 X100 一项。另有双核 RT24 实时核，属于附属实时子系统，一般不在主 CPU Core 列表中单列，如需可另行补充。


## 二、SOC / 芯片型号清单（SoC List）

| id | SoC（Vendor Prefix + Full Model） |
|---|---|
| 1 | BOSC XiangShan Nanhu SoC |
| 2 | T-Head TH1520 |
| 3 | SOPHGO CV1800B |
| 4 | SOPHGO SG2002 |
| 5 | SOPHGO SG2000 |
| 6 | SOPHGO SG2042 |
| 7 | SOPHGO SG2044 |
| 8 | Canaan K230 |
| 9 | Canaan K510 |
| 10 | SpacemiT K1 |
| 11 | SpacemiT M1 |
| 12 | SpacemiT Ky X1 |
| 13 | StarFive JH7110 |
| 14 | StarFive JH7110S |
| 15 | Allwinner D1 |
| 16 | SiFive FU740-C000 |
| 17 | ESWIN EIC7700X |
| 18 | ESWIN EIC7702X |
| 19 | Zhihe A210 |
| 20 | SpacemiT K3 |

> 注：
> - A210 由 Zhihe（知合计算）推出，故 SOC 写作 "Zhihe A210"。
> - Milk-V Jupiter 同时兼容 SpacemiT K1 / M1 两款 SoC，此处分别列项；


## 三、开发板型号清单（Board List，统一为 品牌+型号+中文别名 三段式）

| id | Board（Brand + Model + 中文别名） | SoC | IP Core | Support Date |
|---|---|---|---|---|
| 1 | RuyiBook（如意香山本） | BOSC XiangShan Nanhu SoC | XiangShan Nanhu | 2025 |
| 2 | Sipeed Lichee Pi 4A | T-Head TH1520 | XuanTie C910 | 2025 |
| 3 | Milk-V Meles | T-Head TH1520 | XuanTie C910 | 2025 |
| 4 | Milk-V Duo | SOPHGO CV1800B | XuanTie C906 | 2025 |
| 5 | Milk-V Duo 256M | SOPHGO SG2002 | XuanTie C906 | 2025 |
| 6 | Milk-V Duo S | SOPHGO SG2000 | XuanTie C906 | 2025 |
| 7 | Sipeed LicheeRV Nano | SOPHGO SG2002 | XuanTie C906 | 2025 |
| 8 | Milk-V Pioneer | SOPHGO SG2042 | XuanTie C920 | 2025 |
| 9 | Canaan CanMV K230 | Canaan K230 | XuanTie C908 | 2025 |
| 10 | Sipeed Lichee Pi 3A | SpacemiT K1 | SpacemiT X60 | 2025 |
| 11 | Banana Pi BPI-F3 | SpacemiT K1 | SpacemiT X60 | 2025 |
| 12 | Milk-V Jupiter | SpacemiT K1 / M1 | SpacemiT X60 | 2025 |
| 13 | SpacemiT MUSE Book（MUSE 笔记本） | SpacemiT M1 | SpacemiT X60 | 2025 |
| 14 | SpacemiT MUSE Box（MUSE 主机） | SpacemiT M1 | SpacemiT X60 | 2025 |
| 15 | SpacemiT MUSE Pi Pro（MUSE Pi Pro 单板机） | SpacemiT M1 | SpacemiT X60 | 2025 |
| 16 | Orange Pi RV2 | SpacemiT Ky X1 | SpacemiT X60 | 2025 |
| 17 | StarFive VisionFive 2 | StarFive JH7110 | SiFive U74 | 2025 |
| 18 | Milk-V Mars | StarFive JH7110 | SiFive U74 | 2025 |
| 19 | AWOL Nezha D1（哪吒 D1） | Allwinner D1 | XuanTie C906 | 2025 |
| 20 | SiFive HiFive Unmatched | SiFive FU740 | SiFive U74 | 2025 |
| 21 | ESWIN EBC7700 | ESWIN EIC7700X | SiFive P550 | 2026 |
| 22 | SiFive HiFive Premier P550 | ESWIN EIC7700X | SiFive P550 | 2026 |
| 23 | ESWIN EBC7702 | ESWIN EIC7702X | SiFive P550 | 2026 |
| 24 | SOPHGO SG2044 EVB | SOPHGO SG2044 | XuanTie C920V2 | 2026 |
| 25 | Sipeed A210 SODIMM V2 | Zhihe A210 | XuanTie C920 ×4 + XuanTie C908 ×4 | 2026 |
| 26 | StarFive VisionFive 2 Lite | StarFive JH7110S | SiFive U74 | 2026 |
| 27 | Canaan K510 CRB-V1.2 KIT | Canaan K510 | Canaan Dual-core RISC-V 64-bit CPU | 2026 |
| 28 | Milk-V Megrez | ESWIN EIC7700X | SiFive P550 | 2026 |
| 29 | Ruyi RISC-V Book（如意笔记本） | T-Head TH1520 | XuanTie C910 | 2026 |
| 30 | Ruyi RISC-V Book 2（如意二代笔记本） | Zhihe A210 | XuanTie C920 ×4 + XuanTie C908 ×4 | 2026 |
| 31 | Milk-V Jupiter2 | SpacemiT K3 | SpacemiT X100 + A100 | 2026 |
| 32 | SpacemiT K3 CoM260 Kit | SpacemiT K3 | SpacemiT X100 + A100 | 2026 |
| 33 | SpacemiT K3 Pico-ITX | SpacemiT K3 | SpacemiT X100 + A100 | 2026 |

**几点补充说明：**
- 条目 24（SOPHGO SG2044 EVB）的 IP Core 列可以修改为 "XuanTie C920"，也可以保留现在的XuanTie C920V2 ; IP Core list 中使用的是"XuanTie C920"，未作细分。
- 条目 25 / 30 的 IP Core 写成 “XuanTie C920 ×4 + XuanTie C908 ×4”，因为 Zhihe A210 是混合架构（4 大核 C920 + 4 小核 C908），单写一个型号会丢失信息；若追求极简，也可只写 "XuanTie C920 + C908"。
- 条目 27 的 Canaan K510 的自研 RISC-V 64 位双核 CPU，官方未给出独立核代号，统一写为 "Canaan Dual-core RISC-V 64-bit CPU"。或者改为 "—"（该 SoC 的 CPU 核型号官方未公开）。


---


# 面向 2027 年规划的 RISC-V SoC / 开发板预期清单
综合 2026 年 RISC-V 中国峰会（10 月 19–20 日）、Hot Chips 2026 以及各家官方规格书与媒体披露的信息，符合你两条筛选条件（①2027 年 6 月前明确上市；②2026 年已发布 SoC 但尚无对应消费级开发板）的项目集中在三类：**服务器级 CPU、香山昆明湖 V3 衍生 SoC、车规与 AI 推理芯片**。下面按置信度分档列出，便于你做计划排期。

## 一、高置信度（官方已宣布明确时间表，可放心列入 2027 H1 计划）

### A. SoC / CPU 芯片
| SoC / CPU | 厂商 | IP Core | 关键规格 | 发布状态 | 2027 H1 上市预期 |
|---|---|---|---|---|---|
| **SpacemiT V100**（Vital Stone） | 进迭时空 + 开芯院 | 6× XiangShan Kunminghu V2R2 + 40× SpacemiT X100 | 46 核混合架构，最高 2.4 GHz，8×DDR5-4800，52×PCIe 5.0，RVA23 完整合规 | **2026-10-19 正式发布**，配套三类服务器整机（C2201/G5201/S5236）同步亮相 | 整机已实物演示，2027 H1 进入批量交付与开发者样机阶段 |
| **T-Head XuanTie C950** | 阿里达摩院 / 平头哥 | XuanTie C950（5 nm，3.2 GHz） | 单核 SPECint2006 > 70 分，集成 TPE 矩阵引擎，原生支持 Qwen3/DeepSeek V3 推理 | **2026-03-24 发布** | 玄铁官方已预告"**明年将会有基于最新玄铁 950 的服务器终端产品亮相**"，即 2027 年内 |
| **SiFive BigSky SF-2U870** | SiFive | 32× SiFive P870-D（TSMC N6，2.0 GHz） | 2U 机架式服务器，256 GB DDR5-5600，4×PCIe Gen5 x16，Ubuntu 26.04 LTS + RHEL 10 开箱支持 | **2026-08-24 Hot Chips 发布并限量部署** | 2027 H1 进入规模发售，配套 CUDA-on-RISC-V 移植推进 |
| **T-Head 真武 V900**（训推一体 AI 芯片，含 RISC-V 控制平面） | 阿里平头哥 | 玄铁系列（控制核） | 数据中心级 AI 训推一体 | 官网已预告"**2027 年第一季度上市**" | 时间点完全落在 2027 Q1 |

### B. 开发板 / 整机形态
| 开发板 / 整机 | SoC | IP Core | 形态 | 2027 H1 上市预期 |
|---|---|---|---|---|
| **SpacemiT C2201 / G5201 / S5236** 三类服务器整机 | SpacemiT V100 | XiangShan Kunminghu V2R2 + SpacemiT X100 | 2U/4U 服务器 + 参考主板 + BMC | 已发布并实机演示，2027 H1 转入量产交付 |
| **SiFive BigSky SF-2U870 开发平台** | SiFive BigSky | SiFive P870-D | 2U 机架服务器 | 已限量部署，2027 H1 公开发售 |
| **玄铁 C950 服务器终端产品**（合作伙伴整机） | XuanTie C950-based SoC | XuanTie C950 | 服务器 | 玄铁官方口径为 2027 年内亮相 |

## 二、中等置信度（官方有路线图，但具体月份需关注后续披露）
| 项目 | 厂商 | IP Core | 状态 | 2027 H1 预期 |
|---|---|---|---|---|
| **XiangShan Kunminghu V3 SoC** | 开芯院 + 合作 SoC 厂商 | XiangShan Kunminghu V3（SPECint2006 22.6/GHz） | 第三代昆明湖 V3 已成为香山默认分支，2025 年 10/11 月已有两家企业完成 SoC 流片，**2026 Q1 回片** | 2027 H1 可能出现基于昆明湖 V3 的开源/合作 SoC 开发板（与开芯院 SMT 工作组生态推进相关） |
| **T-Head XuanTie C925 / C930 车规版（C925A / C930A）** | 阿里达摩院 | XuanTie C925A / C930A | 2026 RISC-V 峰会公布的自动驾驶路线图中，C950A 之前会先落地这两款 | 路线图覆盖 2026–2027，具体量产月份未披露 |
| **Nano-core（北京大学系 RISC-V 近存算一体芯片）** | Nano-core Chip | 自研 RISC-V 近存计算核 | 已完成 3 款芯片流片，官方称"**客户送样与首批量产 2027 年初**" | 2027 Q1/Q2 有望出样，开发板概率较低，多为整机/卡形态 |
| **珠峰 200**（砺睿微，中兴微子公司） | Lirui Wei（中兴微） | 自研 RISC-V 数据中心 CPU | 首次对外露出，完整规格**2026 年底前披露** | 2027 H1 可能出工程样机，开发板未明确 |

## 三、低置信度 / 谨慎列入（不建议放进 2027 H1 主计划）
| 项目 | 厂商 | 状态 | 风险 |
|---|---|---|---|
| **T-Head XuanTie C950A**（车规自动驾驶） | 阿里达摩院 | 官方时间表为 **2027 年底**推出 | 已明确不在 2027 H1 |
| **Milk-V Oasis**（JH8100） | Milk-V / StarFive | 多次跳票，2026 年仍未见明确量产信息 | 历史交付记录不佳，规划时不应作为硬依赖 |
| **Sophgo SG2380 / 其他厂商下一代消费级 SoC** | SOPHGO 等 | 无 2027 H1 上市的官方确认 | 信息不足 |

## 四、对 2027 规划的几点建议
1. **服务器方向是 2027 年主战场**：V100、C950、BigSky SF-2U870 三条产品线都在 2026 Q3–Q4 集中亮相，2027 H1 将进入批量交付与开发者可采购阶段，这是过去 RISC-V 生态从未有过的密度。
2. **RVA23 与 Server Platform 规范统一了软件基线**：V100 与 BigSky 都覆盖 RVA23 + Server SoC + BRS + Security Model 全套规范，Ubuntu 26.04 LTS 与 RHEL 10 已原生支持，意味着 2027 年的移植工作可以"一次搞定、多平台复用"，不必再为每颗芯片单独定制 OS。
3. **车规芯片（C950A、E908A）建议放到 2027 H2 甚至 2028 规划**，与你当前生态支持清单以开发板/主机为主的方向错位。
4. **优先级建议**：高置信度三件套（V100 整机、C950 服务器产品、BigSky 平台）可在 2027 Q1 完成采购排期；昆明湖 V3 衍生 SoC 建议以"持续跟踪 + 预留支持位"的方式处理；中等置信度的几项每季度复核一次。


