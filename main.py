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

        driverwait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//table[@id='serverSideDataTable']//a[@data-uname='lotsearchLotnumber']")))

        models_returned = self.driver.find_elements(By.XPATH, "//table[@id='serverSideDataTable']//span[@data-uname='lotsearchLotmodel']")
        lotnumbers_returned = self.driver.find_elements(By.XPATH, "//table[@id='serverSideDataTable']//a[@data-uname='lotsearchLotnumber']")

        model_list = []

        for model in models_returned:
            model_list.append(model.text)

        try:
            list_position = model_list.index("SKYLINE")
            skyline_lotnumber = lotnumbers_returned[list_position]
            skyline_lotnumber.click()
            driverwait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//label[@data-uname="lotdetailTitledescription"]')))
        except ValueError:
            print("Model SKYLINE not found (see screenshot)")
            self.driver.save_screenshot("challenge_6_valueError_screenshot.png")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
