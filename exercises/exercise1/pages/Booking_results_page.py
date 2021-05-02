from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Booking_results_page:
    DROPDOWN = (By.XPATH, "//*[@data-type='dropdown']")
    RATING_AND_PRICE = (By.XPATH, "//*[@data-type='class_and_price']")
    PRICE_RANGE = (By.XPATH, "//*[contains(@data-id,'pri-3')]")
    FILTER_BY_REVIEWS = (By.XPATH, "//*[@id='filter_review']//*[@data-id='review_score-80']")
    HANDLE_LOWER = (By.XPATH,"//*[contains(@class,'noUi-handle noUi-handle-lower')]")
    FILTER_BY_HOTELS = (By.XPATH, "//*[contains(@data-value,'204')]")
    FILTER_BY_AirC = (By.XPATH, "//*[contains(@data-id,'roomfacility-11')]")
    FILTER_BY_DOWNTOWN = (By.XPATH, "//*[contains(@data-id,'di-2287')]")
    LOADER = (By.CSS_SELECTOR, ".sr-usp-overlay")

    TOTAL_PROPERTIES = (By.CSS_SELECTOR, ".sr_header > h1")
    LIST_OF_HOTELS = (By.CSS_SELECTOR, "#hotellist_inner > div.sr_item")
    HOTEL_NAME = (By.XPATH, ".//*[@class='js-sr-hotel-link hotel_name_link url']/span")
    PRICE  = (By.CSS_SELECTOR, ".bui-price-display__value")
    NUMBER_OF_REVIEWS = (By.CSS_SELECTOR, ".bui-review-score__text")
    SCORE = (By.CSS_SELECTOR, ".bui-review-score__badge")
    LOCATION = (By.CSS_SELECTOR, ".sr_card_address_line > a.bui-link")
    IMAGE_URL = (By.CSS_SELECTOR, ".hotel_image")

    def filter_hotels(self):
        dropdown_button = self.driver.find_element(*self.DROPDOWN)
        dropdown_button.click()
        sort_by_rating_and_price = self.driver.find_elements(*self.RATING_AND_PRICE)[-1]
        sort_by_rating_and_price.click()

        #Total nights => can't find this filter in the page are you sure this option is still available?

        price_range = self.driver.find_element(*self.PRICE_RANGE)
        self.driver.execute_script("arguments[0].scrollIntoView();", price_range)
        price_range.click()

        filter_by_reviews = self.driver.find_element(*self.FILTER_BY_REVIEWS)
        self.driver.execute_script("arguments[0].scrollIntoView();", filter_by_reviews)
        filter_by_reviews.click()

        filter_by_hotels = self.driver.find_element(*self.FILTER_BY_HOTELS)
        self.driver.execute_script("arguments[0].scrollIntoView();", filter_by_hotels)
        filter_by_hotels.click()

        filter_by_airC = self.driver.find_element(*self.FILTER_BY_AirC)
        self.driver.execute_script("arguments[0].scrollIntoView();", filter_by_airC)
        filter_by_airC.click()

        filter_by_downtown = self.driver.find_element(*self.FILTER_BY_DOWNTOWN)
        self.driver.execute_script("arguments[0].scrollIntoView();", filter_by_downtown)
        filter_by_downtown.click()

        #wait to download and update results (to be sure is the correct list)
        wait = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(self.LOADER)) 

    def print_results(self):
        total_properties = self.driver.find_element(*self.TOTAL_PROPERTIES)
        print(total_properties.text)
        print()
        print("Top 5:")
        
        list_of_hotels = filter_by_downtown = self.driver.find_elements(*self.LIST_OF_HOTELS)[:5]
        for hotel in list_of_hotels:
            name = hotel.find_element(*self.HOTEL_NAME)
            price = hotel.find_element(*self.PRICE)
            number_of_reviews = hotel.find_element(*self.NUMBER_OF_REVIEWS)
            number_of_reviews = number_of_reviews.text.split(" ")[0]
            score = hotel.find_element(*self.SCORE)
            full_location = hotel.find_element(*self.LOCATION)
            location = full_location.get_attribute("textContent").splitlines()[1].strip()
            image_url = hotel.find_element(*self.IMAGE_URL)
            image_url = image_url.get_attribute("src")

            print("Hotel Name:",name.text)
            print("Price:",price.text)
            print("Number of reviews:", number_of_reviews)
            print("Score:",score.text)
            print("Location:",location)
            print("Image url:",image_url)
            print()


    def __init__(self, driver):
        self.driver = driver