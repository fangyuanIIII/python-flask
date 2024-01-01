"""
设计模式
"""

#单例模式
# 保证一个类只有一个实例，并提供一个全局访问点
from singleclass import singleclass
a = singleclass
print(a)

#工厂模式
from factoryclass import FactoryClass
b = FactoryClass()
studengt = b.getPerson("Student")
teacher = b.getPerson("Teacher")
print(studengt)
print(teacher)
