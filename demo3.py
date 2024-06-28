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
import numpy as np
import os
driver = webdriver.Chrome()
driver.get('https://exam.edu.foshan.gov.cn/iexamfs/KsLoginSuccessAction.action')
time.sleep(1)
pyautogui.keyDown('Enter')
cookies = driver.get_cookies()
desired_cookie_name = 'your_cookie_name'
cookies_with_desired_name = [cookie for cookie in cookies if cookie['value'] == desired_cookie_name]
print(cookies)
print(cookies_with_desired_name)
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
    'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'SESSION=7f17f8ff-c71c-4fec-8b95-80da0d0cfae1; name=value'

}
response = requests.get(url,headers=headers)
image_stream = BytesIO(response.content)
print(response.content)
 # 使用Pillow打开图片
img = Image.open(image_stream)
# 保存图片为BMP格式
img.save('L:\\pycham\\pycharm demo\\demo2\\pic\\serialno.bmp', 'BMP')
image = Image.open('L:\\pycham\\pycharm demo\\demo2\\pic\\serialno.bmp')
image = image.convert('L')
image = np.asarray(image)
print(image.shape)
image = (image > 135) * 255
split_parts = [
    [36, 46],
    [51, 61],
    [68, 78],
    [84, 94]
]
letters = []
save_folder = 'L:\\pycham\\pycharm demo\\demo2\\pic1'
for part,idx in split_parts:

    letter = image[7:, part[0]: part[1]]
    letters.append(letter.reshape(10*23))
    file_path = os.path.join(save_folder, f'letter_{idx}.png')
'''
def load_dataset():
    X = []
    y = []

    for i in range(70):
        path = "./train/%d%d.png" % (i / 7, i % 7)
        pix = np.asarray(Image.open(path).convert("L"))
        X.append(pix.reshape(10*23))
        y.append(int(i / 7))
    return np.asarray(X), np.asarray(y)
'''

'''
#将目标定向在账号框
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input').send_keys('123456789')
time.sleep(0.5)
#将目标定向在密码框
driver.find_element(By.NAME,'keyvalue').send_keys('123456789')
time.sleep(0.5)
'''


