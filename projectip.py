#coding=utf-8
import urllib.request,urllib.error
import re 
import xlwt
from bs4 import BeautifulSoup

#主程序
def main():
    baseurl="https://www.kuaidaili.com/free/inha/"
    # savepath=""
    # getdata()
    # savedata(savepath)
    askdata(baseurl)

#爬取全部数据并且解析数据
def getdata():
    pass


#爬取一页
def askdata(url):
    header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
    }
    html=""
    request=urllib.request.Request(url,headers=header)
    response=urllib.request.urlopen(request)
    html =response.read().decode("utf-8")
    #print(html)
    # with open ("chtml.html","w") as f:
    #     f.write(html)


#保存数据
def savedata(savepath):
    pass





if __name__=="__main__":
    main()