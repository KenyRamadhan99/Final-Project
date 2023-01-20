import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestDashboard(unittest.TestCase):

    def setUp(self):
        self.manage = webdriver.Chrome(ChromeDriverManager().install())

    def test_search_positive_with_name(self):
        manage = self.manage
        manage.get("https://itera-qa.azurewebsites.net/")  # buka situs
        manage.maximize_window()
        time.sleep(3)
        manage.find_element(By.XPATH, "//*/form/ul/li[2]/a").click()
        time.sleep(3)
        manage.find_element(By.ID, "Username").send_keys("derandals")
        time.sleep(2)
        manage.find_element(By.ID, "Password").send_keys("Ramadhan1998")
        time.sleep(2)
        manage.find_element(By.NAME, "login").click()
        time.sleep(3)
        manage.find_element(By.XPATH, "//*[@id='searching']").send_keys("sarankumar")
        time.sleep(1)
        manage.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(2)

        response_data = manage.find_element(By.XPATH, "//*/tbody/tr[2]/td[1]").text
        self.assertEqual(response_data, "sarankumar")

    def test_search_negative_with_name(self):
        manage = self.manage
        manage.get("https://itera-qa.azurewebsites.net/")  # buka situs
        manage.maximize_window()
        time.sleep(3)
        manage.find_element(By.XPATH, "//*/form/ul/li[2]/a").click()
        time.sleep(3)
        manage.find_element(By.ID, "Username").send_keys("derandals")
        time.sleep(2)
        manage.find_element(By.ID, "Password").send_keys("Ramadhan1998")
        time.sleep(2)
        manage.find_element(By.NAME, "login").click()
        time.sleep(3)
        manage.find_element(By.XPATH, "//*[@id='searching']").send_keys("asdasdad")
        time.sleep(1)
        manage.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(2)

        response_data = manage.find_element(By.XPATH, "//*/tbody/tr[2]/td").text
        self.assertEqual(response_data, "No Match")


if __name__ == '__main__':
    unittest.main()