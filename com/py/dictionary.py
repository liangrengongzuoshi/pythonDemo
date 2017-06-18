# encoding=utf-8
'''
@author: liangzai
'''

'''
del dict['name']    删除字典中name条目
del dict    删除整个字典
dict.clear()    清空字典


copy()    字典浅复制
get(key, default=None)    获取字典key内容
has_key(key)    是否存在key
items()    以列表返回可以遍历的（键，值）元组数组
keys()    返回所有的key
values()    以列表返回字典所有值
setdefault(key, default=None)    如果key不存在，才会添加key，并设置value为default
dict.update(dict2)    将字典dict2的键值更新到dict

pop(key[,default])    删除字典给定键key所对应的值，返回被删除的值
    pop("key")    如果字典有key删除key并返回key的value，如果没有抛出异常
    pop("key", "default")    同上，如果没有key不会抛出异常，会返回default
popitem()    随机返回并删除字典中的一对键和值。


'''

if __name__ == '__main__':
    mydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
 
    dict2 = mydict.copy()
    dict3 = {}
    dict3.update(mydict)
    
    print(mydict.pop("Name", "没有"))
 
    mydict.setdefault("Name", "name")
    mydict.setdefault("name", "name")
 
    print(str(mydict))
    print(len(mydict))
    
    print(mydict)
    print(dict2)
    print(dict3)
    
    
    
    del mydict['Name'];  # 删除键是'Name'的条目
    mydict.clear();  # 清空词典所有条目
    del mydict ;  # 删除词典
    pass
