#模块与包
"""
包 -- 文件夹
模块-- 文件
函数或类--内容

模块的导入
    import math #用import导入模块   ctrl加鼠标右键可以打开模块的文件中去
    math.pi     #用  模块名.函数名  的形式调用模块的某一函数

导入自己定义的模块
    建立一个py文件比如module1.py   比如此函数中有个函数为add
    在另外一个程序代码中只需import module1
    调用模块中的函数  module1.add


模块的运行方式
    脚本模式    自身模块开发时，作为独立程序由计时器直接运行
        __name__的内容为__main__
        需加入以下判断语句
        if __name__=='__main__':  #该代码就是为了自己方便测试自己的代码，还有就是当别人导入模块时不会错误引入不必要的代码 
                                #填了这个代码之后，这之后的代码只在脚本模式中运行
    模块模式    被其他模块导入，为其他模块提供资源（变量、函数、类的定义）
        __name__的内容为模块名
        import 模块名  #直接导入

多次执行import时，一个模块只会被导入一次


模块搜索路径
内置模块——模块所在目录——环境变量 PYTHONPATH（默认包含python的安装路径） ——python安装路径下的lib文件夹——lib下的site-packages文件夹（即第三方模块）——sys.path.append()的追加目录

搜索指定文件的路径 os模块
    import os
    print(__file__)         #获取整个路径
    print(os.path.dirname(__file__))  #获取指定文件夹所在的目录（文件夹）
    #不能使用字符串截取，因为不同操作系统的路径表示不同


其他导入模块的方式
1）from..import..  从模块中引入指定的函数
from module1 import addfuc
print(addfuc(2,3))

2）from..import 从模块中引入指定的多个函数
from module1 import addfuc,divid   #引入时用逗号隔开即可
print(addfuc(2,3))

3）from..import*   从模块中引入全部函数


import与from..import..的区别
    import 需要模块名.函数名  比如module.addfuc()  且不会出现变量的重名问题
    import module1  
    def addfuc():  #该addfuc函数可运行
        pass

    from..import.. 会出现重名，但是可以使用as别名的方法避免
    from module1 import add as addfuc1   #此处已经将add更改为addfuc1函数
    import module1 
    print(addfuc1(1,2)) 
    def addfuc():  #该addfuc函数可运行
        pass
    
    其次as也可以简化模块名，简化书写
    import module1 as m1  #将模块module1简化为m1
    print(m1.addfuc(1,2))
"""

#包  
"""
包就是一个文件夹 package
生成包时会生成一个叫__init__.py 的文件，这个文件为包的标识，不能删除

应用“包”时,必须使用全名
比如import project.package.module1
    print(project.package.module1.addfuc)  #此处为调用函数addfuc,并使用全名调用
或者from project.package import module1  
    print(module1.addfuc)                   #此处调用可不写全名
或者直接引入函数from project.package import module1.addfuc
               print(addfuc)

这样引入较为麻烦，可以用__init__.py文件先引用
比如在__init__.py写入import project.package.module1
那么在其他文件代码中直接就可以使用
import project.package
project.package.module1.addfuc(12,2)  调用addfuc

可以在module1中用__all__=["变量1","变量2"]指定开放几个变量
也就是说，这几个变量能被其他文件访问到


包内模块导入？？？
绝对导入
import project.package.module1  父层导入包

相对导入  用.或..   在当前目录下的引用，在执行相对导入之前，父模块必须显式的绝对导入
from.module1 import* 

from ..package.module1 import*  此处用..调用父层的包
"""

"""
cll就是命令行界面
gui就是图形用户界面
"""