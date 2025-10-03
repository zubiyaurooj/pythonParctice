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

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element("xpath",'//input[@id="name"]').send_keys("zubiya urooj")
driver.find_element("xpath",'//input[@id="email"]').send_keys("zubiyaurooj29@gmail.com")
driver.find_element("xpath",'//input[@id="phone"]').send_keys("8379076327")
driver.find_element("xpath",'//textarea[@id="textarea"]').send_keys("chaya nagar near mata mandir amt")
time.sleep(2)
driver.find_element("xpath",'//input[@id="female"]').click()
time.sleep(2)
driver.find_element("xpath",'//input[@id="thursday"]').click()
element=driver.find_element("xpath",'//select[@id="country"]')
elementcountry=Select(element)
elementcountry.select_by_visible_text("India")
time.sleep(2)
colour=driver.find_element("xpath",'//select[@id="colors"]')
multiplecolour=Select(colour)
multiplecolour.select_by_visible_text("White")
time.sleep(3)
animal=driver.find_element("xpath",'//select[@id="animals"]')
multipleanimal=Select(animal)
multipleanimal.select_by_visible_text("Dog")
time.sleep(2)

driver.find_element("xpath",'//input[@id="datepicker"]').send_keys('10/05/2025')
time.sleep(2)
driver.find_element("xpath","//button[text()='Point Me']").click()

driver.find_element("xpath",'//input[@id="txtDate"]').click()
time.sleep(2)
driver.find_element('xpath',"//a[text()='7']").click()

driver.find_element("xpath",'//input[@id="start-date"]').send_keys('10/05/2025')
driver.find_element("xpath",'//input[@id="end-date"]').send_keys('10/05/2025')
driver.find_element("xpath",'//button[@class="submit-btn"]').click()

input("Enter")