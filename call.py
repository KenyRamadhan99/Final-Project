from selenium import webdriver
import time
import data
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_login_success(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://itera-qa.azurewebsites.net/Login") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"Username").send_keys(data.username) # isi usernam
        time.sleep(2)
        browser.find_element(By.ID,"Password").send_keys(data.password) # isi password
        time.sleep(2)
        browser.find_element(By.NAME,"login" ).click()
        time.sleep(2)