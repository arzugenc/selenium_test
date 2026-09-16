from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
driver.maximize_window()

google_url="https://www.google.com/?hl=tr" 
driver.get(google_url)
sleep(2)

search_box=driver.find_element(By.CLASS_NAME,'gLFyf') 
sleep(2)

search_box.send_keys("python")
sleep(2)

search_box.send_keys(Keys.ENTER)
sleep(2)

driver.quit()
