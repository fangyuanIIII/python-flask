"""
自定义函数
"""
# 含有pass就是抽象函数
def func_(args):
    return

#返回多个
def func_more():
    return "",1,""

x,y,z = func_more()

"""
参数传递
参数可以是字符串，字典，元组，数字列表 函数 等
"""

def a1(func):
    func()

def a2():
    pass
a1(a2)

def a(a,b,c):
    print("a")
#参数传递
a(1,2,3)
#关键字参数传递
a(a=1,b=1,c=1)
#传参赋予=号后面的都必须是赋予=
a(1,b=1,c=1)
"""
参数设置默认值
参数设置默认值 后面的传参都要设置默认值
"""
def b(a="",b=1,c=True):
    print("a")

"""
不定长参数传递
1.位置传递    合并为元组
2.关键字传递   合并为字典
"""
#位置传递   以*args接收    args是元组参数类型
def c(*name):
    print(name)

c(1,"a","c")
#支持元组嵌套传递参数
c((1,"a","c"))

#关键字传递  根据关键字组成字典
def d(**args):
    print(args)
d(a="b",b=1,c=True)


def pass_(args):
    pass

"""
x = name2();
type(x) = None 在条件语句None是False
"""
def none_():
    print("语句")

"""
做注释说明
"""
def add(x,y):
    """

    :param x:  数字
    :param y:  数字
    :return:   返回两个数据相加之后的结果
    """
    result = x + y
    return result

"""
函数的嵌套使用
def func_(args):
    func2_(args)
    return
    
def func2_(args):
    return
"""

"""
变量

num_ = 1
def func_(args):
    #num = 1   #是内部变量外面访问不了
    global num #global声明num是全局变量
    num = 1 
"""

"""
lambda 匿名函数      lambda 传入参数:函数体(函数体只能运行一行代码)
"""
def test(func):
    func(1,2)

def a11(x,y):
    print(x+y)
#普通函数传递
test(a11)
#lambda表达式
test(lambda x,y:print(x+y))
