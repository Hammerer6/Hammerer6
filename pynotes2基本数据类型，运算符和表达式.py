#基本数据类型
"""
a=11
print(tuple(a))
此处的tuple()函数用来查看数据类型

int整型数据类型
    十进制转化为二进制
    print(bin(100)) #binary
    十进制转化为八进制
    print(0ct(100)) #octonary
    十进制转化为十六进制
    print(hex(100))

    任何数的进制转换为十进制,以二进制为例
    a2=0b01100100
    print(a2)
    print函数默认打印出十进制

float浮点型
    a=2.1e-2
    print(a,type(a))
    此处e-2表示科学计数法十的负二次方,如果此处为e2就表示十的二次方
    浮点型默认保留一位小数

bool布尔类型
    state=True
    print(state+3)
    4
    bool布尔类型在底层逻辑中False就是0，Ture就是0
    False与Ture的开头需要大写
    非零数字就可以是Ture？

complex复数类型
    复数=实数+虚数
    j:如果一个数的平方是-1，那么这个数就是j
    写法一c=3+4j
    写法二c=complex(3,4) 打印出来是3+4j

自动数据转换
不同数据类型进行运算时，结果默认为更高精度类型
精度从低到高：bool<int<float<complex
比如bool+float
print(Ture+3.2)结果为浮点型

强制数据转换
int()
float转换成int
a=2.22
b=int(a)
print(b)
结果为2

布尔型可以任意转换，
什么时候bool类型是false？(10种)
0.0浮点零   复数0j   布尔False  空字符串'' 空元组（）  空列表[]  空集合set()  空字典dict()  空对象None
"""

#运算符和表达式
"""
1算术运算符
    加减乘除+-*/
    但是需要注意计算机无法精准储存，
    比如浮点数运算中0.03不等于0.1*0.3

    **幂运算
    c=2**10 #2的十次方
    print(c)
    1024

    /整数除法
    除法不管什么类型，默认结果为小数

    //取整
    取最接近的整数

    %摸运算
    取相除后的余数

    divmod()函数可以同时取得商和余数
    d,e=divmod(7,2) #此处的进行了两次赋值，分别把d赋值7，把e赋值2
    print(d) #取商
    print(e) #取余数
2比较运算符
    ==等于  !=不等于
    > <  大于小于
    >=大于等于   <=小于等于
    比如a=10 b=20
    (a==b)返回False

3赋值运算符
    =   c=a+b
    +=  c+=a就等于c=c+a
    *=  c*=a就等于c=c*a
    %=  c%=a就等于c=c%a
    以此可参考算术运算符，其实就是c的缩写

4位运算符
    &按位移
    例
    a=60
    b=13
    print(bin(a))
    print(bin(6))
    输出为
    0b111100
    0b110

    a=0b00111100
    b=0b00001101
    print(a&b)
    #
    a  00111100
    b  00001101
    结果00001100
    接就是说把零不一样的位置换掉了
    #
    输出结果为12，也就是00001100的十进制表达方法

    除此之外还有^异或等位算符

5逻辑运算符   优先级顺序为 NOT、AND、OR。
    如果a=10 b=20
    and  布尔“与”   满足所有条件才成立  1and1 =1  1and0 =0  0and1 =0  0and0 =0  只要都为1才可以  第一个条件错误，结果就都错误
    or   布尔“或”   满足一个条件才成立  1or1 =1   1or0 =1   0or1 =1   0or0 =0   只要有1就可以   只要有一个条件正确就都正确
    not  布尔“非”    not(a and b) 返回Flase

    例
    month=5
    if month==3 or month==4 or month==5
        print("春")
    else:
        print("不是春")
    
        短路原则
            and中的短路
            print(10 and 20)
            输出为 20
            检验两个数值，不一致。但是代码已经运行到最后一行，只能输出20

            print(0 and 20)
            输出为0
            代码运行到0时已经满足条件为第一个变量为错误0的条件，所以只能输出为0   只有一个错误程序就不能再运行
            具体条件1and1 =1  1and0 =0  0and1 =0  0and0 =0

            or中的短路
            print(0 or 20)
            输出为20
            因为0为错误，但是程序还能运行，可以输出，并输出为20
        
        优先级
        not>and>or
        print(1>2 or 4>3 and not 6<5)
              False or Ture and not Flase #not先组合并运算
              False or Ture               #然后and再组合运算
              True                        #最后or再组合运算
        所以输出结果为True
        print(1>2) or (4>3 and (not 6<5)))

6成员运算符
    如果a=10 b=20
    in 如果在指定序列中找到值返回Ture，没有则返回False布尔值
    not in  如果在指定序列中没有找到值返回Ture，没有则返回False布尔值

    str="我是习啊习"
    print("习" in str)
    True

    list=[1,2,3]  #list列表
    tuple=(6,7,8) #tuple元组
    dict={"我","你","name3"}  #dict字典
    等都可以使用成员运算符 in ，not in
 
 7身份运算法
    is     判断两个标识符是不是引自一个对象
    is not 判断两个标识符是不是引自一个不同对象

    a=10000
    b=10000
    print(a == b)
    print(a is b)
    True
    True

    print(a,id(a))
    print(b,id(b))
    输出的id结果一样

    python的整数缓存
    1)交互模式下 [-5,256] 超出这个数就会随机分配内存地址，所以再cmd模式下的id会有所不同
    2)pycharm或者文件中无穷  所以id结果相同

    id()函数返回对象的唯一标识符，标识符是一个整数
        cpython中的id()函数用于获取对象的内存地址

运算符的优先级
算术运算符>位运算符>比较运算符>身份运算符>成员运算符>逻辑运算符  最后是赋值语句
"""
