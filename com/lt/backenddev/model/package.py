"""
python包  里面有一个__init__.py文件
[-i 网站]指定下载地址
有很多第三方工具包需要下载 pip install ***  [-i 网站]

科学计算 numpy
数据分析 pandas
大数据计算 pyspark,apache-flink
图形可视化 matplotlib,pyecharts
人工智能  tensorflow

"""


"""
闭包

函数的嵌套
global声明全局变量
nonlocal  修改外部函数的值
"""

#简单闭包
def outer(out_):
    def inner(in_):
        print(f"out:{out_}in:{in_}")
    return inner

inner = outer("外")
inner("内")

#闭包使用nonlocal  修改外部函数的值
def outer1(count=0):
    def inner(val:int):
        #不使用nonlocal    out_的值不能在inner函数内更改  相当于外部final了
        nonlocal count
        count += val
        print(f"result:{count} add:{val}")
    return inner

inner1 = outer1()
inner1(2)
inner1(6)


"""
装饰器
将一个函数，方法不改变代码  ，能够在前后添加自定义逻辑
"""
#固定方法
def func_():
    import time
    print("睡觉")
    time.sleep(2)

#闭包装饰器
def outer2(func):
    def inner():
        print("睡觉之前")
        func()
        print("睡觉之后")
    return inner

inner2 = outer2(func_)
inner2()

#装饰器语法糖   outer2就是前面写的函数
@outer2
def func_2():
    import time
    print("睡觉")
    time.sleep(2)

func_2()



