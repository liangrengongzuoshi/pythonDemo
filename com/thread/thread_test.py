# encoding=utf-8

import time

import multiprocessing as mp
import threading as td


count = 1000000

def job(q, name):
    t = time.time()
    res = 0
    for i in range(count):
        res += i + i ** 2 + i ** 3
    q.put(res)
    t2 = time.time()
    print("%s - %s" % (name, str(t2 - t)))


def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q, "multicore-1"))
    p2 = mp.Process(target=job, args=(q, "multicore-2"))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:', res1 + res2)

def multithread():
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q, "multithread-1"))
    t2 = td.Thread(target=job, args=(q, "multithread-2"))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)
    

def normal():
    res = 0
    for _ in range(2):
        for i in range(count):
            res += i + i ** 2 + i ** 3
    print('normal:', res)



if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1)
    multicore()
    print('multicore time:', time.time() - st2)

