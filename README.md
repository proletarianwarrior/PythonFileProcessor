## PythonFileProcessor使用说明

作者：能动B2104 杨牧天

## class PythonFileProcessor(source_folder: str)

> **source_folder**: 源文件夹路径

### def statistic_line_num(self, include_comments: bool = True, correct_error: bool = False, timeout: int = 5, **args):

> **include_comments**: 在计算代码行数时是否计算注释行，默认为True
>
> **correct_error**: 是否检验代码是否合理，”不合理“分为两种情况，第一种为代码有错误，第二种为代码运行时间超过规定时间，默认为False
>
> **timeout**: 当correct_error设置为True时有意义，表示代码运行的规定时间，默认为5，单位为秒

**\*\*args**

> **target_folder**: 目标文件夹路径，目标文件夹即为储存py文件的文件夹，默认为程序当前路径下名为“作业”的文件夹
>
> **new_folder**: 是否新建文件夹。如果是，则根据target_folder新建文件夹，如果不是，则需目标路径存在，默认为True
>
> **deep_search**: 是否进行深度搜索，如为True则搜索该文件夹包括其子文件夹下所有文件，如为False则只搜索目标文件夹下文件，默认为False

## 代码示例

文件结构：

```shell
我的作业:.
│  main.py
│  text.py
│
└─文件
        file1.py
        file2.py
        file3.py
```



### 示例1

> 所有文件均无错误

输入：

```python
with PythonFileProcessor("我的作业") as py_processor:
    num = py_processor.statistic_line_num(correct_error=True, deep_search=True)
    print(f"代码总数为：{num}")
```

输出：

```shell
欢迎使用Python作业处理器！

已成功将文件 我的作业\main.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功将文件 我的作业\text.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功将文件 我的作业\文件\file1.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功将文件 我的作业\文件\file2.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功将文件 我的作业\文件\file3.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功更新工作目录 C:\Users\DanYang\PycharmProjects\Dan\test\作业

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file1.py 代码检测
文件预览：
# -*- coding: utf-8 -*- # @Time : 2023/7/4 [...]
代码输出：
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file1.py 检测通过！

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file2.py 代码检测
文件预览：
# -*- coding: utf-8 -*- # @Time : 2023/7/4 [...]
代码输出：
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file2.py 检测通过！

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file3.py 代码检测
文件预览：
# -*- coding: utf-8 -*- # @Time : 2023/7/4 [...]
代码输出：
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file3.py 检测通过！

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\main.py 代码检测
文件预览：
import math print(math.asin(0.5))
代码输出：
0.5235987755982989
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\main.py 检测通过！

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\text.py 代码检测
文件预览：
import time print(time.time())
代码输出：
1688492897.070046
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\text.py 检测通过！

代码总数为：19
```

### 示例2

> main.py文件中出现sqrt(-1)错误

输入：

```python
with PythonFileProcessor("我的作业") as py_processor:
    num = py_processor.statistic_line_num(correct_error=True, deep_search=True)
    print(f"代码总数为：{num}")
```

输出：

```shell
欢迎使用Python作业处理器！

已成功将文件 我的作业\main.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功将文件 我的作业\text.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功将文件 我的作业\文件\file1.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功将文件 我的作业\文件\file2.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功将文件 我的作业\文件\file3.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功更新工作目录 C:\Users\DanYang\PycharmProjects\Dan\test\作业

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file1.py 代码检测
文件预览：
# -*- coding: utf-8 -*- # @Time : 2023/7/4 [...]
代码输出：
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file1.py 检测通过！

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file2.py 代码检测
文件预览：
# -*- coding: utf-8 -*- # @Time : 2023/7/4 [...]
代码输出：
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file2.py 检测通过！

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file3.py 代码检测
文件预览：
# -*- coding: utf-8 -*- # @Time : 2023/7/4 [...]
代码输出：
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file3.py 检测通过！

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\main.py 代码检测
文件预览：
import math print(math.sqrt(-1))
代码输出：
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\main.py 无法运行!

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\text.py 代码检测
文件预览：
import time print(time.time())
代码输出：
1688493035.7109165
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\text.py 检测通过！

代码总数为：17
```

### 示例3

> main.py文件中出现sqrt(-1)错误, text.py中出现超时错误

输入：

```python
with PythonFileProcessor("我的作业") as py_processor:
    num = py_processor.statistic_line_num(correct_error=True, deep_search=True)
    print(f"代码总数为：{num}")
```

输出：

```shell
欢迎使用Python作业处理器！

已成功将文件 我的作业\main.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功将文件 我的作业\text.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功将文件 我的作业\文件\file1.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功将文件 我的作业\文件\file2.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功将文件 我的作业\文件\file3.py 
移动到文件夹 C:\Users\DanYang\PycharmProjects\Dan\test\作业

已成功更新工作目录 C:\Users\DanYang\PycharmProjects\Dan\test\作业

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file1.py 代码检测
文件预览：
# -*- coding: utf-8 -*- # @Time : 2023/7/4 [...]
代码输出：
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file1.py 检测通过！

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file2.py 代码检测
文件预览：
# -*- coding: utf-8 -*- # @Time : 2023/7/4 [...]
代码输出：
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file2.py 检测通过！

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file3.py 代码检测
文件预览：
# -*- coding: utf-8 -*- # @Time : 2023/7/4 [...]
代码输出：
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\file3.py 检测通过！

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\main.py 代码检测
文件预览：
import math print(math.sqrt(-1))
代码输出：
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\main.py 无法运行!

开始执行文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\text.py 代码检测
文件预览：
import time print(time.sleep(10))
代码输出：
文件 C:\Users\DanYang\PycharmProjects\Dan\test\作业\text.py 运行超时！

代码总数为：15
```

