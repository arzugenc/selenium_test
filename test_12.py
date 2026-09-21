from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

wait = WebDriverWait(driver, 10)

close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.tox-notifications-container button[aria-label='Close']")))
close_button.click()

wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))

editor_body = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
editor_body.clear()

message = "Selenium testi basariyla tamamlandi!"
editor_body.send_keys(message)

assert editor_body.text == message

driver.switch_to.default_content()

header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
assert "An iFrame containing the TinyMCE WYSIWYG Editor" in header.text

driver.quit()