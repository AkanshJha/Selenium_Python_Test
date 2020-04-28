class CaptureScreenshot:
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, filepath):
        if filepath is not None:
            self.driver.save_