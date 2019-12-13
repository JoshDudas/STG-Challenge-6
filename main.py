import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class TestAutomatedChromeBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_getSkyLine(self):
        self.driver.get("https://copart.com")
        driverwait = WebDriverWait(self.driver, 10)

        driverwait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@ng-click='search()']")))

        search_btn = self.driver.find_element(By.XPATH, "//button[@ng-click='search()']")
        search_field = self.driver.find_element(By.XPATH, "//input[@id='input-search']")

        search_field.send_keys("Nissan")
        search_btn.click()

        models_returned = self.driver.find_elements(By.XPATH, "//table[@id='serverSideDataTable']//div[")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
