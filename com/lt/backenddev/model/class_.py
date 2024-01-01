"""
面向对象
"""
#设计类

#声音
# import winsound
# winsound.Beep(2000,3000)
class Student:
    #属性
    name = None
    age = None


    def __init__(self,name,age):
        self.name = name
        self.age = age

    #成员方法 self是默认值    调用直接a()不用管self   有其他参数需要传参
    def a(self):
        print("你好")

    #魔术方法  对象直接输出字符串
    def __str__(self):
        return f"name:{self.name}, age:{self.age}"

    # 魔术方法  一般用作 >  <  比较
    def __lt__(self, other):
        return self.age < other.age

    # 魔术方法  一般用作 >=  <= 比较
    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


#创建对象
stu = Student("",0)
stu.name = "李彪"
stu.age = 12

stu1 = Student("韩信",12)
print(stu1.name,stu1.age)

# 打印魔术方法__str__  的值
# print(stu1)
#比较 魔术方法__lt__的值
# print(stu > stu1)
#比较 魔术方法__le__ 的值
# print(stu >= stu1)
#比较 魔术方法__eq__ 的值
# print(stu == stu1)

"""
封装 继承 多态
"""
#封装  私有成员变量  私有成员方法
class Store:
    """
    封装  私有成员变量   以__ 开头
    """
    __name = None

    """
    封装  私有成员方法   以__ 开头
    """
    def __a(self):
        print("")

#继承  单继承 多继承  1.继承成员变量和方法  2.复写复类成员变量和方法
# 3.调用父类成员变量和方法  类名.成员变量   类名.成员方法(self)  或者super().成员变量   super().成员方法()
class GrandParent:
    # __id = None
    name = "爷"

    def a(self):
        print("爷a")

class Parent(GrandParent):
    # __id = None
    code = "aaa"
    #复写
    name = "父"

    # 复写
    def a(self):
        print("父a")
        #调用父类成员变量和方法   方法1
        # GrandParent.name
        # GrandParent.a(self)
        # 调用父类成员变量和方法   方法2
        super().name

        super().a()

class Child(Parent,GrandParent):
    # __id = None
    d = ""

c1 = Child()
d1 = Parent()
print("%%%%%%%%%%%%%%%%")
d1.a()
print("%%%%%%%%%%%%%%%%")
# 继承成员变量 按照类继承顺序读取
# print(c.code,c.name,c.a())
# print(c1.a())

"""
多态 完成某种行为 使用不同对象得到不同状态    作用设计标准
pass抽象
"""
class A:
    #抽象方法
    def a(self):
        pass

class B(A):
    #复写A
    def a(self):
        print("")
        # print("B")

class C(A):
    def a(self):
        print("")
        # print("C")

def printA(a :A):
    a.a()

b = B()
c = C()
printA(b)
printA(c)

