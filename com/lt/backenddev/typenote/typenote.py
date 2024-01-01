"""
类型注释
:类型[类型s]   类型s可以多个以,分割
"""
a :int = 1
b :str = "a"

c :list = []
d :dict = {}
e :set = {}

c :list[int] = []
d :dict[str,int] = {}
e :set[int] = {}

def func_(a :int,b :str):
    print("")

# -> list指定返回类型
def funcre_(data:list) -> list:
    return data

"""
union联合类型
union[int,str]  可以单独是int 可以单独是str  又可以既是int又是str
"""
from typing import Union
a1 :Union[int,str] = ""
a2 :Union[int,str] = 1

def funca(a :Union[int,str]):
    print()

def funca(a :Union[list,str,int]) -> Union[list]:
    return a