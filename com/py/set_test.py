# encoding=utf-8
'''
@author: liangzai
'''

'''
定义：
    ss = {1, 2, "sadf"}
    ss = set({1, 2, "sdd"})
    ss = set("asdfdd")
'''

'''
set集合是无序的、元素不重复
    set & set                &交集
    set | set                |并集
    set - set                -差集
    set ^ set                对称差集：互相都没有
    
    seta.issubset(setb)      seta是否是setb的子集
    seta.issuperset(setb)    seta是否是setb的父集
    in                        是否是set的元素
'''

'''
 .add(增加)添加一项
 .update（[增加多项]）
 .remove(删除)（没有的话报错）
 .discard(删除)（没有不会报错）
 
 .copy(复制)
 .pop(删除任意一个并返回这个元素)
'''

def main():
    ss = {2,3,4,5,6}
    print(ss, type(ss))
    
    
    ss2 = set('')
    ss2.add('boy')
    ss2.add('girl')
    print(ss2)
    ss2.remove('boy')
    ss2.discard('boy')
    ss2.update([1,2,3,4])
    ss2.update("1234")
    print(ss2)
    
    a = set('abc')
    b = set('bcd')
    c = set('c')
    
    print('a-b=', a - b)    #差集
    print('a&b=', a & b)    #交集
    print('a|b=', a | b)    #并集
    print('a^b=', a ^ b)    #对称差集：互相都没有
    
    print(a == b)
    print(a != b)
    print('b' in b)
    print(c in b)
    
    print(c.issubset(b))
    print(b.issuperset(c))
    
if __name__ == '__main__':
    main()
    pass