import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url="https://hit.yuketang.cn/pro/portal/home/"
driver=webdriver.Edge()
driver.get(url)
# 程序打开网页后20秒内 “手动登陆账户”
time.sleep(20)

with open('cookies.txt', 'w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.quit()