from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("https://www.facebook.com")

print("Application tittle is ",driver.title)
print("Application URL is ",driver.current_url)

driver.close()