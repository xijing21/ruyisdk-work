## 命名规范（Naming Conventions）

```
Checkstyle
Issue: Abbreviation in name 'getLogMaxSizeMB' must contain no more than '1' consecutive capital letters.
Group: Naming Conventions
Module: AbbreviationAsWordInName
```
分析问题:
该问题是关于命名规范（Naming Conventions）中的一个具体检查项：`AbbreviationAsWordInName`。它指出在标识符名称中连续大写字母的数量不能超过1个。

解决方案:
要解决这个问题，可以采取以下步骤：
1. **理解规则**：
   - 规则要求标识符名称中的连续大写字母数量不超过1个。例如，`MyTest` 是允许的，但 `MyTEST` 则不允许。
2. **调整代码**：
   - 查找所有违反此规则的标识符名称并进行修正。对于示例中的 `getLogMaxSizeMB`，需要将其改为符合规则的形式，如 `getLogMaxSizeMb` 或 `getLogMaxSizeMode`.
3. **配置Checkstyle**：
   - 如果有特殊情况需要忽略某些变量（如静态、最终变量），可以在Checkstyle配置文件中设置 `ignoreFinal`, `ignoreStatic`, 和 `ignoreStaticFinal` 参数来控制这些变量的检查行为。

```
Abbreviation in name 'IConsoleOutput' must contain no more than '1' consecutive capital letters.
Abbreviation in name 'IRuyisdkLogger' must contain no more than '1' consecutive capital letters.
```
这里接口类中使用了前缀I来表示Interface。这种方式在Eclipse 等早期框架中广泛存在。尤其是大型代码库或者API设计中。如：
org.eclipse.core.runtime.ILog;
org.eclipse.core.runtime.IStatus;
**Eclipse 命名风格**（如 `ILog`、`IStatus`）确实在 Java 生态中广泛存在，尤其是在一些早期框架（如 Eclipse、.NET 等）中。这种风格通过 `I` 前缀明确标识接口，使得代码更直观，特别是在大型代码库或 API 设计中。

如果你更喜欢这种风格，并希望 **Checkstyle** 允许 `I` 前缀的接口命名，可以按以下方式调整规则：

---

### **1. 修改 Checkstyle 配置（`checkstyle.xml`）**
默认情况下，Checkstyle 的 `AbbreviationAsWordInName` 规则会限制连续大写字母的数量（如 `IConsoleOutput` 被认为有 2 个连续大写字母 `I` 和 `C`）。你可以调整该规则：

#### **方案 1：放宽连续大写字母限制**
```xml
<module name="AbbreviationAsWordInName">
    <property name="allowedAbbreviationLength" value="2" />  <!-- 允许 2 个连续大写字母（如 ILogger） -->
# 上面这里参数由2改为0后，所有warning全部全成了error，改回0后正常了。因此这里还是设置的0
    <property name="ignoreFinal" value="false" />
    <property name="allowedAbbreviations" value="I,UI,XML,JSON" />  <!-- 明确允许的缩写 -->
</module>
```

#### **方案 2：完全禁用该规则（不推荐）**
```xml
<!-- 直接移除或注释掉 AbbreviationAsWordInName 模块 -->
<!-- <module name="AbbreviationAsWordInName"/> -->
```

---

### **2. 团队达成命名约定**
如果决定采用 `I` 前缀风格，建议在团队内明确规范：
- **接口**：`I + UpperCamelCase`（如 `ILogger`）
- **实现类**：`Impl` 后缀或其他业务相关名称（如 `LoggerImpl`、`FileLogger`）
- **抽象类**：`Abstract` 前缀（如 `AbstractLogger`）

示例：
```java
// 接口
public interface IConsoleOutput { ... }

// 实现类
public class ConsoleOutputImpl implements IConsoleOutput { ... }
```

---

### **3. 与 Google Style 的权衡**
| **Eclipse 风格 (`I` 前缀)** | **Google 风格 (无前缀)** |
|----------------------------|--------------------------|
| 明确区分接口和类，提高可读性 | 所有类型命名一致，简化规则 |
| 在大型代码库中更易维护 | 强调面向接口编程，减少对前缀的依赖 |
| 传统框架（如 Eclipse）常用 | 现代 Java 项目（如 Guava、JDK）常用 |

如果项目本身是 **Eclipse 插件** 或遵循其传统风格，使用 `I` 前缀是合理的。否则，建议优先遵循 **Google Style** 以保持与现代 Java 生态的一致性。

---

### **4. 如果存在同名类**
即使存在同名类，也可以通过以下方式解决：
```java
// 接口
public interface ILogger { ... }

// 实现类（添加 Impl 或具体描述）
public class LoggerImpl implements ILogger { ... }
// 或
public class FileLogger implements ILogger { ... }
```

---

### **结论**
- **可以修改 Checkstyle** 允许 `I` 前缀，但需团队达成一致。
- **推荐妥协方案**：对接口使用 `I` 前缀，但对其他缩写（如 `XML`、`JSON`）仍保持限制。
- **长期维护性**：如果项目独立且团队习惯 `I` 前缀，这种方式完全可行；如果与 Google 生态（如 Android）协作，建议逐步迁移到无前缀风格。

### 总结
<img width="697" height="757" alt="image" src="https://github.com/user-attachments/assets/415d8011-570a-4e0f-9252-1036c0061741" />
allowedAbbreviations 增加 I；
<img width="702" height="764" alt="image" src="https://github.com/user-attachments/assets/c1c4bb2a-9fab-4f5d-add7-950f4d40f337" />


## CustomImportOrder

```
Issue: Extra separation in import group before 'java.io.IOException'
Group: Imports
Module: CustomImportOrder
```
### 分析问题原因
这个问题是由Checkstyle的一个特定规则引起的，即“CustomImportOrder”模块。该模块用于定义导入语句的顺序和分组规则。当Checkstyle检测到导入语句的排序不符合预定的规则时，就会抛出此类问题。
具体来说，“Extra separation in import group before 'java.io.IOException'”表示在导入组中，'java.io.IOException'之前的导入语句之间有多余的分隔。这可能是因为导入语句的顺序与Checkstyle配置中定义的顺序不一致。
### 解决方案
为了解决这个问题，您可以按照以下步骤调整导入语句的顺序：
1. **了解当前规则**：首先，确定Checkstyle配置文件中“CustomImportOrder”模块的具体规则。这通常涉及到导入包的顺序和分组方式。
2. **调整导入顺序**：根据Checkstyle的规则，重新排列导入语句。确保每个导入语句都位于正确的位置，并且相邻的导入语句之间没有多余的分隔。
3. **验证配置**：运行Checkstyle检查，确认问题已经解决。如果仍然存在问题，可能需要进一步调整导入顺序或检查Checkstyle配置文件中的规则。
4. **更新配置文件**：如果必要，可以根据项目的具体情况调整Checkstyle配置文件中的规则，使其更符合项目的编码习惯。
通过以上步骤，您可以有效地解决由“CustomImportOrder”模块引发的导入语句排序问题。

Google Java 编程风格规范中对导入语句的顺序和规则有明确要求，旨在保持代码的一致性和可读性。以下是具体规则：
### 1. 导入语句的分组和顺序
导入语句应分为以下三个明确的组，每组之间用空行分隔：
- **标准库导入**：来自 `java.` 和 `javax.` 包的导入语句。
- **第三方库导入**：非标准库的第三方包导入语句。
- **本地项目导入**：当前项目中的包导入语句。
### 2. 组内排序规则
在每个组内，导入语句应按照字母顺序排列，确保逻辑清晰且易于查找。
### 3. 禁止使用通配符导入
避免使用 `import packagename.*` 的形式，因为这可能导致命名冲突和不确定性。
### 4. 行内限制
每行只导入一个类或接口，例如：
```java
import java.io.IOException;
import java.util.List;
```
### 5. 特殊规则
- 如果导入语句涉及多个类或接口，确保它们按照字母顺序排列，避免重复或冗余。
- 导入语句应放置在源文件的顶部，位于包声明之后、类声明之前。
### 6. 相关资源
您可以参考 Google Java Style Guide 的完整定义，了解更多细节和示例。此外，GitHub 上提供了 Google Code 风格的配置文件，支持 Eclipse IDE 和 IntelliJ IDE 的集成，地址为：[Google Code 风格配置文件](https://github.com/codeset/google-java-stylegui)。
通过遵循这些规则，可以确保代码的可读性和一致性，同时便于团队协作和维护。

---

图片中的文字如下：
```
Issue: Extra separation in import group before 'org.eclipse.swt.graphics.Color'
Group: Imports
Module: CustomImportOrder
```
### 分析问题
这个问题是由 Checkstyle 的 `CustomImportOrder` 模块引起的。该模块用于定义导入语句的顺序和分组规则。当 Checkstyle 检测到导入语句的排序不符合预定的规则时，就会抛出此类问题。
具体来说，问题描述指出在导入语句 `org.eclipse.swt.graphics.Color` 之前存在额外的分离（即多余的空行或不必要的间距）。这违反了导入语句应该紧凑排列的规则。
### 解决办法
1. **检查导入顺序**：
   - 确保 `org.eclipse.swt.graphics.Color` 的导入语句位于正确的导入组中，并且与其他相关导入语句紧密排列在一起。
   - 根据 Google Java Style Guide 的建议，导入语句应按以下顺序排列：
     1. 标准库导入（如 `java.*`, `javax.*`）。
     2. 第三方库导入。
     3. 项目内部导入。
2. **移除额外空行**：
   - 在导入语句之间不应有多余的空行。确保所有导入语句紧凑排列，只在必要时（如不同导入组之间）使用单个空行分隔。
3. **验证配置**：
   - 运行 Checkstyle 检查，确认问题已解决。如果仍存在问题，可能需要进一步调整导入顺序或检查 Checkstyle 配置文件中的规则。
4. **更新配置文件**：
   - 如果必要，可以根据项目的具体情况调整 Checkstyle 配置文件中的规则，使其更符合项目的编码习惯。
通过以上步骤，您可以有效地解决由 `CustomImportOrder` 模块引发的导入语句排序问题。

---

**文字识别**
Issue: Only one statement per line allowed.
Group: Coding Problems
Module: OneStatementPerLine
**问题分析**
这个CheckStyle问题表明在代码中有违反“每行只能有一个语句”规则的实例。这意味着在同一行上可能有多个独立的语句被写在一起，这是不被允许的。
**如何解决**
要解决这个问题，您需要将同一行的多个语句分开，确保每个语句都单独占据一行。这样做可以提高代码的可读性和可维护性，同时遵守CheckStyle的编码规范。
例如，如果您有以下代码：
```java
int a = 5; int b = 10;
```
您需要将其改为：
```java
int a = 5;
int b = 10;
```
这样，每个赋值语句都单独占一行，从而解决了CheckStyle报告的问题。请对您的代码进行类似的调整，以确保每行只有一个语句。完成后，再次运行CheckStyle验证问题是否已经解决。


### 总结
import 调整按照如下顺序排列；不同的导入组之间不适用空行隔开（使用空行反而报错了）
 - 导入语句应按以下顺序排列：
   1. 标准库导入（如 `java.*`, `javax.*`）。
   2. 第三方库导入，如eclispe的相关库
   3. 项目内部导入。
- 不得使用任何通配符（会报 OneStatementPerLine）
错误的示范：
import java.io.*;
import java.nio.file.*;

正确的示范：精确到具体的类；


## RequireEmptyLineBeforeBlockTagGroup
### 文字识别
**Issue:** 
Javadoc tag '@param' should be preceded with an empty line.
Javadoc tag '@return' should be preceded with an empty line.  
**Group:** Javadoc Comments  
**Module:** RequireEmptyLineBeforeBlockTagGroup  
### 问题分析
该 CheckStyle 问题指出在 Javadoc 注释中，`@return` 标签前缺少一个空行。根据 CheckStyle 的要求，Javadoc 标签（如 `@param`, `@return`, `@throws` 等）之前应有一个空行以提高代码的可读性和规范性。
### 如何解决
为了解决这个问题，您需要在 `@return` 标签前添加一个空行。以下是具体的步骤和示例：
#### 步骤
1. 找到包含 `@return` 标签的 Javadoc 注释块。
2. 在 `@return` 标签前插入一个空行。
#### 示例
假设原始代码如下：
```java
/**
 * This method calculates the sum of two numbers.
 * @param a The first number.
 * @param b The second number.
 * @return The sum of a and b.
 */
public int add(int a, int b) {
    return a + b;
}
```
修改后的代码应为：
```java
/**
 * This method calculates the sum of two numbers.
 * @param a The first number.
 * @param b The second number.
 *
 * @return The sum of a and b.
 */
public int add(int a, int b) {
    return a + b;
}
```
请注意，虽然示例中只展示了 `@return` 标签的处理方式，但同样的原则也适用于其他 Javadoc 标签，如 `@param`、`@throws` 等。确保在每个标签前都有一个空行，以满足 CheckStyle 的要求。
完成上述修改后，重新运行 CheckStyle 验证问题是否已解决。这样可以确保您的代码符合 CheckStyle 规范，提高代码质量和一致性。

<img width="869" height="374" alt="image" src="https://github.com/user-attachments/assets/e506b8c4-2348-4ae1-be13-24ecf37c6368" />

实际上，并不是缺乏空行，而是因为有一个空格，导致没有被正确识别为空行，从而报错。这个问题的解决办法如下：
修改您的 google_check.xml 文件，将 RequireEmptyLineBeforeBlockTagGroup 规则禁用。
allowOneLineTags: 是否允许单行 Javadoc（如 /** @return 0 */）。默认为 false。

<img width="971" height="889" alt="image" src="https://github.com/user-attachments/assets/afa7f635-12bc-48b2-aa4b-2a7e88763636" />
取消RequireEmptyLineBeforeBlockTagGroup勾选


## Missing a Javadoc comment.

```
Issue: Missing a Javadoc comment.
Group: Javadoc Comments
Module: MissingJavadocMethod
```
在代码中，Missing a Javadoc comment. 提示太多了，在google style中，哪些注释是必须或者建议提供的，哪些可以省略？

在 Google Java 编码规范中，Javadoc 注释的使用有明确的要求，并非所有代码都需要注释，而是根据场景判断是否必要。以下是关于必须、建议和可以省略的 Javadoc 注释的说明：
### 必须提供 Javadoc 注释的情况
1. **公共类和接口**  
   所有公共类、接口及其公共方法必须使用 Javadoc 注释，说明其用途和行为。
2. **公共方法**  
   公共方法的 Javadoc 需要描述方法的功能、参数、返回值以及可能抛出的异常。
3. **抽象类和接口**  
   抽象类和接口的公共方法需要详细说明其实现要求或使用场景。
### 建议提供 Javadoc 注释的情况
1. **受保护的方法**  
   受保护的方法（protected）建议添加 Javadoc，以便子类理解其用途。
2. **复杂的逻辑**  
   代码逻辑复杂或难以理解时，建议通过 Javadoc 进行解释。
3. **工具类或辅助方法**  
   工具类中的公共方法建议提供 Javadoc，说明其使用方式和适用场景。
### 可以省略 Javadoc 注释的情况
1. **私有方法**  
   私有方法通常不需要 Javadoc，除非其逻辑非常复杂且难以理解。
2. **简单的 getter/setter 方法**  
   对于简单的 getter 和 setter 方法，可以省略 Javadoc，尤其是当方法名已清晰表达其功能时。
3. **测试类**  
   测试类中的方法通常不需要 Javadoc，除非测试逻辑特别复杂。
### 如何解决 "Missing a Javadoc comment" 提示过多的问题
1. **调整 Checkstyle 配置**  
   可以通过修改 `googlecheck.xml` 文件，禁用对某些场景（如私有方法或简单 getter/setter）的 Javadoc 检查规则。例如，注释掉或调整 `JavadocMethod` 模块的配置。
2. **选择性添加注释**  
   根据上述规范，仅对必须或建议添加注释的代码编写 Javadoc，避免过度注释。
3. **使用 IDE 快捷键优化注释**  
   利用 Eclipse 或 IntelliJ 的快捷键生成规范的 Javadoc，确保注释格式一致且高效。
通过合理区分必须、建议和可以省略的注释场景，既能满足 Google Java 编码规范的要求，又能减少不必要的提示，提高开发效率。更多细节可参考 Google Java 编码规范（http://google-styleguide.googlecode.com/svn/trunk/javaguide.html ）。


要修改 Checkstyle 配置，使其 **仅强制要求公共类/接口、抽象类/接口及其方法必须有 Javadoc 注释**，而对其他情况（如私有方法、简单 getter/setter 等）仅鼓励但不强制，可以按以下步骤调整 `google_checks.xml` 或自定义配置文件：
---
### **1. 修改 `JavadocMethod` 模块**
默认情况下，`JavadocMethod` 会检查所有方法（包括私有方法）。我们可以通过以下配置限制其检查范围：
```xml
<module name="JavadocMethod">
    <!-- 仅检查 public、protected 方法，忽略 private 方法 -->
    <property name="scope" value="protected"/>
    <!-- 忽略简单的 getter/setter 方法（如 getXxx()、setXxx()） -->
    <property name="allowMissingPropertyJavadoc" value="true"/>
    <!-- 忽略抽象方法（由父类或接口的 Javadoc 继承） -->
    <property name="allowedAnnotations" value="Override, Deprecated"/>
    <!-- 忽略参数和返回值的 Javadoc（可选） -->
    <property name="validateThrows" value="false"/>
</module>
```
#### **关键参数说明**：
- `scope="protected"`：仅检查 `public` 和 `protected` 方法，忽略 `private` 方法。
- `allowMissingPropertyJavadoc="true"`：忽略简单的 getter/setter 方法（符合 JavaBean 规范的方法）。
- `allowedAnnotations`：允许 `@Override` 和 `@Deprecated` 的方法省略 Javadoc（避免重复注释）。
---
### **2. 修改 `JavadocType` 模块**
确保 **公共类、接口、抽象类** 必须有 Javadoc，但允许私有类/内部类省略：
```xml
<module name="JavadocType">
    <!-- 仅检查 public、protected 类，忽略 private 类 -->
    <property name="scope" value="protected"/>
    <!-- 忽略匿名内部类（如 new Runnable() {...}） -->
    <property name="excludeScope" value="nothing"/>
    <!-- 忽略简单的记录类（record） -->
    <property name="allowMissingParamTags" value="true"/>
</module>
```
#### **关键参数说明**：
- `scope="protected"`：仅检查 `public` 和 `protected` 类，忽略 `private` 类。
- `excludeScope`：可以进一步限制检查范围（如 `package-private`）。
---
### **3. 修改 `JavadocVariable` 模块**
仅检查 **公共常量（static final）** 是否有 Javadoc，忽略其他字段：
```xml
<module name="JavadocVariable">
    <!-- 仅检查 public static final 字段 -->
    <property name="scope" value="public"/>
    <!-- 忽略简单的常量（如 serialVersionUID） -->
    <property name="excludeScope" value="protected"/>
</module>
```
---
### **4. 完整配置示例**
以下是调整后的核心模块配置（完整文件可参考 [Google Checks](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml)）：
```xml
<module name="Checker">
    <module name="TreeWalker">
        <!-- 强制公共类/接口必须有 Javadoc -->
        <module name="JavadocType">
            <property name="scope" value="protected"/>
        </module>
        
        <!-- 强制公共/受保护方法必须有 Javadoc，忽略私有方法 -->
        <module name="JavadocMethod">
            <property name="scope" value="protected"/>
            <property name="allowMissingPropertyJavadoc" value="true"/>
            <property name="allowedAnnotations" value="Override, Deprecated"/>
        </module>
        
        <!-- 强制公共常量必须有 Javadoc -->
        <module name="JavadocVariable">
            <property name="scope" value="public"/>
        </module>
    </module>
</module>
```
---
### **5. 验证配置**
- 使用 `mvn checkstyle:check` 或 IDE 插件检查代码。
- 确保以下情况**不会报错**：
  - 私有方法（`private void foo()`）。
  - 简单的 getter/setter（`public String getName()`）。
  - 匿名内部类（`new Runnable() {...}`）。
- 确保以下情况**必须提供 Javadoc**：
  - 公共类（`public class MyClass`）。
  - 接口方法（`public void doSomething()`）。
  - 抽象类方法（`protected abstract void bar()`）。
---
### **6. 进阶优化（可选）**
如果希望进一步减少噪音，可以：
1. **禁用对测试类的检查**：
   ```xml
   <module name="SuppressionXpathSingleFilter">
       <property name="checks" value="Javadoc*"/>
       <property name="query"="//PACKAGE_DEF[./ANNOTATION[./IDENT[@text='Test']]]"/>
   </module>
   ```
2. **使用 `SuppressionFilter` 忽略特定文件**：
   ```xml
   <module name="SuppressionFilter">
       <property name="file" value="config/suppressions.xml"/>
   </module>
   ```
---
### **总结**
通过调整 `scope`、`allowedAnnotations` 和 `allowMissingPropertyJavadoc` 等参数，可以实现：
- **强制**：公共类/接口、抽象类/接口及其方法必须有 Javadoc。
- **鼓励**：受保护方法、私有类等可以省略（但建议补充）。
- **忽略**：简单的 getter/setter、私有方法、测试类等。
这样既能保证核心代码的可读性，又能减少不必要的注释负担。

### 总结
- public 接口类及其public方法必须有注释；
- public 类和方法需要注释；
- public 方法、变量需要注释，但是主要是给不容易看懂的部分重点注释即可，不要求全部

<img width="649" height="566" alt="image" src="https://github.com/user-attachments/assets/67b745ec-70f4-4dc5-a663-2d7f5ff16286" />

这张图片显示的是Eclipse中的一个Checkstyle模块配置界面，具体是“MissingJavadocType”模块的配置。以下是对各个配置项的解释：
1. **Severity（严重性）**:
   - 这个选项用于设置违反此规则的严重程度。
   - 常见的配置值有：
     - `ignore`: 忽略此违规。
     - `info`: 信息级别，不会影响编译或构建过程。
     - `warning`: 警告级别，可能会在编译时产生警告。
     - `error`: 错误级别，会导致编译失败。
2. **Properties（属性）**:
   - **excludeScope**: 指定要排除的范围，默认值为`nothing`，表示不排除任何范围。
   - **scope**: 指定要检查的范围，默认值为`protected`，表示只检查受保护的成员。
   - **skipAnnotations**: 指定要跳过的注解，默认值为`Generated`，表示跳过带有`@Generated`注解的成员。
3. **Tokens（标记）**:
   - 这些选项用于指定哪些类型的声明需要Javadoc注释。
   - **Interface declaration**: 接口声明。
   - **Class declaration**: 类声明。
   - **Enum declaration**: 枚举声明。
   - **Annotation declaration**: 注解声明。
   - **RECORD_DEF**: 记录类型声明（Java 14及以上版本）。
4. **Translate tokens**: 翻译标记，将选定的标记翻译成相应的配置。
5. **Sort tokens**: 对标记进行排序。
6. **Default**: 将配置重置为默认值。
7. **Cancel**: 取消当前配置更改。
8. **OK**: 确认并保存当前配置更改。
这些配置项允许开发人员根据项目的具体需求定制Checkstyle规则，以确保代码质量和一致性。



在Checkstyle配置中，除了您提到的默认值外，`Properties`（属性）还可以根据项目需求进行更详细的设置。以下是补充的配置内容和常见值：
1. **excludeScope**  
   - **含义**：指定要排除的检查范围，避免对某些范围的代码应用规则。  
   - **常见配置值**：  
     - `nothing`（默认）：不排除任何范围。  
     - `public`：排除公共成员（仅检查非公共成员）。  如果设置为 `public`，则所有 `public` 成员会被排除，仅检查非 `public` 成员（即 `protected`、包私有和 `private` 成员）。
     - `protected`：排除受保护成员（仅检查非受保护成员）。  如果设置为 `protected`，则 `protected` 及更广范围的成员（如 `public`）会被排除，仅检查包私有和 `private` 成员。 
     - `package`：排除包私有成员（仅检查非包私有成员）。  排除包私有成员，检查 `public`、`protected` 和 `private` 成员。  
     - `private`：排除私有成员（仅检查非私有成员）。  排除 `private` 成员，检查 `public`、`protected` 和包私有成员。
2. **scope**  
   - **含义**：指定要检查的范围，仅对符合条件的成员应用规则。  
   - **常见配置值**：  
     - `protected`（默认）：仅检查受保护成员及其子类。  
     - `public`：仅检查公共成员。  
     - `package`：检查包私有成员及更广范围（公共和受保护成员）。  
     - `private`：检查所有成员（包括私有成员）。  
3. **skipAnnotations**  
   - **含义**：指定要跳过的注解，避免对带有特定注解的成员应用规则。  
   - **常见配置值**：  
     - `Generated`（默认）：跳过带有`@Generated`注解的成员。  如果项目中使用了代码生成工具（如 Lombok、MapStruct 等），@Generated 注解常用于标记自动生成的代码，跳过这些检查可以提高效率
     - `Override`：跳过带有`@Override`注解的成员。  
     - `Deprecated`：跳过带有`@Deprecated`注解的成员。  
     - 自定义注解：如`@MyAnnotation`，跳过带有自定义注解的成员。  


4. **additionalJavadocTags**  
   - **含义**：允许在Javadoc注释中使用自定义标签。  
   - **常见配置值**：  
     - `@todo`：允许使用`@todo`标签。  
     - `@note`：允许使用`@note`标签。  
5. **allowMissingJavadoc**  
   - **含义**：是否允许缺少Javadoc注释。  
   - **常见配置值**：  
     - `false`（默认）：不允许缺少Javadoc注释。  
     - `true`：允许缺少Javadoc注释。  
6. **allowMissingParamTags**  
   - **含义**：是否允许缺少`@param`标签。  
   - **常见配置值**：  
     - `false`（默认）：不允许缺少`@param`标签。  
     - `true`：允许缺少`@param`标签。  
7. **allowMissingReturnTag**  
   - **含义**：是否允许缺少`@return`标签。  
   - **常见配置值**：  
     - `false`（默认）：不允许缺少`@return`标签。  
     - `true`：允许缺少`@return`标签。  
8. **allowMissingThrowsTags**  
   - **含义**：是否允许缺少`@throws`标签。  
   - **常见配置值**：  
     - `false`（默认）：不允许缺少`@throws`标签。  
     - `true`：允许缺少`@throws`标签。  
这些配置项可以根据项目的实际需求进行调整，以确保代码规范的一致性和可维护性。更多详细信息可参考相关配置文档。
