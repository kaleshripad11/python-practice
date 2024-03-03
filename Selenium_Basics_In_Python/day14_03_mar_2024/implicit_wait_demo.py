# Program to demonstrate use of implicit waits in selenium
import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


class ImplicitWaitDemo:
    def __init__(self): # Constructor & it's body
        # Use add_experimental_option("detach", True) from ChromeOptions class to avoid auto close of browser window
        self.chrome_opt = ChromeOptions()
        self.chrome_opt.add_experimental_option("detach", True)
        # Pass above ChromeOptions class object to webdriver as "options" parameter's value
        self.driver = Chrome(options=self.chrome_opt)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(5)

    def login_to_orange_hrm(self):
        self.driver.find_element(By.XPATH, "//*[@name='username']").clear()
        self.driver.find_element(By.XPATH, "//*[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//*[@name='password']").clear()
        self.driver.find_element(By.XPATH, "//*[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//*[contains(@class,'login-button')]").click()
        if self.driver.find_element(By.XPATH, "//span/h6[text()='Dashboard']").text == "Dashboard" :
            print("Test Case Passed!!!")
        else:
            print("Test Case Failed!!!")


# Create object of ImplicitWaitDemo
iwd = ImplicitWaitDemo()
iwd.login_to_orange_hrm()
time.sleep(5)
iwd.driver.quit()




