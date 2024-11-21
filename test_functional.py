import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ProvaAplicacioFlask(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5000/")

    def test_suma(self):
        driver = self.driver
        numero1 = driver.find_element(By.ID, "number1")
        numero2 = driver.find_element(By.ID, "number2")
        numero1.send_keys("5")
        numero2.send_keys("10")
        numero2.send_keys(Keys.RETURN)
        
        resultat = driver.find_element(By.ID, "result").get_attribute("value")
        self.assertEqual(resultat, "15.0")

    def test_invalid_input(self):
        driver = self.driver
        numero1 = driver.find_element(By.ID, "number1")
        numero2 = driver.find_element(By.ID, "number2")
        numero1.send_keys("abc")
        numero2.send_keys("xyz")
        numero2.send_keys(Keys.RETURN)
        
        error_message = driver.find_element(By.XPATH, "//p[@style='color: red;']").text
        self.assertEqual(error_message, "Tots els camps han de contenir números vàlids!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()