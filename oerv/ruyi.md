# ruyi包管理器在openeuler中的集成情况

## 路线
- [ ] 1. ruyi软件包引入openeuler软件包社区：https://atomgit.com/src-openeuler
- [ ] 2. ruyi可以在构建系统中完成构建（所需要的依赖包都满足）   
- [ ] 3. ruyi进入openEuler for RISC-V 官方的系统镜像源，可以直接通过yum install ruyi 安装
- [ ] 4. ruyi进入openEuler for RISC-V 镜像的系统预装软件
- [ ] 5. ruyi在openEuler 中的持续更新与维护（随着ruyi版本的升级，openEuler社区中ruyi包版本的同步升级）

## 依赖分析
### ruyi & openEuler 24.03 LTS-SP3
https://github.com/ruyisdk/ruyi/blob/main/pyproject.toml
<img width="520" height="670" alt="image" src="https://github.com/user-attachments/assets/6675c551-7d26-47da-96b6-c0a746124a08" />

<img width="1528" height="790" alt="image" src="https://github.com/user-attachments/assets/1d0c220d-c04a-46fd-b289-a14770432e1b" />

依赖配置分析结论：openEuler 需要引入 pygit2 =1.6 包；

## 现状
1. 软件包进入oerv： https://gitee.com/yyjeqhc/ruyi   这个暂时在个人仓库，还未进入src-openeuler
<img width="1254" height="614" alt="image" src="https://github.com/user-attachments/assets/2284d8bd-6387-478b-9095-d58c5df94b27" />

2. 构建系统：https://eulermaker.compass-ci.openeuler.openatom.cn/projects
<img width="1242" height="426" alt="image" src="https://github.com/user-attachments/assets/63939834-5727-4b19-bdbf-5822ecc2c6e9" />
<img width="1260" height="664" alt="image" src="https://github.com/user-attachments/assets/640bcc60-c84b-48fb-985d-4839d2ca3582" />

- https://gitee.com/yyjeqhc/python-pygit2.git
- https://gitee.com/yyjeqhc/ruyi.git
- https://gitee.com/src-openeuler/python-arpy.git
- https://gitee.com/src-openeuler/python-semver.git

<img width="1252" height="840" alt="image" src="https://github.com/user-attachments/assets/3bd12beb-741e-4dc8-ac51-892db6431774" />
<img width="1244" height="728" alt="image" src="https://github.com/user-attachments/assets/b6d70c1a-141f-452f-82df-c876e37f5246" />


EBS构建工程 for ruyi：
* 0.43.0： https://eulermaker.compass-ci.openeuler.openatom.cn/project/overview?osProject=yyjeqhc:openEuler-24.03-LTS-SP3:everything


情况：
1. 目前python-pygit2 和 ruyi 在私人仓库，需要进一步进入 src-openeuler 组织。
    * 已经在流程中：
        * https://software-pkg.openeuler.openatom.cn/zh  【审批中】列表中查询
        * python-pygit2 CI已经通过
        * ruyi CI 失败，需要进一步排查问题原因
2. 构建工程中，缺少riscv64 构建成果验证，需要增加；
    * https://eulermaker.compass-ci.openeuler.openatom.cn/project/overview?osProject=yyjeqhc:openEuler-24.03-LTS-SP3:everything  缺少riscv64架构验证
    * https://eulermaker.compass-ci.openeuler.openatom.cn/project/overview?osProject=testruyi
4. ruyi目前已经更新到0.45.0版本，且新增一处 Python 依赖 babel ；
    > 经对照，openEuler 24.03 LTS-SP3 满足babel依赖条件。

其它：
* python-pygit2：https://www.pygit2.org/
    * https://github.com/libgit2/pygit2
    * https://github.com/libgit2/pygit2/blob/712b5bdfae13148fbd727d16be563589a1022aba/build.sh   或者[makefile](https://github.com/libgit2/pygit2/blob/712b5bdfae13148fbd727d16be563589a1022aba/Makefile)  
        > build:	LIBSSH2_VERSION=1.9.0 LIBGIT2_VERSION=1.1.0 sh build.sh
     

todo：
1. 目前引入的 python-pygit2 版本为 1.18.0 ——> 依赖 libgit2 1.9.0 ;但是openEuler中的 libgit2 是 1.7.2 低版本；
    * 为了不影响openEuler其它包依赖关系，优先考虑调整新引入的  python-pygit2 降低版本到 libgit2 版本是 1.7.2 

* [x] ruyi ：python-pygit2 兼容性最好是 (>=1.6, <1.19)；python-pygit2 1.14.1 依赖的 libgit2 版本是1.7.2 （只有这一个版本，上一个和下一个tag的依赖都不是这个版本）
* [x] 重新创建软件包仓库：https://gitee.com/phoebe-xi/python-pygit2
* [x] 更新构建工程中的仓库地址并重新构建：https://eulermaker.compass-ci.openeuler.openatom.cn/project/build?osProject=testruyi  
* [x] 版本对齐：ruyi（升级到 0.45.0 ） 仓库
* [ ] 重新构建高版本ruyi，三架构成功后按照[【贡献软件包】](https://software-pkg.openeuler.openatom.cn/zh)流程推进 python-pygit2 和 ruyi 2个仓库的创建
* [ ] 两个仓库创建成功后，在EBS 构建工程中增加 这两个包 （epol？还是哪个工程？）





