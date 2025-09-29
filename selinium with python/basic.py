from selenium import webdriver #import WebDriver to control browsers.

from selenium.webdriver.common.by import By #import locator strategy (for finding elements).

#launch browser
driver = webdriver.Chrome() # launch Chrome browser

#open url
driver.get("https://example.com") # open a webpage

driver.maximize_window() # maximize window
driver.minimize_window() #minimize window
driver.fullscreen_window() # go fullscreen


print(driver.current_url) # print current page URL

print(driver.title) # print page title

driver.refresh() # reload page  

driver.back() # go back in history

driver.forward() # go forward in history

driver.close() # close current tab

driver.quit() # close browser and end session

#Single element

driver.find_element(By.ID, "username") # finds element by ID

driver.find_element(By.NAME, "password") # finds element by name attribute

driver.find_element(By.CLASS_NAME, "btn") # finds element by class name

driver.find_element(By.TAG_NAME, "a") # finds element by tag (like <a>)

driver.find_element(By.LINK_TEXT, "Click Here") # finds a link with exact text

driver.find_element(By.PARTIAL_LINK_TEXT, "Click") # finds a link with partial text

driver.find_element(By.CSS_SELECTOR, "input[type='text']") # finds using a CSS selector

driver.find_element(By.XPATH, "//input[@id='username']") # finds using XPath


#INTERACTING WITH ELEMENTS

element = driver.find_element(By.ID, "username")
#Finds the element with ID = "username" and stores it in element

#Send input (type into field)
element.send_keys("zubii")
#Types "my_username" into the element

#Clear text
element.clear()
#Clears any existing text inside the input field

#Click
element.click()
#Clicks on the element <eg button, link, checkbox>

#Get text
print(element.text)
#Prints the visible text inside the element (eg :- button label, paragraph text)

#Get attribute
print(element.get_attribute("value"))
#Gets the value of an attribute (egggg:- value in an input field, href of a link)

element.is_displayed()   # True if visible
element.is_enabled()     # True if clickable/usable
element.is_selected()    # True if selected (checkbox, radio, option)

#MOUSE nd keyboard action

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

actons = ActionChains

#hover
element = driver.find_element(By.ID, "menu")
actons.move_to_element(element).perform()

#Right click / double click
actons.context_click(element).perform()
actons.double_click(element).perform()

#drag & Drop
source = driver.find_element(By.ID, "drag")
target = driver.find_element(By.ID, "drop")
actons.drag_and_drop(source, target).perform()

#keyword
element.send_keys(Keys.ENTER)
element.send_keys(Keys.CONTROL, "a")

# wait (sync handling)
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#static wait
time.sleep(3)

# implicit wait
driver.implicitly_wait(10)

#explicit wait
WebDriverWait(driver,10 ).until(
    EC.presence_of_all_elements_located((By.ID, "username"))
)



# HANDLING frames windows , tabs

driver.switch_to.frame("frame_name")
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe"))
driver.switch_to.default_content()   #back to main page

#multiple windopws

main_win = driver.current_window_handle
all_wins = driver.window_handles
driver.switch_to.window(all_wins[1])
driver.close()
driver.switch_to.window(main_win)


#ALERTS

alert = driver.switch_to.alert
print(alert.text)
alert.accept() #ok
alert.dismiss() #cancel
alert.send_keys("some text") #prompt alert




#IMPORT & SETUP

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


#CREATING A SELECT OBJECT 

dropdown = driver.find_element(by.ID, "country") #located select element
Select= Select(dropdown)


# SELECTING OPTIONS


#by visible text
Select.select_by_visible_text("india")

#by index
Select.select_by_index(2)

#by value attribute 
Select.select_by_value("IN")