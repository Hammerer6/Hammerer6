#注释方法
"""
单行注释可用#
多行注释用三个单引号，或者是三个双引号
vscode:选中想要缩进的代码块,按“Tab"键缩进,按“Shift + Tab”键表退格。
"""

#小技巧
"""
可在文件夹重点开查看，并点击后缀模式
以此来更改后缀
"""

#变量定义
"""
a=10 #整数
b="张三" #字符串
c=2000.0 #浮点数，小数
"""

#三种基本变量类型：整型，字符串型，浮点型

    #变量的命名
"""
1.任意数据类型
2.必须是大小写英文、数字、下划线的组合，且不能已数字开头
3.不能和python的关键字相同
如何调出python的关键字
    import keyword
    print(keyword.kwlist)
    比如像as  flase  true def  等
例zhang_age=2
"""

#变量的赋值与类型
"""
print(type(变量)) #查看变量类型
int整型   str字符串型   float浮点型

整体赋值
a=b=c=100或a,b,c=100

赋值的底层逻辑：存下赋值值——创建指向已存值的变量（存物并加上号码牌）
"""

#输出与输入
#输出
"""
简单输出print()

格式化输出
格式化
1.%操作符(最原始)
    单个输入
    age=18
    print("我的年龄是%d岁"%age)

    多个输入
    age=18
    country="中国"
    print("我的年龄是%d岁,我的国家是%s"%(age,country))

    常用的格式化符号
    %c 字符   %c通过str()字符串转换来格式化   %d有符号十进制整数  %f浮点实数。。。。。。

2.format函数(py2.6后)
    顺序填充
    str="我的年龄是{},我的名字是{},我的国家是{}".format(18,"赵","中国")
    print(str)

    索引填充
    str="{0},{1},{0}".format("你好","我的")
    print(str)

    关键字填充
    str="姓名：{name},年龄：{age}".format(name="赵",age=18)
    print(str)

    通过设置字典参数,并**展开map几何
    info={"name":"赵","age":18}
    str="姓名:{name},年龄:{age}".format(**info)
    print(str)

    利用列表list的索引设置参数
    list=["我","叫","什么"]
    str="谁：{0[0]},动词：{0[1]},时间：{1}".format(list,2022)
    print(str)
    解释{}里的数字是format的索引,[]里的数字是list列表的索引

    扩展：数据格式化(与数据切割有关)
    print("圆周率:{:.2f}".format(3.1415926))
    输出结果:圆周率3.14
        {}里的:表示对format()里的数据进行操作，
        {}里的.表示小数,
        那么.2就是两位小数,
        f的意思是浮点数,
        :.2f就表示format()里的数字保留两位小数

    print("圆周率:{:+.2f}".format(3.1415926))
    输出结果:圆周率+3.14

    print("{:,}".format(1000000))
    1,000,000

    print("{:.2e}".format(1000000))
    1.00e+06
    e为科学计数

    print("{:.1%}".format(0.38))
    38.0%
    {}里的1表示百分号后几位小数

    数据格式化公式例子
    {:.2f}  保留小数点后俩位
    {:.0f}  不带小数
    {:0>2d} 数字补零,填左边,宽度为2,此处的宽度是指原始数字加上补上的数字之后的整体字符宽度 (这里的0可以是任意字符)
    ^,>,<分别为居中、右对齐、左对齐，其后跟宽度。
    :后带填充的字符

        填充的对齐例子
        str="习啊习"
        print("{:*>8}".format(str))
        *****习啊习

        str="习啊习"
        print("{:*<8}".format(str))
        习啊习*****

        str="习啊习"
        print("{:*^8}".format(str))
        **习啊习***

3.f-Strings(py3.6后) 推荐，速度较快
    基础套式(f起头,操作内容要用{}括起来)
    name="赵"
    age=18
    print(f"你好,我叫{name},我今年{age}了")

        数据格式化在这里也适用
        str="习啊习"
        print(f"{str:*^8}")
        **习啊习***

    任意表达式
    print(f"{2*100}")
    200

    print(f"{'abc'.upper()}")
    abc的用''括着,是因为外边用了双引号。
    此处的.upper()是一个函数，是可以把变量转换成大写的函数

    多行表达式
    teacher="赵老师"
    days=5
    student="小赵"
    message=(f"{'请假条':_^16}\n"
        f"{teacher}你好：\n"
        f"我想请假{days}天,可以吗\n"
        f"您的学生{student}"
    )
    print(message)
    #此处的\n表示换行

    print(f"{{86}}")
    {86}

多个打印与打印结尾
    print("a","b",20)
    a b 20

    print("www","baidu","com",sep=".")
    这里的sep="."的意思是打印的数据每个用.隔开

    print("world",end="\t")
    这里的end=""意思是给打印的数据后添加一个东西
    这里的\t的作用相当于Tab的空格作用

    print("world",end="\n")
    \n为换行
"""

#输入
"""
概念：
input()的小括号里放入的是提示信息,是在获取数据之前给用户的提示
input()获取数据后放入等号右边的变量中
input()函数接受的输入必须是表达式

password=input("请输入密码")
print("你输入的密码是:",password)
请输入密码123
你输入的密码是: 123

a=input("输出：")
print(type(a))
无论input里输入数字123,还是abc,print出来的结果都是<class 'str'>  
【input默认输出的类型都是str字符串】

a=input("输出：")
print(type(a))
b=a+100
print(b)
报错为TypeError: can only concatenate str (not "int") to str
意思是只能够连接str字符串和str字符串,而100是一个int整型

代码更改——【数据类型转换】
    进行字符串的输出
    a=input("输出：")
    print(type(a))
    b=a+str(100)
    print(b)
    此处强行把数字100转化为str字符串了
    如果输入字符“数字是”
    那么输出结果为“数字是100”

    进行数字的计算并输出
    a=input("输出：")
    print(type(a))
    b=int(a)
    print(type(b))
    c=b+100
    print(c)
    函数int()是把数据转换成整型
    如果输入为1
    那么输出结果为
    <class 'str'>
    <class 'int'>
    101
"""
