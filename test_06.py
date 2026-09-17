from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chromedriver_autoinstaller.install()

driver=webdriver.Chrome()

driver.maximize_window()

site_url="https://tr.wikipedia.org/wiki/Anasayfa"
driver.get(site_url)
sleep(2)

"""driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")"""
"""driver.execute_script("window.scrollTo(document.documentElement.scrollHeight,0);")"""

driver.execute_script("window.scrollTo(0,800);")

"""driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)"""



sleep(3)

driver.quit()
