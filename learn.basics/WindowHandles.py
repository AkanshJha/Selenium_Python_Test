import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Windows.html")

parent_window = driver.current_window_handle
print("Parent Window is - ",parent_window)

#click to open new window
driver.find_element_by_xpath("//button[contains(text(),'click')]").click()

#for popped out window, click on this too.
driver.find_element_by_xpath("//a[contains(text(),'Open New Seperate Windows')]").click()
time.sleep(1)
#click to open new window
driver.find_element_by_xpath("(//button[contains(text(),'click')])[2]").click()

#for opening multiple windows, click on this too
driver.find_element_by_xpath("//a[contains(text(),'Open Seperate Multiple Windows')]").click()
time.sleep(1)
#click to open new window
driver.find_element_by_xpath("(//button[contains(text(),'click')])[3]").click()



all_tabs = driver.window_handles
print("Number of total opened tabs in the browser : ",len(all_tabs))

print("Printing the windows' values : ")
for curr in all_tabs:
    print(curr)
expected_title = "Index"

for wd in all_tabs:
    if wd != parent_window:
        try:
            driver.switch_to.window(wd)
            time.sleep(3)
            print("new window '{}' is selected..".format(wd))
            print("Current title is '{}'.".format(driver.title))
            # if driver.title == expected_title:
            #     print("Finally, Tab, with title '{}' is selected..".format(expected_title))
            #     break;
        except:
            print("Some error occurred..")


print("Selecting the Parent window finally - ")
driver.switch_to.window(parent_window)
time.sleep(3)
driver.quit()