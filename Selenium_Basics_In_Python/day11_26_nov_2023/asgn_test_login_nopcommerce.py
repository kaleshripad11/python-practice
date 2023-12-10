import threading

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(10)
driver.get("https://admin-demo.nopcommerce.com/login")
#driver.find_element(By.XPATH, "//a[normalize-space()='Log in']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='email']").clear()
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("admin@yourstore.com")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").clear()
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
exp_window_title = "Dashboard / nopCommerce administration"
if exp_window_title == driver.title:
    print("Test Passed!!")
else:
    print("Test Failed!!",driver.title)
