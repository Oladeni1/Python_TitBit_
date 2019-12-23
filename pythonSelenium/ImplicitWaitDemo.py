# Waits: Implicit, Explicit & Pause



import time

from selenium import webdriver

# Locators cheatSheet:
# CSS Syntax -> tagname[attribute ='value'] or [attribute* = 'value'] or input#IDvalue
# XPATH Syntax -> //tagname[@attribute = 'value'] or //*[contains(@attribute, 'value')]
list = []
list2 = []
# Launch Browser
driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")
driver.implicitly_wait(7)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise")
print(driver.title)
print(driver.current_url)

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(5)

# Validate 3 products displayed
count = len(driver.find_elements_by_xpath("//div[@class= 'products']/div"))
assert count == 3

# Add all 3 products to cart
products = driver.find_elements_by_xpath("//div[@class= 'product-action']/button")  # element for all 3 products
for product in products:
    list.append(product.find_element_by_xpath("parent::div/parent::div/h4").text)
    product.click()

print(list)   # print names of the 3 fruits

# Click bag to checkout
driver.find_element_by_css_selector("img[alt= 'Cart']").click()

# Click checkOut
driver.find_element_by_xpath("//button[text()= 'PROCEED TO CHECKOUT']").click()

veggies = driver.find_elements_by_css_selector("p.product-name")  # name of fruits found in page 2
for veg in veggies:
    list2.append(veg.text)

print(list2)

# Validate that the name of the fruits selected in page 1 is the same as the name of fruits in page 2
#assert list == list2

# Amount before coupon
originalAmount = driver.find_element_by_css_selector(".discountAmt").text

# Apply promo code
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

# Click Apply button
driver.find_element_by_css_selector(".promoBtn").click()

# print promo information
print(driver.find_element_by_css_selector("span.promoInfo").text)

# Amount after coupon
discountedAmount = driver.find_element_by_css_selector(".discountAmt").text

# validate amount changes
assert float(discountedAmount) < int(originalAmount)

# validate promo information
promoIfo = driver.find_element_by_css_selector("span.promoInfo").text

promoText = promoIfo

assert promoText in promoIfo

# verify that sum prices in page 2 is equal to the grand total after coupon
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")  # element for all the 3 prices
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)  # 23+48+60
    print(sum)

totalAmount = int(driver.find_element_by_class_name("totAmt").text)

assert sum == totalAmount

driver.close()




