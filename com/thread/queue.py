# encoding=utf-8
'''
@author: liangzai
'''

'''
Python的Queue模块中提供了同步的、线程安全的队列类，
包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。
这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。
    Queue模块中的常用方法:
    Queue.qsize() 返回队列的大小
    Queue.empty() 如果队列为空，返回True,反之False
    Queue.full() 如果队列满了，返回True,反之False
    Queue.full 与 maxsize 大小对应
    Queue.get([block[, timeout]])获取队列，timeout等待时间
    Queue.get_nowait() 相当Queue.get(False)
    Queue.put(item) 写入队列，timeout等待时间
    Queue.put_nowait(item) 相当Queue.put(item, False)
    Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
    Queue.join() 实际上意味着等到队列为空，再执行别的操作
'''

import Queue
import threading
import time

exitFlag = 0
lock = threading.Lock()
workqueue = Queue.Queue(10)

class myThread(threading.Thread):
    
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
        
    def run(self):
        print("starting %s" %self.name)
        process_data(self.name, self.q)
        print("exiting %s" %self.name)

def process_data(name, q):
    while not exitFlag:
        lock.acquire()
        if not workqueue.empty():
            data = q.get()
            lock.release()
            print("%s  process  %s" %(name, data))
        else:
            lock.release()
        time.sleep(1)

threadName = ["t-1", "t-2", "t-3"]
nameList = ["11", "22", "33" ,"44", "55", "66"]
threads = []

for t in threadName:
    tt = myThread(t, workqueue)
    tt.start()
    threads.append(tt)

lock.acquire()
for n in nameList:
    workqueue.put(n)
lock.release()

# 等待队列清空
while not workqueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

for t in threads:
    t.join()
print("Main is over.")


