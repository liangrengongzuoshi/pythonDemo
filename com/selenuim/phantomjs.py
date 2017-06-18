# encoding=utf-8
'''
@author: liangzai
'''
from selenium import webdriver
from time import sleep

driver = webdriver.PhantomJS(executable_path="D:\MyFile\phantomjs\phantomjs-2.0\phantomjs.exe")

driver.get("https://www.baidu.com/")

# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text
print(data)

# 打印页面标题
print(driver.title)
driver.find_element_by_id("kw").send_keys("java")
driver.find_element_by_id("su").click()
sleep(1)
# 获取页面快照
driver.save_screenshot("D:\java.png")
# 获取网页源码
print(driver.page_source)
print(driver.current_url)
# 获取当前页面Cookie
print(driver.get_cookies())
# 打印每个cookie
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))
# 删除cookie
# driver.delete_cookie("CookieName")
# driver.delete_all_cookies()

# 关闭资源
driver.quit()

if __name__  == "__main__":
    pass
