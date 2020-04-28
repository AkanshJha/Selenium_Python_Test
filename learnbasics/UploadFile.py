import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

driver.switch_to.frame(0)
time.sleep(2)
upload_button = driver.find_element_by_name("RESULT_FileUpload-10")
driver.execute_script("arguments[0].scrollIntoView();",upload_button)
abs_filepath_str = "C:/Users/deepa/Documents/test.png"
upload_button.send_keys(abs_filepath_str)
time.sleep(4)
driver.quit()