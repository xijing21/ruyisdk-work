# Formatter 配置
## Eclipse Formatter 风格
<img width="623" height="271" alt="image" src="https://github.com/user-attachments/assets/7c234078-8f2a-4023-ac1e-3d446e2ee3b2" />

在Eclipse中，Formatter（格式化器）用于自动调整代码的格式，使其符合一定的编码规范和风格。不同的Formatter提供了不同的编码风格和规则。以下是图中下拉选项中不同Formatter的差异：
1. **Java Conventions [built-in]**:
   - 这是Eclipse内置的Java编码规范，旨在遵循Java官方的编码约定。它包括了一些基本的格式化规则，如缩进、换行等，以保持代码的可读性和一致性。
   - <img width="876" height="1327" alt="image" src="https://github.com/user-attachments/assets/65d09bb0-b331-4ec5-9798-11e8ddadd9e6" />

2. **Eclipse [built-in]**:
   - 这也是Eclipse内置的一种格式化器，可能与Java Conventions类似，但可能会有一些细微的区别。具体差异取决于Eclipse的具体实现和更新。
   - <img width="881" height="1332" alt="image" src="https://github.com/user-attachments/assets/64720ed1-7e6d-4645-83ce-12c18f66a760" />

3. **Eclipse 2.1 [built-in]**:
   - 这可能是Eclipse早期版本的内置格式化器。与 newer versions 相比，它可能在某些格式化规则上有所不同。例如，它可能会使用不同的缩进大小、括号放置规则等。
   - <img width="880" height="1300" alt="image" src="https://github.com/user-attachments/assets/1ab59d26-fbdd-4bc7-9a82-60dbac57a3fc" />

4. **GoogleStyle**:
   - GoogleStyle是Google公司制定的Java编码规范，它与Java官方的编码规范有一些区别。例如，GoogleStyle可能要求使用更严格的命名规则、不同的缩进方式和括号放置规则等。GoogleStyle强调代码的一致性和可维护性，有助于团队成员之间的协作。
总的来说，不同的Formatter提供了不同的编码风格和规则，开发人员可以根据项目的需求和团队的编码标准来选择合适的Formatter。通过选择合适的Formatter，可以确保代码的质量和一致性，提高团队的开发效率和维护成本。
   - <img width="884" height="1322" alt="image" src="https://github.com/user-attachments/assets/2add5b97-5c87-4f4c-93f9-28971f68f462" />


## Formatter 配置
Eclipse中的一个 Formatter 配置界面，包含了多种格式化选项。以下是对各个配置项的详细解释：
### Profile name: 
- **Java Conventions [built-in]**: 这是配置文件的名称，表明这是Eclipse内置的Java编码规范配置。
### Filter:
- **Filter**: 过滤器，用于指定哪些文件或文件夹应该被此配置影响。可以使用通配符（* 和 ?）来匹配文件名或路径。
### Indentation:
- **Tab policy**: 设置制表符的使用策略。这里选择了“Mixed”，即混合模式，意味着在某些情况下使用制表符，在其他情况下使用空格。
- **Use spaces to indent wrapped lines**: 是否使用空格来缩进折行的部分。
- **Indentation size**: 缩进的字符数，这里是4个字符。
- **Tab size**: 制表符的大小，这里是8个字符。
- **Text block indentation**: 文本块的缩进方式，默认为“Default for wrapped lines”。
### Indented elements:
- **Declarations within class body**: 类体中的声明是否缩进。
- **Declarations within enum declaration**: 枚举声明中的声明是否缩进。
- **Declarations within enum constants**: 枚举常量中的声明是否缩进。
- **Declarations within annotation declaration**: 注解声明中的声明是否缩进。
- **Declarations within record declarations**: 记录声明中的声明是否缩进。
- **Statements within method/constructor body**: 方法/构造函数体中的语句是否缩进。
- **Statements within blocks**: 块中的语句是否缩进。
- **Statements within 'switch' body**: switch 语句体中的语句是否缩进。
- **Statements within 'case' body**: case 子句中的语句是否缩进。
- **'break' statements**: break 语句是否缩进。
- **Empty lines**: 空行是否保留。
### Align items in columns:
- **Field declarations**: 字段声明是否对齐。
- **Variable declarations**: 变量声明是否对齐。
- **Assignment statements**: 赋值语句是否对齐。
- **Arrows in switch statements/expression**: switch 语句/表达式中的箭头是否对齐。
- **Use spaces for align**: 对齐时是否使用空格。
- **Blank lines separating independent groups**: 分隔独立组的空白行数量。
### Brace positions:
- 大括号的位置设置。
### Parentheses positions:
- 括号的位置设置。
### Whitespace:
- 空白字符的处理设置。
### Blank Lines:
- 空行的处理设置。
### New Lines:
- 新行的处理设置。
### Line Wrapping:
- **Maximum line width**: 最大行宽，这里是120个字符。
- **Default indentation for wrapped lines**: 折行部分的默认缩进，这里是2个字符。
- **Default indentation for array initializers**: 数组初始化器的默认缩进，这里是2个字符。
- **Never join already wrapped lines**: 不连接已经折行的部分。
- **Prefer wrapping outer expressions**: 优先包装外层表达式，保持嵌套表达式在一行上。
### Wrapping settings:
- 包装设置的详细信息。
### Comments:
- 注释的处理设置。
### Off/On Tags:
- 开关标签的处理设置。
通过调整这些配置项，开发人员可以定制代码的格式化规则，以满足特定的编码规范和团队标准。

差异对比：

