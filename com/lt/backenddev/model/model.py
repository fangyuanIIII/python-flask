"""
模块module 是一个python文件  以.py结尾
里面有类 函数  变量

global声明全局变量
nonlocal修改外部函数的值
"""



"""
模块的导入[from 模块名] import [模块名|类|函数|变量|*][as 别名]
*是全部的意思
"""
import time
time.sleep(5)

from time import sleep
sleep(5)

from time import *
sleep(5)

import  time as t
t.sleep(5)