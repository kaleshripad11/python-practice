# Program to demonstrate explicit wait
import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class ExplicitWaitDemo:
    def __init__(self):
        time.sleep(10)
        self.chrome_opt = ChromeOptions()
        self.chrome_opt.add_experimental_option("detach", True)
        self.driver = Chrome(options=self.chrome_opt)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login_to_orange_hrm(self):
        wait = WebDriverWait(self.driver, timeout=5)
        wait.until(ec.element_to_be_clickable(self.driver.find_element(By.XPATH, "//*[@name='username']")))
        self.driver.find_element(By.XPATH, "//*[@name='username']").clear()
        self.driver.find_element(By.XPATH, "//*[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//*[@name='password']").clear()
        self.driver.find_element(By.XPATH, "//*[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//*[contains(@class,'login-button')]").click()
        if self.driver.find_element(By.XPATH, "//span/h6[text()='Dashboard']").text == "Dashboard":
            print("Test Case Passed!!!")
        else:
            print("Test Case Failed!!!")


ewd = ExplicitWaitDemo()
ewd.login_to_orange_hrm()
time.sleep(3)
ewd.driver.quit()