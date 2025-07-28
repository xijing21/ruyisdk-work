# Eclipse 上配置部署

在Eclipse中，关于代码格式的定义和检查相关的功能有：
- Java > Code Style > Formatter ：用于代码格式化（Source > Format 功能对应），不同的ide有其对应的xml文件
  - https://github.com/google/styleguide/blob/gh-pages/eclipse-java-google-style.xml （仓库很久没有更新，下载最新版本即可）
- Checkstyle(单独安装插件，插件会有版本信息，比如我当前是10.23.0） ：用于在指定的时机进行代码风格检查，会在Problems中展示 Checkstyle Problem；
  - https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml （建议使用与ide插件对应的版本，安装插件就已经存在，一般可以不用单独下载。如果需要配置文件可以使用导出功能导出配置后，再修改，再导入；
这两个插件分别有对应的配置文件，在上面已经给出。

## 基本设置定义
- 基于 Google style 进行配置；鉴于Google style 的两个空格缩进并不符合大多数ide和用户的习惯，一般会进行调整：
- 修改 eclipse-java-google-style.xml 中的内容：
  
| option                        | previous value | modified value | note                   |
| ----------------------------- | -------------- | -------------- | ---------------------- |
| Indentation size              | 2              | 4              | 行缩进空格数           |
| Tab size                      | 2              | 4              | TAB空格数              |
| Maximum line width            | 100            | 120            | 最大行宽               |
| Default indentation for       |                |                |                        |
| wrapped lines                 | 2              | 4              | 折行部分的默认缩进     |
| Default indentation for array |                |                |                        |
| initializers                  | 2              | 4              | 数组初始化器的默认缩进 |

<img width="662" height="930" alt="image" src="https://github.com/user-attachments/assets/b08c936c-2d6b-4f99-b8bf-36de7efc1925" />

- 修改google_checks中的内容：

| module      | property                | previous value | modified value | note                                           |
| ----------- | ----------------------- | -------------- | -------------- | ---------------------------------------------- |
| LineLength  | max                     | 100            | 120            | 单行长度                                       |
| Indentation | basicOffset             | 2              | 4              | 基本缩进量，通常用于控制整个文件的缩进级别     |
|             | braceAdjustment         | 2              | 0              | 大括号调整，用于控制大括号相对于其所在行的位置 |
|             | caseIndent              | 2              | 4              | case语句的缩进量                               |
|             | throwsIndent            | 4              | 4              | throws子句的缩进量                             |
|             | lineWrappingIndentation | 4              | 4              | 行包裹时的缩进量                               |
|             | arrayInitIndent         | 2              | 4              | 数组初始化时的缩进量                           |
- 修改google_checks中的内容：
## Formatter 配置
## Checkstyle 配置
