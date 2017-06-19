#coding=utf-8
'''
Created on 2017年6月15日
@author: liangzai

python 2x和3x版本共存（windows环境）

1.下载安装2.x和3.x两个版本并安装
2.配置环境变量Path
    C:\python3;C:\python3\Scripts;C:\python2;C:\python2\Scripts;
3.安装 Python 3.3 以上的版本时，Python会在C:\Windows文件夹下安装启动器py.exe
4.通过py启动器选择不同版本的python编译执行脚本
    py -2 helloworld.py
    py -3 helloworld.py
5.通过pip选择安装模块；python2,和python3版本不同模块也有可能不同；
    且选择不同 版本安装，会把模块安装到相应版本的Lib\site-packages下，避免冲突
    py -2 -m pip install requests
    py -3 -m pip install requests
6.eclise pyDev可以配置不同版本python编译器，在创建项目时可以选择某个版本的python作为编译器


图像处理模块
    py -2 -m pip install -I --no-cache-dir -v Pillow
    from PIL import Image
selenium模块
    py -2 -m pip install selenium
    from selenium import webdriver
redis模块
    py -2 -m pip install redis
    import redis
requests模块
    py -2 -m pip install requests
    import requests

'''
from com.redis import redisutil

if __name__ == '__main__':
    print("python2.7 -> Hello world.")
    
    print(redisutil.redis_set("ok", "yes,ok"))
    print(redisutil.redis_get("ok"))
    
    a = 0
    if a == 0:
        strs = "asdf"
    print(strs) 
    account = 10
    cvId = 100
    strs = u"账号%s搜索到多份简历，无法唯一定位：%s" %(account, cvId)
    print(strs)
    
    
