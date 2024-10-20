# Flight Booking Automation for BlazeDemo website

This project automates the flight booking process on the BlazeDemo website using Selenium as an automation tool, Python as an language and Page Object Model as a design pattern. The tests cover the complete flow of selecting departure and destination cities, finding flights, and completing a purchase.

## Features

1. Select a random departure city
2. Select a random destination city that differs from the departure city
3. Find available flights
4. Choose the cheapest flight
5. Fill in purchase details and complete the booking process
6. Generates an HTML report for test results

## Prerequisites

Before running the tests, make sure you have the following installed:

- Python 3.x
- pip (Python package manager)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/flight-booking-automation.git
   cd flight-booking-automation

2. **Install the required packages**
You can install the necessary packages using pip. It's recommended to create a virtual environment first.
pip install -r requirements.txt
selenium
webdriver-manager
HtmlTestRunner

3. **Running the Tests**
You can run the tests using the following command:
python -m unittest discover -s testCases -p "*.py"

4. **Generating HTML Reports**
The tests will generate an HTML report.
python -m testCases.e2e
