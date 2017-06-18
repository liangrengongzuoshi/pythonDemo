# encoding=utf-8
'''
@author: liangzai

pip install threadpool
https://chrisarndt.de/projects/threadpool/

'''

import threading
import time

import threadpool

def sayhello(ss):
    name = threading.current_thread().getName()
    print("线程：%s 打印：%s" % (name, ss))
    time.sleep(1)

func_args = ["11", "22", "33", "44", "55", "66", "77", "88"]

pool = threadpool.ThreadPool(10)
requests = threadpool.makeRequests(sayhello, func_args)

for req in requests:
    pool.putRequest(req)
pool.wait()  
print("over.")
