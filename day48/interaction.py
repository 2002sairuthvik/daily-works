from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver =  webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# finding using anchor tag of css selectors
num = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# num.click()

#Find elements by link
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the search <input> by name
search = driver.find_element(By.NAME, value="search")

# sending keyborad input to selenuium
search.send_keys("Python", Keys.ENTER)


# driver.quit()