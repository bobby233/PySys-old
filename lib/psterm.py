# This line includes 79 characters because PEP8 says,"Limit ... 79 characters"

## 欢迎各位用户和开发者基于本终端的代码来开发出自己独特的PySys终端！
# 作者：bobby233<mczsjzsjz@outlook.com>
# 版本：v0.0.1
# 更新时间：2021/3/13
"""更新日志： 0 -> 0.0.1

全部内容

"""

"""PySys用户进入系统后操作的终端

一般情况下，这是用户唯一可以操作PySys的地方，要是没有PSTerm，只可以通过调用内核或者
API的方法来操作整个PySys。由于这是用户而并非开发者操作的工具，所以这个工具必须要做到
极大的人性化和客制化。所以这个工具所提供的操作命令提供如下解决方案：

1. 为了确保用户可以从别的系统(*nix, Windows)的终端顺利地切换到PySys系统的终端，
其中的操作命令和返回结果和Linux相近，例如有'ls''cd'等命令。为何不和Windows相近？你
真的用过Windows的Command Prompt吗？

2. 为了保证PySys默认终端PSTerm的独特性，除了以上的解决方案还提供了PySys风格定制的
命令和返回结果。例如'ls'以单行展示目录和文件，而'ln'以多行的更详细的方式展示。为了
保证人性化和客制化，以上两种解决方案都有很好的兼容性，并且其他PSApp可以随意调用命令，
而不使用API和内核，可以简化开发难度。

在内核文件的第26行和27行注释中，有提到PSApp应用程序的管理是归于PSTerm的，所以本文件
也提供了管理和使用PSApp的方法。但是这只是用户级别的使用和管理，关于系统级别的PSApp的
使用和管理，请到API查看代码。

"""

from ..core import pysys_core