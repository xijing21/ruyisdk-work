# ruyi包管理器在openeuler中的集成情况

## 路线
- [ ] 1. ruyi软件包引入openeuler软件包社区：https://atomgit.com/src-openeuler
- [ ] 2. ruyi可以在构建系统中完成构建（所需要的依赖包都满足）   
- [ ] 3. ruyi进入openEuler for RISC-V 官方的系统镜像源，可以直接通过yum install ruyi 安装
- [ ] 4. ruyi进入openEuler for RISC-V 镜像的系统预装软件
- [ ] 5. ruyi在openEuler 中的持续更新与维护（随着ruyi版本的升级，openEuler社区中ruyi包版本的同步升级）

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


情况：目前python-pygit2 和 ruyi 在私人仓库，需要进一步进入 src-openeuler组织。
