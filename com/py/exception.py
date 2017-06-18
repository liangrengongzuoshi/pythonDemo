# encoding=utf-8
'''
@author: liangzai
'''

import traceback

# 自定义异常
class MyError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

if __name__ == '__main__':
    
    try:
        raise MyError("Bad error.")
        pass
    except:
        traceback.print_exc()
        pass
    else:
        print("except else")
        pass
    finally:
        print("finally")
        pass
    
    pass