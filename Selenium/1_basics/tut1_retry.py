from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

service = Service(executable_path=PATH)

driver = webdriver.Chrome(options=options, service=service)
driver.get("https://stackoverflow.com/questions/75160044/how-to-resolve-this-error-in-selenium-error-couldnt-read-tbscertificate-as-s")
wait = WebDriverWait(driver, 60)

try:
    main = wait.until(
        EC.presence_of_element_located((By.ID, "question-header"))
    )
    
    print(f"Found title: {main.text}")

finally:
    sleep(5)
    
    