class CaptureScreenshot:
    def __init__(self, driver):
        self.driver = driver

    def capture_screenshot(self, filepath=""):
        # if filepath is not None:
        #     self.driver.save_screenshot(filepath)
        # else
        #     print("The path for the screenshot to be saved, is not given properly.")
        if filepath != "":
            try:
                self.driver.save_screenshot(filepath)
            except:
                print("some unexpected error occurred. Please check.")
        else:
            print("The path for the screenshot to be saved, is not given properly.\nPlease check.")
