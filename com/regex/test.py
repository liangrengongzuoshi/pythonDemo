# encoding=utf-8
'''
@author: liangzai
'''

import re

'''
re.match(pattern, string, flags=0)
    pattern 匹配的正则表达式
    string    要匹配的字符串
    flags    标志位：

re.search(pattern, string, flags=0)
    同上
    
    
区别：
    re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
    re.search匹配整个字符串，直到找到一个匹配。
'''
'''
正则表达式修饰符 - 可选标志
    re.I    使匹配对大小写不敏感
    re.L    做本地化识别（locale-aware）匹配
    re.M    多行匹配，影响 ^ 和 $
    re.S    使 . 匹配包括换行在内的所有字符
    re.U    根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
    re.X    该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
'''
def match_test(line):
    match = re.match("(.*) are (.*?) .*", line, re.M | re.I)
    if match:
        print("group(): " + match.group())
        print("group(1): " + match.group(1))
        print("group(2): " + match.group(2))
    else:
        print("None.")
    pass
    
def search_test(line):
    match = re.search("(.*) are (.*?) .*", line, re.M | re.I)
    if match:
        print("group(): " + match.group())
        print("group(1): " + match.group(1))
        print("group(2): " + match.group(2))
    else:
        print("None.")
    pass

'''
re.sub(pattern, repl, string, count=0, flags=0)
    pattern : 正则中的模式字符串。
    repl : 替换的字符串，也可为一个函数。
    string : 要被查找替换的原始字符串。
    count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''
def sub_test():
    phone = "2004-959-559 # 这是一个国外电话号码"
 
    # 删除字符串中的 Python注释 
    num = re.sub(r'#.*$', "", phone)
    print("电话号码是: " + num)
     
    # 删除非数字(-)的字符串 
    num = re.sub(r'\D', "", phone)
    print("电话号码是 : " + num)
    pass

if __name__ == "__main__":
    print(re.match(".pub", "http://liangzai.pub"))
    print(re.search(".pub", "http://liangzai.pub").group())
    
    line = "Cats are smaller than dogs."
    
    # match_test(line)
    # search_test(line)
    sub_test()
        
    line = "大家好我的电话号码是：183-1129-9999，记住了吗？"
    print(re.search(r'(\d{3}-\d{4}-\d{4})', line).group(1))
    
    
    
    
    
    
    
    
    

