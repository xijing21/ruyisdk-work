## openEuler 现状（代码托管平台从gitee迁移到atomgit）
### 代码仓库
原组织(https://gitee.com/openeuler, https://gitee.com/src-openeuler) 下仓库将调整为只读，并发布平台切换公告；
开发者在新平台组织(https://atomgit.com/openeuler, https://atomgit.com/src-openeuler) 下代码仓开展贡献；

sig-RISC-V 维护的仓库：
https://atomgit.com/openeuler/RISC-V
https://atomgit.com/src-openeuler/opensbi

### 构建系统/平台
发版用的软件包构建系统是ebs： https://eulermaker.compass-ci.openeuler.openatom.cn/projects 

### 镜像源/软件源
官方：https://repo.openeuler.org/

## RISC-V SIG 资源
- obs：https://build.tarsier-infra.isrc.ac.cn/project
- repo：https://repo.tarsier-infra.isrc.ac.cn/openEuler-RISC-V/testing/
- 网站：https://images.oerv.ac.cn/home

## LTS版本
- update发版：原则上是一月一次。但是实际执行可能会综合各种影响因素调整。

## 附
1. 软件源码仓库 https://atomgit.com/src-openeuler
2. 发版软件包构建系统 https://eulermaker.compass-ci.openeuler.openatom.cn/projects
```
镜像里软件包源地址：
#generic-repos is licensed under the Mulan PSL v2.
#You can use this software according to the terms and conditions of the Mulan PSL v2.
#You may obtain a copy of Mulan PSL v2 at:
#    http://license.coscl.org.cn/MulanPSL2
#THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
#PURPOSE.
#See the Mulan PSL v2 for more details.

[OS]
name=OS
baseurl=https://repo.openeuler.org/openEuler-24.03-LTS-SP3/OS/riscv64/rva20/$basearch/
metalink=https://mirrors.openeuler.org/metalink?repo=$releasever/OS/riscv64/rva20&arch=$basearch
metadata_expire=1h
enabled=1
gpgcheck=1
gpgkey=http://repo.openeuler.org/openEuler-24.03-LTS-SP3/OS/riscv64/rva20/$basearch/RPM-GPG-KEY-openEuler

[everything]
name=everything
baseurl=https://repo.openeuler.org/openEuler-24.03-LTS-SP3/everything/riscv64/rva20/$basearch/
metalink=https://mirrors.openeuler.org/metalink?repo=$releasever/everything/riscv64/rva20&arch=$basearch
metadata_expire=1h
enabled=1
gpgcheck=1
gpgkey=http://repo.openeuler.org/openEuler-24.03-LTS-SP3/everything/riscv64/rva20/$basearch/RPM-GPG-KEY-openEuler

[EPOL]
name=EPOL
baseurl=https://repo.openeuler.org/openEuler-24.03-LTS-SP3/EPOL/main/riscv64/rva20/$basearch/
metalink=https://mirrors.openeuler.org/metalink?repo=$releasever/EPOL/main/riscv64/rva20&arch=$basearch
metadata_expire=1h
enabled=1
gpgcheck=1
gpgkey=http://repo.openeuler.org/openEuler-24.03-LTS-SP3/OS/riscv64/rva20/$basearch/RPM-GPG-KEY-openEuler

[debuginfo]
name=debuginfo
baseurl=https://repo.openeuler.org/openEuler-24.03-LTS-SP3/debuginfo/riscv64/rva20/$basearch/
metalink=https://mirrors.openeuler.org/metalink?repo=$releasever/debuginfo/riscv64/rva20&arch=$basearch
metadata_expire=1h
enabled=1
gpgcheck=1
gpgkey=http://repo.openeuler.org/openEuler-24.03-LTS-SP3/debuginfo/riscv64/rva20/$basearch/RPM-GPG-KEY-openEuler

[source]
name=source
baseurl=https://repo.openeuler.org/openEuler-24.03-LTS-SP3/source/
metalink=https://mirrors.openeuler.org/metalink?repo=$releasever&arch=source
metadata_expire=1h
enabled=1
gpgcheck=1
gpgkey=http://repo.openeuler.org/openEuler-24.03-LTS-SP3/source/RPM-GPG-KEY-openEuler

[update]
name=update
baseurl=https://repo.openeuler.org/openEuler-24.03-LTS-SP3/update/riscv64/rva20/$basearch/
metalink=https://mirrors.openeuler.org/metalink?repo=$releasever/update/riscv64/rva20&arch=$basearch
metadata_expire=1h
enabled=1
gpgcheck=1
gpgkey=http://repo.openeuler.org/openEuler-24.03-LTS-SP3/OS/riscv64/rva20/$basearch/RPM-GPG-KEY-openEuler

[update-source]
name=update-source
baseurl=https://repo.openeuler.org/openEuler-24.03-LTS-SP3/update/source/
metalink=https://mirrors.openeuler.org/metalink?repo=$releasever&arch=source
metadata_expire=1h
enabled=1
gpgcheck=1
gpgkey=http://repo.openeuler.org/openEuler-24.03-LTS-SP3/source/RPM-GPG-KEY-openEuler
```
