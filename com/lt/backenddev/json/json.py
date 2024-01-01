"""
json数据转换
data类型可以是 列表 元组 字典 集合
str = json.dump(data)    #将容器类型转为字符串
str = json.dump(data,ensure_ascii=
                False)  可以是否二进制编码     没有二进制编码可以显示中文

json = json.load(str)    #将字符串重新转为容器类型
"""
import json


str = json.dump({"key":"value",3:4},ensure_ascii=
                False)
#将字符串重新转为容器类型
dict_ = json.load(str)