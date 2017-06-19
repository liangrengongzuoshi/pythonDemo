# encoding=utf-8
'''
@author: liangzai
'''

'''
定义：
    ll = list()
    ll = list([1, 2, 3])
    ll = [1, 2, 3]
'''

'''
1    list.append(obj)    在列表末尾添加新的对象
2    list.count(obj)    统计某个元素在列表中出现的次数
3    list.extend(seq)    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4    list.index(obj)    从列表中找出某个值第一个匹配项的索引位置
5    list.insert(index, obj)    将对象插入列表
6    list.pop(obj=list[-1])    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7    list.remove(obj)    移除列表中某个值的第一个匹配项
8    list.reverse()    反向列表中元素
9    list.sort([func])    对原列表进行排序

del list[index:index]    通过下标删除元素
'''

'''
1    cmp(list1, list2)    比较两个列表的元素    0-相等
2    len(list)    列表元素个数
3    max(list)    返回列表元素最大值
4    min(list)    返回列表元素最小值
5    list(seq)    将元组转换为列表
'''

if __name__ == '__main__':
    list1 = [1,2,"4", 5, 6]
    list2 = [1,2,"5", 4, 6]
    
    print(cmp(list1, list2))
    list1.remove(2)
    print(list1)
    del list2[1:]
    print(list2)
    
    print("tuple--------")
    # 如果元组只有一个元素，需要在后面加,如：（1,） 非 （1）
    tuple0 = (1)
    print(type(tuple0))
    tuple1 = (1,)
    print(type(tuple1))
    tuple2 = (1,2,3)
    print(tuple1)
    print(tuple2)
    
    
    ll = list([1,2,3,"32"])
    ll = list()
    print(ll)
    
    pass