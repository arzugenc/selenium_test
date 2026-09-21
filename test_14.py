from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/dropdown")

wait = WebDriverWait(driver, 10)

dropdown_elementi = wait.until(EC.visibility_of_element_located((By.ID, "dropdown")))

secim_kutusu = Select(dropdown_elementi)

secim_kutusu.select_by_visible_text("Option 1")
secilen_metin = secim_kutusu.first_selected_option.text
assert secilen_metin == "Option 1", "Hata: Birinci secenek secilemedi!"
print("Birinci secenek basariyla secildi ve dogrulandi.")

secim_kutusu.select_by_value("2")
secilen_metin_2 = secim_kutusu.first_selected_option.text
assert secilen_metin_2 == "Option 2", "Hata: Ikinci secenek secilemedi!"
print("Ikinci secenek de deger uzerinden basariyla secildi ve dogrulandi.")

driver.quit()