# encoding=utf-8
'''
Created on 2017年8月16日

@author: liangzai
'''
from selenium import webdriver
from selenium.webdriver.common.proxy import ProxyType

PATH_PHANTOMJS = "D:\MyFile\phantomjs\phantomjs-2.0\phantomjs.exe"

# CHECK_URL = 'https://www.baidu.com/s?wd=ip'
CHECK_URL = 'http://1212.ip138.com/ic.asp'


if __name__ == '__main__':
    # 不使用代理代打开ip138
    browser=webdriver.PhantomJS(PATH_PHANTOMJS)
    browser.get(CHECK_URL)
    print('1: ', browser.page_source)
    browser.get_screenshot_as_file('D://a.jpg')
    
    # 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId，
    # 意思就相当于浏览器清空缓存后，加上代理重新访问一次url
    proxy=webdriver.Proxy()
    proxy.proxy_type=ProxyType.MANUAL
    proxy.http_proxy='10.11.4.70:3128'
    # 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
    proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
    browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
    browser.get(CHECK_URL)
    print('2: ', browser.page_source)
    browser.get_screenshot_as_file('D://b.jpg')
    
    # 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId，
    # 意思就相当于浏览器清空缓存后，加上代理重新访问一次url
    proxy=webdriver.Proxy()
    proxy.proxy_type=ProxyType.MANUAL
    proxy.http_proxy='10.11.4.50:3128'
    # 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
    proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
    browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
    browser.get(CHECK_URL)
    print('3: ', browser.page_source)
    browser.get_screenshot_as_file('D://c.jpg')
    
    # 还原为系统代理
    proxy=webdriver.Proxy()
    proxy.proxy_type=ProxyType.DIRECT
    proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
    browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
    browser.get(CHECK_URL)
    print('4: ', browser.page_source)
    browser.get_screenshot_as_file('D://d.jpg')
    
    
