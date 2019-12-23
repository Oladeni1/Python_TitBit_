
import time

from selenium import webdriver

# Launch Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")
driver.maximize_window()
#driver.implicitly_wait(7)
driver.get("https://the-internet.herokuapp.com/windows")
print(driver.title)
print(driver.current_url)

#explicit wait declaration:
#wait = WebDriverWait(driver, 7)
#wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Click Here")))

time.sleep(3)
print(driver.find_element_by_xpath("//h3[contains(text(),'Opening a new window')]").text)
driver.find_element_by_link_text("Click Here").click()
childwindow = driver.window_handles[1]

time.sleep(3)
driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

#Assertion:
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text

driver.quit()