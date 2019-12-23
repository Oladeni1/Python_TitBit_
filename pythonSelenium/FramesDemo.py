import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")

#iframe, frameset, frame
driver.get("https://the-internet.herokuapp.com/iframe")
print(driver.title)
print(driver.current_url)
time.sleep(5)

#frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
time.sleep(3)
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to automate")
time.sleep(2)

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)

driver.close()