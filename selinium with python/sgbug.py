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

driver.get("https://sgbau.ucanapply.com/result-details")
time.sleep(2)
driver.maximize_window()
time.sleep(2)

sub= driver.find_element("xpath",'//select[@id="session"]')
subject=Select(sub)
subject.select_by_visible_text("Summer 2025")
time.sleep(2)

cou = driver.find_element("xpath",'//select[@id="coursetype"]')
cource =Select(cou)
cource.select_by_visible_text("UG")
time.sleep(2)

ele=driver.find_element("xpath",'//select[@id="coursecd"]')
element =Select(ele)
element.select_by_visible_text("Bachelor Of Science (Semester Pattern)CGS ( BSC )")

time.sleep(2)
res =driver.find_element("xpath",'//select[@id="resulttype"]')
result =Select(res)
result.select_by_visible_text("Regular")

time.sleep(2)
driver.find_element("xpath",'//input[@id="username"]').send_keys("22AB112645") 

time.sleep(2)
sem =driver.find_element("xpath",'//select[@ id="semester"]')
semster =Select(sem)
semster.select_by_visible_text("Fifth Semester ( Sem - 5)")

time.sleep(2)

driver.find_element("xpath", '//button[@class="btn btn-warning"]').send_keys()


input("Enter")