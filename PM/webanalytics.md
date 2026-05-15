
### RuyiSDK 开发板应用示例
- 文档仓库：https://github.com/ruyisdk/board-docs
- 网站：https://board-docs-frontend.pages.dev/
> 目前前端采用 Astro 静态站方案，文档数据来自 board-docs 仓库中的 Markdown 文件，构建时自动扫描生成页面；
> 目前网站已经通过 Cloudflare 部署，应该是可以直接使用 Cloudflare Analytics 查看访问量,具体还需要研究下。


目前正在将开发板示例[集成](https://github.com/ruyisdk/ruyisdk-website/issues/442)到官网，官网会在首页开辟一个小区域展示最热门的几个开发板，提供“查看所有开发板”跳转到当前的网站。
而且我们的另一个工具vscode插件中，采用了利用webview嵌入开发板示例文档+结合copilot AI插件将开发板文档示例中的知识学习后，可直接帮助用户生成操作指令等智能辅助。

为了更好的衡量和观察直接来自web网站和 vscode插件集成页面中用户访问文档进行开发的统计参数（有没有人在用，增长趋势等），想要在官网首页曝光和推流之前，建立统计数据的观察和统计机制。

1. 关于隐私和合规边界：
*   我们是否允许采集用户 IP？   不允许
*   Web 端是否必须上 Cookie 同意弹窗？  不建议
 
2. 基础设施与运维能力（决定自建还是 SaaS）
*   我们有没有现成的服务器/数据库资源来部署统计服务？   优先考虑免费的SaaS方案，其次免费开源软件自己在服务器上部署；
*   现有的 VSCode 插件是否已经有任何遥测机制？      没有，vscode插件目前不计划做遥测，而是希望通过嵌入的 web 网站的访问量来进行统计。

3. 业务闭环的衡量（决定埋点的深度）
*   当看到“某个开发板文档访问量高”后，我们要做什么？  将这个开发板纳入到官网首页的开发板曝光板块；并优化文档。
*   VSCode 中“Copilot 辅助操作”的成功率，我们需要关注吗？   暂时不关注

按「要什么指标 → 用什么工具 → 怎么埋点 → 怎么分析」给一个可落地方案。

> 附件的，ruyisdk官网 ruyisdk.org （仓库：https://github.com/ruyisdk/ruyisdk-website ） 也还没有建立网页的统计观测。可以综合一起考虑下

---

## 一、要什么指标

1. **规模指标**
   - 日/周/月活跃用户（DAU/WAU/MAU）
   - 页面访问量（PV）、访客数（UV）
   - （可选）VSCode 插件日活用户、webview 打开次数

2. **结构指标**
   - 按开发板型号的访问占比（哪块板最热门）
   - 按来源的占比：官网首页入口、直接访问、搜索引擎、VSCode 内链接等

3. **行为/转化指标（后续可加）**
   - 从“查看文档”到“执行示例/创建工程”的转化
   - 文档内“复制命令”“一键烧录”等按钮点击
   - 用户使用 Copilot 批量操作时，对应文档的访问情况


---



基于你的约束条件（**不采IP、不上Cookie弹窗、优先免费SaaS、VSCode不遥测**），推荐采用 **Umami Cloud（免费 Hobby 层）+ Cloudflare Web Analytics（辅助）** 的组合方案。两者均为无 Cookie、不存储原始 IP 的隐私优先设计，且 Umami 支持自定义事件，恰好满足“按开发板型号”和“按来源”的结构化分析需求。

---

## 一、要什么指标

| 维度 | 指标 | 用途 |
|------|------|------|
| **规模** | PV、UV、DAU/WAU/MAU | 观察整体流量趋势，判断官网首页曝光是否带来增长 |
| **结构** | 开发板型号访问占比、Top 10 热门文档 | **指导首页曝光板块选品**；识别冷门板需优化文档 |
| **来源** | 官网首页、VSCode 插件、直接访问、搜索引擎 | 衡量各渠道贡献，验证 VSCode 集成价值 |
| **行为（后续迭代）** | “复制命令”“一键烧录”按钮点击次数 | 评估文档转化效率，而不仅是“看了就走” |

---

## 二、用什么工具

### 主分析工具：Umami（推荐 Cloud Hobby 免费层）

- **隐私合规**：MIT 开源，默认使用**日盐哈希**（Daily Salted Hash）生成匿名访客 ID，**不存储原始 IP**，无需 Cookie，**无需同意弹窗**即可合规运行。
- **免费层级**：Umami Cloud 提供 **Hobby 永久免费层，每月 10 万 events**，对文档站初期完全够用；若后续超量，可无缝迁移至自托管（Docker 一键部署）。
- **自定义能力**：支持自定义事件与属性，可完美实现“开发板型号”“来源渠道”等维度下钻。
- **API 支持**：可导出 JSON 数据，便于后续用脚本做二次分析或生成周报。

### 辅助工具：Cloudflare Web Analytics（已具备）

- 你的站点已部署在 Cloudflare Pages，**直接开启即可**，零成本、零代码。
- 提供基础 PV/UV、访问地区分布（粗粒度）、Core Web Vitals 性能数据。
- 作为 Umami 的交叉验证（例如对比搜索引擎爬虫与真实流量的差异）。

### 不推荐的工具

| 工具 | 原因 |
|------|------|
| **Google Analytics 4** | 默认使用 Cookie 和持久标识符，在中国及欧盟语境下通常**需要 Cookie 同意弹窗**，与你的约束冲突。 |
| **Plausible Cloud** | 隐私友好，但 SaaS 无永久免费层（仅 30 天试用），不符合“优先免费 SaaS”。 |
| **自部署 Matomo** | 功能过重，需配置 Cookieless 模式，运维成本高，违背“优先 SaaS”原则。 |

---

## 三、怎么埋点

### 1. 基础脚本安装（Astro 全局 Layout）

在 Astro 项目的全局 `Layout.astro` 或 `BaseHead.astro` 中，加入 Umami 跟踪脚本：

```html
<!-- Umami 跟踪脚本 -->
<script
  defer
  src="https://cloud.umami.is/script.js"
  data-website-id="YOUR_WEBSITE_ID"
  data-domains="board-docs-frontend.pages.dev"
></script>
```

- `defer` 保证不阻塞 Astro 静态页渲染。
- 若后续切到自托管，只需换 `src` 地址即可。

### 2. 开发板页面自动上报（结构指标）

Astro 的开发板文档页面通常是基于 Markdown/MDX + 动态路由（如 `/boards/[slug].astro`）。在该页面模板加载完成后，上报自定义事件：

```javascript
// 在开发板详情页的前端脚本中
if (window.umami) {
  window.umami.track('board_view', {
    board_name: 'lichee-pi-4a',      // 从 Astro props 或 frontmatter 注入
    category: 'allwinner',            // 可选：厂商/架构分类
    source: new URLSearchParams(location.search).get('ref') || 'direct'
  });
}
```

**效果**：Umami 后台可直接按 `board_name` 维度筛选，看哪块板访问量最高。

### 3. 来源标记策略（区分官网 vs VSCode）

不依赖 HTTP Referrer（不可靠），采用**显式 URL 参数标记**：

| 入口 | 跳转链接示例 |
|------|-------------|
| **RuyiSDK 官网首页** | `https://board-docs-frontend.pages.dev/?ref=ruyi-homepage` |
| **VSCode 插件 webview** | `https://board-docs-frontend.pages.dev/boards/xxx?ref=vscode-plugin` |
| **GitHub 仓库链接** | `https://board-docs-frontend.pages.dev/?ref=github-repo` |
| **直接访问/搜索引擎** | 无参数，记为 `direct`/`organic` |

在页面脚本中统一读取 `?ref=` 并写入事件属性，确保来源归因 100% 准确。

### 4. VSCode 插件集成（无遥测，纯 Web 统计）

VSCode 插件通过 webview 嵌入文档站时，**不要**在插件侧打任何遥测点。仅在加载的 URL 上带参数：

```typescript
// VSCode 插件侧
const panel = vscode.window.createWebviewPanel(
  'boardDocs', '开发板文档', column, { enableScripts: true }
);
// 直接 iframe 加载文档站，带上 source 标记
panel.webview.html = `
  <iframe 
    src="https://board-docs-frontend.pages.dev/boards/${boardId}?ref=vscode-plugin" 
    width="100%" height="100%" frameborder="0">
  </iframe>
`;
```

- 文档站内的 Umami 脚本在 webview 中正常执行，请求发往 Umami 服务器。
- 由于 Umami 不采 IP、不设 Cookie，即使在 VSCode 受限 webview 环境中也能正常工作，**无需处理跨域或 CSP 弹窗**。

### 5. 行为埋点（后续迭代预留）

在文档内的交互按钮上埋点：

```html
<button 
  onclick="window.umami && window.umami.track('cta_click', { 
    action: 'copy_flash_cmd', 
    board_name: 'lichee-pi-4a' 
  }); copyToClipboard()"
>
  复制烧录命令
</button>
```

---

## 四、怎么分析（闭环机制）

### 1. Dashboard 日常看板（Umami 网页端）

| 视图 | 操作 | 决策输出 |
|------|------|----------|
| **实时/近 7 日流量** | 观察 DAU/WAU 曲线 | 判断官网首页上线后是否有明显跳升 |
| **Top Pages** | 筛选 `/boards/*` 路径 | 识别最热门的 5-10 个开发板型号 |
| **Events → board_view** | 按 `board_name` 分组排序 | **直接生成“首页曝光板块”选品清单** |
| **Events → 按 source 过滤** | 对比 `ruyi-homepage` vs `vscode-plugin` | 评估两渠道贡献比，指导运营资源分配 |

### 2. 每周数据 Review 流程（建议周五下午）

1. **导出数据**：通过 Umami API 拉取上周 Events 数据。
   ```bash
   curl -H "Authorization: Bearer TOKEN" \
     "https://api.umami.is/v1/websites/ID/events?startAt=...&endAt=..."
   ```
2. **生成简报**：用 Python/Pandas 做透视表：
   - 开发板型号 × PV/UV 矩阵
   - 来源占比饼图
   - 周环比增长率
3. **决策会议**：根据 Top 10 开发板，更新官网首页的“热门开发板”模块；对访问量低但战略重要的板，安排文档优化。

### 3. 与首页曝光联动机制

```text
数据观察 → 决策 → 行动
    ↓
Umami 显示 "lichee-pi-4a" 周 PV 占 35%
    ↓
决策：将其放入官网首页第一屏 "热门开发板"
    ↓
行动：官网更新后，继续观察该板流量是否进一步放大（验证入口有效性）
```

### 4. 数据导出与二次分析（可选）

若 Umami Cloud 的 100k events/月不够用，或需要更复杂的漏斗分析：

- **方案 A**：自托管 Umami（Docker + PostgreSQL，成本约 $5/月 VPS）。
- **方案 B**：通过 Umami API 每日同步到本地/免费的 BI 工具（如 Metabase 或 Grafana），做长期趋势库。

---

## 五、分阶段实施路线图

| 阶段 | 时间 | 任务 | 产出 |
|------|------|------|------|
| **Phase 1** | 1-2 天 | 接入 Umami Cloud Hobby，在 Astro Layout 放全局脚本；开发板页面加 `board_view` 事件 | 基础 PV/UV 和开发板维度可见 |
| **Phase 2** | 2-3 天 | 官网首页、VSCode 插件、GitHub 等入口统一加 `?ref=` 参数；页面脚本读取并上报 | 来源结构指标清晰 |
| **Phase 3** | 持续 | 建立每周五数据 Review 机制；根据 Top 开发板调整首页曝光 | 数据驱动运营闭环 |
| **Phase 4** | 后续迭代 | 加行为埋点（复制命令、一键烧录）；评估文档转化漏斗 | 从“看文档”延伸到“用文档” |

---

## 六、隐私与合规自检清单

- [x] **不采集 IP**：Umami 默认使用日盐哈希，原始 IP 不落地存储。
- [x] **无 Cookie**：无需弹窗，不违反《个人信息保护法》及 GDPR 的同意要求。
- [x] **无指纹追踪**：Umami 不收集 User-Agent 以外的设备指纹，不用于跨站追踪。
- [x] **隐私政策声明**：建议在 RuyiSDK 官网和文档站页脚加一句简短说明：“本站使用匿名统计工具分析访问趋势，不收集个人身份信息。”
- [x] **VSCode 零遥测**：所有统计发生在 webview 加载的网页侧，插件本体不上报任何数据。

---

**总结**：以 **Umami Cloud 免费层** 为核心，配合已有的 **Cloudflare Web Analytics**，通过 URL `ref` 参数区分来源，通过自定义事件绑定开发板型号，即可在**零 Cookie 弹窗、不采 IP、零服务器运维**的前提下，建立起从“访问统计”到“首页曝光决策”的完整数据闭环。
