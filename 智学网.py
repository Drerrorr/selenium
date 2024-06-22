from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import pytesseract
from PIL import Image
import requests
from io import BytesIO
import time
import cv2
driver = webdriver.Chrome()
driver.get('https://www.zhixue.com/login.html')
driver.find_element(By.XPATH,'/html/body/div[9]/div[1]/div[2]/div/div[4]/input[1]').send_keys('123456789')
driver.find_element(By.XPATH,'/html/body/div[9]/div[1]/div[2]/div/div[4]/input[2]').send_keys('123456789')
driver.find_element(By.ID,'signup_button').click()
src = driver.find_element(By.TAG_NAME,'signup_button').get_attribute('src')
print(src)
captcha_url = src    #获取图片的地址（src）
time.sleep(200000)
