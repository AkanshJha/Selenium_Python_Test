from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
drpdwn = Select(driver.find_element_by_id("RESULT_RadioButton-9"))

drpdwn.select_by_visible_text("Morning")
time.sleep(2)
print("1")
drpdwn.select_by_index(2)
time.sleep(2)
print("2")
drpdwn.select_by_value("Radio-2")
time.sleep(2)
print("3")

all_options = drpdwn.options
print(len(drpdwn.options))
for option in all_options:
    print(option.text)
driver.quit()

