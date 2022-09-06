**Use Python 3.10.6**

`解决 Executable path has been deprecated please pass in a Service object in Selenium Python
```from selenium.webdriver.chrome.service import Service
PATH=Service ("/Users/yiyi/Documents/driver/chromedriver")
driver= webdriver.Chrome(service=PATH)
driver.get("https://www.dcard.tw/f")````