# age=18
# country="中国"
# print("我的年龄是%d岁,我的国家是%s"%(age,country))

# str="我的年龄是{},我的名字是{},我的国家是{}".format(18,"赵","中国")
# print(str)

# str="{0},{1},{0}".format("你好","我的")
# print(str)

# str="姓名：{name},年龄：{age}".format(name="赵",age=18)
# print(str)

# info={"name":"赵","age":18}
# str="姓名:{name},年龄:{age}".format(**info)
# print(str)

# list=["我","叫","什么"]
# str="谁：{0[0]},动词：{0[1]},时间：{1}".format(list,2022)
# print(str)

# print(":{:,}".format(1000000))

# print(":{:.2e}".format(1000000))
# print("{:.2%}".format(0.38))

# str="习啊习"
# print("{:*^8}".format(str))

# name="赵"
# age=18
# print(f"你好,我叫{name},我今年{age}了")

# str="习啊习"
# print(f"{str:*^8}")

# print(f"{'abc'.upper()}")

# teacher="赵老师"
# days=5
# student="小赵"
# message=(f"{'请假条':_^16}\n"
#     f"{teacher}你好：\n"
#     f"我想请假{days}天,可以吗\n"
#     f"您的学生{student}"
# )
# print(message)

# print("www","baidu","com",sep=".")

# password=input("请输入密码")
# print("你输入的密码是:",password)

# a=input("输出：")
# print(type(a))
# b=int(a)
# print(type(b))
# c=b+100
# print(c)

# b="a"+str(100)
# print(b)

# a2=0b01100100
# print(a2)

# state=True
# print(state+3)

# a=60
# b=13
# print(bin(a))
# print(bin(6))

# print(0 or 20)

# str="我是习啊习"
# print("习" in str)


#习题输出本月有多少天
# years=input("请输入年份:")
# month=input("请输入月份:")
# list1=[1,3,5,7,8,10,12] #31天
# list2=[4,6,9,11] #30天
# if month in list1:
#     print("本月31天")
# elif month in list2 :
#     print("本月30天")
# else:
#     if int(years) % 4 == 0 :
#         print("本月28天")
#     else :
#         print("本月29天")

# for i in range(0,13,3): #range(start,stop,[step]) 此处的3为步数
#     print(i)

# n=["aa","bb","cc"]
# for _ in range(len(n)):
#     print(f"位置{_},元素{n[_]}")

# total=0
# n=2
# while n <= 100:
#     total += n
#     n += 2
# print(f"和得{total}")

# total=0
# n=1
# while n <= 100:
#     if n%2==0:
#         total += n
#     n += 1
# print(f"和得{total}")

# a=["周一","周二","周三","周四"]
# b=0
# n=0
# while b<=5:
#     b+=n
#     n+=1
#     print(f"第{n}周：")
#     for i in a:
#         print(i,end="、")
#     print()

#？？？九九乘法表
# for i in range(1,10):
#     for j in (1,i+1):
#         print(f"{i}x{j}={i*j}",end="")
#     print("")

# for row in range(1, 10):
#     for col in range(1, row+1):
#         print("{0}x{1}={2:2}  ".format(col, row, row * col), end="")
#     print("")
#？？？

#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}x{i}={i*j}\t",end="")
#     print()

# str1="abcdefd"
# #正向索引0,1,2,3,4,5,6
# #反向索引-7,-6,-5,-4,-3,-2,-1
# print(len(str1))  #len()函数获取字符串长度
# print(str1[2])  #打印第三位、位于2字符
# print(str1[2:5])
# print(str1[2:-1])
# print(str1[2:])
# print(str1[:2])
# print(str1[2:len(str1):2])
# print(str1[-1:-7:-2])

# str1="a"
# str1+="b"
# print(str1+"c")

# str="a"\
#     "b"\
#     "c"
# print(str)

# listvar=["a","b","c"]
# res="*".join(listvar)
# print(res)

# str="IT习"
# str_utf8=str.encode("UTF-8")
# str_gbk=str.encode("GBK")
# print(str_utf8)
# print(str_gbk)

# a=list("习啊习")
# print(a)

# a=list(range(2,-3,-1))
# print(a)

# a=[x*2 for x in range(5)]
# print(a)

# namelist=[1,"love","你"]
# for name in namelist:
#     print(name)

# namelist=[1,"love","你"]
# nameadd=input("请输入",)
# namelist.append(nameadd)
# print("添加后",namelist)

# a=[1,2,3]
# b=[4,5,6]
# a.append(b)
# print(a)

# a=[1,2,3]
# b=[4,5,6]
# a.extend(b)
# print(a)

# a=[1,2,3]
# b=[4,5,6]
# res=a+b
# print(res)

# a=[1,2,3]
# b=a*2  #扩大倍数
# print(b)

# a=[1,2,3]
# a.insert(0,0)
# print(a)

# a=[1,2,3]
# b=a.pop()
# print(a,b)

# a=[1,2,3]
# a[1]=0
# print(a)

# a=["z","x","q"]
# findname=input("请输入查找的内容")
# if findname in a:
#     print("yes")
# else:
#     print("no")

# a=[12,"你"]
# b=[13,"我"]
# c=[a,b]
# print(c)
# print(c[0][0])

# a=[12,"你"]
# b=[13,"我"]
# c=[14,"他"]
# d=[a,b,c]
# for _ in d:
#     # print(_)
#     for i in _:
#         print(i,end=",")
#     print()

# import random
# officelist=[[],[],[]]
# names=["a","b","c","d","e","f","g","h"]
# for name in names :
#     num=random.randint(0,2)  #[0,2]的闭区间
#     #print(num)
#     #print(name,end=",")
#     officelist[num].append(name)
# print(officelist)

# i=0
# for office in officelist:
#     print(f"办公室{i+1}的人数为{len(office)}")
#     i+=1
#     for name in office:
#         print(name,end="\t")
#     print()
#     print("-"*10)

# set1={1,2,3,3,4}
# set1.update("woai")
# print(set1)


# set1={1,2,3,3,4}
# set2={"aa","bb"}
# set1.update(set2)
# print(set1)

# def num2add(a,b):
#     c=a+b
#     print(c)
# num2add(1,2)

# def num2add(a,b):
#     return a+b
# def num3add(a,b,c):
#     sum=num2add(num2add(a,b),c)
#     return print(sum)

# num3add(1,2,3)

# def line():
#     return print("-")
# def numline(num):
#     i=0
#     while i<num:
#         line()
#         i+=1

# numline(3)

# def printinfo(name,age,*args): 
#     print(f"名字{name},年龄{age}")
#     print("电影评分从低到高",args)
# printinfo("我",18,9.9,5.6)

# def printinfo(name,age,**kwargs):     
#     print(f"名字{name},年龄{age}")
#     print("电影评分从低到高",kwargs)
# printinfo("我",18,学历="博士",出生地="河南")

# def printinfo(name,age,*args):     
#     print(f"名字{name},年龄{age}")
#     print("电影评分从低到高",args)
# list=[9.9,5.6]
# printinfo("我",18,*list)

# def printinfo(name,age,**kwargs):     
#     print(f"名字{name},年龄{age}")
#     print("附加信息",kwargs)
# info={"学历":"博士","出生地":"河南"}
# printinfo("我",18,**info)


# def test1 (a,b,c,*,name,age):
#     print(f"{a},{b},{c},{name},{age}")
# test1(1,2,3,name="wo",age=22)  

# def printnum(n):
#     print(n)
#     if n==1:    #使用if循环增加边界判断
#         return
#     printnum(n-1)

# printnum(100)


# def fun(n):
#     if n <=1:
#         return 1
#     return fun(n-1)*n
# print(fun(5))

# def fc(n):
#     if n<=1:
#         return n
#     else:
#         return fc(n-1)+fc(n-2)
# print(fc(9))

# import module1

# import os
# print(__file__)
# print(os.path.dirname(__file__)) 



# #coding=utf-8
# import urllib.request,urllib.error  

# def askurl(url):
#     head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
#     }
#     request=urllib.request.Request(url,headers=head)
#     html=""
#     try:
#         response=urllib.request.urlopen(request)
#         html=response.read().decode("utf-8")
#         print(html)
#     except urllib.error.URLError as e:
#         if hasattr (e,"code"):
#             print(e.code)
#         if hasattr(e,"reason"):
#             print(e.reason)

# askurl("https://movie.douban.com/top250?start=0")

