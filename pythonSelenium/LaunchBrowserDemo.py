import time

from selenium import webdriver

# Launch Browser
driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\geckodriver.exe")
#driver = webdriver.Ie(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\IEDriverServer.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")

print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)

driver.back()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.close()





