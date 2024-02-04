from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


def login_to_orange_hrm(user,password):
    time.sleep(2)
    # Finding element by NAME(name attribute's value)
    driver.find_element(By.NAME, "username").send_keys(user)
    driver.find_element(By.NAME, "password").send_keys(password)

    # Finding element by CLASS_NAME(class attribute's value)
    driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()


login_to_orange_hrm("Admin","admin123")

# Find element by XPATH(xml path to reach desired element on dom)
time.sleep(2)
driver.find_element(By.XPATH, "//li[6]/a/span").click()

# Ex 1: CSS_SELECTOR = 'tagName.className'
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input.orangehrm-firstname").send_keys("John")

time.sleep(2)
driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()


# Find element by CSS_SELECTOR
# Ex 1: CSS_SELECTOR = "tagName[attribute='value']"
# Ex 2: CSS_SELECTOR = "tagName#id"
# Ex 3: CSS_SELECTOR = "tagName#id[attribute='value']"
# Ex 4: CSS_SELECTOR = "tagName.className"
# Ex 5: CSS_SELECTOR = "tagName.className[attribute='value']"
