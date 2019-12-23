
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
time.sleep(5)

# Click shop button:
shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)

# Complete element Xpath locator for adding blackberry product: "//div[@class= 'card h-100'] /div/h4/a/ div/button"
# Identify all 4 products on the page
products = driver.find_elements_by_xpath("//div[@class= 'card h-100']")

# Scroll to top of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")   # scroll from 0 to highest
time.sleep(3)

# Perform for loop to add product to basket
for product in products:
    print(product.find_element_by_xpath("div/h4/a").text)
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()  # This Clicks add button of item with name Blackberry
time.sleep(2)

# Scroll to top of the page
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")   # scroll from highest to 0
time.sleep(3)

# Click To CheckOut:
driver.find_element_by_class_name("btn-primary").click()

# Assert that product on page 1 is present in page 2 -> Check Out page
assert productName == productName
print(productName)

# Final CheckOut: "btn-success"
driver.find_element_by_class_name("btn-success").click()

# Insert country of destination
driver.find_element_by_id("country").send_keys("Nigeria")
time.sleep(5)

# select checkbox:
driver.find_element_by_class_name("checkbox-primary").click()

# Click purchase button:
driver.find_element_by_class_name("btn-lg").click()

successText = driver.find_element_by_class_name("alert-success").text
print(successText)

# Assertion true
assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in successText

# Take screenshot
driver.get_screenshot_as_file("EndToEnd_screenshot.png")

driver.close()







