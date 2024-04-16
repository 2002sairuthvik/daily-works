from selenium import webdriver
from selenium.webdriver.common.by import By

#keep the chrome open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver =  webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(f"The price of pot is {price.text}")

# search_bar =  driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# button =  driver.find_element(By.ID, value="submit")
# print(button.size)

# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
events = {}

for n in range(len(event_times)):
    events[n] = {
        'time' : event_times[n].text,
        'name' : event_names[n].text
    }

print(events)

driver.quit()