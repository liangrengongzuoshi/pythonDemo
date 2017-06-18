# encoding=utf-8
'''
@author: liangzai
'''

import random

'''
a~b之间随机数
'''
def get_random(a, b):
    return random.randint(a, b)


if __name__ == '__main__':
    print(get_random(1, 10))
