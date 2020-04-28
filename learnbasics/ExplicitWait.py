from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
wait = WebDriverWait(driver,10)

driver.get("https://www.expedia.co.in/")
#click on fligh button
driver.find_element(By.XPATH,"//button[@data-lob='flight']").click()
print("Clicked on Flight..")

#set from and to
driver.find_element_by_xpath("(//span[text()='Flying from']/following-sibling::input)[1]").send_keys("PNQ")
driver.find_element_by_xpath("(//span[text()='Going to']/following-sibling::input)[1]").send_keys("DEL")
time.sleep(3)
print("Source and Destination are selected..")

#set departing date
driver.find_element_by_xpath("(//span[text()='Departing']/following-sibling::input[@placeholder='dd/mm/yyyy'])[2]").clear()
driver.find_element_by_xpath("(//span[text()='Departing']/following-sibling::input[@placeholder='dd/mm/yyyy'])[2]").send_keys("01/08/2020")
driver.find_element_by_xpath("(//span[text()='Departing']/following-sibling::input[@placeholder='dd/mm/yyyy'])[2]").send_keys(Keys.ESCAPE)
print("Departure Date is set..")

#set Return date
driver.find_element_by_xpath("(//span[text()='Returning']/following-sibling::input[@placeholder='dd/mm/yyyy'])[1]").clear()
driver.find_element_by_xpath("(//span[text()='Returning']/following-sibling::input[@placeholder='dd/mm/yyyy'])[1]").send_keys("16/08/2020")
driver.find_element_by_xpath("(//span[text()='Returning']/following-sibling::input[@placeholder='dd/mm/yyyy'])[1]").send_keys(Keys.ESCAPE)
print("Return Date is set..")

#Click on search button
driver.find_element_by_xpath("//button[@type = 'submit']/span[text()='Search']").click()
print("Clicked on search button..")
time.sleep(3)

filter_checkbox = wait.until(ec.element_to_be_clickable(By.XPATH,"(//input[@classes='filter-checkbox'])[2]"))

filter_checkbox.click()
driver.quit()