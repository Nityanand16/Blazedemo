import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.Home_Page import HomePage
from pageObjects.FlightSelectionPage import FlightSelectionPage
from pageObjects.PurchasePage import PurchasePage
import HtmlTestRunner
from database.purchase_details_data import get_purchase_details
from selenium.common.exceptions import TimeoutException, WebDriverException


class FlightBookingTest(unittest.TestCase):
    driver = None

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.Purchase_Page = None

    @classmethod
    def setUpClass(cls):
        try:
            service = Service(ChromeDriverManager().install())
            cls.driver = webdriver.Chrome(service=service)
            cls.driver.maximize_window()
            print("Browser setup completed.")
        except WebDriverException as e:
            print(f"Failed to initialize WebDriver: {e}")
            raise

    def setUp(self):
        try:
            self.home_page = HomePage(self.driver)
        except Exception as e:
            print(f"Error during setup: {e}")
            raise

    def test_1_navigate_to_homepage(self):
        try:
            self.home_page.load()
            self.assertEqual(self.driver.title, "BlazeDemo", "Page title does not match.")
            print("Navigated to BlazeDemo homepage successfully.")
        except AssertionError as e:
            print(f"Assertion error: {e}")
            raise
        except Exception as e:
            print(f"Error in test_1_navigate_to_homepage: {e}")
            raise

    def test_2_select_cities(self):
        try:
            self.home_page.load()

            # Select a random departure city
            random_departure = self.home_page.select_random_departure_city()

            # Select a random destination city, ensuring it's different from the departure city
            random_destination = self.home_page.select_random_destination_city(exclude_city=random_departure)

            # Verify that the selected values match
            self.assertEqual(self.driver.find_element(By.NAME, "fromPort").get_attribute("value"), random_departure)
            self.assertEqual(self.driver.find_element(By.NAME, "toPort").get_attribute("value"), random_destination)

            print(f"Departure city selected: {random_departure}")
            print(f"Destination city selected: {random_destination}")
        except AssertionError as e:
            print(f"Assertion error in test_2_select_cities: {e}")
            raise
        except Exception as e:
            print(f"Error in test_2_select_cities: {e}")
            raise

    def test_3_find_flights(self):
        try:
            self.home_page.click_find_flights()
            self.assertIn("/reserve", self.driver.current_url, "Failed to navigate to the reservation page.")
            print("Successfully navigated to the reservation page.")
        except AssertionError as e:
            print(f"Assertion error in test_3_find_flights: {e}")
            raise
        except Exception as e:
            print(f"Error in test_3_find_flights: {e}")
            raise

    def test_4_select_cheapest_flight(self):
        try:
            # Initialize the FlightSelectionPage object
            self.flight_selection_page = FlightSelectionPage(self.driver)

            # Find and select the cheapest flight
            cheapest_flight = self.flight_selection_page.get_cheapest_flight()
            self.flight_selection_page.choose_flight(cheapest_flight)

            # Wait for navigation to the purchase page
            WebDriverWait(self.driver, 30).until(
                EC.url_contains("/purchase")
            )

            current_url = self.driver.current_url
            self.assertIn("/purchase", current_url, "Failed to navigate to the purchase page.")
            print("Successfully navigated to the purchase page.")
        except TimeoutException as e:
            print(f"Timeout waiting for purchase page: {e}")
            raise
        except AssertionError as e:
            print(f"Assertion error in test_4_select_cheapest_flight: {e}")
            raise
        except Exception as e:
            print(f"Error in test_4_select_cheapest_flight: {e}")
            raise

    def test_5_fill_purchase_details(self):
        try:
            # Wait for the form to be visible
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "inputName"))
            )

            purchase_page = PurchasePage(self.driver)

            # Get purchase details dynamically
            purchase_details = get_purchase_details()

            # Pass the dictionary directly to the fill_purchase_details method
            purchase_page.fill_purchase_details(purchase_details)

            current_url = self.driver.current_url
            print(f"Final URL after confirming purchase: {current_url}")
        except TimeoutException as e:
            print(f"Timeout while waiting for purchase page elements: {e}")
            raise
        except Exception as e:
            print(f"Error in test_5_fill_purchase_details: {e}")
            raise

    @classmethod
    def tearDownClass(cls):
        try:
            if cls.driver:
                cls.driver.quit()
                print("Browser closed.")
        except Exception as e:
            print(f"Error during tearDownClass: {e}")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Nityanand/Blazedemo/pythonProject/reports'))