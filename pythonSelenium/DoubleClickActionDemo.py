import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")
print(driver.title)
print(driver.current_url)

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
time.sleep(5)
#action.context_click(driver.find_element_by_id("double-click")).perform()
action.double_click(driver.find_element_by_id("double-click")).perform()
time.sleep(5)
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" in alert.text
alert.accept()

driver.close()