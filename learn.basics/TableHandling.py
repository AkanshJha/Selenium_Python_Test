from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")

num_of_rows = len(driver.find_elements_by_xpath("//table[@name='BookTable']/tbody/tr"))
num_of_cols = len(driver.find_elements_by_xpath("//table[@name='BookTable']/tbody/tr[1]/th"))

print("Number of rows : ",num_of_rows)
print("Number of Columns : ", num_of_cols)

print("Extracted table data is given below - \n")
for c in range(1, num_of_cols+1):
    val = driver.find_element_by_xpath("//table[@name='BookTable']/tbody/tr[1]/th[{}]".format(c)).text
    print(val, end=" | ")
print()
for r in range(2, num_of_rows+1):
    for c in range(1, num_of_cols+1):
        val = driver.find_element_by_xpath("//table[@name='BookTable']/tbody/tr[{}]/td[{}]".format(r,c)).text
        print(val, end=" | ")
    print()

driver.quit()