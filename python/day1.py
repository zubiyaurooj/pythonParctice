from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# --- Step 1: Open Browser ---
driver = webdriver.Chrome()  # Make sure chromedriver is installed and in PATH

# --- Step 2: Open Wikipedia ---
driver.get("https://www.wikipedia.org")

# --- Step 3: Find search box and type something ---
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Python (programming language)")
search_box.send_keys(Keys.RETURN)

# --- Step 4: Wait for page to load ---
time.sleep(3)
# --- Step 5: Extract the first paragraph text ---
first_paragraph = driver.find_element(By.CSS_SELECTOR, "p").text
print("First paragraph:\n", first_paragraph)

# --- Step 6: Close browser ---
driver.quit()
