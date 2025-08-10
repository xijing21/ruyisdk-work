## Comments
### Files
用于新建文件时自动插入的注释模板，通常包括文件头部的版权声明、作者信息、日期等。

Default：
```
/**
 * 
 */
```

Google Style：
```
/**
 * ${file_name}.
 */
```

### Types
用于类、接口、枚举等类型定义的注释模板。

Default：
```
/**
 * ${tags}
 */
```

Google Style：
```
/**
 * ${type_name}.
 *
 * ${tags}
 */
```
### Fields
用于类中字段的注释模板，通常描述字段的用途或含义。

Default：
```
/**
 * 
 */
```

Google Style：
```
/**
 * The ${field_name}.
 */
```
### Constructors
用于构造方法的注释模板，描述构造方法的功能、参数和用途。

Default：
```
/**
 * ${tags}
 */
```

Google Style：
```
/**
 * Constructs a new ${enclosing_type}.
 *
 * ${tags}
 */
```
### Methods
用于普通方法的注释模板，描述方法的功能、参数、返回值和可能的异常。

Default：
```
/**
 * ${tags}
 */
```

Google Style：
```
/**
 * ${enclosing_method}.
 *
 * ${tags}
 */
```
### Overriding methods
用于重写父类方法的注释模板，通常包含对父类方法行为的简要说明。

Default：
```

```

Google Style：
```

```
### Delegate methods
用于委托方法（即调用其他方法实现功能）的注释模板，通常说明被委托的方法及其用途。

Default：
```
/**
 * ${tags}
 * ${see_to_target}
 */
```

Google Style：
```
/**
 * ${enclosing_method}.
 *
 * ${tags}
 * ${see_to_target}
 */
```
### Getters
用于生成 getter 方法的注释模板，通常描述返回值的含义。

Default：
```
/**
 * @return the ${bare_field_name}
 */
```

Google Style：
```
/**
 * Returns the ${bare_field_name}.
 *
 * @return the ${bare_field_name}
 */
```
### Setters
用于生成 setter 方法的注释模板，通常描述参数的含义和设置后的效果。

Default：
```
/**
 * @param ${param} the ${bare_field_name} to set
 */
```

Google Style：
```
/**
 * Sets the ${bare_field_name}.
 *
 * @param ${param} the ${bare_field_name} to set
 */
```
### Modules
用于模块（Java 9 引入的模块系统）的注释模板，描述模块的功能和依赖关系。

Default：
```
/**
 * ${tags}
 */
```

Google Style：
```
/**
 * ${module_name}.
 *
 * ${tags}
 */
```
