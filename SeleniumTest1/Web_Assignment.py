import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class MyfirstTC(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # first_TestCase Search a video
    def test_search(self):
        self.driver.get("https://youtube.com")
        self.driver.find_element_by_id("search").send_keys("python")
        self.driver.find_element_by_id("search-icon-legacy").click()

    # second_TestCase playack a video
    def test_playback(self):
        self.driver.get("https://youtube.com")
        self.driver.find_element_by_id("search").send_keys("python")
        self.driver.find_element_by_id("search-icon-legacy").click()
        # click on the video for playback
        self.driver.find_element_by_xpath("(//*[@id='title-wrapper'])[2]").click()

    #Third_TestCase to upload a video
    def test_upload(self):
        self.driver.get("https://youtube.com")
        self.driver.find_element(By.XPATH, '//*[text()="Sign in"]').click()
        #Sign in to youtube
        self.driver.find_element_by_id("identifierId").send_keys("xyz@gmail.com")
        self.driver.find_element_by_id("identifierNext").click()
        self.driver.find_element_by_name("password").send_keys("12345#")
        self.driver.find_element_by_id("passwordNext").click()
        self.driver.find_element_by_class_name("style-scope ytd-masthead style-default")

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
if __name__=='__main__':
    unittest.main()
