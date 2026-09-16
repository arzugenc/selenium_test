from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
driver.maximize_window()

site_url="https://www.trendyol.com/"
driver.get(site_url)
sleep(4)


driver.execute_script("window.open('https://www.udemy.com/?utm_audience=mx&gad_source=1','_blank');")
sleep(4)

driver.execute_script("window.open('https://www.btkakademi.gov.tr/','_blank');")
sleep(4)

driver.switch_to.window(driver.window_handles[0])
sleep(4)

driver.close()
sleep(4)

driver.quit()