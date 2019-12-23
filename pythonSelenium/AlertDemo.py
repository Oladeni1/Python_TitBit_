# Locators cheatSheet:
# CSS Syntax -> tagname[attribute ='value'] or [attribute* = 'value'] or input#IDvalue
# XPATH Syntax -> //tagname[@attribute = 'value'] or //*[contains(@attribute, 'value')]

# Launch Browser
import time

from selenium import webdriver

ValidationText = "Option2"

driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)

driver.find_element_by_css_selector("#name").send_keys(ValidationText)
driver.find_element_by_id("alertbtn").click()
time.sleep(3)
alert = driver.switch_to.alert
alertText = alert.text
assert ValidationText in alertText
alert.accept()
time.sleep(2)
driver.close()