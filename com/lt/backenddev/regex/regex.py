"""
正则表达式
match 从头匹配
search 匹配  从前到后直到找到第一个匹配返回
#findall 全部匹配搜索  返回列表
"""
import re

str_ = "asdadaddasdac  ada12313 sda"

#match 从头匹配
result = re.match("sda",str_)
print(result)

#search 匹配  从前到后直到找到第一个匹配返回
result1 = re.search("sda",str_)
print(result1)
print(result1.span()) #查找的下标位置（1,4）
print(result1.group()) # 查找到的字符串"sda"

#findall 全部匹配搜索
result2 :list = re.findall("sda",str_)
print(result2)

"""
r"
元字符匹配

单字符匹配
.     匹配任意字符
[]    匹配[]中列举的字符
\d    匹配数字 0-9
\D    匹配非数字
\s    匹配空白  空格，tab
\S    匹配非空白
\w    匹配单词字符  a-z A-Z 0-9  _
\W    匹配非单词字符

数字匹配
*     匹配前一字符出现0至无数次
+     匹配前一字符出现1至无数次
？    匹配前一字符出现0次或1次
{m}   匹配前一字符出现m次
{m,}  匹配前一字符最少出现m次
{m,n} 匹配前一字符出现m到n次

边界匹配
^     匹配字符串开头
$     匹配字符串结尾
\b    匹配一个单词的边界
\B    匹配非单词边界

分界匹配
|     匹配左右任意一个表达式
()     匹配括号中字符作为一个分组
"
"""

