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

site_url="https://dosya.co/"  
driver.get(site_url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "my_file_element")))

file_upload = driver.find_element(By.ID, "my_file_element")
file_path = "C:/Users/arzug/Desktop/selenium_test/test_08.py"
file_upload.send_keys(file_path)

driver.find_element(By.XPATH,'//*[@id="upload_controls"]/tbody/tr[4]/td[2]/input').click()

driver.find_element(By.XPATH, '//*[@id="tos_modal"]/div/div[2]/button[2]').click()



WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/table/tbody/tr[3]/td/div/div[1]')))

result=driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr[3]/td/div/div[1]')
print(result.text)


sleep(7)




driver.quit()