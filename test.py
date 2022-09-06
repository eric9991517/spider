# 引入啟動瀏覽器相關套件
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 套件位置(User Chrome)
PATH=Service ("/Users/yiyi/Documents/driver/chromedriver")
driver= webdriver.Chrome(service=PATH)
# 使用Dacrd網站做範例
driver.get("https://www.dcard.tw/f")
search = driver.find_element(By.NAME,"query")
# 清除預設文字
search.clear()
search.send_keys("軟體工程師")
search.send_keys(Keys.RETURN)

# Explicit Waits（明確等待）
WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sc-f860e6e9-1"))
)

# 讀取標題
titles=driver.find_elements(By.CLASS_NAME,"sc-c384d921-3")

for title in titles:
    print(title.text)

time.sleep(5)
driver.quit()