import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import test_login
from test_login import TestLoginRegister


class testEditData(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_edit_data_name(self):
        driver = self.driver
        TestLoginRegister.test_Login(self)
        time.sleep(3)
        searching = driver.find_element(By.XPATH, "//*/tbody/tr[2]/td[1]").text
        driver.find_element(By.NAME, "searching").send_keys(searching)
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/form/input[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/tr[2]/td[7]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.ID, "Name").clear()
        driver.find_element(By.ID,"Name").send_keys("Patsy Artefak")
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/div[7]/div/input").click()
        time.sleep(3)
        driver.find_element(By.NAME, "searching").send_keys("Patsy Artefak")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)

        response_edit = driver.find_element(By.XPATH,"//*/tbody/tr[2]/td[1]").text
        self.assertEqual(response_edit, "Patsy Artefak")

    def test_edit_data_company(self):
        driver = self.driver
        TestLoginRegister.test_Login(self)
        time.sleep(3)
        searching = driver.find_element(By.XPATH, "//*/tbody/tr[2]/td[1]").text
        driver.find_element(By.NAME, "searching").send_keys(searching)
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/form/input[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/tr[2]/td[7]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.ID,"Company").clear()
        driver.find_element(By.ID,"Company").send_keys("Frogobox")
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/div[7]/div/input").click()
        time.sleep(3)
        driver.find_element(By.NAME, "searching").send_keys("Patsy Artefak")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)

        response_edit = driver.find_element(By.XPATH,"//*/tbody/tr[2]/td[2]").text
        self.assertEqual(response_edit, "Frogobox")

    def test_edit_data_address(self):
        driver = self.driver
        TestLoginRegister.test_Login(self)
        time.sleep(3)
        searching = driver.find_element(By.XPATH, "//*/tbody/tr[2]/td[1]").text
        driver.find_element(By.NAME, "searching").send_keys(searching)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/tr[2]/td[7]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.ID, "Address").clear()
        driver.find_element(By.ID, "Address").send_keys("asber23")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/div[7]/div/input").click()
        time.sleep(3)
        driver.find_element(By.NAME, "searching").send_keys("Patsy Artefak")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)

        response_edit = driver.find_element(By.XPATH, "//*/tbody/tr[2]/td[3]").text
        self.assertEqual(response_edit, "asber23")

    def test_edit_data_city(self):
        driver = self.driver
        TestLoginRegister.test_Login(self)
        time.sleep(3)
        searching = driver.find_element(By.XPATH, "//*/tbody/tr[2]/td[1]").text
        driver.find_element(By.NAME, "searching").send_keys(searching)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/tr[2]/td[7]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.ID, "City").clear()
        driver.find_element(By.ID, "City").send_keys("bandung")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/div[7]/div/input").click()
        time.sleep(3)
        driver.find_element(By.NAME, "searching").send_keys("Patsy Artefak")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)

        response_edit = driver.find_element(By.XPATH, "//*/tbody/tr[2]/td[4]").text
        self.assertEqual(response_edit, "bandung")

    def test_edit_data_phone(self):
        driver = self.driver
        TestLoginRegister.test_Login(self)
        time.sleep(3)
        searching = driver.find_element(By.XPATH, "//*/tbody/tr[2]/td[1]").text
        driver.find_element(By.NAME, "searching").send_keys(searching)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/tr[2]/td[7]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.ID, "Phone").clear()
        driver.find_element(By.ID, "Phone").send_keys("123123123123")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/div[7]/div/input").click()
        time.sleep(3)
        driver.find_element(By.NAME, "searching").send_keys("Patsy Artefak")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)

        response_edit = driver.find_element(By.XPATH, "//*/tbody/tr[2]/td[5]").text
        self.assertEqual(response_edit, "123123123123")

    def test_edit_data_email(self):
        driver = self.driver
        TestLoginRegister.test_Login(self)
        time.sleep(3)
        searching = driver.find_element(By.XPATH, "//*/tbody/tr[2]/td[1]").text
        driver.find_element(By.NAME, "searching").send_keys(searching)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/tr[2]/td[7]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.ID, "Email").clear()
        driver.find_element(By.ID, "Email").send_keys("derandals@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/div[7]/div/input").click()
        time.sleep(3)
        driver.find_element(By.NAME, "searching").send_keys("Patsy Artefak")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)

        response_edit = driver.find_element(By.XPATH, "//*/tbody/tr[2]/td[6]").text
        self.assertEqual(response_edit, "derandals@gmail.com")

    def test_edit_data_cancel_update(self):
        driver = self.driver
        TestLoginRegister.test_Login(self)
        time.sleep(3)
        searching = driver.find_element(By.XPATH, "//*/tbody/tr[2]/td[1]").text
        driver.find_element(By.NAME, "searching").send_keys(searching)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/tr[2]/td[7]/a[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/div/a").click()




unittest.main()