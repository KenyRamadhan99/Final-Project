from selenium import webdriver
import unittest
import time
from random_username.generate import generate_username
import call
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()


class TestCreate(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_create_new_data_success(self): 
        browser = self.browser
        driver.maximize_window 
        call.test_login_success(self) # ini manggil method login 
        time.sleep(2)

        # jalanin test case login yang diatas begitu udah login,click button create
        browser.find_element(By.XPATH,"/html/body/div/div/p[1]/a").click() 
        time.sleep(2)

        # dibawah ini untuk input form 
        browser.find_element(By.XPATH,"//*[@id='Name']").send_keys(generate_username)
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='Company']").send_keys("SanberCode") 
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='Address']").send_keys("Jakarta") 
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='City']").send_keys("Jakata") 
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='Phone']").send_keys("696969696") 
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='Email']").send_keys("test@testing.com") 
        time.sleep(2)
        
        #submit data 
        browser.find_element(By.XPATH,"/html/body/div/form/div/div[7]/div/input" ).click() #klik submit
        time.sleep(2)

        #validasi data nya kita search data yang udah kita input 
        browser.find_element(By.XPATH,"//*[@id='searching']").send_keys("test@testing.com") 
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div/form/input[2]").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td[7]/a[2]").click()
        time.sleep(2)
        
        # Screenshot

        #kalo validasi sukses nanti bakal web scrapping isi data yang udah diinput ke console
        create_success = browser.find_element(By.XPATH,"/html/body/div/div").text
        time.sleep(2)
        print(create_success)

    def test_create_new_data_failed(self): 
        browser = self.browser 
        call.test_login_success(self) # ini manggil method login 
        time.sleep(2)

        # jalanin test case login yang diatas begitu udah login,click button create
        browser.find_element(By.XPATH,"/html/body/div/div/p[1]/a").click() 
        time.sleep(2)

        # dibawah ini untuk input form 
        browser.find_element(By.XPATH,"//*[@id='Name']").send_keys("")
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='Company']").send_keys("") 
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='Address']").send_keys("") 
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='City']").send_keys("") 
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='Phone']").send_keys("") 
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='Email']").send_keys("") 
        time.sleep(2)
        
        #submit data 
        browser.find_element(By.XPATH,"/html/body/div/form/div/div[7]/div/input" ).click() #klik submit
        time.sleep(2)

       
        
        # Screenshot

           
        # def tearDown(self): 
        #     self.browser.close() 

if __name__ == "__main__": 
    unittest.main()          
          


    
