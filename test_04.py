from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()

driver.maximize_window()

site_url="https://store.steampowered.com/?l=turkish"
driver.get(site_url)
sleep(3)

"""
game_name=driver.find_element(By.CLASS_NAME,"tab_item_title").text
print(f"oyun adı: {game_name}")
sleep(2)

"""
game_name=driver.find_elements(By.CLASS_NAME,"tab_item_title") 
"""
game_name[0]
game_name[-1] 
"""
print(f"oyun adları : {game_name}.text")
sleep(2)

 


driver.quit()
