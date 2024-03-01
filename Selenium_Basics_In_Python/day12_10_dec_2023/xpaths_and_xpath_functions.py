from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import format_exc
import time

# XPath : XML Path
# Xpath's are the way of locating elements in dom
# Two types of xpath's are : Absolute Xpaths & Relative Xpaths
# Absolute Xpath : This is the detailed path to locate a html element under dom
# Absolute Xpath Example : /html/head/body/h1
# Relative Xpath : This is the short path to locate an element under dom. In this paths element attributes are used to
# locate element
# Syntax 1: //tagName[@attribute='value]
# Syntax 2: //tagName[@attribute1='value1'][@attribute2='value2']
# Relative Xpath Example : *//input[@attribute='xyz']

# Setup webdriver & launch the browser
driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://magento.softwaretestingboard.com/")
    time.sleep(10)
except:
    print("Exception occurred : ", format_exc())
finally:
    pass

# Absolute XPath
print("Is logo displayed on UI?: ", driver.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/a/img").is_displayed())

# Relative XPath
print("Is logo displayed on UI?: ", driver.find_element(By.XPATH, "//*[@class='logo']").is_displayed())

# Relative XPath with multiple attributes
print(driver.find_element(By.XPATH, "//*[starts-with(@class,'level-')][@id='ui-id-3']/span").text)

# XPath Functions
# text() : This function requires entire text present on the web element; Syntax => //tagName[text()='Value']
print(driver.find_element(By.XPATH, "//*[text()='Women']").tag_name)

# contains() :
# This function can be used to locate element based on the partial text present in element's attribute value
# Syntax : //tagName[contains(@attribute,'value')]
print("Copyright Text On Footer : ", driver.find_element(By.XPATH, "//*[contains(@class,'pyri')]").text)

# starts-with() :
# This function can be used to locate element based on the initial string of the attribute's value
# Syntax : //tagName[starts-with(@attribute,'value')]
print("Content Heading on the Page : ", driver.find_element(By.XPATH, "//*[starts-with(@class,'content-')]").text)