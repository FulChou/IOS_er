# Pylance 代码高亮修改颜色

Pylance 是vscode 里面一个非常好用的python插件。Pylance为Python 3提供了一些很棒的功能，包括：

- 字串
- 签名帮助，带有类型信息
- 参数建议
- 代码补全
- 自动导入（以及添加和删除导入代码操作）
- 输入代码的时候报告代码错误和警告（诊断）
- 代码大纲
- 代码导航
- 类型检查模式
- 本地多个工作区支持
- IntelliCode 兼容性
- Jupyter Notebooks 兼容性
- 语法高亮

## 语法高亮

Visual Studio Code使用TextMate语法作为主要的标记引擎。 TextMate语法作为输入处理单个文件，并根据以正则表达式表示的词汇规则将其分解。

语义标记化允许语言服务器基于语言服务器有关如何在项目上下文中解析符号的知识来提供其他令牌信息。 主题可以选择使用语义标记来改善和完善语法中的语法突出显示。 编辑器将语义标记中的突出显示应用于语法中的突出显示。

这是一个语义突出显示可以添加的示例：

没有语法高亮:

![ semantic highlighting disabled ](https://static01.imgkr.com/temp/38ddc5418e0e4bc7b48f0946ab7fe9f8.png)

语法高亮:

![ semantic highlighting enabled ](https://static01.imgkr.com/temp/611f8bbd0fcd44b38b7e9cca0d510de6.png)

## 需求！：

Pylance 默认的变量为红色，太多红色看久了对眼睛不好的同时，也让你有一个全是bug的感觉！我们可以通过将Pylance语义标记类型和修饰符与所需颜色相关联，在settings.json中自定义语义颜色。

- 类型
  - class, enum
  - parameter, variable, property, enumMember
  - function, member
  - module
  - intrinsic
  - magicFunction (dunder methods)
  - selfParameter, clsParameter
- 修饰符
  - declaration
  - readonly, static, abstract
  - async
  - typeHint, typeHintComment
  - decorator
  - builtin

范围检查器工具使您可以探索源文件中存在哪些语义标记以及它们匹配的主题规则。

在settings.json中定制语义颜色的示例：

```
{
    "editor.semanticTokenColorCustomizations": {
        "[One Dark Pro]": { // Apply to this theme only
            "enabled": true,
            "rules": {
                "magicFunction:python": "#ee0000",
                "function.declaration:python": "#990000",
                "*.decorator:python": "#0000dd",
                "*.typeHint:python": "#5500aa",
                "*.typeHintComment:python": "#aaaaaa",
                "variable": "#61b15a", // 强推这个绿色！
                // 左边类型：右边定义的颜色
            }
        }
    }
}
```

:fire:推荐一个选择颜色的网站： https://colorhunt.co/