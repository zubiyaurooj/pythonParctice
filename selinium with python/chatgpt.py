import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-save-password-bubble")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito") 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("https://chatgpt.com/")

time.sleep(2)
driver.maximize_window()
time.sleep(2)

element=driver.find_element("xpath",'//div[@id="prompt-textarea"]')

element.send_keys("what is python")
time.sleep(2)

driver.find_element("xpath",'//button[@id="composer-submit-button"]').click()

input("Enter")
