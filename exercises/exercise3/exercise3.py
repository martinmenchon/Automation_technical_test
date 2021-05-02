from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def init_browser():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36") # To change user Agent
    driver = webdriver.Remote('http://localhost:5555/wd/hub',desired_capabilities= webdriver.DesiredCapabilities.FIREFOX,options=firefox_options)
    
    #Remove navigator.webdriver Flag using JavaScript
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.implicitly_wait(20)
    driver.maximize_window()
    return driver

if __name__ == "__main__":
    URL = 'https://www.wmphvacations.com'

    try:
        driver = init_browser()
        driver.get(URL)

        random_secs = random.randint(5, 15)
        time.sleep(random_secs)

        MENU_1 = (By.CSS_SELECTOR, "#menu-main-menu-1 > li:nth-child(3)")
        MENU_2 = (By.CSS_SELECTOR, "#menu-main-menu-1 > li:nth-child(5)")
    
        menu1 = driver.find_element(*MENU_1)
        menu1.click()
        driver.save_screenshot("/exercises/exercise3/screenshot1.png")
        random_secs = random.randint(1, 3)
        time.sleep(random_secs)# To take the screenshot without moving anything and also creating a random behaviour
        
        menu2 = driver.find_element(*MENU_2)
        menu2.click()
        driver.save_screenshot("/exercises/exercise3/screenshot2.png")
        random_secs = random.randint(1, 3)
        time.sleep(random_secs)# To take the screenshot without moving anything and also creating a random behaviour
        
    finally:
        driver.quit()