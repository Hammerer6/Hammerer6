#coding=utf-8
import urllib.request,urllib.error
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3

#主要程序
def main():
    baseurl="https://movie.douban.com/top250?start="
    datalist=getdata(baseurl)

    #savepath="豆瓣电影top250.xls"
    dbpath="movie.db"
    #savedata(datalist,savepath)
    savedatadb(datalist)


#影片详情的re规则
#影片详情链接
findlink=re.compile(r'<a href"(.*?)">')
#影片图片
findimgsrc=re.compile(r'<img .*src="(,*?)"',re.S)  #    re.S此处的作用为忽略换行符
#影片片名
findtitle=re.compile(r'<span class="title">(.*)</span>')
#影片评分
findrating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findjudgenum=re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findinq=re.compile(r'span class="inq">(.*)</span>')
#找到影片的相关内容
findbd=re.compile(r'<p class="">(.*?)</p>',re.S)



#爬取网页
def getdata(baseurl):
    datalist=[]
    for i in range(0,10):   #获取页面信息的函数
        url=baseurl+str(i*25)   #str将内容转化为字符串的模式
        html=askurl(url)
    #逐一解析数据
    soup=BeautifulSoup(html,"html.parser")
    for item in soup.find_all('div',class_="item"):
        data=[]
        item=str(item)

        link=re.findall(findlink,item)[0]
        data.append(link)

        imgsrc=re.findall(findimgsrc,item)[0]
        data.append(imgsrc)

        titles=re.findall(findtitle,item)  #片名可能只有一个中文名，没有外文名,所以需要写判断
        if (len(titles)==2):
            ctitle=titles[0]
            data.append(ctitle)
            otitle=titles[1].replace("/","")
            data.append(otitle)
        else:
            data.append(titles[0])
            data.append(' ')

        rating=re.findall(findrating,item)[0]
        data.append(rating)

        judgenum=re.findall(findjudgenum,item)[0]
        data.append(judgenum)

        inq=re.findall(findinq,item)
        if len(inq)!=0:
            inq=inq[0].replace("。","") #去掉句号
            data.append(inq)
        else:
            data.append(" ") #留空
        bd=re.findall(findbd,item)[0]
        bd=re.sub("<br(\s+)?/>(\s+)?"," ",bd)  #去掉<br/>
        data.append(bd.strip())#去掉前后的空格

        datalist.append(data)

    return datalist


#得到一个特定的网页
def askurl(url):
    head={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
    }
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr (e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
    
#保存数据
def savedata(datalist,savepath):
    print("save...")
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet=book.add_sheet("豆瓣电影top250",cell_overwrite_ok=True)
    col=("电影链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) #依次输入列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savepath)


def savedatadb(datalist,dbpath):
    init_db(dbpath)
    conn =sqlite3.connect(dbpath)
    cur =conn.cursor
    

    for data in datalist:
            for index in range (len(data)):
                if index ==5 or index == 6:
                    continue
                data[index]='"'+data[index]+'"'
            sql='''
                    insert into movie250(
                    info_link,pic_link,cname,ename,rated,instroduction,info)
                    values(%s)'''%",".join(data)
            cur.execute(sql)
            conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql='''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        instroduction text,
        info text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor=conn.cursor
    cursor.execute(sql)
    conn.commit
    conn.close



#测试专用，此处调用主函数main()
if __name__=="__main__":
    main()
    #init_db("text.db")
    print("爬取完毕")