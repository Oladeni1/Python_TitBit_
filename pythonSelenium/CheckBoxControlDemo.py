# Locators cheatSheet:
# CSS Syntax -> tagname[attribute ='value'] or [attribute* = 'value'] or input#IDvalue
# XPATH Syntax -> //tagname[@attribute = 'value'] or //*[contains(@attribute, 'value')]

# Launch Browser
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)

checkboxes = driver.find_elements_by_xpath("//input[@type= 'checkbox']")

print(len(checkboxes))  # 3 checkboxes

for checkbox in checkboxes:
    print(checkbox.get_attribute("value"))  # Prints all checkbox options
    time.sleep(5)
    checkbox.click()  # All checkboxes clicked
    assert checkbox.is_selected()

    time.sleep(3)

driver.close()


