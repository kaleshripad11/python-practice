# Syntax : By.<Locator_Name>, "value"
# Example : By.CSS_SELECTOR, "input[type='email']"

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://only-testing-blog.blogspot.com/2014/01/")

print(driver.find_element(By.TAG_NAME, "h3").text) #TextBox




