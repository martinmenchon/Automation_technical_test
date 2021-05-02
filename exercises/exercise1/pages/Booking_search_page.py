from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from string import Template

class Booking_search_page:
    SEARCH_INPUT = (By.ID, 'ss')
    CALENDAR_FIELD = (By.CSS_SELECTOR, ".xp__input-group.xp__date-time")
    FAMILY_FIELD = (By.CSS_SELECTOR, '#xp__guests__toggle')
    CHILDREN_BUTTON = (By.XPATH, "//*[@aria-describedby='group_children_desc']")
    SEARCH_BUTTON = (By.CSS_SELECTOR,'.sb-searchbox__button')
    DATE_TEMPLATE = Template("//*[@data-date='${date}']")

    def search_flights(self,destiny,initial_date,ending_date,number_of_children):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(destiny)

        date_field = self.driver.find_elements(*self.CALENDAR_FIELD)[0]
        date_field.click()
        
        wait = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable( (By.XPATH,self.DATE_TEMPLATE.substitute(date=initial_date)) ))
        wait.click()

        ending_date_button = self.driver.find_element_by_xpath(self.DATE_TEMPLATE.substitute(date=ending_date))
        ending_date_button.click()

        family_field = self.driver.find_element(*self.FAMILY_FIELD)
        family_field.click()
        children_button = self.driver.find_elements(*self.CHILDREN_BUTTON)[1]
        for i in range(0,number_of_children):
            children_button.click()

        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def __init__(self, driver,url):
        self.driver = driver
        self.driver.get(url)
