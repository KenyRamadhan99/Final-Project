import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginRegister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Login(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*/form/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element(By.ID, "Username").send_keys("derandals")
        time.sleep(2)
        driver.find_element(By.ID, "Password").send_keys("Ramadhan1998")
        time.sleep(2)
        driver.find_element(By.NAME, "login").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR, "body > div > div > h3").text
        self.assertEqual(response_data, "Welcome derandals")
