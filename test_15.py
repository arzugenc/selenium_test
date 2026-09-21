from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/hovers")

wait = WebDriverWait(driver, 10)
aksiyon = ActionChains(driver)

ilk_profil_resmi = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='figure'])[1]")))

aksiyon.move_to_element(ilk_profil_resmi).perform()

kullanici_adi = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='figcaption'])[1]/h5"))).text
assert kullanici_adi == "name: user1", "Hata: Ilk kullanici adi gorunmedi!"
print("Ilk profilin uzerine gelindi ve kullanici adi basariyla dogrulandi.")

profil_linki = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[text()='View profile'])[1]")))
assert profil_linki.is_displayed(), "Hata: Profil linki gorunur degil!"
print("Kullanici profili goruntuleme linki basariyla dogrulandi.")

driver.quit()