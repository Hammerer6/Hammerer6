#面向对象
"""
class people:
    def __init__(self,name):#与普通函数不同，类中的函数需要添加初始值self
        self.name=name #自己调用自己的值，并构建实例化，方便下面继承
        print(self.name)
out_p1=people("i am")  #此时因为__init__方法直接运行，无需实例化


class people:
    def __init__(self,name):
        self.name=name
    def outprint(self):
        print(self.name)
# out_p=people("i am")  
out_p2=people("i am") #实例化类，为调取其中的outprint函数
out_p2.outprint()
"""



"""

class people:
    name="" #确定属性
    age=0
    def __init__(self,n,a): #初始化函数
        self.name=n
        self.age=a
    def intro(self):
        print(f"my name is {self.name},my age is {self.age}")
# out_p=people("wo",18)#传入值，并实例化类
# out_p.intro()

#单继承
class student(people):#括号里为父类
    grade=""#加入子类属性
    def __init__(self,n,a,g):
        people.__init__(self,n,a)#people.__init__调用父类的函数构造
        self.grade=g 
    def intro(self): #覆写父类的函数，添加新的值
        print(f"my name is {self.name},my age is {self.age},i am study in {self.grade} grade")
# out_p=student("wo",18,"1")
# out_p.intro()


#方法重写
#当父类和子类同时拥有一个函数时，子类会覆盖父类的函数。可以使用super()调用被覆盖的父类函数
class parent:
    def __init__(self):
        print("parent method")

class child(parent):
    def __init__(self):
        print("child method")#覆写
x=child()
y=parent()
super(child,x).__init__()#调用被覆盖前的父类函数


#类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。 

#类的私有属性变量
#_property定义私有属性,私有属性在类外部无法直接进行访问



"""


