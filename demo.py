from selenium import webdriver
import time
import ddddocr
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://pg.eeagd.edu.cn/ks/h5/index.html#/xgk/ggxx')
driver.implicitly_wait(10)
login= driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div[1]/ul/li[2]')
login.click()
driver.find_element(By.XPATH,'//*[@id="username"]').send_keys('###########')
time.sleep(2)
for _ in range(3):
    #将目标定向在密码框
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('###########')
    time.sleep(2)
    element = driver.find_element(By.XPATH,'//*[@id="randomImage"]')
    element.screenshot('C:\\Users\\ASUS\\Desktop\\demo2\\pic\\randCode.jpg')
    ocr = ddddocr.DdddOcr(beta=True)  # 切换为第二套ocr模型
    image = open('C:\\Users\\ASUS\\Desktop\\demo2\\pic\\randCode.jpg', "rb").read()
    result = ocr.classification(image)
    print(result)
    #将目标定向在账号框
    driver.find_element(By.XPATH,'//*[@id="addcode"]').send_keys(result)
    time.sleep(0.5)
    button = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div[2]/div/div[1]/form/div[4]/button[1]')
    button.click()
    time.sleep(2)
    success = driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div/span[2]').text
    if success == '退出':
        print('登录成功')
        break
    else:
        print('重新登陆')
time.sleep(100)