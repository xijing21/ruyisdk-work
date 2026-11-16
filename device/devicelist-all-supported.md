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
3. **混合架构设备 IP Core 列写法**：统一采用 "SpacemiT X100 + A100" 两核并列写法。如需也可拆分为 "SpacemiT X100（CPU）+ SpacemiT A100（AI）"。

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
> 同一款芯片如果有多个“商品名”的，列一行（作为同一款芯片），如下面的“SpacemiT K1 / M1 / Ky X1 ” 。
> 行业里"一款芯片"的判定标准:
> **同一块硅片（die）+ 同一套外设集成 = 同一款芯片；型号名只是 SKU 标签。** 芯片行业的通行判定粒度是"硅片"（die）层面，而不是"商品名"层面——同一颗 die 通过**降频、屏蔽单元、换封装、换商品名**派生出多个 SKU 是行业通用做法（高通骁龙 860/870/888+、联发科天玑 1000/1000+ 都是同一颗芯片的不同频率档，而天玑 1000L 则是另一颗芯片）。
> 判断标准有三条：① 硅片面积/制程是否相同；② 集成的 CPU/GPU/ISP/外设 IP 是否完全一致；③ 是否仅通过频率/屏蔽/封装做差异化。

| id | SoC（Vendor Prefix + Full Model） |
|---|---|
| 1 | BOSC XiangShan Nanhu SoC |
| 2 | T-Head TH1520 |
| 3 | SOPHGO CV1800B / SG2000 / SG2002 |
| 4 | SOPHGO SG2042 |
| 5 | SOPHGO SG2044 |
| 6 | Canaan K230 |
| 7 | Canaan K510 |
| 8 | SpacemiT K1 / M1 / Ky X1 |
| 9 | StarFive JH7110 / JH7110S |
| 10 | Allwinner D1 |
| 11 | SiFive FU740 |
| 12 | ESWIN EIC7700X / EIC7702X |
| 13 | Zhihe A210 |
| 14 | SpacemiT K3 |

> 注：
> SOPHGO CV1800B / SG2000 / SG2002 三者在 RISC-V 核心数量、型号、频率上没有任何差异(C906@1GHz + C906@700MHz)。SG2000/SG2002 与 CV1800B 的区别在于额外集成了一颗 ARM Cortex-A53 核心，但这不影响 RISC-V 部分的等同性。因此，如果只关心 RISC-V 计算资源，这三款芯片可以合并为同一 RISC-V 平台。
> - A210 由 Zhihe（知合计算）推出，故 SOC 写作 "Zhihe A210"。
> - Milk-V Jupiter 同时兼容 SpacemiT K1 / M1 两款 SoC，此处分别列项；


## 三、开发板型号清单（Board List，统一为 品牌+型号+中文别名 三段式）
> 板卡、设备、整机产品型号，按照商品宣传和推广的型号来区分。
> 同构或者异构产品，只有当 CPU 主核心是 RISC-V 芯片的，才考虑纳入设备清单。

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
| 12 | Milk-V Jupiter | SpacemiT M1 | SpacemiT X60 | 2025 |
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
| 31 | Milk-V Jupiter2 | SpacemiT K3 | SpacemiT X100 + A100 | 2026(纳入2027报告) |
| 32 | SpacemiT K3 CoM260 Kit | SpacemiT K3 | SpacemiT X100 + A100 | 2026(纳入2027报告) |
| 33 | SpacemiT K3 Pico-ITX | SpacemiT K3 | SpacemiT X100 + A100 | 2026(纳入2027报告) |

**几点补充说明：**
- 条目 24（SOPHGO SG2044 EVB）的 IP Core 列可以修改为 "XuanTie C920"，也可以保留现在的XuanTie C920V2 ; IP Core list 中使用的是"XuanTie C920"，未作细分。
- 条目 25 / 30 的 IP Core 写成 “XuanTie C920 ×4 + XuanTie C908 ×4”，因为 Zhihe A210 是混合架构（4 大核 C920 + 4 小核 C908），单写一个型号会丢失信息；若追求极简，也可只写 "XuanTie C920 + C908"。
- 条目 27 的 Canaan K510 的自研 RISC-V 64 位双核 CPU，官方未给出独立核代号，统一写为 "Canaan Dual-core RISC-V 64-bit CPU"。或者改为 "—"（该 SoC 的 CPU 核型号官方未公开）。


