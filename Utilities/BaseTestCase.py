import unittest
import json
import os
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #   SetUp is done based on the Driver Configuration Selection in TestConfiguration.json file.
        current_directory = (os.path.dirname(os.getcwd()))
        data = []
        with open(current_directory + '\\Utilities\TestConfiguration.json') as f:
            for line in f:
                data.append(json.loads(line))

        driver_config = data[0]

        if driver_config['Driver'] == 'Firefox':
            cls.driver = webdriver.Firefox()
        elif driver_config['Driver'] == 'Chrome':
            chrome_driver = (os.path.dirname(os.getcwd()) + "/Utilities/chromedriver")
            os.environ["webdriver.chrome.driver"] = chrome_driver
            cls.driver = webdriver.Chrome(chrome_driver)
        else:
            print('Invalid WebDriver Configuration in TestConfiguration.json file.')

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        return cls.driver
    def test_1(self):
        self.assertRegex()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
