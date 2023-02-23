#数据类型

#字符串string
"""
在python可以使用单引号，双引号和三引号括起来。使用\转义特殊字符
python3源码文件默认以utf-8编码，所有字符串都是unicode字符串

paragraph=""" 
"""          此处可写多行

字符串string中的转义字符
    字符串歧义
    my_str="I'm a student"  #换一种写法，不使用转义符
    my_str='I'm a student' #此处因为字符串中有'报错，因此可添加转义符号\，避免错误
    my_str='I\'m a student' #已添加转义符

    path="c:\temp\1/mp3"  #打印会出错
    path="c:\\temp\\1/mp3"  #方法一，增加\转义符
    path=r"c:\temp\1/mp3"   #方法二,添加r不让转义符生效

    类似的转义字符还有很多
    比如 \\  \'  \"  等

字符串的切片（截取与连接）
    str1="abcdefd"
    #正向索引0,1,2,3,4,5,6
    #反向索引-7,-6,-5,-4,-3,-2,-1
    print(len(str1))  #len()函数获取字符串长度
    print(str1[2])  #打印打印第三位、位于2字符
    print(str1[2:5]) #打印从第三位开始(位于2)到第五位(位于4)的字符
    print(str1[2:-1]) #打印位于2开始直到字符串结尾的前一个,-1表示索引值的最后一个
    print(str1[2:len(str1)]) #打印从位于二到结束
    print(str1[2:]) #打印从位于二到结束
    print(str1[:2]) #打印从头到位于2索引值的字符
    print(str1[2:len(str1):2]) #从索引值位于2开始打印到结尾,且每隔一位
    print(str1[-1:-7:-1]) #此处结果为ced  从最后一位开始打印到位于索引值-7但是不包括位于索引值-7，因为-7处是开区间，且倒序打印
    print(str1[-1:-7:-2]) #此处结果为ced  从最后一位开始打印到位于索引值-7但是不包括位于索引值-7，因为-7处是开区间，且每隔一位打印

    字符串的拼接
    str1="a"
    str1+="b"
    print(str1+"c")  #此处打印abc

    str="a"\   
        "b"\ #字符串可以用\实现写多行，解决一行打不完的问题
        "c" 
    print(str)#此处打印abc

字符串的常见操作还有很多
    比如 find()  join()拼接  replace("","",n)替换 等等  
    listvar=["a","b","c"]
    res="*".join(listvar)   #join将某字符串拼接为字符串
    print(res)
    a*b*c

    replace("","",n)替换  第一处为需要替换掉的，第二处为要替换的，n为次数
    lstrip()去掉右侧的空白符  rstrip()左

    字符串操作的判断类型
    isspace()字符串中只包含空白，则返回Ture，否则返回False
    isalpha()字符串至少有一个并且所有字符都是字母则返回True，否则返回False
    islnum()字符串至少有一个并且所有字符都是字母或者数字则返回True，否则返回False
    isdecimal()字符串必须是纯数字
    isdigit() 字符串只包含数字，则返回Ture，否则返回False
    isnumeric()字符串只包括数字字符，则返回Ture，否则返回False
    半角，全角模式
    len()长度
    center()填充字符，原字符居中(默认空格填充)

    字符串操作的编码和解码
    "字符集"就是将不同语言文字用一个二进制的编码对应起来的编码库
    如 unicode utf-8
    python3默认是unicode，16位的编码
    max()返回字符串中的编码最大的字母
    min()返回字符串中的编码最小的字母

    ord()内置函数可以返回汉字或者字母的unicode编码
    chr()内置函数返回编码的汉字或数字

    encode()内置函数可以转换字符集
    str="IT习"
    str_utf8=str.encode("UTF-8")
    str_gbk=str.encode("GBK")
    print(str_utf8)
    print(str_gbk)

    b'IT\xe4\xb9\xa0'
    b'IT\xcf\xb0'

    不同编码储存同一个字符的大小不一样
    乱码就是不同字符集的编码解析不同，底层储存不变，也就是密码本变了
    b表示字节  2字符=2字节 1字节8bit  bit就是0或1
"""

#list列表[]
"""
列表里可放数字、布尔值、字符串""，重复的

列表的创建与元素访问
    列表的创建
        1)直接赋值
        namelist=[]

        2)通过list()方法创建或强制类型转化为列表
        a=list("习啊习")
        print(a)
        ['习', '啊', '习']

        a=list(range(2,-3,-1))  #操作range()函数的方法和字符串的切片一样，（起始位,结束位,间隔位）
        print(a)
        [2, 1, 0, -1, -2]

        3)列表推导式创建列表
        a=[x*2 for x in range(5)]  #此处x为定义值，x*2也就是说x乘以2。后面for...in 表示从range()中拿出指定数字赋值给x
        print(a)
        [0, 2, 4, 6, 8]

    列表的访问
        列表和字符串都属于序列的概念，所以很多方法都是类似的
        列表的切片，可以参考字符串的相关操作

列表的常用操作 for..in   len()  max()  min()  sum()
    列表的循环遍历
    namelist=[1,"love","你"]
    for name in namelist:   #
        print(name)

    其中max() min()是比较编码的大小
    但是字符串与数字无法比较

    sum()对全部为数值型元素的列表求和

常用数据操作 增删改查
增加
    append()追加，尾加
    namelist=[1,"love","你"]
    nameadd=input("请输入",)
    namelist.append(nameadd)
    print("添加后",namelist)

    extend()扩展
        a=[1,2,3]
        b=[4,5,6]
        a.append(b)
        print(a)
        [1, 2, 3, [4, 5, 6]]  #append()是把元素整个添加

        a=[1,2,3]
        b=[4,5,6]
        a.extend(b)
        print(a)
        [1, 2, 3, 4, 5, 6]  #extend()把列表中的元素逐一添加
    
    +操作  #此操作占内存 id()查看
        a=[1,2,3]
        b=[4,5,6]
        res=a+b
        print(res)
        [1, 2, 3, 4, 5, 6]
    
    *操作
        a=[1,2,3]
        b=a*2  #扩大倍数
        print(b)
        [1, 2, 3, 1, 2, 3]

    insert()插入
        a=[1,2,3]
        a.insert(0,0) #此处的括号的第一个位为插入到的索引值，第二位为插入值
        [0, 1, 2, 3]

删除 del  pop()  remove()
    del list[制定列表要删除的索引值]

    pop()删除并弹出某个元素,括号里填索引值进行操作
        a=[1,2,3]
        b=a.pop()  #此处b取得弹出并删除的元素。如括号里不填，默认弹出最后一个元素。
        print(a,b)
        [1, 2] 3
    
    remove()  #直接删除指定内容的元素，但是只删除匹配到的第一个。括号里填内容

修改 
    重新赋值
    a=[1,2,3]
    a[1]=0  #将列表中索引值为1的值更改为0
    print(a)
    [1, 0, 3]

查 
    in和not in
    a=["z","x","q"]   #为什么数字会报错？
    findname=input("请输入查找的内容")
    if findname in a:
        print("yes")
    else:
        print("no")

    index() 查找元素的索引值，并返回对应数据的索引值。括号第一个需要查找的元素，第二个是可填查找的指定区间

    count() 统计某个元素出现了几次

排序和反转
    列表的排序和反转不会影响到列表的地址   id()查看地址
    reverse()反转列表所有元素
    sort()排序 升序  比如数字1234
    sort(reverse()) 降序  

列表的嵌套(二维列表、三维列表)
a=[] 一维列表
a=[[],[],[]] 二维列表 #有三个元素的空列表，每个元素都是一个空列表

运用
二维数据类似表格的储存形式
a=[12,"你"]
b=[13,"我"]
c=[14,"他"]
d=[a,b,c]
print(d)
输出为[[12, '你'], [13, '我'],[14,"他"]]
#[[12, '你'], #[0][0],[0][1]
#[13, '我'],  #[1][0],[1][1]
#[14,"他"]]   #[2][0],[2][1]    #可见二维数据类似表格的储存形式
print(d[0])  #获得第一个元素中的整个列表
print(d[0][0])  #取得第一个元素中列表中的第一个元素。第一个[]是第一层列表，第二个[]是第二层列表

二维列表的最佳访问方式
a=[12,"你"]
b=[13,"我"]
c=[14,"他"]
d=[a,b,c]
for _ in d:                 
    # print(_)
    for i in _:
        print(i,end=",")
    print()                  #空格
12,你,
13,我,
14,他,

题目：3个办公室，有8个老师等待工位分配，编写程序完成随机的分配
查看分配结果
import random
officelist=[[],[],[]]
names=["a","b","c","d","e","f","g","h"]
for name in names :
    num=random.randint(0,2)  #[0,2]的闭区间
    #print(num)
    #print(name,end=",")
    officelist[num].append(name)
print(officelist)

查看分配后的数字和具体的人
i=0
for office in officelist:
    print(f"办公室{i+1}的人数为{len(office)}")
    i+=1
    for name in office:
        print(name,end="\t")
    print()
    print("-"*10)

"""

#浅拷贝和深拷贝  待听

#tuple元组()
"""
应用场景可以是原始数据不允许别人更改，可使用元组保存
tuple与list类似，但是tuple中的元素不能修改  可重复
但是其中可以包含可变对象，比如list
创建一个元组小需要加一个,

tup1=()    #创建一个空元组
tup2=(1,)  #创建一个元组小需要加一个英文逗号,

以下两种形式也是元组  小括号可以省略
tup3=50,5030,3
tup4=2,

增删改查，基本不存在，但也存在 tuple中的元素不能修改
    增（连接）
    在tuple中没有增加这个概念，只有连接
    如果我们需要往tuple中添加什么，可以用两个tuple相加
    tuple1=(1,2,3)
    tuple2=(4,5,6)
    tuple3=tuple1+tuple2

    删(能删除元组对象，而不是元素)
    tuple1=(1,2,3)
    del tuple1

    改(不能改) tuple的可变元素可更改
    但是能修改tuple里边的list对象

    查
    切片也可使用
    计数count()

    tuple()函数可以强制转换为tuple元组

    生成器
    s=(x*2 for x in range(5))
    print()
"""

#dict字典{}
"""
字典是无序的对象集合，使用键-值（key-value）存储，具有极快的查找速度
键key必须是不可变的类型，且同一字典中其是唯一的

info={} #定义一个空字典
info={"name":"习","age":18}  需要注意的是冒号:

访问
info={"name":"习","age":18}
print(info{"name"})  #通过键key访问值value

print(info{"gender"})  #访问一个不存在的值会报错keyerror
print(info.get("gender")) #用get的方法，即使没有找到对应的值，默认也会返回None
print(info.get("gender","m"))  #m为没有找到对应值时的返回自定义默认值

使用列表创建字典 fromkeys
namelist=["我","你","他"]
dic={}.fromkeys(namelist) #以list列表中的元素的内容作为键，创建字典，值默认为none
dic={}.fromkeys(namelist,"帅") #统一默认值为帅
dic={}.fromkeys(namelist,["帅","好看","漂亮"])  #无法逐一设置不同的默认值  因为通过id()看到namelist里的元素底层储存是一个位置

增删改查
    增加
        info={"name":"习","age":18}
        newid=input("请输入新的学号")
        info["id"]=newid
        print(info)

    删除
        del
        info={"name":"习","age":18}
        del info["name"]  #删除指定键后，其value值也会被删除
        print(info)
        del info  #直接删除字典

        clear()  清空元素

        pop()
        info={"name":"习","age":18}
        age=info.pop("age")  #通过键删除值，并返回删除的值
        print(info,gender)
        gender=info.pop("gender","不存在该键")  #返回默认值 不存在该键

        gender=info.popitem() #删除最后一个键值对，返回的是yuanzuleix
        gender=info.popitem() #如果这行代码执行，除去第一行弹出的那个值之外又会弹出一个最后的值

    修改
        直接赋值修改
        info={"name":"习","age":18}
        info["age"]=20
        print(info)

        update()
        info={"name":"习","age":18}
        info.update({"id":1,"age":20})  #指定的键存在就更新数据，指定的键不存在就新增
        #另一种写法info.update(age=20,id=1)  赋值写法
        print(info)

    查
        for in 遍历
        info={"name":"习","age":18}
        for i in info:  #默认或得到的是字典的键key，但是拿不到值
            print(i)

        info={"name":"习","age":18}
        for key in info.keys():      #keys 可以得到所有的键key，可以理解为列表
            print(key)

        info={"name":"习","age":18}
        for value in info.values():   #values 可以得到所有的值value，可以理解为列表
            print(value)

        info={"name":"习","age":18}
        for key,value in info.items():   #items 可以得到所有的键值对，可以理解为元组   forin里的key,value本身就是一个元组
            print(f"key={key},value={value}")


扩展：使用枚举函数enumerate同时拿到“列表”的索引值和元素内容
list=["a","b"]
for i,x in enumerate(list):  #此处的i表示索引值，x表示值
    print(i,x)
"""

#set集合{}
"""
set集合和dict字典类似，也是一组key的集合，但是不能储存value
set是无序的，而且不能储存重复的key，重复元素会自动被过滤
set中只能存放不可变元素
set可以被看成数学意义上的无序和无重复元素的集合，因此两个set可以做数学意义上的交集&并集|差集-等操作
set中可以存放许多数据类型，但是只能存放不可变元素,比如dict字典和list列表都不可以存放在其中，tuple元组可以
set()函数可以强制转换为集合

set集合是“无序的”，但是不等于随机。通过哈希值计算后安哈希值排列

set集合自动去重
set1={1,2,3,3,4}
print(set1)
set1={1,2,3,,4}

增删改查
    增加  
        add  无序增加
        set1={1,2,3,3,4}
        set1.add(5)#此处增加例一个数值5，但是是无序增加
        print(set1)

        update  依次添加到集合中
        set1={1,2,3,3,4}
        set1.update("woai") #依次添加，但是按""中的拆分添加
        print(set1)
        {1, 2, 3, 4, 'o', 'a', 'i', 'w'}

        set1={1,2,3,3,4}
        set2={"aa","bb"}
        set1.update(set2)  #依次添加，但是按""中的
        print(set1)
        {1, 2, 3, 4, 'aa', 'bb'}

    删 clear  remove  pop
    clear清空集合中的元素
    pop随机弹出并删除一个元素
    remove只能通过元素内容来删除

    改 变相删除，先删后增
    其实不存在修改的概念
    remove后add

    查 for in遍历
    in   not in


集合的运算  
    交集&或intersection   并集|或union   差集-difference  异或集又被称为 对差集 ^或symmetric_difference
    子集或超集  <=检查一个集合是否在另一个集合的子集  如果a的元素全部在b中，那么啊就是b的子集，b就是a的超集

    在做集合的运算时，不会影响原来的集合，只是返回一个运算结果
    s1={1,2,3}
    s2={3,4,5}
    result=s1&s2
    print(result)

集合的应用
列表去重
num=[1,2,3,3,4,5]
s=set(num)   #转换为set  但是顺序会被打乱
res=list(s)  #再次转换回来list

冰冻集合 frozenset
冰冻集合一旦创建不能修改，只能进行集合的运算操作
s=frozenset()
"""

#数据类型总结
"""

"""
