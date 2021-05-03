from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import uuid
from datetime import datetime
import traceback
import os

def init_browser():
    driver = webdriver.Remote('http://localhost:5555/wd/hub',desired_capabilities= webdriver.DesiredCapabilities.FIREFOX)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

def find_download_page(driver):
    SEARCH_BUTTONS = (By.CSS_SELECTOR,'a.btn.btn-outline.btn-xl.page-scroll')
    PDF_BUTTON = (By.XPATH,"//*[contains(@class,'btn-orange')]")

    search_button = driver.find_elements(*SEARCH_BUTTONS)[0]
    search_button.click()
    documents_button = driver.find_elements(*SEARCH_BUTTONS)[3]
    documents_button.click()
    pdf_button = driver.find_elements(*PDF_BUTTON)[3]
    pdf_button.click()

def download_pdf(driver):
    DOWNLOAD_BUTTON = (By.CLASS_NAME,'download-button')
    
    list_of_buttons = driver.find_elements(*DOWNLOAD_BUTTON)
    for button in list_of_buttons:
        pdf_url = button.get_attribute("href")
        file_data = requests.get(pdf_url)
        timestamp = str(datetime.now())[:10]
        uuid_number = str(uuid.uuid4())
        file_size = pdf_url.split("/")[-1].split("_")[-1]
        
        file_name = timestamp+'_'+uuid_number+'_'+file_size
        try:
            os.mkdir('/exercises/exercise2/Downloads/')
        except:
            pass
        with open('/exercises/exercise2/Downloads/'+file_name, 'wb') as f:
            f.write(file_data.content)
        f.close()

if __name__ == "__main__":
    URL = 'https://file-examples.com'
    try:
        driver = init_browser()
        driver.get(URL)
        find_download_page(driver)
        download_pdf(driver)
    except Exception:
        traceback.print_exc()
    finally:
        driver.quit()