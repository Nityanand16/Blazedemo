from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FlightSelectionPage:
    def __init__(self, driver):
        self.driver = driver
        self.flight_rows_locator = "//table/tbody/tr"
        self.cheapest_flight = None

    def get_cheapest_flight(self):
        #Method to find and return the cheapest flight row element.
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.flight_rows_locator))
        )
        flight_rows = self.driver.find_elements(By.XPATH, self.flight_rows_locator)
        cheapest_price = float('inf')

        for flight in flight_rows:
            price_text = flight.find_element(By.XPATH, "td[last()]").text
            price = float(price_text.replace('$', '').replace(',', ''))
            if price < cheapest_price:
                cheapest_price = price
                self.cheapest_flight = flight

        print(f"Cheapest flight price: ${cheapest_price}")
        return self.cheapest_flight

    def choose_flight(self, flight):
        #Clicks the 'Choose This Flight' button for the specified flight.
        choose_button = flight.find_element(By.XPATH, ".//input[@value='Choose This Flight']")
        choose_button.click()