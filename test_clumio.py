from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pytest

class TestClumio():

    @pytest.fixture()
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        global driver
        driver = webdriver.Remote( "http://localhost:4444", options=options);
    
       

    def test_first(self,setup):
        driver.get("https://www.google.com/")
        print(driver.session_id)
        time.sleep(10)


        driver.find_element(By.ID, "APjFqb").send_keys("hello")
        print(driver.title)
        assert driver.title == "Google"
        
        driver.close()
       
        driver.quit()
        

    def test_second(self,setup):
        driver.get("https://www.youtube.com/")
        time.sleep(10)
        print(driver.title)
        assert driver.title == "YouTube"
        
        driver.close()
        driver.quit()

    def test_third(self,setup):
        driver.get("https://www.facebook.com/")
        print(driver.title)
        assert driver.title == "Facebook – log in or sign up"
        driver.close()
        driver.quit()
        


             


