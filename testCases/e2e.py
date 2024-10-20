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


class FlightBookingTest(unittest.TestCase):
    driver = None

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.Purchase_Page = None

    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()

    def setUp(self):
        self.home_page = HomePage(self.driver)
        #self.flight_selection_page = FlightSelectionPage(self.driver)
        #self.purchase_page = PurchasePage(self.driver)

    def test_1_navigate_to_homepage(self):
        #Test the navigation to the homepage and verify the page title
        self.home_page.load()
        self.assertEqual(self.driver.title, "BlazeDemo", "Page title does not match.")
        print("Navigated to BlazeDemo homepage successfully.")

    def test_2_select_cities(self):
        #Test selecting a random departure and destination city ensuring they are different
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

    def test_3_find_flights(self):
        #Test clicking the 'Find Flights' button and navigating to the flights page
        self.home_page.click_find_flights()
        self.assertIn("/reserve", self.driver.current_url, "Failed to navigate to the reservation page.")
        print("Successfully navigated to the reservation page.")

    def test_4_select_cheapest_flight(self):
        """Test selecting the cheapest flight from the list of flights"""
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

    def test_5_fill_purchase_details(self):
        #Test filling in purchase details and completing the flight booking
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

    @classmethod
    def tearDownClass(cls):
        #Close the browser after the test
        if cls.driver:
            cls.driver.quit()
            print("Browser closed.")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Nityanand/Blazedemo/pythonProject/reports'))