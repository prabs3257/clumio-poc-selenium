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
        # serv_obj = Service("/Users/prabhavchopra/Downloads/chromedriver_mac_arm64/chromedriver")
        # driver = webdriver.Chrome(service=serv_obj, options=options)
        global driver
        driver = webdriver.Remote( "http://localhost:4444", options=options);
    
       

    def test_first(self,setup):
        driver.get("https://www.google.com/")
        time.sleep(60)

        driver.find_element(By.ID, "APjFqb").send_keys("hello")
        print(driver.title)
        assert driver.title == "Google"
        
        driver.close()
       
        driver.quit()
        

    def test_second(self,setup):
        driver.get("https://www.youtube.com/")
        time.sleep(60)
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
        
# selenium_server_url = (f'http://{selenium_server_ip}:4444'
#                 if selenium_server_ip
#                 else test_data['selenium_node_url']
#             )

#             chrome_options = webdriver.ChromeOptions()
#             chrome_options.add_argument('--start-maximized')
#             chrome_options.add_argument('--browser.helperApps.neverAsk.saveToDisk=text/csv/zip')
#             chrome_options.add_argument('--no-sandbox')
#             chrome_options.headless = False

# chrome_options.set_capability('screen-resolution', '1920x1080')
#             capabilities = chrome_options.to_capabilities()
#             web_driver = webdriver.Remote(
#                 command_executor=selenium_server_url,
#                 desired_capabilities=capabilities,
#                 options=chrome_options,
#             )

# if test_data['browser'] == 'firefox':
#         if test_data['run_environment'] == 'local':
#             web_driver = webdriver.Firefox(executable_path=firefox.GeckoDriverManager().install())



             


