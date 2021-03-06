import time
from learnbasics.CaptureScreenshot import CaptureScreenshot
from selenium import webdriver


driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
cs = CaptureScreenshot(driver)
driver.get("http://testautomationpractice.blogspot.com/")
time.sleep(2)
#Scroll down by Pixels
driver.execute_script("window.scrollBy(0,200)","")
time.sleep(2)
cs.capture_screenshot_in_png("C:/Users/deepa/Documents/test.png")
#scroll till an element
time.sleep(2)
email = driver.find_element_by_xpath("//email[text()='david@myemail.com']")
driver.execute_script("arguments[0].scrollIntoView();",email)
time.sleep(2)

#scroll till the end of the page
time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
cs.capture_screenshot_in_anyformat("C:/Users/deepa/Documents/filename.jpg")
time.sleep(2)

driver.quit()
