import time
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options


def setup_download_path(changed_download_path=""):
    if changed_download_path != "":
        chrome_options = Options()
        # chrome_options.add_experimental_option("prefs", {"download.default_directory": "{}".format(
        # changed_download_path)})
        chrome_options.add_argument("download.default_directory={}".format(changed_download_path))
        print("Preferences has been modified.")
        return chrome_options
    else:
        print("Invalid Path. Please check.")


def delete_file_if_exists(filepath=""):
    if filepath != "":
        try:
            if os.path.exists(filepath):
                print("File Exists")
                os.remove(filepath)
                print("file has been deleted")
            else:
                print("File does not exist.")
                return
        except:
            print("Could not delete the file. Please verify.")


# this is not working with the updated downloaded path
# chrome_opt = setup_download_path("D:\test download")
# driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe", options=chrome_opt)
downloaded_filepath = "C:/Users/deepa/Downloads/samplefile.pdf"
driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Windows.html")
ac = ActionChains(driver)

more = driver.find_element_by_xpath("//a[text()='More']")
file_download_option = driver.find_element_by_xpath("//a[text()='File Download']")
ac.move_to_element(more).move_to_element(file_download_option).click().perform()
time.sleep(2)
# click on download button
#downloaded_filepath = "C:/Users/deepa/Downloads/samplefile.pdf"
delete_file_if_exists(downloaded_filepath)
download_button = "//a[text()='Download']"
driver.find_element_by_xpath(download_button).click()
time.sleep(30)
if os.path.exists(downloaded_filepath):
    print("file has been downloaded successfully and available on ", downloaded_filepath)
else:
    print("File is not downloaded yet. Or some error occurred while downloading the file.")
driver.quit()
