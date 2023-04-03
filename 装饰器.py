#装饰器@
"""
def hi():
    print("hi")
    def greet ():
        return "greet"
    def welcome ():
        return "welcome"
    print(greet())
    print(welcome())
    print("outhi")
hi()
#greet () #hi()函数内的greet ()不可被访问

"""


"""
def hi(name="right"):
    def greet():
        return"greet"
    def welcome():
        return"welcome"
    if name=="right":
        return greet    #此处不是greet()，因为greet()会被直接执行，而写成greet是为了让greet到处传递
    else:
        return welcome
a=hi()
print(a)
#返回值 <function hi.<locals>.greet at 0x0000026A1D76B378> ，hi函数指向greet函数

print(a())
#返回值 greet ，直接执行函数

"""

# def hi():
#     return "hi"
# def afterhi(func): #func为需要代入的函数
#     print("after hi do something")
#     print(func())

# afterhi(hi)  #将hi函数作为参数带入afterhi函数，并执行

"""
def newdecorator(func):
    def warpfunc():
        print("before func")
        func()
        print("after func")
    return warpfunc
def func():
    print("i am func")

func=newdecorator(func)  #封装func函数
func()   #运行结果已经为func装饰newdecorator
# 结果before func
# i am func
# after func



@newdecorator   #此处直接简化了func=newdecorator(func)的封装这一步骤
def func():
    print("i am func")

func()
# 结果before func
# i am func
# after func


"""


from functools import wraps
def newdecorator(func):
    @wraps(func)   #@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。
    def decorated(*args,**kwargs):  #*args,**kwargs分别表示无关键字参数和有关键字参数，当我们在写程序时，不确定将来要往函数中传入多少个参数
        if not can_run :  #判断函数
            return "function will not run"
        return func(*args,**kwargs)
    return decorated

@newdecorator
def func():
    return("function is running")

can_run=True  #赋予can_run的意义
print(func())
#function is running



#类装饰器
# 装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。
# 使用类装饰器主要依靠类的__call__方法
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()

