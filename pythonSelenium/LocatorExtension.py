import time

from selenium import webdriver

# Locators cheatSheet:
# CSS Syntax -> tagname[attribute ='value'] or [attribute* = 'value'] or input#IDvalue
# XPATH Syntax -> //tagname[@attribute = 'value'] or //*[contains(@attribute, 'value')]

# Launch Browser
driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://login.salesforce.com/")
print(driver.title)
print(driver.current_url)


driver.find_element_by_css_selector("#username").send_keys("olatunde@yahoo.com")
driver.find_element_by_css_selector(".password").send_keys("1@Latunde")
time.sleep(5)
driver.find_element_by_css_selector("#password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
print(driver.title)
# //tagname[text() = 'thetext']
driver.find_element_by_xpath("//a[text() = 'Cancel']").click()
time.sleep(5)
driver .close()
