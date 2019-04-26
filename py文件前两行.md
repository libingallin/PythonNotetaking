很多python文件的头两行是：
```python
#!/usr/bin/python
# -*- coding: utg-8 -*-
```

## :pencil: `#!/usr/bin/python`
`#!`的特殊组合称作SheBang，其出现的位置是文本文件的第一行的前面两个字符。Linux类的系统中，发现文本文件出现SheBang时，系统就会去找SheBang后面的内容，尝试加载对应程序去解析此文件。即Linux中运行此Python文件时，系统就会尝试加载/usr/bin/python去解析此Python文件。

综合起来即：对于常见的第一行是`#!/usr/bin/python`的Python的文件在运行时，系统会尝试去找到对应的/usr/bin/python去解析并执行此Python文件。

## :pencil: `# -*- coding: utg-8 -*-`
Python文件编码声明，就是用来指定文件编码的。
根据官网的定义，之所以加上这么一句话，则是因为在python2.1时，想要输入Unicode字符，只能用基于Latin-1的“unicode-escape”的方式输入，这就导致了对于其他非Latin-1的国家和用户想要输入Unicode字符，显得很繁琐和不方便。而我们希望的是根据自己的喜好和需要，以任意编码方式输入字符串，最终允许在Python文件中通过文件开始处的字符串形式去声明自己的Python文件用何种编码。此声明放在注释代码内，且给出了该声明格式的严格定义。
1. 如果没有此文件编码类型声明，则Python默认以ASCII编码去处理。所以，如果Python文件中没有编码声明而文件中又包含非ASCII编码的字符的话，Python解析器解析的Python文件自然就会报错了。

2. 文件编码类型声明必须放在Python文件的第一行或者第二行。换句话，如果把文件编码类型声明放在其他行，则无法被识别。

3. 编码声明所支持的格式有如下三种：
    * 带等号的
     ```python 
     # coding=<encoding name>
     ```
    * 带冒号的
     ```python
     #!/usr/bin/python
     # -*- coding: <encoding name> -*-
     ```
    * vim的配置
     ```python
     #!/usr/bin/python
     # vim: set fileencoding=<encoding name>:
     ```
     > 此种写法专门用于vim
    
4. 声明的格式的语法只要符合正则表达式：

    ```python
    coding[:=]\s*([-\w.])+
    ```

5. 如果你的Python文件本身编码是带BOM的UTF-8，即文件前三个字节是\xef\xbb\xbf，那么即使你没有声明文件编码也自动当做是UTF-8的编码。如果你声明了文件编码则必须是声明了（和你文件编码本身相一致）UTF-8，否则由于声明的编码和实际编码不一致，则自然会报错。
