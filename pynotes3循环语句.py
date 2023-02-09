#判断语句和循环语句
"""
流程控制
1顺序结构 自上而下
2分支结构 分情况执行
3循环结构 不断重复执行
"""

#python用缩进表达程序的范围，缩进一般使用四个空格

#条件判断
"""
基础
if Ture:
    print("Ture")
    print("Test")
else:
    print("False")

1语法
1)单分支结构: 穷举所有情况，分别执行
light="绿灯"
if light == "绿灯":
    print("绿灯行")
if light = "红灯":
    print("红灯停")
#第一个语句无论成功还是不成功，第二个语句都会执行

2)双分支结构：两种情况相斥。如果、、否则、、
light="绿灯"
if light == "绿灯":
    print("绿灯行")
else:
    print("停")

3)多分支结构：多种相斥情况，如果、、、那么如果、、否则、、
light="绿灯"
if light == "绿灯":
    print("绿灯行")
elif light == "黄灯":
    print("黄灯停一停")
else:
    print("停")
#第一个语句成功，剩下的语句都不会执行。第二个也是同样。 但是如果前两个条件都不成立就会输出最后else
#也就是说只要找到一个条件，剩下的都会停止运行，效率比1)的要高

4)嵌套分支结构，某一情况中，包含了更多的情况。条件嵌套
#例一
light="绿灯"
pedestrian=1
if light == "绿灯":
    if pedestrian == 1:
        print("礼让")
    else:
        print("绿灯行")
else:
    print("停")

#例二
light="绿灯"
pedestrian=1
turn_round=1
if light == "绿灯":
    if pedestrian == 1:
        print("礼让")
    else:
        print("绿灯行")
else:
    if turn_round=1:
        print("可以转头")
    else:
        print("停")
"""

#循环控制语句
"""
1 for循环
    for ... in 循环 可以依次把list列表或tuple元组中的元素迭代出来

    for i in range(5): #range(5)相当于[0,5)  此处的i可以是任意字符，因为这个是在过程中随机的变量
        print(i)
    0,1,2,3,4

    for i in range(0,13,3): #range(start,stop,[step]) 此处的3为步数
        print(i)
    0,3,6,9,12

    字符串也可迭代
    city="dancheng"
    for i in city:
        print(i,end="\t") #end="\t"为打印字符后后带四个空格，end=""为结尾，\t为四个空格

    列表中
    n=["aa","bb","cc"]
    for _ in range(len(n)):
        print(f"位置{_},元素{n[_]}")
    输出为
    位置0,元素aa
    位置1,元素bb
    位置2,元素cc
"""

"""
2 while循环
while...else再条件语句为false时执行else的语句块

while True:      #死循环
    s=input("请输入")
    print("您输入了:",s)

i=0          #起始值   循环加，以达到目的
while i<5:   #判断值
    print(i) #结果值
    i+=1     #叠加值  i=i+1

计算1-100自然数相加的和
total=0          #储存值
n=1
while n <= 100:
    total += n   #使储存值与相加值相联
    n += 1       #相加值
print(f"和得{total}") #打印储存值

求1-100得偶数相加的和
方法一
total=0
n=1
while n <= 100:
    if n%2==0:
        total += n
    n += 1
print(f"和得{total}")
方法二
total=0
n=2
while n <= 100:
    total += n
    n += 2
print(f"和得{total}")

方法三 内置函数 求1-100自然数
print(sum(range(101)))

"""
#break、continue、pass语句
"""
break可以跳出for和while循环
continue可以跳出当前循环，直接进行下一轮循环
pass使空语句，一般做占位语句，不做任何事情

break语句
i=0
while i<10:
    i+=1
    if i==5:
        break  结束整个循环
    print(i)
输出数字一到四

contiue语句
i=0
while i<10:
    i+=1
    if i==5:
        continue  跳过为5的一个循环
    print(i)
输出除数字5以外的数字一到九

for i in range(3):
    cmd = input("请输入")
    if cmd==("exit"):    
        break           #此处根据if的语句退出循环
    print("您输入了",cmd)
else:                    #此处退出，并输出 您输入了三次命令   如果break退出，这个条件就不会输出
    print("您输入了三次命令")

循环的嵌套
要达到以下结果
周一、周二、周三、周四、
第2周：
周一、周二、周三、周四、
第3周：
周一、周二、周三、周四、
第4周：
周一、周二、周三、周四、

方法一
a=["周一","周二","周三","周四"]
for i in range(4):
    print(f"第{i+1}周")
    for j in a:
        print(j,end="、")
    print()       #此处代表换行
#此处的j只在自己的小循环里有效，i则对所有的循环有效
#大循环可以访问小循环，但是小循环不能访问大循环

方法二
a=["周一","周二","周三","周四"]
b=0
n=0
while b<=5:
    b+=n
    n+=1
    print(f"第{n}周：")
    for i in a:
        print(i,end="、")
    print()
"""