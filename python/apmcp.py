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

driver.get("https://www.msamb.com/ApmcDetail/APMCPriceInformation")
time.sleep(3)
driver.maximize_window()
time.sleep(3)

language=driver.find_element("xpath",'//select[@id="language"]')
selectlan=Select(language)
selectlan.select_by_visible_text("English")
time.sleep(3)
driver.find_element("xpath",'//div[@id="APMCTitle"]').click()
time.sleep(3)

driver.find_element("xpath","//a[text()='District- Commodity Wise']").click()
time.sleep(3)

selectdis=driver.find_element("xpath",'//select[@id="drpDistrictCommodity"]')
selectDistrict=Select(selectdis)
selectDistrict.select_by_index(3)
time.sleep(3)

element = driver.find_element("xpath",'//td[@colspan="7"]')
print(element.text)

input("Enter")
