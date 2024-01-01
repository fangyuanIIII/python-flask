#随机数
import random
#系统声音
import winsound
#系统
import os
winsound.Beep(2000,3000)
#取随机数
num = random.randint(0,100 )


os.listdir("D:/")  # return list
os.path.isdir("D:/dev")  #bool
os.path.exists("D:/dev")  #bool
os.path.abspath("filepath")  #绝对路径

os.path.abspath(__file__)  #当前basefunc.py的绝对路径
os.path.dirname("filepath") #目录路径当前的父目录
os.path.join("diepath","dirname")  #os.path.join(os.path.dirname(os.path.abspath(__file__)),"A")

#方法 变量的类型
type(1)

#类型转换  将变量的转为字符串
str(1)

#将变量转为数字     变量是数字
int("1")

#将变量转为浮点数    变量是数字
float("1.11")

#长度 变量长度
len()

#输入语句
# input()
#输入语句带前缀字符串
# input("")
#输出语句
print()

"""
range语句 一般在for循环语句中
for x in range(100)
    print(x)
range(100) 从0 到 99
range(2,100) 从2 到 99
range(2,100,3) 从2 5 8 11 14 ... 98
"""
