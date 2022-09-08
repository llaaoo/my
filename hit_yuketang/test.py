import json
import warnings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
'''
# 第一步输入这个：去除开头警告
warnings.simplefilter('ignore', ResourceWarning)
# 第二个输入这个：隐藏式启动谷歌浏览器执行UI测试用例
edge_options = Options()
edge_options.add_argument('--headless')
driver = webdriver.Edge(options=edge_options)
'''
# 注意输入了这代码之后，不需要输入打开浏览器的代码了！（driver = webdriver.Chrome()）这一行代码不需要输入了！
url="https://hit.yuketang.cn/pro/portal/home/"
driver=webdriver.Edge()
driver.get(url)

# 首先清除由于浏览器打开已有的cookies
driver.delete_all_cookies()

with open('cookies.txt', 'r') as f:
    # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookies_list = json.load(f)

    # 方法1 将expiry类型变为int
    for cookie in cookies_list:
        # 并不是所有cookie都含有expiry 所以要用dict的get方法来获取
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)

    # 方法2删除该字段
    # for cookie in cookieslist:
    #     # 该字段有问题所以删除就可以
    #     if 'expiry' in cookie:
    #         del cookie['expiry']
#driver.refresh()
#driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[3]/div/div[1]/div/div/div/div[2]/button').click()
url2="https://hit.yuketang.cn/pro/lms/8692P7E5cKJ/10521902/studycontent"
driver.get(url2)
course_num=[]
for unit in range(2,14):
    course_num.append(driver.find_element(By.XPATH,f'//*[@id="chapter-section"]/div[{unit}]/span[2]').text)
print(course_num)
k=-1
num=0
for j in range(2, 14):
    k=k+1
    if k<len(course_num):
        num=course_num[k]
        for i in range(1,int(num)):
            driver.find_element(By.XPATH,f'//*[@id="app"]/div[2]/div[2]/div[3]/div/div[2]/div[1]/section[2]/div[{j}]/div[2]/div[{i}]/div[2]/div').click()
            #driver.execute_script("arguments[0].click();",element)
            n = driver.window_handles  # 这个时候会生成一个新窗口或新标签页的句柄，代表这个窗口的模拟driver
            #print('当前句柄: ', n)  # 会打印所有的句柄
            driver.switch_to.window(n[-1])
            time.sleep(3)
            driver.close()
            driver.switch_to.window(n[0])
    else:
        driver.quit()
        driver.get(url)
        driver.quit()
        print('end')



