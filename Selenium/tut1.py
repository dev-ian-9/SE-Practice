from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

service = Service(executable_path=PATH)

driver = webdriver.Chrome(options=options, service=service)
driver.set_window_size(800, 1000)

driver.get("https://www.reddit.com/r/pcgamingtechsupport/comments/l30f10/pc_restarts_when_trying_to_start_a_league_of/")
wait =  WebDriverWait(driver, 60)
time.sleep(1)

try:
    main = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "FreakyChicken"))   # Google search result
    )
    
    main.click()
    
finally:
    time.sleep(3)
    driver.quit()

