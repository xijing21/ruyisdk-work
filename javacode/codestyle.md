
## 配置说明
Eclipse中的Checkstyle插件配置界面的各个配置项的解释：
1. **Available modules**:
   - 左侧面板，显示了所有可用的Checkstyle模块。这些模块可以分为不同的类别。
2. **Configured modules for group "XXXX"**:
   - 右侧面板，显示了当前配置的“XXXX”组中的模块。每个模块都有以下几个属性：
     - **Enabled**: 是否启用该模块。
     - **Module**: 模块的名称。
     - **Severity**: 该模块的严重程度，这里都设置为“inherit”，意味着它们继承了父级或全局设置的严重程度。
     - **Comment**: 对模块的注释或描述。
4. **Buttons and Actions**:
   - **Add...**: 添加新的模块到当前组。
   - **Remove**: 移除选定的模块。
   - **Open...**: 打开模块编辑器以进一步配置模块。
   - **OK/Cancel**: 确认或取消当前的配置更改。
5. **Description Section**:
   - 提供了关于所选模块的简要描述和功能说明。
6. **Open module editor(s) on add action**:
   - 当添加新模块时，是否打开模块编辑器进行进一步的配置。
这个配置界面允许开发者在项目中定制Checkstyle规则，确保代码符合特定的格式和风格标准。

## Indentation
<img width="619" height="518" alt="image" src="https://github.com/user-attachments/assets/1da71e32-3e9a-406c-b13e-774ca9645f0a" />

图片中显示的是Eclipse中Checkstyle插件的“Indentation”模块配置界面。以下是对各个配置项的解释：
1. **Severity**: 设置此规则的严重程度。可以选择不同的级别，例如error, warning, info等。 `Severity: inherit`表示该规则的严重级别继承自父配置或默认配置。例如，若父规则设置为`error`，子规则未明确指定时自动继承该级别。这种设计常用于多层级配置中保持一致性。
2. **arrayInitIndent**: 数组初始化时的缩进量。
3. **basicOffset**: 基本缩进量，通常用于控制整个文件的缩进级别。
4. **braceAdjustment**: 大括号调整，用于控制大括号相对于其所在行的位置。
5. **caseIndent**: case语句的缩进量。
6. **forceStrictCondition**: 强制严格条件，可能用于控制某些特定情况下的缩进行为。
7. **lineWrappingIndentation**: 行包裹时的缩进量。
8. **throwsIndent**: throws子句的缩进量。
这些配置项允许开发者自定义Java代码的格式，以确保代码的一致性和可读性。通过调整这些参数，可以满足特定的编码规范要求。

### arrayInitIndent（数组初始化缩进量）
**定义**：控制数组初始化时元素相对于数组声明的缩进空格数。  
**示例**：
```java
// arrayInitIndent=4 时的效果
int[] arr = {
    1, 2, 3  // 元素缩进4个空格
};
```
若设置为2，则元素缩进2个空格。
### braceAdjustment（大括号调整）
**定义**：调整大括号`{}`的垂直位置，决定其是否与代码块起始行对齐或换行后缩进。  
**示例**：
```java
// braceAdjustment=0（与起始行对齐）
if (condition) {
    code;
}
// braceAdjustment=4（换行后缩进4格）
if (condition) 
    {
    code;
    }
```
该参数影响代码块的可读性风格。
### lineWrappingIndentation（行包裹缩进）
**定义**：当表达式过长换行时，后续行相对于首行的缩进量。  
**示例**：
```java
// lineWrappingIndentation=8 时的效果
String message = "This is a very long string that "
        + "needs line wrapping.";  // 换行后缩进8格
```
若设置为4，则缩进4个空格。
以上示例均基于Checkstyle的代码格式化规则，实际效果可能因工具或配置环境略有差异。

##
<img width="1024" height="706" alt="image" src="https://github.com/user-attachments/assets/bea0c5a0-e3f9-44ca-bbeb-765cf283d5ee" />

- **AtclauseOrder**: 检查@clauses的顺序是否符合规范。
- **InvalidJavadocPosition**: 检查Javadoc的位置是否正确。
- **JavadocMethod**: 检查方法级别的Javadoc是否符合规范。
- **JavadocParagraph**: 检查Javadoc段落的结构和格式。
- **JavadocTagContinuationIndentation**: 检查Javadoc标签续行的缩进是否符合规范。
- **MissingJavadocMethod**: 检查缺少方法级别的Javadoc。
- **MissingJavadocType**: 检查缺少类型级别的Javadoc。
- **NonEmptyAtclauseDescription**: 检查@clauses的描述是否非空。
- **RequireEmptyLineBeforeBlockTagGroup**: 要求在块标签组之前有空行。
- **RequireEmptyLineBeforeBlockTagGroup**: 同上，可能是重复条目。
- **SingleLineJavadoc**: 检查单行Javadoc的格式。
- **SummaryJavadoc**: 检查总结性的Javadoc是否符合规范。


## Filters
<img width="1018" height="711" alt="image" src="https://github.com/user-attachments/assets/07bce197-71b8-4777-bc7b-0ef48db85e39" />
 **Specific Modules**:
   - **SuppressionCommentFilter**: 用于处理带有抑制注释的代码。
   - **SuppressionFilter**: 处理抑制过滤。
   - **SuppressionXPathFilter**: 使用XPath表达式来抑制AST树中的节点。
   - **SuppressionXPathSingleFilter**: 单个XPath表达式的抑制过滤器。
   - **SuppressWarningsFilter**: 抑制警告信息。
   - **SuppressWithNearbyCommentFilter**: 通过附近的注释来抑制检查。
   - **SuppressWithNearbyTextFilter**: 通过附近的文本内容来抑制检查。

