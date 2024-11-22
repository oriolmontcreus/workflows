import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class TestWebApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = Service("/usr/local/bin/chromedriver")
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.get("http://127.0.0.1:5000/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

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

    def test_subtraction(self):
        driver = self.driver
        numero1 = driver.find_element(By.ID, "number1")
        numero2 = driver.find_element(By.ID, "number2")
        numero1.send_keys("10")
        numero2.send_keys("5")
        numero2.send_keys(Keys.RETURN)
        
        resultat = driver.find_element(By.ID, "result").get_attribute("value")
        self.assertEqual(resultat, "5.0")

    def test_multiplication(self):
        driver = self.driver
        numero1 = driver.find_element(By.ID, "number1")
        numero2 = driver.find_element(By.ID, "number2")
        numero1.send_keys("5")
        numero2.send_keys("5")
        numero2.send_keys(Keys.RETURN)
        
        resultat = driver.find_element(By.ID, "result").get_attribute("value")
        self.assertEqual(resultat, "25.0")

    def test_division(self):
        driver = self.driver
        numero1 = driver.find_element(By.ID, "number1")
        numero2 = driver.find_element(By.ID, "number2")
        numero1.send_keys("10")
        numero2.send_keys("2")
        numero2.send_keys(Keys.RETURN)
        
        resultat = driver.find_element(By.ID, "result").get_attribute("value")
        self.assertEqual(resultat, "5.0")

if __name__ == "__main__":
    unittest.main()
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

if __name__ == "__main__":
    unittest.main()