# This line includes 79 characters because PEP8 says,"Limit ... 79 characters"

## 注意：此文件禁止除bobby233以外的用户或开发者复制、更改或调用代码！
# 作者：bobby233<mczsjzsjz@outlook.com>
# 版本：v0.0.1
# 更新时间：2020/8/21
"""更新日志： 0 -> 0.0.1

全部内容

"""

"""PySys系统运行的核心

这个文件是PySys系统的核心（重要的事情多说几遍），所以如果你不是很懂Python的话，千万
不要轻易修改和删除这个文件；如果你很懂Python……那也不要随意修改和调用，这里的代码并不是
最好的解决方法，而且函数和类的关联性都非常强，如果随意修改可能也会导致数据的丢失，
还有，请看第三行。所以这个文件除了PySys创始人本人以外，其他人一律不允许调用和复制。

在这个文件中，会分为几个模块进行代码开发：
1. 文件系统及目录浏览
2. 时间操作
3. 网络操作

到这里就有人要问了：“为什么没有APP（应用程序）操作?”
这个问题我也考虑过很久，到最后我得出的结论是，核心文件不需要放APP操作。因为APP操作
本质上是在终端完成的，不属于核心的操作，归入PSTerm管辖。

整体设计就是这样了，如果你对这个文档有意见或者建议的话，请给我发邮件，我的邮箱是：
mczsjzsjz@outlook.com，感谢支持！

PySys本体不提供中文的语言支持，和VSCode一样，如果你需要中文的支持的话，可以前往
PySys的GitHub仓库(https://github.com/bobby233/pysys)或我的个人博客
(https://bobby233.github.io)按照上方的教程进行安装和配置。

"""

class FileSys:
    """关于文件和目录的所有操作

    这里有例如cd, touch, mkdir这样的命令支持，分为两个模块进行函数开发和维护：
    1. 目录操作
    2. 文件操作

    除了函数，当然还有常数，这里的常数就只有FS（文件系统）了，PySys使用我自己
    开发的一款文件系统——PSFSb(PySys FileSystem base)，这是一款基础的FS，提供
    简单易懂的目录格式，与任何FS都不同，拥有管理高效、目录少等优点，但是由于这个FS
    是我一人研究出的基础FS，所以有很多不足，希望大家能够提供建议。常数的位置放在
    每一个类的开头，后面的亦然。

    """

    # 常数：PSFSb
    PSFSB = {
        "/": {
            "bin/": {},
            "psu/": {}, # TODO 添加多用户 短期内（9月前）不可能完成
            "tmp/": {}
        },
        "R/": {
            "back/": {},
            "bin/": {}
        }
    }
    absd = "/"

    # 函数：目录操作
    def init_psfsb(self, **args):
        """初始化PSFSb并写入文件，args内先是bin/，后是psu/"""

        print("Getting temp...", end='')
        _ipsfsb = self.PSFSB    # 写入模板
        print("\tDone.")

        # 是否有args
        print("Other temp?", end='')
        if args:
            print("\tYes.\nAdding temp...", end='')
            _ipsfsb["/"]["bin/"] = args["bin/"]
            _ipsfsb["/"]["psu/"] = args["psu/"]
            print("\tDone.")
        else:
            print("\tNo.")
        
        # 写入文件
        print("Writing to file(disk.psfsb)...", end='')
        with open("disk.psfsb", "w") as d:
            from json import dump
            dump(_ipsfsb, d)
        print("\tDone.")
    
    def get_disk(self, file="disk.psfsb") -> bool:
        """获取DISK硬盘，可以自定义文件名"""

        # 是否有硬盘文件
        try:
            with open(file) as f:
                from json import load
                self.DISK = load(f)
                return True
        except FileNotFoundError:
            return False
    
    def sync_disk(self, file="disk.psfsb", backup=False):
        """[备份R/back/]并同步磁盘"""

        if backup:
            self.DISK["R"]["back"] = self.DISK["/"]
        else:
            ...

        with open(file, "w") as f:
            from json import dump
            dump(self.DISK, f)
    
    def change_abs(self, nabs: str, spec: bool=False) -> bool:
        """更改当前的绝对路径"""

        # 是否有那个路径
        try:
            n = nabs.split('|')
            _target = ''
            for i in range(len(n)):
                _target += '["' + n[i] + '"]'
            exec("_t = self.DISK" + _target)
            self.absd = nabs
            return _target
        except KeyError:
            if spec:
                return _target
            else:
                return False

    def change_dir(self, ndir: str) -> bool:
        """更改当前的相对路径"""

        # 检测特殊路径
        if "../" in ndir:
            self.absd = self.absd.split('|')[:-2]
            if self.absd:
                return True
            else:
                self.absd = "/"
                return False
        else:
            # 是否有那个路径
            try:
                self.change_abs(self.absd + ndir)
                return True
            except KeyError:
                return False
    
    def remove_abs(self, rabs: str, spec: bool=False) -> bool:
        """删除指定的绝对路径"""

        # 做好原先的路径备份
        _origin = self.absd
        # 是否有那个路径
        try:
            exec("del self.DISK" + self.change_abs(rabs, spec))
            self.change_abs(_origin)
            return True
        except KeyError:
            return False
    
    def remove_dir(self, rdir: str) -> bool:
        """删除指定的相对路径"""

        # 不允许出现特殊../
        if "../" in rdir:
            return False
        else:
            try:
                self.remove_abs(self.absd + rdir)
                return True
            except KeyError:
                return False
    
    def make_dir(self, mdir: str):
        """新建目录（不允许绝对路径）"""

        # 做好原先的路径备份
        _origin = self.absd
        # 直接创建
        exec("self.DISK" + self.change_abs(self.absd+mdir, True) + "= {}")
    
    # 函数：文件操作
    def make_file(self, mf: str):
        """新建文件（不允许绝对路径）"""

        _target = list(self.change_abs(self.absd + '|' + mf + '/', True))
        del _target[-3]
        _target = ''.join(_target)
        exec("self.DISK" + _target + '= "FILEMARK::KRAMELIF"')
    
    def ramove_file(self, rf: str):
        """删除文件（不允许绝对路径）"""

        # 实际上就是remove_abs，只不过这样可以更加人性化
        self.remove_abs(self.absd + '|' + rf, True)

class Time:
    """关于时间的操作

    这里不但有直接获取时间的基本操作，而且有时区换算、日期计算和计时等高级操作。

    时间的操作涉及到单位，这里全部使用SI的国际标准单位——秒(s)，这里的所有操作
    基本上没有任何技术的难度，所以介绍更少。

    """

    def get_time(self, tformat="PSDTF"):
        """获取本地时间，可以更换格式，这里推荐使用PSDTF(PySys Default Time Format)
        来获取时间，如果你不想要这种格式，可以更换POSIX、CTIME和WIN（Windows
        默认格式）的格式。"""

        # 是否支持格式
        if tformat in ("PSDTF", "POSIX", "CTIME", "WIN"):
            from time import time, ctime
            from datetime import date
            # 各种格式
            if tformat == "PSDTF":
                # time, yyyy-mm-dd day, POSIX
                _ct = ctime()
                return [_ct.split()[3],
                        date.today().isoformat(), _ct.split()[0],
                        time()]
            elif tformat == "POSIX":
                return time()
            elif tformat == "CTIME":
                return ctime()
            else:
                _dt = date.today()
                return [ctime().split()[3],
                        '/'.join(_dt.year, _dt.month, _dt.day)]
        else:
            return False
    
    def get_cal(self, year: int, month: int) -> str:
        """获取日历"""

        from calendar import month
        return month(year, month)
    
    def set_tz(self, tz: int=8):
        """设置时区，保存在db.json"""

        # 是否有db.json
        try:
            _db = open("db/db.json")
        except FileNotFoundError:
            db = {"timezone": tz}
            with open("db/db.json", "w") as d:
                from json import dump
                dump(db, d)
        else:
            from json import load, dump
            db = load(_db)
            db["timezone"] = tz
            dump(db, _db)
            _db.close()
    
    def get_tz(self) -> int:
        """获取时区，返回整数timedelta"""

        # 是否有db.json
        try:
            _db = open("db/db.json")
        except FileNotFoundError:
            return 8
        else:
            from json import load
            return load(_db)["timezone"]
            _db.close()
    
    def get_utc(self) -> str:
        """获取UTC时间，返回ISO格式"""

        from datetime import datetime
        return datetime.utcnow().isoformat()
    
    def get_day(self, isodate: str) -> int:
        """获取指定日期的星期（ISO格式），需要ISO格式的日期，即PSDTF格式的日期"""

        from datetime import datetime
        return datetime.fromisoformat(isodate).isoweekday()
    
    def get_diff(self, isodateone: str, isodatetwo: str) -> int:
        """获取两个日期之间的间隔天，需要ISO/PSDTF格式的日期"""

        from datetime import datetime
        return (datetime.fromisoformat(isodateone) - \
                datetime.fromisoformat(isodatetwo)).days

class Network:
    """所有关于网络的操作，没有文档，代码都是以前写的，和其他代码风格不同
    主要是没有经过测试，不保证稳定性"""

    network = False

    import urllib.request

    def check_network(self, url="https://www.baidu.com"):
        """通过连接一个网站来确定是否有到指定网站网络；
        需要网站链接"""
        print("Connecting to", url + "...")
        try:
            _net_checker = urllib.request.urlopen(url)
        except urllib.request.HTTPError:
            print("Connect failed")
        else:
            print("Connect succeed")
            self.network = True

    def get_code(self, url="https://www.baidu.com"):
        """获取一个网站的源码；
        需要网站链接"""
        if self.network:
            _opener = urllib.request.urlopen(url)
            _code = _opener.readlines()
            print("These are the code:")
            print("=====CODE START HERE=====")
            for cd in _code:
                print(str(cd, 'utf-8'), end="")
            print("\n=====CODE END HERE=====")
        else:
            check_network(url)
            if self.network:
                _opener = urllib.request.urlopen(url)
                _code = _opener.readlines()
                print("These are the code:")
                print("=====CODE START HERE=====")
                for cd in _code:
                    print(str(cd, 'utf-8'), end="")
                print("\n=====CODE END HERE=====")

    def download_as_file(self, url, filename):
        """将网站上面的所有代码下载至指定的文件；
        需要指定域名和文件名"""
        if self.network:
            print("Downloading page on", url, "to", filename)
            _opener = urllib.request.urlopen(url)
            _code = _opener.read().decode()
            with open(filename, "w") as f:
                f.write(_code)
            print("Download succeed")
        else:
            check_network(url)
            if self.network:
                print("Downloading page on", url, "to", filename)
                _opener = urllib.request.urlopen(url)
                _code = _opener.read().decode()
                with open(filename, "w", newline="") as f:
                    f.write(_code)
                print("Download succeed")