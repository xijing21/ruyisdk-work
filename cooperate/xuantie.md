## 与 xuantie 合作
## 历史合作情况
1. RevyOS：https://github.com/revyos/revyos/blob/master/README.cn.md 

RevyOS是由RuyiSDK团队的RevyOS小队支持开发的一款针对XuanTie芯片生态的Debian优化定制发行版。
RevyOS 围绕玄铁C906、C910、C920、C908等芯片提供了完整而全面的适配和优化支持，默认集成支持玄铁扩展指令集和RVV 1.0的GCC工具链，并搭载使用RVV 1.0指令集优化过的Glibc和Kernel。
目前，RevyOS 在办公、网页浏览、观看视频等方面已经能满足用户的基本使用需求。
基于上述定制和优化的 RevyOS，在 Lichee RV，Lichee Pi 4A 等硬件平台上，能够提供优秀的性能和极佳的体验。

但是：目前 RevyOS 因为组织架构调整的原因已经停止维护了，原来的团队人员聚焦发展 openRuyi 发行版（openRuyi 是 rpm发行版），这个导致原来的RevyOS的合作难以继续了。

2. 编译器：对xuantie自定义扩展的支持与适配，协助提交到gcc上游社区
目前据了解，gcc 上游也都合入了 xtheadvector xuantie自定义扩展的合入，并且ruyisdk的gcc与玄铁厂商的gcc在针对这方面的支持方面没有不同，同时上游也是如此。
如果按照这个状态，xuantie gcc 不一定有合作的需求了（没有特别了解，但是RVI发布RV20/22/23后，芯片厂商基本上也统一到相关的规范上了）

这部分我不了解各家 gcc 的差异，可以帮我调研并探需这方面的合作机会

3. 基于RuyiSDK包管理器的资源集成：将 xuantie 的开发者资源接入到包管理器中。参考接入标准：https://ruyisdk.org/docs/Other/partner-guide

4. 集成开发环境：玄铁有自己的集成开发环境“集成开发工具剑池CDK”，初步预计合作意愿可能不强列。但是不排除多个工具支持玄铁芯片的渠道，毕竟他们做软件是为了支持硬件，最终是为了多买芯片/开发板等硬件，这是他们的核心利润。

5. 课程合作：之前已经基于玄铁学院开展了一些合作，详见：https://www.xrvm.cn/community/risc_v



