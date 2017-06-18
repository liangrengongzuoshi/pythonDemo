# encoding=utf-8
'''
@author: liangzai
'''
import time

import redis


redis_host = "127.0.0.1"
redis_port = 9999


pool = redis.ConnectionPool(host=redis_host, port=redis_port, db=0)

def getRedis():
    return redis.Redis(connection_pool=pool)

'''赋值，key存在会覆盖'''
def redis_set(key, value):
    try:
        return getRedis().set(key, value)
    except Exception:
        pass
    
'''赋值，key不存在才会赋值'''
def redis_setnx(key, value):
    try:
        return getRedis().setnx(key, value)
    except Exception:
        pass

'''赋值，并设置过期时间'''
def redis_setex(key, value, delay):
    try:
        return getRedis().setex(key, value, delay)
    except Exception:
        pass

'''根据key获取value'''
def redis_get(key):
    try:
        return getRedis().get(key)
    except Exception:
        pass

'''删除key'''
def redis_del(key):
    try:
        return getRedis().delete(key)
    except Exception:
        pass

'''判断key是否存在'''
def redis_exist(key):
    try:
        return getRedis().exists(key)
    except Exception:
        pass

'''给key设置过期时间'''
def redis_expire(key, delay):
    try:
        return getRedis().expire(key, delay)
    except Exception:
        pass
    
if __name__ == '__main__':
    print(redis_set("a", "aa"))
    print(redis_setnx("a", "aaa"))
    print(redis_get("a"))
    
    print(redis_expire("a", 3))
    print(redis_expire("key", 10))
    
    print(redis_setex("aa", "value", 3))
    print(redis_get("aa"))
    time.sleep(4)
    print(redis_get("aa"))
