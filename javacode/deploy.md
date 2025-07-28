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


## Formatter 配置
1. Eclipse > windows > preferences > Java > code style > Formatter
2. Formatter界面：  Import，导入之前下载后的 eclipse-java-google-style.xml（这里导入的是未修改之前的xml，接着需要edit）
3. Edit，对照配置项（参考截图）修改对应的选项并保存即可。

## Checkstyle 配置
1. Eclipse > windows > preferences > Checkstyle
2. 选中界面表格中的 Google Checks > Export，导出一个Google_Checks.xml文档到本地任一地方；
3. 按照之前标记的表格，将Google_Checks.xml中对应的选项的值进行修改并保存；
4. 回到Checkstyle界面，New > External Configuration File > Location Browse 选中修改后的 Google_Checks_modify.xml  > ok
5. 注意：这里会弹出提示窗口：
  <img width="608" height="223" alt="image" src="https://github.com/user-attachments/assets/8f2d7c6d-69b5-4b0a-a337-2c4e11001e22" />
  
6. Edit properties...  
7. Find unresolved properties
   
  ```
  Unresolved Properties found
  The following unresolved properties were found:
  ${org.checkstyle.google.severity}
  ${org.checkstyle.google.suppressionfilter.config}
  ${org.checkstyle.google.suppressionxpathfilter.config}
  
  Add them to the additional configuration properties?
  No   Yes
  ```

8. 针对上面的三个问题，第一个采用配置的方式，其它两个回到xml文档中，删除响应的配置；保存后再次导入，会再次提示，但是只有一个选项：${org.checkstyle.google.severity} ；为其配置值：warning
9. 如果后续要修改${org.checkstyle.google.severity} ：表格中选中对应项 > Properties > Additional properties 
<img width="1366" height="813" alt="image" src="https://github.com/user-attachments/assets/8275ebec-ac85-41cb-9682-1c190fa2ef32" />


## 验证
1. 项目右键 > Checkstyle > check code with checkstyle
   <img width="645" height="156" alt="image" src="https://github.com/user-attachments/assets/6c963c6c-06d9-4c22-84c3-43a777c1ea0c" />

2. Problem 窗口查看 Checkstyle Problem；
上面的配置主要是围绕缩进等配置的，因此可以看看有关的错误；

3. java文件右键 > source > format :会发现Problem 窗口中有关缩进的一些问题消失。

当然这是代码不规范的情况下的检查和修改；还有一些其它问题及设置，在后续进行配置修改的说明。
