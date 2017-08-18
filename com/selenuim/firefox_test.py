# encoding=utf-8
'''
Created on 2017年8月16日

@author: liangzai
'''
from selenium import webdriver
from selenium.webdriver.common.proxy import ProxyType



CHECK_URL = 'https://www.baidu.com/s?wd=ip'
## 火狐不支持动态添加代理

if __name__ == '__main__':
    profile = webdriver.FirefoxProfile()
    '''新tab页打开新链接'''
    profile.set_preference("browser.link.open_newwindow", 3)
    profile.set_preference("browser.link.open_external", 3)
    profile.set_preference("browser.link.open_newwindow.restriction", 3)
    profile.set_preference("browser.link.open_newwindow.override.external", 3)
    
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0")
    profile.update_preferences()
    
    browser = webdriver.Firefox(firefox_profile=profile)
    browser.get(CHECK_URL)
    #browser.get_screenshot_as_file('D://a.jpg')
    
    # 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId，
    # 意思就相当于浏览器清空缓存后，加上代理重新访问一次url
    
    proxy=webdriver.Proxy()
    proxy.proxy_type=ProxyType.MANUAL
    proxy.http_proxy='10.11.4.50:3128'
    # 将代理设置添加到webdriver.DesiredCapabilities.FIREFOX中
    proxy.add_to_capabilities(webdriver.DesiredCapabilities.FIREFOX)
    browser.start_session(webdriver.DesiredCapabilities.FIREFOX)

    browser.get(CHECK_URL)
    browser.get_screenshot_as_file('D://b.jpg')
    browser.quit()
    
    
    