#函数
"""
将具有独立功能的代码块组织为一个小模块，这就是函数
函数的定义
def 函数名(形式参数):
    函数体即功能性代码
    return 返回值
函数的调用
变量名 = 函数名(实际参数)  变量名为输出结果

函数的定义
def printinfo():   #此处定义这个函数名为printinfo,其后的小括号是为了传递参数，此处为不带参数的函数，小括号无意义
    print("-------")
    print("人生苦短")

函数的调用
printinfo()

带参数的函数
def num2add(a,b):  #此处的a,b为形式参数
    c=a+b
    print(c)
调用
num2add(1,2)   #此处的1，2为实际参数

def num2add(a,b):
    return a+b           #return 为结束此函数，后面的代码就不执行了
result = num2add(1,2)   #result承载计算结果
print(result)

函数(调用)的嵌套
def num2add(a,b):
    return a+b
def num3add(a,b,c):
    sum=num2add(num2add(a,b),c)
    return print(sum)
调用
num3add(1,2,3)
6

作业
根据用户输入的数字，打印相应的数量的线条
def line():
    return print("-")
def numline(num):
    i=0
    while i<num:
        line()
        i+=1

numline(3)
"""

#函数的进阶
"""
def func():  #函数的命名和变量名规则相同，见名知意
    pass  #此处的pass是空语句，占位作用

函数名也可以作为变量进行赋值、传递、储存
赋值与传递
def fuc():
    print("q")
res=fuc()  #赋值给res变量
res()       #res变量可以作为函数运行，fuc的函数功能传递给了res函数

储存与传递
def func1():
    print("q")
def func2():
    print("q")
def func3():
    print("q")
myfuns=[func1,func2,func3] #此处列表可储存函数
for f in myfuncs:    #每一个函数拿出来进行运行
    f()

函数参数
1)标准参数
    （定义时）形式参数
    标准参数：位置参数、默认参数

    def printinfo(name,age=18):  #此处age被赋值默认值为18  但是有默认值的对象不能放在无默认值的前面
        print(f"名字{name},年龄{age}")
    printinfo(我,20)     #此处按照参数的位置进行赋值

    指定参数赋值
    def printinfo(name,age=18):  
        print(f"名字{name},年龄{age}")
    printinfo(age=20)   #此处根据age参数名字进行指定赋值

2)可变（个数）参数
    *与**的打包
        可变参数：*  将多个参数储存为元组对象
        def printinfo(name,age,*args):    #此处的args可以命名为任意名字，只是约定习俗为args 
            print(f"名字{name},年龄{age}")
            print("电影评分从低到高",args)  输出调用时不用加*
        printinfo("我",18,9.9,5.6)
        输出结果为
        名字我,年龄18
        电影评分从低到高 (9.9, 5.6)         #args为元组(9.9, 5.6)

        关键字参数：** 将多个参数储存为字典对象
        def printinfo(name,age,**kwargs):     
            print(f"名字{name},年龄{age}")
            print("附加信息",kwargs)
        printinfo("我",18,学历="博士",出生地="河南")  #此处应对kwargs输入为键值对
        输出结果为
        名字我,年龄18
        附加信息 {'学历': '博士', '出生地': '河南'}

    *与**的解包
        *将传进来的字符串、元组、列表、集合转化为多个标准参数
        def printinfo(name,age,*args):     
            print(f"名字{name},年龄{age}")
            print("电影评分从低到高",args)
        list=[9.9,5.6]
        或
        tuple=(9.9,5.6)
        或
        set={9.9,5.6}
        printinfo("我",18,*list)  #此处的*把list里的数据解析了出来,如果此处不加*,数据就会变成([])的形式
        输出结果
        名字我,年龄18
        电影评分从低到高 (9.9, 5.6)

        **将传进来的字典，转化为多个关键字参数
        def printinfo(name,age,**kwargs):     
            print(f"名字{name},年龄{age}")
            print("附加信息",kwargs)
        info={"学历":"博士","出生地":"河南"}
        printinfo("我",18)
        输出结果
        名字我,年龄18
        附加信息 {'学历': '博士', '出生地': '河南'}


函数调用时的顺序
（调用时）实际参数：位置参数、关键字参数    # 关键字参数之后不能再使用位置参数，只能使用关键字参数
顺序 args、*args、**kwargs

3)命名关键字参数
*号后面的参数，只能用命名关键字参数调用赋值
def test1 (a,b,c,*,name,age):
    print(f"{a},{b},{c},{name},{age}")
test1(1,2,3,name="wo",age=22)       *号后面的参数，只能用命名关键字参数调用赋值

返回值
可以返回全部数据类型
def test():
    pass
    return 2
res=test()
print(res)
2

def test(a,b):
    add=a+b
    chu=a//b
    return add,chu
ad,ch=test(5,1)     #此处用ad和ch分别接受return的值
print(f"加{ad},除{ch}")
"""

#全局变量和局部变量
"""
局部变量 函数内部定义的变量
def test1():
    a=100       #此处的a就为局部变量
    print(a)

全局变量 再文件内有效，能在多个函数中使用的变量
a=100       #定义全局变量
def test1():
    print(a)

全局变量和局部变量相同名字
a=100 
def test1():
    a=200       #优先运行局部变量
    print(a)
运行后得到200

在函数中修改全局变量
a=100 
def test1():
    global a    #在函数中声明全局变量的关键字 global
    a=200       
    print(a)
执行后200

可以通过local()打印局部变量，通过global()打印全局变量
a=100
def test1():
    a=200
    print(locals())
    print(globals())
print(locals())           #此处需要注意，local会根据它自己所处的位置打印函数，如果它位于函数内部就会打印局部变量，如果位于外部就会打印全局变量
print(globals())

形式参数就是当前函数的局部变量？？？

"""

#递归函数 （自己调用自己的函数）
"""
问题：打印从100到1的整数
for in 循环
    for i in range(100,0,-1):
        print(i)

递归迭代
    def printnum(n):
        print(n)
        printnum(n-1) #此处printnum函数调用自己，以此达到循环的作用
    printnum(100)
    这个函数运行只会报错，因为没有边界判断

    进一步改进函数
    def printnum(n):
        print(n)     #执行运算
        if n==1:    #使用if循环增加边界判断
            return  #返回数组或者结束函数
        printnum(n-1)  #调用自身函数
    printnum(100)

递归函数的写法
    1）编写函数体（功能）
    2）确定结束条件和返回值
    3）调用函数本身，修改参数，达到循环的目的

阶乘
def fun(n):
    if n <=1:
        return 1
    return fun(n-1)*n
print(fun(5))
"""