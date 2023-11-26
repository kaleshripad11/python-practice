# Import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://demo.guru99.com/test/newtours/index.php")
driver.find_element(By.NAME, "userName").send_keys("mercury")
driver.find_element(By.NAME, "password").send_keys("mercury")
driver.find_element(By.NAME, "submit").click()

actual_success_msg = driver.title
if actual_success_msg == "Login Successfully":
    print("Test Passed!!!")
else:
    print("Test Failed!!!")

driver.close()