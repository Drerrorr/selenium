# -*- coding =uft-8 -*-
# @TIME ： 2020/12/31 23:01
# @Author ： lkl
# @File ： demo3.py
# @Software: PyCharm
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from io import BytesIO
import time
import ddddocr
from PIL import Image

driver = webdriver.Chrome()
driver.get('https://exam.edu.foshan.gov.cn:49000/iexam/iexam/basis/KsLoginAction/toLogin.do')
time.sleep(1)
cookies = driver.get_cookies()#获取所有cookie
cookie_value = next((cookie['value'] for cookie in cookies if cookie['name'] == 'SESSION'), None)#筛选出SESSION的值
print(cookie_value)
src = driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[2]/td/form/div/div[2]/div[3]/img').get_attribute('src')#获取src
print(src)#获取图片的地址（src）
url=src
headers = {
    'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'SESSION=%s;common-secure' % cookie_value ,
    'Host':'exam.edu.foshan.gov.cn:49000',
    'Referer':'https://exam.edu.foshan.gov.cn:49000/iexam/iexam/basis/KsLoginAction/toLogin.do',
    'Sec-Fetch-Dest':'image',
    'Sec-Fetch-Mode':'no-cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'sec-ch-ua':'"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"'


}
response = requests.get(url,headers=headers)#使用特定headers请求
image_stream = BytesIO(response.content)
print(response.content)
img = Image.open(image_stream) # 使用Pillow打开图片
img.save('C:\\Users\\ASUS\\Desktop\\demo2\\pic\\randCode.jpg')# 保存图片为jpg格式


ocr = ddddocr.DdddOcr(beta=True)  # 切换为第二套ocr模型
image = open('C:\\Users\\ASUS\\Desktop\\demo2\\pic\\randCode.jpg', "rb").read()
result = ocr.classification(image)
print(result)
time.sleep(1000000)
'''
#将目标定向在账号框
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input').send_keys('123456789')
time.sleep(0.5)
#将目标定向在密码框
driver.find_element(By.NAME,'keyvalue').send_keys('123456789')
time.sleep(0.5)
'''

