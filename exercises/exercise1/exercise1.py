import traceback
from selenium import webdriver
from pages.Booking_search_page import Booking_search_page
from pages.Booking_results_page import Booking_results_page

def init_browser():
    driver = webdriver.Remote('http://localhost:5555/wd/hub',desired_capabilities= webdriver.DesiredCapabilities.FIREFOX)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver 

if __name__ == "__main__":
    URL = 'http://www.booking.com'
    DESTINY = 'Barcelona'
    # Choose a valid date (I can implement something to check if this range is valid, but I think is not the aim of this test)
    INITIAL_DATE = '2021-06-10'
    ENDING_DATE = '2021-06-30'
    NUMBER_OF_CHILDREN = 2 #Adults number = 2 is the default number of the page

    try:
        driver = init_browser()
        search_page = Booking_search_page(driver,URL)
        search_page.search_flights(DESTINY,INITIAL_DATE,ENDING_DATE,NUMBER_OF_CHILDREN)

        results_page = Booking_results_page(driver)
        results_page.filter_hotels()
        results_page.print_results()
    except Exception:
        traceback.print_exc()
    finally:
        driver.quit()


