"""
列表list     序列类型
元组tuple    序列类型
字符串str     序列类型
集合set      非序列类型
字典dict     非序列类型

支出下标索引    list tuple str
支持重复元素    list tuple str

#可变数据类型指的是可以在原地修改（即不创建新的对象）的数据类型
可变       list set dict

通用函数
len()  max()  min()  sorted( 集合,reverse=True)排序
"""
sorted({},reverse=True)

"""
list定义
list = []
list = list()
取数据正向取  list[0] list[1] ...
取数据反向取  list[-1] list[-2]...

嵌套
list = [[]]
嵌套取数据
list[0][0]
"""
a1 = ["a",1,False,"a"]
a3 = list()
#取下标索引
a1.index("a")
#在列表的1号位插入"b"数据
a1.insert(1,"b")
#在列表末尾添加数据
a1.append("c")
#将一个列表的数据添加到a1上
a1.extend(["d","e"])
#统计列表元素的数量
a1.count("a")
#统计列表长度
len_ = len(a1)
#删除列表数据
del a1[0]
#删除a1一位数据并将这个数据返回
element = a1.pop(0)
#删除元素
a1.remove("a")
#清空列表
a1.clear()
#嵌套
a2 = [["a",1,False],"b",True]

"""
tuple元组  和列表的函数一样
tuple = (1,2)
tuple = ("a",)   #当是单个元素时必须后面加 , 才能识别是元组不然是字符串类型
tuple = tuple()
"""
b1 = ("a","b",1,True)
b1.index(1)
num = b1.count("a")
len_ = len(b1)

"""
字符串
"""
c1 = "12aaaaabbbss and ad21"
char_a = c1[2]
# 定位
c1.index("and")
#替换
c1.replace("and","")
#去除前后空格
c1.strip()
#会将前后12字符去除 与顺反无关
c1.strip("12")

c1.count("and")
len(c1)
c1.split(" ")

"""
序列支持切片   列表 元组 字符串支持切片
a = []
a = ()
a = ""
a[2:4] 取出下标为 2 ,3的元素
a[:4] 取出下标为 0,1,2 ,3的元素
a[:] 取出全部元素
a[::] 取出全部元素

a[::-1]反转数据

a[::2] 取出（步长为2） 的元素 0,2,4
"""

"""
set集合
set = {"a",1,True}
set = set()

集合差集difference   返回一个新集合是左边与右边不一样的元素
d3 = {1,2,3}.difference({1,5,6})   # 返回{2,3}
消除集合差集difference_update  删除左边与右边一样的元素
{1,2,3}.difference_update({1,5,6})  # {1,2,3}变成 {2,3}
集合联合union   返回一个新集合包含所有元素
d5 = {1,2,3}.union({1,5,6})   
"""
d1 = {"a"}
d2 = set()
#添加操作
d1.add("b")
#移除操作
d1.remove("a")
element1 = d1.pop()
d1.clear()
d3 = {1,2,3}.difference({1,5,6})
d4 = {1,2,3}.difference_update({1,5,6})
d5 = {1,2,3}.union({1,5,6})

len(d5)

"""
字典dict
dict = {"key":"value"}
dict = dict()
"""
e1 = {"a":"a1","b":"b1",3:"3",4:5}
e2 = dict()
#新增元素
e1["c1"] = "c1"
#获取元素
c1_value  = e1["c1"]
#删除元素并返回
elemente = e1.pop("c1")
e1.clear()
for key in e1.keys():
    pass
len(e1)

