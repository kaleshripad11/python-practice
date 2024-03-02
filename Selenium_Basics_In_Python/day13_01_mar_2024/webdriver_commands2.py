import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()

# From selenium 4 web browsers will be closed automatically. To avoid auto close use ChromeOptions class
options.add_experimental_option("detach", True)

# Pass ChromeOptions object to webdriver reference. This will not allow browser window to be closed automatically
driver = Chrome(options=options)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)

# Perform login
driver.find_element(By.XPATH, "//*[@name='username']").clear()
driver.find_element(By.XPATH, "//*[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//*[@name='password']").clear()
driver.find_element(By.XPATH, "//*[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//*[contains(@class,'login-button')]").click()

# Navigate to another module after login
driver.find_element(By.XPATH, "//span[text()='Time']").click()
# Navigational commands
# back() => Navigate backward
time.sleep(2.5)
driver.back()

# forward() => Navigate forward
time.sleep(2.5)
driver.forward()

# refresh() => Refresh the page
time.sleep(3)
driver.refresh()

# Browser commands
# close() => Kill only the current webdriver session where webdriver was focused
# driver.close()

# quit() => Kill all the webdriver sessions
driver.quit()
