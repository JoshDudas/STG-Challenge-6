import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class TestAutomatedChromeBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver_wait = WebDriverWait(self.driver, 10)
        self.model_list = []
        self.lotnumbers_returned = []

    def load_and_search_site(self):
        self.driver.get("https://copart.com")
        search_btn = self.driver.find_element(By.XPATH, "//button[@ng-click='search()']")
        search_field = self.driver.find_element(By.XPATH, "//input[@id='input-search']")

        search_field.send_keys("Nissan")
        search_btn.click()

    def wait_for_page_to_load(self):
        self.driver_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="serverSideDataTable"]')))
        self.driver_wait.until(
            expected_conditions.invisibility_of_element((By.XPATH, '//img[@src="/images/icons/loader.gif"]')))

    def get_search_results(self):
        models_returned = self.driver.find_elements(By.XPATH,
                                                    "//table[@id='serverSideDataTable']//span[@data-uname='lotsearchLotmodel']")
        self.lotnumbers_returned = self.driver.find_elements(By.XPATH,
                                                        "//table[@id='serverSideDataTable']//a[@data-uname='lotsearchLotnumber']")
        for model in models_returned:
            self.model_list.append(model.text)

    def go_to_specific_model_page(self):
        try:
            list_position = self.model_list.index("SKYLINE")
            skyline_lotnumber = self.lotnumbers_returned[list_position]
            skyline_lotnumber.click()
            self.driverwait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//label[@data-uname="lotdetailTitledescription"]')))
        except ValueError:
            print("Model SKYLINE not found (see screenshot)")
            self.driver.save_screenshot("challenge_6_valueError_screenshot.png")


    def test_getSkyLine(self):
        self.load_and_search_site()
        self.wait_for_page_to_load()
        self.get_search_results()
        self.go_to_specific_model_page()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
