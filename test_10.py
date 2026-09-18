from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()

driver.maximize_window()

site_url="https://www.trendyol.com/"
driver.get(site_url)
sleep(2)

"""driver.save_screenshot("images1.png")"""
   
element=driver.find_element(By.CLASS_NAME,"just-for-you-slider")
element.screenshot("images2.png")



sleep(2)
driver.quit()