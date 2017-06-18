# encoding=utf-8
'''
@author: liangzai
pip install multiprocessing
'''

from multiprocessing.dummy import Pool, Queue
import threading
import time

# 队列
tasks = Queue()

for i in range(9):
    tasks.put(str(i)*2)

def main(name):
    while True:
        time.sleep(1)
        if name.empty():
            print("name is over.")
            break
        else:
            thread = threading.current_thread().getName()
            print("线程：%s 打印：%s" % (thread, name.get()))

# 启动四个线程
pool = Pool(4, main, (tasks,)) 

while True:
    time.sleep(5)
    if tasks.empty():
        print("tasks is over.")
        # 终结线程池
        pool.terminate()
        break
    
print("main is over.")


