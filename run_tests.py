
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FlaskAppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://127.0.0.1:5000")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_addition(self):
        driver = self.driver
        number1 = driver.find_element_by_id("number1")
        number2 = driver.find_element_by_id("number2")
        number1.send_keys("10")
        number2.send_keys("20")
        number2.send_keys(Keys.RETURN)
        result = driver.find_element_by_id("result").get_attribute("value")
        self.assertEqual(result, "30.0")

    def test_invalid_input(self):
        driver = self.driver
        number1 = driver.find_element_by_id("number1")
        number2 = driver.find_element_by_id("number2")
        number1.send_keys("abc")
        number2.send_keys("20")
        number2.send_keys(Keys.RETURN)
        error = driver.find_element_by_id("error").text
        self.assertEqual(error, "Tots els camps han de contenir números vàlids!")

if __name__ == "__main__":
    unittest.main()