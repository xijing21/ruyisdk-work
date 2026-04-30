## Release Check
> 发版测试通过后，正式发版检查清单

### 仓库 release 发版：

- [X] https://github.com/ruyisdk/ruyi/releases   @xxxxen0n
  - [X] 正式版本版本号
  - [X] 安装包
  - [X] 必要的变更描述
- [X] https://github.com/ruyisdk/ruyisdk-vscode-extension/releases   @U2FsdGVkX1
  - [X] 正式版本版本号
  - [X] 安装包
  - [X] 必要的变更描述
- [X] https://github.com/ruyisdk/ruyisdk-eclipse-plugins/releases    @liukaijie
  - [X] 正式版本版本号
  - [X] 安装包
  - [X] 必要的变更描述（建议可以人为总结，精简突出主要的更新）

### news

- [ ] https://github.com/ruyisdk/packages-index/tree/main/news
  - [ ] ruyi    @xxxxen0n
  - [ ] ruyisdk-vscode-extension  @U2FsdGVkX1
  - [X] ruyisdk-eclipse-plugins   @liukaijie

### 文档：文档仓库更新文档（新功能/新特性）

> 对照changelog进行核对和逐个沟通确认

- [ ] https://github.com/ruyisdk/docs 
  - [ ] ruyi     @xxxxen0n
    - [ ] docs: 为什么要制作sysroot，怎么制作sysroot；在ruyisdk中如何使用sysroot  @qingwan12138
  - [ ] ruyisdk-vscode-extension  @U2FsdGVkX1
    - [ ] docs: 一键编译功能
  - [ ] ruyisdk-eclipse-plugins   @liukaijie
    - [ ] 待更新

### 安装包多平台发布

- [X] 发布到 mirror.iscas/ruyisdk  @xxxxen0n

  - [X] ruyi ： https://fast-mirror.isrc.ac.cn/ruyisdk/ruyi/
  - [X] ruyisdk-vscode-extension ：https://fast-mirror.isrc.ac.cn/ruyisdk/ide/plugins/vscode/  
  - [X] ruyisdk-eclipse-plugins ：https://fast-mirror.isrc.ac.cn/ruyisdk/ide/plugins/eclipse/
- [X] ruyi 发布到 pypi：https://pypi.org/project/ruyi/
- [X] VSCode 插件发布到 openVSX 和 visualstudio marketplace  @U2FsdGVkX1

  - [X] openVSX：https://open-vsx.org/extension/RuyiSDK/ruyisdk-vscode-extension
  - [X] visualstudio：https://marketplace.visualstudio.com/manage/publishers/RuyiSDK
- [X] Eclipse 插件发布到 Eclipse Marketplace  @liukaijie

  - [X] https://marketplace.eclipse.org/content/ruyisdk#metrics

## 宣发  @zhangyuxi
> ruyisdk.cn 和 IM 渠道、wechat-articles是默认一般会有的推送渠道

- [ ] 在 ruyisdk.cn 上宣发（参考https://github.com/ruyisdk/packages-index/tree/main/news 对应版本文档）；
- [ ] IM渠道推送
- [X] 在RuyiSDK双周进展汇报（ https://github.com/ruyisdk/wechat-articles） 发（可随双周进展的发布时间总结发版信息）：待下次双周报再随双周报时间同步
- [X] 根据S/A/B/C策略，分析内容，决策更多发布的途径和方式
  - [ ] sysroot制作和使用可以做个一个小系列教程推出，注意跟进
  - [ ] vscode 一键编译功能：至少可以在技术论坛上发个技术分享文章


---
## 总结
- 文档预计会滞后完善
- 注意文档完成后的推广跟进


---
其它备忘：
- 为本release checklist 制作一个 issue 模版，至于 ruyisdk 仓库；以后每次发版进行 check
- 目前的发布版本号采用的是ruyi的版本号，之前只有ruyi一个实体正常，现在是3个软件发版，需要梳理和调整
