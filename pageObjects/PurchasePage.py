# PurchasePage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class PurchasePage:
    def __init__(self, driver):
        self.driver = driver

    def fill_purchase_details(self, details):
        #Fill the purchase details form using the details provided in the dictionary
        self.driver.find_element(By.ID, "inputName").send_keys(details["name"])
        self.driver.find_element(By.ID, "address").send_keys(details["address"])
        self.driver.find_element(By.ID, "city").send_keys(details["city"])
        self.driver.find_element(By.ID, "state").send_keys(details["state"])
        self.driver.find_element(By.ID, "zipCode").send_keys(details["zip_code"])

        # Select card type (Visa, MasterCard, etc.)
        card_type_dropdown = Select(self.driver.find_element(By.ID, "cardType"))
        card_type_dropdown.select_by_visible_text(details["card_type"])

        # Fill card details
        self.driver.find_element(By.ID, "creditCardNumber").send_keys(details["card_number"])
        self.driver.find_element(By.ID, "creditCardMonth").clear()
        self.driver.find_element(By.ID, "creditCardMonth").send_keys(details["card_month"])
        self.driver.find_element(By.ID, "creditCardYear").clear()
        self.driver.find_element(By.ID, "creditCardYear").send_keys(details["card_year"])
        self.driver.find_element(By.ID, "nameOnCard").send_keys(details["name_on_card"])

        """Submit the form"""
        self.driver.find_element(By.XPATH, '//input[@value="Purchase Flight"]').click()