

# Js DOM can access any elements on web page just like how selenium does
# selenium have a method to execute javascript code in it
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
time.sleep(5)

# Implementation of JavaScript Executor:
driver.find_element_by_name("name").send_keys("Angular Application site")
print(driver.find_element_by_name("name").get_attribute("value"))  # To get inputted text
print(driver.execute_script('return document.getElementsByName("name")[0].value'))  # To get inputted text
shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")  # To scroll 0 to highest

# Print displayed text on the page:
print(driver.find_element_by_class_name("text-white").text)  # To get inbuilt text
time.sleep(3)

# Assertion1: True statement
assert "Copyright © ProtoCommerce 2018" == driver.find_element_by_class_name("text-white").text

# Assertion2: Untrue statement
assert not "A Copyright © ProtoCommerce 2018" == driver.find_element_by_class_name("text-white").text

driver.close()

