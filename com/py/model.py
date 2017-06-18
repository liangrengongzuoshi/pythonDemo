# encoding=utf-8
'''
@author: liangzai
'''

import os
import sys
import time


if __name__ == '__main__':
    print(sys.argv)
    
    # 环境变量
    print(os.environ)
    print(os.environ.get("HOME", "None"))

    # 当前目录
    print(os.getcwd())
    
    time.sleep(1)
    sys.exit(0)
    print("over before.")