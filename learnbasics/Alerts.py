from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")

#clicking on Alert Button
driver.find_element(By.XPATH,"//button[text()='Click Me']").click()
print("Clicking on Alert button")
time.sleep(2)

#clicking on OK button of Alert
#driver.switch_to_alert().accept()  # this systax has been deprecated and causes error
driver.switch_to.alert.accept()
print("Clicking on Alert-Accept button")
time.sleep(2)
#clicking on Alert Button
driver.find_element(By.XPATH,"//button[text()='Click Me']").click()
print("Clicking on Alert button")
time.sleep(2)

#clicking on Cancel button of Alert
#driver.switch_to_alert().dismiss()  #this systax has been deprecated and causes error.
driver.switch_to.alert.dismiss()
print("Clicking on Alert-Dismiss button")
time.sleep(2)

driver.quit()