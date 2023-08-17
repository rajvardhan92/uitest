import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# Launch the browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Open URL - http://www.google.com
driver.get("http://www.google.com")

# Step 3: Enter the keyword "amazon" in the search bar
search_bar = driver.find_element(By.NAME, 'q')
search_bar.send_keys("amazon")
search_bar.send_keys(Keys.RETURN)

# Wait for search results
wait = WebDriverWait(driver, 10)
search_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h3')))

# Step 4: Print all the search results
for result in search_results:
    print(result.text)

# Click on the link which takes you to the amazon login page
amazon_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Amazon.in')
amazon_link.click()

# Wait for the page to load
wait.until(EC.title_contains("Amazon"))

time.sleep(10)

# Step 6: Login to https://www.amazon.in/
login = driver.find_element(By.ID, 'nav-link-accountList')
login.click()

time.sleep(5)

email = driver.find_element(By.ID, 'ap_email')
email.send_keys('rajvc1992@gmail.com')
clickcontinue = driver.find_element(By.ID, 'continue')
clickcontinue.click()

time.sleep(10)

password =driver.find_element(By.ID, 'ap_password')
password.send_keys('********')

time.sleep(5)

signin =driver.find_element(By.ID, 'signInSubmit')
signin.click()

time.sleep(10)
# Step 7: Click on all buttons on search & select Electronics


try:
    searchselect = driver.find_element(By.ID, 'searchDropdownBox')
except NoSuchElementException:
    print("Element with ID 'searchDropdownBox' not found.")

searchselect = driver.find_element(By.ID, 'searchDropdownBox')
searchselect.click()

serach = driver.find_element(By.ID,'twotabsearchtextbox')

serach.send_keys('dell computers')


# Step 8: Search for dell computers
submitsearch = driver.find_element(By.ID, 'nav-search-submit-button')
submitsearch.click()



# Step 9: Apply the filter of range Rs 30000 to 50000
pricerange=driver.find_element(By.ID, 'p_36/7252030031')




# Step 10: Validate all the products on the first 2 pages are shown in the range of Rs 30000 to 50000


product_price_elements = driver.find_elements(By.CLASS_NAME, 'a-price-whole')

# Counter for tracking the number of pages visited
page_count = 1

for page in range(2):  # Visit the first two pages
    print(f"Validating products on page {page_count}")

    for price_element in product_price_elements:
        price_text = price_element.text
        price = int(price_text.replace("Rs ", "").replace(",", ""))

        if 30000 <= price <= 50000:
            print(f"Product price {price_text} is within the range Rs 30000 to 50000")
        else:
            print(f"Product price {price_text} is not within the desired range")

    # Navigate to the next page if not the last page
    if page_count < 2:  # Assuming 2 pages need to be visited
        next_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Next')
        next_button.click()
        page_count += 1

    # Wait for the new page to load before finding the price elements again
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'a-price-whole')))
    product_price_elements = driver.find_elements(By.CLASS_NAME, 'a-price-whole')


product_containers = driver.find_elements(By.CLASS_NAME, 'product-container-class')

for container in product_containers:
    rating_element = container.find_element(By.CLASS_NAME, 'product-rating-class')
    rating_text = rating_element.text
    if rating_text == "5 out of 5":
        add_to_wishlist_button = container.find_element(By.CLASS_NAME, 'add-to-wishlist-class')
        add_to_wishlist_button.click()
        print("Added a 5-star product to the wish list")
        break  # Exit the loop after adding the first matching product



wishlist_elements = driver.find_elements(By.CLASS_NAME, 'wishlist-element-class')

if len(wishlist_elements) > 0:
    print("Product added to the wish list")
else:
    print("Product not added to the wish list")

# Close the browser
#driver.quit()
