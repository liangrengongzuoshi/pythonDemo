# encoding=utf-8
'''
@author: liangzai
'''

if __name__ == '__main__':
    str1 = " hello world. "
    str2 = "hello world."
    print("# 删除空格strip")
    print(str1.strip())
    print(str1)
    print(str2)
    print("# 字符串比较cmp")
    print(cmp("aaa", "aaa"))
    print("# 截取str[:]")
    str3 = "0123456789"
    print(str3[0:3]) #截取第一位到第三位的字符
    print(str3[:])   #截取字符串的全部字符
    print(str3[6:])  #截取第七个字符到结尾
    print(str3[:-3]) #截取从头开始到倒数第三个字符之前
    print(str3[2])   #截取第三个字符
    print(str3[-1])  #截取倒数第一个字符
    print(str3[::-1]) #创造一个与原字符串顺序相反的字符串
    print(str3[-3:-1]) #截取倒数第三位与倒数第一位之前的字符
    print(str3[-3:]) #截取倒数第三位到结尾

    print("# 字符串查找find")
    print(str3.find("34"))
    
    print(str3[0:100])  #没有超界异常
    
    
    