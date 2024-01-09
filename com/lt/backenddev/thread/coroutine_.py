"""
协程
通俗理解只要在 def 里面只看到一个 yield 关键字，就表示是协程。

"""
import time

def work1():
    while True:
        print("----work1---")
        yield
        time.sleep(0.5)
        print('-- 1')

def work2():
    while True:
        print("----work2---")
        yield
        time.sleep(0.5)
        print('-- 2')

def work3():
    while True:
        print("----work3---")
        yield
        time.sleep(0.5)
        print('-- 3')

def main():
    w1 = work1()
    w2 = work2()
    w3 = work3()
    while True:
        next(w1)
        next(w2)
        next(w3)


import asyncio
"""
async 可以申明协程异步方法，当某个方法被 async 关键字申明后， 调用方法不会返回结果，而是返回一个协程对象
await 可以在协程方法中，挂起自身的协程，并等待另一个协程完成，直到返回结果。
 await 只能出现在 通过 async 关键字修饰的方法中。
  也就是说， await 和 async 必须配合使用。
当有多个任务配合 切换调用，又需要异步来提高效率，这时就需要使用协程来优化。
"""

async def func1():
    print('-- func1')
    return 1


async def func2():
    print('-- func2')
    ret = await func1()
    print(ret)


def runasyncio():
    # print(func1())
    # 异步协程方法，需要 async 库的 run 方法来调用；
    asyncio.run(func2())

"""
使用greenlet
pip install greenlet

"""
import time
import greenlet


g1 = None
g2 = None
g3 = None
# 任务1
def work1():
    print("----work10---")
    for i in range(2):
        print("----work1---")
        time.sleep(1)
        # 切换到协程2里面执行对应的任务
        g2.switch()


# 任务2
def work2():
    print("----work20---")
    for i in range(2):
        print("----work2---")
        time.sleep(1)
        # 切换到第一个协程执行对应的任务
        g3.switch()


def work3():
    print("----work30---")
    for i in range(2):
        print("----work3---")
        time.sleep(1)
        # 切换到第一个协程执行对应的任务
        g1.switch()


def initgreenlet():
    global g1
    global g2
    global g3

    # 创建协程指定对应的任务
    g1 = greenlet.greenlet(work1)
    g2 = greenlet.greenlet(work2)
    g3 = greenlet.greenlet(work3)
    # 切换到第一个协程执行对应的任务
    g1.switch()

if __name__ == '__main__':
    initgreenlet()

"""
使用gevent
pip install gevent
gevent 内部封装的greenlet，其原理是当一个greenlet遇到IO(指的是input output 输入输出，
比如网络、文件操作等) 操作时，就自动切换到其他的 greenlet，等到IO操作完成，
再在适当的时候切换回来继续执行。
 由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，
 就保证总有 greenlet 在运行，而不是等待IO

"""
# import gevent
# # import requests
#
# # 有耗时操作时需要
# monkey.patch_all()  # 将程序中用到的耗时操作的代码， 换为gevent中自己实现的模块
#
#
# def work(n):
#     for i in range(n):
#         # 获取当前协程
#         print(gevent.getcurrent(), i)
#         # gevent.sleep(2)
#
#     print('\n')
#
# def initgevent():
#     g1 = gevent.spawn(work, 5)
#     g2 = gevent.spawn(work, 3)
#     g3 = gevent.spawn(work, 5)
#
#     # g1.join()
#     # g2.join()
#     # g3.join()
#
#     # 等价于上面三个方法
#     gevent.joinall([g1, g2, g3])





