"""
异常捕获
传递性 可以将层级嵌套函数方法的异常捕获到
"""
try:
    print("aa")
except:
    print("错误")

try:
    print("aa")
except Exception as e:
    print("错误")
else:
    print("没有异常执行")
finally:
    print("打印")

#捕获异常
try:
    pass
except NameError as e:
    print(e)
#捕获多个异常
try:
    pass
except (NameError,ZeroDivisionError):
    print("异常")

try:
    pass
except (NameError,ZeroDivisionError) as e:
    print(e)
