"""
多线程
"""
import threading
# import time as t, threading as thread
import time as t
import threading as thread

# def sing():
#     print('唱歌')
#     t.sleep(2)

def sing(msg):
    print('唱歌msg')
    t.sleep(2)
def dance():
    print('跳舞')
    t.sleep(2)
def play(msg):
    print('玩msg')
    t.sleep(2)


sing_thread = threading.Thread(target=sing,args={"aa"})
dance_thread = threading.Thread(target=dance)
play_thread = threading.Thread(target=play,kwargs={"msg":"bb"})
sing_thread.start()
dance_thread.start()
play_thread.start()
