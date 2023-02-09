#文件操作

#文件操作-写
"""
基本流程
f=open("text.txt","w")   #此处读取text.txt  如果没有就会新建此文件。  w为write的缩写，即写入
f.write("woshi")         #写入内容woshi
f.close()                #关闭文件，为了让系统不报错

相对路径  就是相对当前源码所在的路径
绝对路径  从盘符开始的路径
f=open(r"c:/Users/习/Desktop/pynotes/text.txt","w")   此处的r为了让\不产生转义效果，需在路径前加r 或者可直接再每个中添加\\
f.write("woshi")         
f.close()  

中文编码问题
默认使用记事本打开会正常显示，因为windows系统默认使用GBK字符集
pycharm默认打开乱码，默认使用UFT-8字符集
f=open("text.txt","w",encoding="UTF-8")   #此处指定了编码
f.write("我是")         
f.close()

写入多行  writelines
    f=open("text.txt","w",encoding="UTF-8")
    f.write("我是\n","习\n","啊哈哈哈\n")      #直接在写入内容中加入\n换行   
    f.close()

    content=["我是\n","习\n","啊哈哈哈\n"]    #直接在写入内容的列表中加入\n换行 并使用writelines
    f=open("text.txt","w",encoding="UTF-8")
    f.writelines(content)         
    f.close()

    content=["我是","习","啊哈哈哈"]
    f=open("text.txt","w",encoding="UTF-8")
    f.write("\n",join(content))                #如果列表中没有\n 换行，就用join函数把元素以\n连接起来
    f.close()
"""

#文件操作-读
"""
基本流程
f=open("text.txt","r",encoding="UTF-8")   #r为read的缩写
data=f.read(2)  #此处需要一个变量接收读取的内容,此处的2为指针从头开始读取到的两位字符
print(data)
data=f.read(4)   #此处的4为指针从头开始读取到的四位字符
print(data)  
f.close()

读取多行 readlines
    循环读法，读出全部内容
        f =open("text.txt","r",encoding="UTF-8")
        while True:
            content=f.readline()
            if content:
                print(f"{content}",end="")
            else:
                break;
        f.close()

    readlines读法，读出全部内容

        f =open("text.txt","r",encoding="UTF-8")
        content=f.readlines()
        print(content)

        i=1
        for data in content:
            print(f"{i}:{data}",end="")
            i+=1
        f.close()

tell函数返回读取指针当前所在的位置(指针所在位置前面的字节数)
先写入
f=open("text.txt","w",encoding="UTF-8")
f.write("ii我是")         
f.close()

f=open("text.txt","w",encoding="UTF-8")
content=f.read(2)
print("当前指针所在的位置",f.tell())          #此处需要注意，汉字的字节数在各自编码中占的数量不一样，所以tell的结果也不一样
f.close()

seek(offset,[,whence])定位文件读取的指针所在的位置，指定的是字节数

"""

#访问模式（可查看文档模式列表）
"""
当文件不存在时，w和a会新建文件。但是r会报错

r+ 可读可写  （write）   但是这里的write写会覆盖掉之前的,但是只有一部分
w+  会清除全部的，只剩下写入的

二进制文件操作(音乐、图片、视频等)
rb读取   wb 写入
只是将文件单纯的用0和1保存起来，不用指定字符集
文件的复制，也就是单纯的读取rb与写入wr

f_in=open("photo.jpg","rb")
f_out=open("photocopy.jpg","wb")

while Ture:
    data =f_in.read(100)   #此处的100bytes字节为指定储存空间，是以十六进制的表达方法
    if data:                #判断data有无内容
        f_out.write(data)
    else:
        break
f_in.close()
f_out.close()

文件的写入过程：
数据---缓冲区（内存中）---文件中（硬盘上）close运行后
flush可以刷新缓冲区
truncate 截断 从指针位置到结束的字符全部删除，只保留之前的内容

文件对象
文件对象是一个可迭代对象，比如可for in

文件对象属性和状态
f=open("text.txt","w",encoding="UTF-8")
f.name 文件名
f.mode  打开的模式
f.writable 文件可写
f.readable  文件可读

"""