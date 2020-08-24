# PySys项目

*这是一个新的画饼项目，至GUI之前，此文档不太可能会更新，请耐心等待。*  
*如果真的很想要看文档请去文件查看。*  
  
没错，这又是一个系统的项目（**注意：这个项目和Pysys项目不同，请注意大小写**），在多次考虑后，我决定先进行设计，然后再开始写代码，我们先来看设计吧。

## 整体设计

整体目录相较于上一版本将会大量更改，将计划采用规范的程序目录，tree如下：

````txt
PySys/
|-- api/                API
|   |-- pysys_api.py    API
|
|-- bin/                可运行文件
|   |-- pysys.py        启动PySys系统
|
|-- core/               PySys系统的核心文件
|   |-- pysys_core.py   核心文件
|
|-- db/                 数据库
|   |-- db.json         生成的数据库
|
|-- lib/                功能
|   |-- dblog.py        数据库和日志的生成
|   |-- psterm.py       PSTerm终端的实现文件
|
|-- log/                日志
|   |-- log.log         生成的日志
|
|-- README.md           README介绍
````

下面来依次分析每一个目录。

### API

这里存放有PySys系统对外的API接口，将大部分有用的函数写入不同分类的文件（*注：现暂未分类*），开发者只需要根据需要调用里面不同的文件即可开发出适用于PySys的程序了。

### Bin

这里存放有PySys系统的可运行文件，包括系统本身、系统救援模式等，这些都是和核心一样重要的文件，如果没有特殊需要请不要更改其中的任何文件。

### Core

这里存放有PySys系统最底层的核心文件，按照功能分类将底层函数写入不同的文件（*注：现暂未分类*），如果没有特殊需要请不要更改里面的任何文件，否则可能导致系统损坏不可用。开发者可以通过邮件发送特殊需求来申请调用核心文件。

### DB(Database)

这里存放有PySys系统生成的数据库文件，其中`db.json`存放系统生成的数据库，其他APP可能会生成类似于`someapp_db.json`的文件。如果没有特殊需要请不要更改里面的任何文件，否则可能导致系统和APP数据损坏不可用。

### Lib

这里存放有PySys系统的功能文件，比如`psterm.py`就是PSTerm终端的文件，这也是和核心文件一样重要的文件，如果没有特殊需要请不要更改其中的任何文件，否则可能导致系统基本交互功能损坏不可用。

### Log

这里存放有PySys系统的日志文件，其中`log.log`存放系统生成的日志，其他APP可能会生成类似于`someapp_log.log`的文件。如果系统没有出现问题可以适当地删除部分日志来节约空间。

### 其他会生成的文件夹

* app/（暂时不可用）：这里存放有PySys系统额外下载安装的APP，以文件夹或`someapp.psapp`打包的形式出现。
* tmp/（暂时不可用）：这里存放有PySys系统联网下载的临时文件，以`tempfile.pstmp`的形式出现。

## 开发顺序与设计

由于这个改版过的Pysys重写的代码量较大，所以不可能一次性写完并提交，这样我们就可以分几个阶段来完成整个系统的开发，具体步骤如下：

1. [x] 完成核心`pysys_core.py`的设计和开发
2. [ ] **完成网页的介绍**
3. [ ] 完成交互终端PSTerm的设计和开发
4. [ ] 完成日志和数据库生成文件的设计和开发
5. [ ] 完成API的设计和开发并进行文档规范
6. [ ] 完善README和文档

**第二步的网页开发与翻译正在进行中，具体请看[我的博客](https://bobby233.github.io)**
