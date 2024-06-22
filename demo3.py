# -*- coding =uft-8 -*-
# @TIME ： 2020/12/31 23:01
# @Author ： lkl
# @File ： demo3.py
# @Software: PyCharm
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import sklearn
import numpy
import wget
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import pytesseract
from PIL import Image
import requests
from io import BytesIO
import time
driver = webdriver.Chrome()
driver.get('https://exam.edu.foshan.gov.cn/iexamfs/KsLoginSuccessAction.action')
time.sleep(1)
pyautogui.keyDown('Enter')
src = driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/img').get_attribute('src')
print(src)
captcha_url = src    #获取图片的地址（src）
url = src
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Content-Type': 'application/json',
    'Accept' :'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Host': 'exam.edu.foshan.gov.cn',
    'Sec-Fetch-platform':'"Android"',
    'Sec-Fetch-Mode':'no-cors',
    'Sec-Fetch-Dest':'image',
    'Referer':'https://exam.edu.foshan.gov.cn/iexamfs/KsLoginSuccessAction.action',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'

}
response = requests.get(url,headers=headers)
if response.status_code == 200:
    # 使用BytesIO创建一个可读的二进制流
    image_stream = BytesIO(response.content)
    print(response.content)
    # 使用Pillow打开图片
    img = Image.open(image_stream)
    # 保存图片为BMP格式
    img.save('L:\pycham\pycharm demo\demo2\pic', 'BMP')
else:
    print('Failed to retrieve image')

'''
response = requests.get(captcha_url)
image_data = response.content
print(type(image_data))
image_bytes = bytes(image_data)
print(image_bytes[:8])
try:
    captcha_image = Image.open(
        BytesIO(image_data))
    captcha_image.show()
except IOError as e:
    print(e)


#将目标定向在账号框
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input').send_keys('123456789')
time.sleep(0.5)
#将目标定向在密码框
driver.find_element(By.NAME,'keyvalue').send_keys('123456789')
time.sleep(0.5)
'''

'''
captcha_url = src    #获取图片的地址（src）
response = requests.get(captcha_url)
captcha_image = Image.open(BytesIO(response.content))
text = pytesseract.image_to_string(captcha_image, lang='eng')
captcha_code = ''.join(filter(str.isalnum, text))
driver.find_element(By.NAME,'rand').send_keys(captcha_code)
time.sleep(0.5)
time.sleep(200000)
#driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[4]/td/img[1]').click()
'''
