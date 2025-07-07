from selenium import webdriver
import time
import ddddocr
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://exam.edu.foshan.gov.cn:49000/iexam/iexam/basis/KsLoginAction/toLogin.do')
driver.implicitly_wait(4)
element = driver.find_element(By.XPATH,'//*[@id="ks_randImage"]')
element.screenshot('C:\\Users\\ASUS\\Desktop\\demo2\\pic\\randCode.jpg')
ocr = ddddocr.DdddOcr(beta=True)  # 切换为第二套ocr模型
image = open('C:\\Users\\ASUS\\Desktop\\demo2\\pic\\randCode.jpg', "rb").read()
result = ocr.classification(image)
print(result)
#将目标定向在账号框
driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[2]/td/form/div/div[2]/div[1]/input').send_keys('123456789')
time.sleep(0.5)
#将目标定向在密码框
driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[2]/td/form/div/div[2]/div[2]/input').send_keys('123456789')
time.sleep(0.5)
driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[2]/td/form/div/div[2]/div[3]/input').send_keys(result)
time.sleep(0.5)
button = driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[2]/td/form/div/div[4]/button')
button.click()
time.sleep(100)
