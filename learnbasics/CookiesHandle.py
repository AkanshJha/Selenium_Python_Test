from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.amazon.in/")

#get al the cookies created by browser
cookies = driver.get_cookies()
print(len(cookies))

driver.quit()