import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome() 

amazon_url="https://www.amazon.com.tr/?&tag=trtxtgoabkde-21&ref=pd_sl_7r6v9rntlw_e&adgrpid=154611856018&hvpone=&hvptwo=&hvadid=674177764078&hvpos=&hvnetw=g&hvrand=1460131071119493291&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9243132&hvtargid=kwd-10573980&hydadcr=12932_2354400&mcid=b91d2f791c1635c295f4e0c69fca222b&hvocijid=1460131071119493291--&hvexpln=nav&language=tr_TR&gad_source=1"
time.sleep(2)
driver.get(amazon_url)
print(driver.title)
time.sleep(3)
driver.quit()
