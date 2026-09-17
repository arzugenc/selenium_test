from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()

driver.maximize_window()

site_url="https://tr.wikipedia.org/wiki/Anasayfa"
driver.get(site_url)
sleep(2)

driver.find_element(By.XPATH,'//*[@id="mp-itn"]/ul/li[3]').click()
sleep(2)

driver.quit()





