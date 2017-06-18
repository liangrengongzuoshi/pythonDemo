# encoding=utf-8
'''
@author: liangzai
'''

import traceback

'''
读取文件
'''
def read_file(path):
    try:
        myfile = open(path, "r")
        return myfile.read()
    except:
        traceback.print_exc()
    finally:
        myfile.close()

'''
保存至文件
'''
def save_file(html, path, code):
    try:
        f = open(path, "w")
        html = html.encode(code, 'ignore')
        html = html.decode(code, 'ignore')
        f.write(html)
    except:
        traceback.print_exc()
    finally:
        f.close()
    
if __name__ == "__main__":
    strs=u"Hello world."
    save_file(strs, "D://ttt.txt", "utf-8")
    print(read_file("D://ttt.txt"))
