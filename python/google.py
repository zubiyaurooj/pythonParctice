from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Start browser
driver = webdriver.Chrome()  # Make sure chromedriver is installed and in PATH

# 2. Open a webpage
driver.get("https://www.google.com")

# 3. Find the search box by name attribute
search_box = driver.find_element(By.NAME, "q")

# 4. Type something into the search box
search_box.send_keys("Selenium with Python")
search_box.send_keys(Keys.RETURN)  # Press Enter key

# 5. Wait for results to load
time.sleep(3)

# 6. Print the title of the page
print(driver.title)

# 7. Close the browser
driver.quit()
