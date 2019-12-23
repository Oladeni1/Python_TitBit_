
import time

from selenium import webdriver

# Locators cheatSheet:
# CSS Syntax -> tagname[attribute ='value'] or [attribute* = 'value'] or input#IDvalue
# XPATH Syntax -> //tagname[@attribute = 'value'] or //*[contains(@attribute, 'value')]

# Launch Browser
# driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")

driver = webdriver.Firefox(executable_path= "C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\geckodriver.exe")
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
print(driver.title)
print(driver.current_url)

driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder = 'From']").send_keys("del")
time.sleep(2)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(cities))
for city in cities:
    if city.text == "Del Rio, United States":
        city.click()
        break
time.sleep(5)

# Destination city:
driver.find_element_by_xpath("//p[text()='Delhi, India']").click()
time.sleep(10)
driver.close()