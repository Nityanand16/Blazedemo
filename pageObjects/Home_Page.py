# Home_Page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("http://blazedemo.com")

    def get_departure_options(self):
        #Retrieve the list of departure city options.
        dropdown = Select(self.driver.find_element(By.NAME, "fromPort"))
        return [option.text for option in dropdown.options]

    def get_destination_options(self):
        #Retrieve the list of destination city options.
        dropdown = Select(self.driver.find_element(By.NAME, "toPort"))
        return [option.text for option in dropdown.options]

    def select_random_departure_city(self):
        #Select a random departure city from the dropdown.
        departure_options = self.get_departure_options()
        random_departure = random.choice(departure_options)
        dropdown = Select(self.driver.find_element(By.NAME, "fromPort"))
        dropdown.select_by_visible_text(random_departure)
        print(f"Departure city selected: {random_departure}")
        return random_departure

    def select_random_destination_city(self, exclude_city=None):
        #Select a random destination city, ensuring it's different from the departure city if specified.
        destination_options = self.get_destination_options()

        random_destination = random.choice(destination_options)
        if exclude_city:
            while random_destination == exclude_city:
                random_destination = random.choice(destination_options)

        dropdown = Select(self.driver.find_element(By.NAME, "toPort"))
        dropdown.select_by_visible_text(random_destination)
        print(f"Destination city selected: {random_destination}")
        return random_destination

    def click_find_flights(self):
        #Clicks the 'Find Flights' button.
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()