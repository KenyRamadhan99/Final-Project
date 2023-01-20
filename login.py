import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginRegister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Login_success(self):
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

    def test_Login_ignore_lettercase(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*/form/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element(By.ID, "Username").send_keys("derandALs")
        time.sleep(2)
        driver.find_element(By.ID, "Password").send_keys("Ramadhan1998")
        time.sleep(2)
        driver.find_element(By.NAME, "login").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
        self.assertEqual(response_data, "Wrong username or password")

    def test_Login_invalid_username(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*/form/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element(By.ID, "Username").send_keys("derand")
        time.sleep(2)
        driver.find_element(By.ID, "Password").send_keys("Ramadhan1998")
        time.sleep(2)
        driver.find_element(By.NAME, "login").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
        self.assertEqual(response_data, "Wrong username or password")

    def test_Login_invalid_password(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*/form/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element(By.ID, "Username").send_keys("derandals")
        time.sleep(2)
        driver.find_element(By.ID, "Password").send_keys("Ramadhan1")
        time.sleep(2)
        driver.find_element(By.NAME, "login").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
        self.assertEqual(response_data, "Wrong username or password")
  
    def test_Login_null_username(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*/form/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element(By.ID, "Username").send_keys("")
        time.sleep(2)
        driver.find_element(By.ID, "Password").send_keys("Ramadhan1998")
        time.sleep(2)
        driver.find_element(By.NAME, "login").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
        self.assertEqual(response_data, "Wrong username or password")

    def test_Login_null_password(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*/form/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element(By.ID, "Username").send_keys("derandals")
        time.sleep(2)
        driver.find_element(By.ID, "Password").send_keys("")
        time.sleep(2)
        driver.find_element(By.NAME, "login").click()
        time.sleep(3)

        response_data = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
        self.assertEqual(response_data, "Wrong username or password")
unittest.main()          
          