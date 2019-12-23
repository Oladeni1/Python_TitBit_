
# Chrome Option is used in python to control browser execution
# PythonChromeOptionResources: https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

# This job is running on headless browser with ChromeOption

from selenium import webdriver

# ChromeOptions: Many more (if requires):
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # maxBrowser
chrome_options.add_argument("headless")  # Run on headless
chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate error

driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe", options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)

print(driver.current_url)

# Assertion true:
assert "ProtoCommerce" == driver.title

assert "https://rahulshettyacademy.com/angularpractice/" == driver.current_url

# Assertion not true:
assert not "AProtoCommerce" == driver.title

