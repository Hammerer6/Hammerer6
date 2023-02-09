#准备工作-获取数据-解析内容-保存数据

#准备工作 分析网站
"""
https://movie.douban.com/top250?start=0
分析网站得知页面包含250条电影数据，分10页，每页25条
每条url的不同之处：最后的数值=（页数-1）*25

f12键可以打开浏览器的开发者模式

headers是向服务器的请求

一般python代码前需要加入#coding=utf-8，为了防止在处理中文时发生错误

if __name__=="__main__": #测试程序和函数

引入模块module
引入系统级的模块
import sys
import os

安装第三方库
pip 库名

项目需要的包
from bs4 import BeautifulSoup  #网页解析，获取数据
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error   #指定url 获取网页数据
import xlwt              #进行excel操作
import sqlite3           #进行sqlite数据库操作

三个功能——函数
爬取网页
解析数据
保存数据


基本代码
def main():
    baseurl="https://movie.douban.com/top250"
    #1爬取网页
    datalist=getdata(baseurl)

#爬取网页
def getdata(baseurl):
    datalist=[]

    return datalist
#保存数据
def savedata(savepath)
"""

#urllib的使用实践
"""
#coding=utf-8
import urllib.request
import urllib.parse
#get请求  直接访问网站即可
#此处使用response对象函数 其属性有许多，比如response.css("**")  get等等
response= urllib.request.urlopen("https://www.baidu.com") #把获取访问的网站的源码封装到response这个对象里
print(response.read().decode("utf-8"))  #此处读取获得的源码，并用decode解码

#post请求
data=bytes(urllib.parse.urlencode({"hi,nihao"}),encoding="utf-8") #bytes函数把数据转换成字节文件，encoding把字节解码
#https://httpbin.org/post为测试访问网站                             #urllib.parse.urlencode把数据封装进去
response= urllib.request.urlopen("https://httpbin.org/post",data=data)  #data函数为提交的数据
print(response.read().decode("utf-8"))

#超时处理  此处为了防止程序因为爬取失败的判断
try:
    response= urllib.request.urlopen("https://httpbin.org/get",timeout=1)  #timeout后的时间是超时的时间
    print(response.read().decode("utf-8"))
except urllib.error.URLError as erro:   #urllib.error.URLError 是超时的错误类型
    print("超时！连接错误")


response= urllib.request.urlopen("https://httpbin.org/get")
print(response.status)
#显示为200为正常   418错误为对方已经知道我们是爬虫
print(response.getheaders())  #获得header全部数据
print(response.getheader("server"))#获得header中的server数据

#伪装
url="https://httpbin.org/post"
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
}         #此处从本质上来说是一个字典的形式{键：值}
data =data=bytes(urllib.parse.urlencode({"hi,nihao"}),encoding="utf-8")  #封装数据
req=urllib.request.Request(url=url,data=data,headers=headers,method="post")  #请求
response=urllib.request.urlopen(req)   #获取网站源码
print(response.read().decode("utf-8")) #读取源码
"""

#bs4(即beautifulsoup4) 
#将复杂的html文档转化为一个复杂的树形结构，每个节点都是python对象
#所有的对象可以归纳为4种：Tag  navigablestring  beautifulsoup  comment
"""
from bs4 import BeautifulSoup

file=open("./baidu.html","rb") #此处./为当前目录的意思，rb=read ，bytes
html=file.read().decode("utf-8")               #读取文档并储存在html变量中
bs=BeautifulSoup(html,"html.parser")  #parser函数将代码片段转换成计算机可读的数据结构

#Tag 拿到标签及其内容：只拿到她找到的第一个
print(bs.title)
print(bs.a)

#navigablestring  拿到标签里的内容（字符串）
print(bs.title.string)
print(bs.a.attrs) #拿到一个标签里的所有属性


#beautifulsoup  整个文档
print(bs.name)
print(bs)  #即打印整个文档内容

#comment 注释 是一个特殊的navigablestring，输出的内容不包含注释内容
print(bs.a.string)

#文档的遍历 bs4的遍历文件树
print(bs.head.contents)
print(bs.head.contents[1]) #一般输出为[]列表的形式，这里的[1]表示拿到列表中的第二位

#文档搜索
#1)find_all()找到指定标签，并放在一个列表里
#字符串过滤
t_list=bs.find_all("a") #标签是a就会被找出来
print(t_list)

#正则表达式搜索 search()方法来匹配
import re
t_list=bs.find_all(re.compile("a"))  #只要标签含有a就会被找出来

#方法搜索 传入一个函数，根据函数的要求来搜索
def name_is_exists(tag):
    return tag.has_attr("name")
t_list=bs.find_all(name_is_exists)
for item in t_list:
    print(t_list)


#kwargs 参数
t_list=bs.find_all(id="head")  #找到id为head的内容
t_list=bs.find_all(href="www")

#text参数
t_list=bs.find_all(text="hao123")
t_list=bs.find_all(text=["hao123",1,"贴吧"])

#limit函数
t_list=bs.find_all("a",limit=2) #此处limit限制找到的个数

#css选择器
t_list=bs.select("title")#按标签来查找
t_list=bs.select("#u1")  #按id寻找，id为u1的
t_list=bs.select("head>title")#通过子标签来查找
#多种查找，可查看文档练习
"""

#re模块正则表达式
"""
正则表达式的常用操作符
.表示任何单个字符
[]对单个字符集给出取值范围
详情可看官方文档

re库主要功能函数
re.search() 在一个字符中搜索匹配正则表达式的第一个位置，返回match对象
re.match() 从一个字符串的开始位置起匹配正则表达式，返回match对象
re.finall() 搜索字符，以列表的形式返回全部能匹配的子串
详情可看官方文档

正则表达式的限定匹配
re.l 使匹配对大小写不敏感
re.S 使.匹配包括换行在内的所有字符
详情可看官方文档

#re的使用
import re

pat=re.compile("AA") #所要验证的模板AA
m=pat.search("AABCAAA") #对比查找"AABCAAA"中的字母，但是search只能验证第一个遇到的正确的
print(m)
#返回值<re.Match object; span=(0, 2), match='AA'>   此处的区间（0，2）是一个左闭右开的索引值

#简化
m=re.search("asd","asdd")  #("规则模板","被校验的对象")
print(m)

#findall可以找到所有的对象并放到列表里
m=re.findall("asd","asdfasdfasd") #("规则模板","被校验的对象") 
print(m)

print(re.findall("[A-Z]","AsdfasdDasd"))  #[A-Z]找到所有的大写字母

print(re.findall("[A-Z]+","AdDAsdDFCVasd")) #[A-Z]+找到所有的大写字母组合
#['A', 'DA', 'DFCV']

#sub函数 替换
print(re.sub("a","A","aabbvbnnjubu"))#找到a并用A替换  ("用于替换","替换者","字符串")
#AAbbvbnnjubu

#建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符问题
a=r"\aadd-\'"
print(a)
#输出为\aadd-\'

"""







