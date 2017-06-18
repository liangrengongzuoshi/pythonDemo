# encoding=utf-8
'''
@author: liangzai
'''

from time import sleep
from selenium import webdriver


loadTimeout = 2
scriptTimeout = 3


profile = webdriver.FirefoxProfile()
profile.set_preference("browser.link.open_newwindow", 3)
profile.set_preference("browser.link.open_external", 3)
profile.set_preference("browser.link.open_newwindow.restriction", 3)
profile.set_preference("browser.link.open_newwindow.override.external", 3)

profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0")
profile.update_preferences()

driver = webdriver.Firefox(timeout=loadTimeout, capabilities=None, proxy=None, firefox_profile=profile)

driver.set_page_load_timeout(loadTimeout)
driver.set_script_timeout(scriptTimeout)

driver.implicitly_wait(loadTimeout)


driver.get("https://www.baidu.com")

# 打印页面标题
print(driver.title)
driver.find_element_by_id("kw").send_keys("java")
driver.find_element_by_id("su").click()
sleep(1)
driver.save_screenshot("D:\java.png")

# from selenium.webdriver.common.by import By

'''页面选择器'''
# By ID
element = driver.find_element_by_id("content_right")
# element = driver.find_element(by=By.ID, value="content_right")
print(element.text)

# By Class Name
element = driver.find_elements_by_class_name("s_ipt")
# element = driver.find_elements(By.CLASS_NAME, "s_ipt")
print(element[0].text)

# By Tag Name
element = driver.find_element_by_tag_name("script")
# element = driver.find_element(By.TAG_NAME, "script")
print(element.text)

# By Name
element = driver.find_element_by_name("referrer")
# element = driver.find_element(By.NAME, "cheese")
print(element.text)

# By a标签内容
# element = driver.find_element_by_link_text("java")
# element = driver.find_element(By.LINK_TEXT, "cheese")
# print(element.text)

# By 部分a标签内容
element = driver.find_element_by_partial_link_text("java")
# element = driver.find_element(By.PARTIAL_LINK_TEXT, "cheese")
print(element.text)

# By CSS
element = driver.find_element_by_css_selector("div.s_tab")
# element = driver.find_element(By.CSS_SELECTOR, "#food span.dairy.aged")
print(element.text)

# By XPath
inputs = driver.find_elements_by_xpath("//input")
# inputs = driver.find_elements(By.XPATH, "//input")
print(inputs[0].text)

sleep(3)
# 关闭资源 
driver.quit()
