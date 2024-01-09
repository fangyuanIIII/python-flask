"""
进程  multiprocessing
多线程  threading
协程   asyncio
"""
from multiprocessing import Process,Pool,Queue
from threading import Thread
import asyncio
import os, time, random

import threading
from concurrent.futures import ThreadPoolExecutor


def test(x, y):
    for i in range(x, y):
        print(i, threading.current_thread().name)


#    time.sleep(0.1)

def initThread1():

    thread1 = Thread(name='t1', target=test, args=(1, 10))
    thread2 = Thread(name='t2', target=test, args=(11, 20))

    thread1.start()  # 启动线程1
    thread2.start()  # 启动线程2

"""
继承
"""
class mythread(threading.Thread):
  def run(self):
    for i in range(1,10):
      print(i, threading.current_thread().name )
      # time.sleep(0.1)
def initThread2():
    thread1 = mythread(name='t1')
    thread2 = mythread(name='t2')

    thread1.start()
    thread2.start()

"""
锁lock
"""
# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance

    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)


balance = 0
lock = threading.Lock()

def run_thread2(n):
    for i in range(100000):

        # 先要获取锁:
        lock.acquire()

        try:
            # 放心地改吧:
            change_it(n)

        finally:
            # 改完了一定要释放锁:
            lock.release()


def initThread3():
    t1 = threading.Thread(target=run_thread2, args=(5,))
    t2 = threading.Thread(target=run_thread2, args=(8,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(balance)

# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum

def initThreadPool():
    # 创建一个包含2条线程的线程池
    pool = ThreadPoolExecutor(max_workers=2)
    # 向线程池提交一个task, 20会作为action()函数的参数
    future1 = pool.submit(action, 20)
    # 向线程池再提交一个task, 30会作为action()函数的参数
    future2 = pool.submit(action, 30)
    # 判断future1代表的任务是否结束
    print(future1.done())
    time.sleep(3)
    # 判断future2代表的任务是否结束
    print(future2.done())
    # 查看future1代表的任务返回的结果
    print(future1.result())
    # 查看future2代表的任务返回的结果
    print(future2.result())
    # 关闭线程池
    pool.shutdown()

if __name__=='__main__':
    initThreadPool()












