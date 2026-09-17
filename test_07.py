from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()

driver.maximize_window()

site_url="https://the-internet.herokuapp.com/javascript_alerts"
driver.get(site_url)
sleep(2)

#//*[@id="content"]/div/ul/li[1]/button
#//*[@id="content"]/div/ul/li[2]/button
#//*[@id="content"]/div/ul/li[3]/button


"""driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[1]/button').click()
sleep(3)

site_alert=Alert(driver)
site_alert.accept()
sleep(2)

alert_result=driver.find_element(By.ID,'result')
print(alert_result.text)
sleep(3)
"""


"""driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[2]/button').click()
sleep(3)

site_alert=Alert(driver)
site_alert.dismiss()
sleep(2)

alert_result=driver.find_element(By.ID,'result')
print(alert_result.text)
sleep(3)"""


driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()
sleep(3)

site_alert=Alert(driver)
site_alert.send_keys("python")
site_alert.accept()
sleep(2)

alert_result=driver.find_element(By.ID,'result')
print(alert_result.text)
sleep(3)


driver.quit()
