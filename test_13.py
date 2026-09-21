from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")

wait = WebDriverWait(driver, 10)

ana_pencere = driver.current_window_handle

tiklama_linki = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Click Here")))
tiklama_linki.click()

wait.until(EC.number_of_windows_to_be(2))

for pencere in driver.window_handles:
    if pencere != ana_pencere:
        driver.switch_to.window(pencere)
        break

yeni_sekme_basligi = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3"))).text
assert yeni_sekme_basligi == "New Window", "Hata: Yeni sekme basligi eslesmedi!"
print("Yeni sekme basariyla acildi ve dogrulandi.")

driver.close()

driver.switch_to.window(ana_pencere)

ana_sekme_basligi = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3"))).text
assert ana_sekme_basligi == "Opening a new window", "Hata: Ana sekme basligi eslesmedi!"
print("Ana sekmeye basariyla geri donuldu.")

driver.quit()