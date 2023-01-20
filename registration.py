import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegister(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #TC RC1 Access to Sign up page
    def test_a_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(1) > a").click() # klik tombol sign up
        time.sleep(2)

    #TC RC2 Access Sign up with input all field 
    def test_b_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(1) > a").click() # klik tombol sign up
        time.sleep(2)
        driver.find_element(By.ID,"FirstName").send_keys("Dwiky") # isi first name
        time.sleep(1)
        driver.find_element(By.ID,"Surname").send_keys("Priambodo") # isi surename
        time.sleep(1)
        driver.find_element(By.ID,"E_post").send_keys("Test") # isi e-post
        time.sleep(1)
        driver.find_element(By.ID,"Mobile").send_keys("0818692636") # isi mobile
        time.sleep(1)
        driver.find_element(By.ID,"Username").send_keys("dwikykiky123") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("try123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("try123") # isi confirm password
        time.sleep(1)
        driver.find_element(By.ID,"submit").click() # klik tombol submit
        time.sleep(3)

    #TC RC3 Access Sign up with input mandatory field only
    def test_c_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(1) > a").click() # klik tombol sign up
        time.sleep(2)
        driver.find_element(By.ID,"FirstName").send_keys("Dwiky") # isi first name
        time.sleep(1)
        driver.find_element(By.ID,"Surname").send_keys("Kiki") # isi surename
        time.sleep(1)
        driver.find_element(By.ID,"Username").send_keys("Test") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("try123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"submit").click() # klik tombol submit
        time.sleep(3)

    #TC SU4 Access Sign up without input field
    def test_d_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(1) > a").click() # klik tombol sign up
        time.sleep(2)
        driver.find_element(By.ID,"FirstName").send_keys("") # isi first name
        time.sleep(1)
        driver.find_element(By.ID,"Surname").send_keys("") # isi surename
        time.sleep(1)
        driver.find_element(By.ID,"E_post").send_keys("") # isi e-post
        time.sleep(1)
        driver.find_element(By.ID,"Mobile").send_keys("") # isi mobile
        time.sleep(1)
        driver.find_element(By.ID,"Username").send_keys("") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("") # isi confirm password
        time.sleep(1)
        driver.find_element(By.ID,"submit").click() # klik tombol submit
        time.sleep(3)
        
unittest.main()