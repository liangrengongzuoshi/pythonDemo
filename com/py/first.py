# encoding=utf-8
'''
@author: liangzai
'''

'''
标准数据类型
    String（字符串）
    Numbers（数字）
    List（列表）：有序的对象结合
        ['str', 100, 3.14]
    Tuple（元组）：元素不可二次赋值
        ('str', 100, 3.14)
    Dictionary（字典）：无序的对象结合
    
数字型包括:整型，长整型，浮点型，复数型；
非数字型包括:字符串，列表，元组和字典 ；
非数字型的共同点:都可以使用切片、链接（+）、重复（*）、取值（a[]）等相关运算;


strings, tuples, 和 numbers 是不可更改的对象，
而 list,dict 等则是可以修改的对象。
    即如果函数的参数是不可更改对象，函数内部对参数做修改是不影响函数传递参数的原值的

'''

'''
数据类型转换
    type(n)    查看n的数据类型

    int(x, [,base])    base代表进制，默认10进制
    long(x, [,base])
    float(x)
    str(x)
    
    list(s)    将序列 s 转换为一个列表
    tuple(s)   将序列 s 转换为一个元组
    dict(d)    创建一个字典。d 必须是一个序列 (key,value)元组
    
    set(s)    转换为可变集合
    frozenset(s)    转换为不可变集合
    repr(x)    将对象 x 转换为表达式字符串
    
    eval(str)    用来计算在字符串中的有效Python表达式,并返回一个对象
'''

if __name__ == '__main__':
    mylist = [1,2,3,'4']
    print(mylist)
    mytuple = (1,2,3,'4')
    print(mytuple)
    mydict={1: "aa", "b":"bb"}
    print(mydict)
    
    print(int("23", 10))
    
