from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
time.sleep(4)
# Open site
driver.get("https://www.saucedemo.com/v1/")
time.sleep(4)
# Enter username
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(4)
# Enter password
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(4)
# Click login button
driver.find_element(By.ID, "login-button").click()

# Wait few seconds so you can see result
time.sleep(4)

# driver.quit()