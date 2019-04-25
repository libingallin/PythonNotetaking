# :memo:文档

## 1 项目文档
API文档适用于项目用户。

+ [ ] 项目根目录下的**README文件**应该为项目的用户和维护者提供一些基本信息，应该是纯文本格式，或者以某种极易阅读的标记语言来编写，如reStructured Text（推荐，因为是目前PypI唯一可以理解的格式）或者MARKDOWN，应该包含几行解释项目或者库的目的、软件主要安装源的URL和一些基本的致谢信息。*该文件是代码阅读者的主要入口。*

+ [ ] **INSTALL文件**对于Python来说不太必要（不过可能有助于遵守GPL这类许可证的要求）。安装步骤通常会简化为一个命令，如`bashpip install module`或者`pip setup.py install`，添加到README文件中。

+ [ ] 应该使用提供**LICESENCE文件**，并且指定软件是基于什么许可证开放使用的。

+ [ ] **TODO文件**或者README中的TODO小节应该列出代码的开发计划。

+ [ ] **CHANGELOG文件**或者README中的CHANGELOG小节应该简要概述项目最近一些版本中代码库的变更点。

## 2 项目发行文档
由项目实际情况而定，项目可能包含如下的部分或全部内容。
+ [ ] **项目入门introduction**应该使用一到两个极简的用例，简要概述产品能够用来做什么。这就是项目的30秒自我称述。

+ [ ] **项目教程tutorial**应该更详细地介绍一些主要用例。读者能够跟着一步一步地搭建一个可以工作的原型。

+ [ ] **API参考reference**，通常从代码中生成，列出所有公共可用的接口、参数和返回值。

+ [ ] **开发者文档Developmenter documentation**是为潜在的贡献者准备的，可以包含项目的代码约定和通用设计策略。

### Sphinx
[Sphinx](http://www.sphinx-doc.org/en/master/)是最流行的Python文档工具。能够将reStructured Text标记语言文本转成多种输出格式，包括HTML、LaTeX（可进一步成PDF）、帮助手册和普通文本。

Sphinx文档可以免费托管在[Read the Docs](https://readthedocs.org/)上，这是一个非常好的平台，可以为你的源码库配置提交钩子（hook），自动重构文档。

### reStructured Text
Sphinx使用的是reStructured Text标记语法，几乎所有的Python文档都是用它来编写的。如果`setuptools.setup()`的`long_description`参数内容以reStructured Text标记语法编写，那么它可以在PyPI上渲染成HTML，如果是其他则以文本形式展示。[reStructured Text Primer](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)和[reStructuredText快速参考](http://docutils.sourceforge.net/docs/user/rst/quickref.html)是一些学习资源。

## 3 代码文档建议
**注释Comments**用来阐明代码，可以使代码更容易理解。Python中，以**#**开始。

**文档字符串docstrings**用来描述模块、类和函数。
```python
def square_and_rooter(x):
    """Return the square root of self times self."""
    pass
```
通常情况下，注释遵循[PEP 8#comments](https://www.python.org/dev/peps/pep-0008/#comments)（Python Style Guide），更多关于字符串文档docstring的信息在[PEP 0257#specification](https://www.python.org/dev/peps/pep-0257/#specification)(The Docstring Conventions Guide)。

### 代码注释
不要使用三个引号来注释代码。

### Docstrings
-[ ] 有些工具使用docstrings来嵌入比注释更多的行为，如单元测试。nice且不会出错。

-[ ] Sphinx会将docstrings解析为reStructured Text并正确地成呈现为HTML。这使得在项目文档中嵌入示例代码段变得非常容易
。
-[ ] [Doctest](https://docs.python.org/3/library/doctest.html)会读取所有嵌入的docstrings——看起来像Python命令行的输入（前缀是>>>），并运行它们，检查命令的输出是否和下一行的文本相匹配。这就允许开发人员将实际例子和函数用法嵌入到源代码中，同时还可以确保代码经过测试和工作。
```python
def my_func(a, b):
    """
    >>> my_func(2, 3)
    6
    >>> my_func('a', 3)
    'aaa'
    """
    return a * b
```

### docstrings v.s. 注释
不可互换。对于函数和类来说，开始的注释是程序员的一个说明/笔记，而docstrings描述的是这个函数/类的操作。

docstrings内置于Python，这意味你可以使用Python强大的内省能力在运行时获取docstings，如:
```python
# This func slows down program execution for some reason.
def square_and_rooter(x):
    """Return the square root of self times self."""
    pass
```

```python
square_and_rooter.__doc__
```
```python
help(square_and_rooter)
```

注释通常用来解释一小段代码是用干什么的，或者算法的具体。而docstrings更多用来向其他人（或6个月后的你自己）解释代码中特殊函数是怎样使用的或类/函数/模块的用途。

在大或者复杂的项目中，给出更多关于函数或函数干什么的或可能会引起什么异常或返回什么或参数的更多描述，这是很棒的做法。docstrings最流行的风格如[NumPy style](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html)
```python
def random_number_generation(arg1, arg2):
    """
    Summary line.
    
    Extended description of function.
    
    Parameters
    ----------
    arg1: int
        Description of arg1
    arg2: str
        Description of arg2
    
    Returns
    -------
    int
        Description of return value
    """
    return 42
```