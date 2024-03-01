import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Application or Basic commands
# get() => Open web url using [Ex : driver.get("url")]
driver.get("https://demo.openmrs.org/openmrs/login.htm")

# title => Get window title [Ex : driver.title]
print("Browser window title : ", driver.title)

# current_url => Print current url present in the URL bar [Ex : driver.current_url]
print("Current URL : ",driver.current_url)

# page_source => Print page source [Ex : driver.page_source]
print("Entire page source : ", driver.page_source.strip())

# Conditional Commands[Returns boolean values]
# is_displayed() => Can be used to check if an element is present or not
print("Is logo displayed on UI?: ", driver.find_element(By.XPATH, "//*[contains(@src,'Logo')]").is_displayed())

# is_enabled() => Can be used to check if an element is enabled or not
print("Is UserName field enabled on UI?: ", driver.find_element(By.ID, "username").is_enabled())

# is_selected() => Can be used to check if an element is selected or not[Mostly used in dropdowns
time.sleep(5)
print("Is session 'Laboratory' selected : ", driver.find_element(By.XPATH, "//*/li[@id='Laboratory']").is_selected())


