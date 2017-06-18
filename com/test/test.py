# encoding=utf-8
'''
@author: liangzai
'''

from com.util import mydef

if __name__ == '__main__':
    for i in range(5):
        print(i)
    print("hello world.")
    for x in range(1, 5):
        print(x)

    print("random: %s" % (mydef.get_random(1, 10)))