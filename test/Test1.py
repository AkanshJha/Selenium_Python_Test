from selenium import webdriver

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get("https:\\www.google.co.in")
driver.maximize_window()
driver.quit()