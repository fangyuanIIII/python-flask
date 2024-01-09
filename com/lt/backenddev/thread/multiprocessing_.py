"""
进程  multiprocessing
多线程  threading
协程   asyncio
"""
from multiprocessing import Process,Pool,Queue
import os, time, random

def fuc1():
    for i in range(3):
        print("---- fuc1 ----", os.getpid(), os.getppid())
        time.sleep(1)


def fuc2(num):
    for i in range(3):
        print("---- fuc2 ----", os.getpid(), os.getppid(), num)
        time.sleep(1)


def fuc3(num, s1):
    for i in range(3):
        print("---- fuc3 ----", os.getpid(), os.getppid(), num, s1)
        time.sleep(1)


"""
进程Process
"""
def initProcess():
    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    p1 = Process(target=fuc1)
    p2 = Process(target=fuc2, args=(22,))  # 传递元组，单个元素记得加逗号。否则可能报错
    p3 = Process(target=fuc3, args=(33, 'hello'))  # 传递元组，单个元素记得加逗号。否则可能报错
    # 也可写成
    # p3 = multiprocessing.Process(target=fuc3, kwargs={"num": 33, "s1":'hello'})
    #可以设置子进程守护，当主进程执行完，子进程不再执行，直接结束
    # p1.daemon = True
    p1.start()
    p2.start()
    p3.start()
    #                               进程的编号：  父进程的编号：
    print('-- end main process : ', os.getpid(), os.getppid())

"""
进程池pool
"""
def process_pool():
    p = Pool(5)  # 调用多少个并行进程 进行程序运行，pool的默认容量为 CPU的计算核的数量

    for i in range(10):
        p.apply_async(fuc2, args=(i,))

    print('-- main: Waiting for all subprocesses done...')

    #调用join方法会等待所有子进程执行完毕， 调用join之前必须调用close
    #调用close 之后就不能继续添加新的 Process了。
    p.close()
    p.join()


# 写数据进程执行的代码:
def write(q):
    print('---- Process to write: ', os.getpid())

    for value in ['A', 'B', 'C']:
        print('-- write :', value)
        q.put(value)  # put 之后，get 就可以马上接收
        time.sleep(random.random())
        # time.sleep(5)


# 读数据进程执行的代码:
def read(q):
    print('---- Process to read: ', os.getpid())

    while True:
        value = q.get(True)
        print('-- get :', value)

"""
进程间通信queue
"""
def initQueue():
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()

    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()

    # 等待pw结束:
    pw.join()

    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

"""
分布式进程

"""
import  queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()

# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

def getTask():
    return task_queue
def getResult():
    return result_queue


def init_server():


    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable=getTask)
    QueueManager.register('get_result_queue', callable=getResult)

    server_addr = '127.0.0.1'
    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=(server_addr, 5000), authkey=b'abc')

    # 启动Queue:
    manager.start()

    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # 从 result 队列读取结果:

    print('Try get results...')

    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)

    # 关闭:
    manager.shutdown()

    print('master exit.')

def init_client():
    # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # 连接到服务器，也就是运行task_master.py的机器:
    server_addr = '127.0.0.1'
    print('Connect to server %s...' % server_addr)

    # 端口和验证码注意保持与task_master.py设置的完全一致:
    m = QueueManager(address=(server_addr, 5000), authkey=b'abc')

    # 从网络连接:
    m.connect()
    # 获取Queue的对象:
    task = m.get_task_queue()
    result = m.get_result_queue()

    # 从task队列取任务,并把结果写入result队列:
    for i in range(10):

        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n * n)
            time.sleep(1)
            result.put(r)

        except Queue.Empty:
            print('task queue is empty.')

    # 处理结束:
    print('worker exit.')


if __name__ =='__main__':
    init_server()








