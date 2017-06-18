# encoding=utf-8
'''
@author: liangzai
'''

'''
1；函数式使用线程：调用thread模块中的start_new_thread()函数来产生新线程
    thread.start_new_thread(function, args)
        function    方法名
        args        方法参数
'''

import thread
import threading
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        count += 1
        time.sleep(delay)
        print("线程：%s，时间：%s" %(threadName, time.ctime(time.time())))
    else:
        print("线程：%s over." %threadName)
        thread.exit()

def thread_test_1():        
    try:
        thread.start_new_thread(print_time, ("Thread_a", 1))
        thread.start_new_thread(print_time, ("Thread_b", 2))
    except:
        print("error create threads.")
        
    while 1:
        pass

'''
2：使用Threading模块创建线程,继承threading.Thread
        重写__init__方法和run方法
'''

def print_time2(name, delay, counter):
    while counter > 0:
        time.sleep(delay)
        print("%s: %s" % (name, time.ctime(time.time())))
        counter -= 1

# 通过工厂方法获取一个新的锁对象
lock = threading.Lock()

# 继承父类threading.Thread
class myThread(threading.Thread):
    def __init__(self, tid, name, counter):
        threading.Thread.__init__(self)
        self.tid = tid
        self.name = name
        self.counter = counter
    
    def run(self):
        global lock
        # 加锁
        if lock.acquire():
            print("starting %s" %self.name)
            print_time2(self.name, 1, 5)
            print("exiting %s " %self.name)
            #释放锁
            lock.release()

if __name__ == "__main__":
    thread1 = myThread(1, "thread-1", 5)
    thread2 = myThread(2, "thread-2", 8)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    print("t-1 over.")
    thread2.join()
    print("t-2 over.")
    
