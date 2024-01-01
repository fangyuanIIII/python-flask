"""
单例类
保证一个类只有一个实例，并提供一个全局访问点
"""
class SingleClass(object):
    __name = None
    def __init__(self):
        super(SingleClass, self).__init__()
        self.__name = ''

singleclass = SingleClass()

