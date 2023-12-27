from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

from cookieClickerConstants import *

def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path=PATH)
    
    driver = webdriver.Chrome(options=options, service=service)
    driver.set_window_size(800, 1000)
    driver.get(TARGETSITE)
    driver.implicitly_wait(10)
    

    lang_eng = driver.find_element(By.ID, "langSelect-EN")
    lang_eng.click()
    
    sleep(3)
    
    cookie = driver.find_element(By.ID, 'bigCookie')
    cookie_count = driver.find_element(By.ID, 'cookies')
    
    items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]
    upgrades = None
    
    actions = ActionChains(driver)
    
    for i in range(5000):
        actions.click(cookie)
        actions.perform()
        count = int(cookie_count.text.split(" ")[0])
        
        for item in items:
            item_price = int(item.text)
            
            if item_price < count:
                actions.click(item)
                            
            
if __name__ == '__main__':
    main()