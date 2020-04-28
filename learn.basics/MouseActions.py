import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Register.html")
time.sleep(2)

switchTo = driver.find_element_by_xpath("//a[text()='SwitchTo']")
windows_e = driver.find_element_by_xpath("//a[text()='Windows']")
print("ActionChains object is created..")
act = ActionChains(driver)
print("Mouse Hovering..")

#mouse Hover
act.move_to_element(switchTo).move_to_element(windows_e).click().perform()
time.sleep(3)

#double click
#driver.get("http://testautomationpractice.blogspot.com/")
time.sleep(2)
#copyText = driver.find_element_by_xpath("//button[text()='Click Me']")

act.double_click(switchTo).perform()
time.sleep(3)

#Right Click
act.context_click(switchTo).perform()
# driver.save_screenshot("../newscreenshots")
driver.quit()