from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")

try:
    #selecting frame by Index
    #driver.switch_to.frame(0)

    #selecting frame by ID
    driver.switch_to.frame("frame-one1434677811")
    print("Frame is selected..")
except:
    print("Error Occurred while selecting the Frame..")

try:
    driver.find_element_by_name("RESULT_TextField-1").send_keys("Akansh Jha")
    print("Name is entered in text box..")
except:
    print("Error Occurred while entering the value..")

#after performing operation, click on alert button, which is out of the frame.
    # try:
    #     driver.find_element(By.XPATH,"//button[text()='Click Me']").click()
    # except:
    #     print("Error occurred while accessing the element out of the frame..")
#this code will cause error, because we are trying to access the element(out of the frame). from inside of the
# rame

#to overcome this, we have to bring the focus out of the frame.

driver.switch_to.default_content() #this will bring the focus to main window.
print("Default content has been selected..")


try:
    driver.find_element(By.XPATH,"//button[text()='Click Me']").click()
    print("Element outside the frame, is accessed.")
except:
    print("Error occurred while accessing the element out of the frame..")

driver.quit()