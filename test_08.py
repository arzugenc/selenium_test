from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()

driver.maximize_window()

site_url="https://the-internet.herokuapp.com/upload"
driver.get(site_url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "file-upload")))

file_upload = driver.find_element(By.ID, "file-upload")
file_path = "C:/Users/arzug/Desktop/selenium_test/test_04.py"
file_upload.send_keys(file_path)

driver.find_element(By.ID,"file-submit").click()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div/h3')))

result=driver.find_element(By.XPATH,'//*[@id="content"]/div/h3')
print(result.text)

#//*[@id="content"]/div/h3
sleep(3)

driver.quit()