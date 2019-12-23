import time
from selenium import webdriver
# Locators cheatSheet:
# CSS Syntax -> tagname[attribute ='value'] or [attribute* = 'value'] or input#IDvalue
# XPATH Syntax -> //tagname[@attribute = 'value'] or //*[contains(@attribute, 'value')]

# Launch Browser
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\geckodriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)

driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_css_selector("input[name ='email']").send_keys("rahulshettyacademy.com")
driver.find_element_by_id("exampleCheck1").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(2)
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@type = 'submit']").click()
time.sleep(5)
driver.find_element_by_class_name("alert-success").is_displayed()
print(driver.find_element_by_xpath("//*[contains(@class,  'alert-success')]").text)

# Assertion/validation:
message = driver.find_element_by_xpath("//*[contains(@class,  'alert-success')]").text
assert "successfully" in message

time.sleep(5)
driver.close()

