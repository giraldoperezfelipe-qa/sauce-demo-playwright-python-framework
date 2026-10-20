# Sauce demo playwright python framework

This is a small, end-to-end automation testing demo built using Python and Playwright, targeting the demo e-commerce store SauceDemo.

🚀 Features

    1. Automated Login Flow: Tests standard users, locked-out users, and performance glitch users.
    2. Shopping Cart Operations: Adds items to the cart, verifies item details, and removes items.
    3. Checkout Process: Fills out checkout information and completes a successful order.

🛠️ Prerequisites

Make sure you have the following installed on your machine:
-   Python (version 3.8 or higher)
-   pip (Python package manager)

📦 Installation & Setup

    1. Clone the repository:
    git clone <REPO_LINK>
    cd sauce-demo-playwright-python-framework

    2. Create and activate a virtual environment (recommended):
    python -m venv venv

      # On Windows, run in Powershell:
      venv\Scripts\activate

      # On macOS/Linux, run in Terminal:
      source venv/bin/activate

    3. Install dependencies:
    pip install pytest playwright

    4. Install Playwright browsers:
    playwright install

🏃‍♂️ Running the Tests

To run the demo script or test suite, use the following commands:

    Run all tests (headless mode):
    pytest

    Run tests with the browser UI visible (headed mode):
    pytest --headed

    Run a specific test file:
    pytest tests/test_checkout.py


📊 See the results in Allure report

For checking the results in a report, you must:

    1. Install allure:
    npm install -g allure-commandline

    2. Run the tests, and clean the allure folder:
    pytest --alluredir=allure-results --clean-alluredir  

    3. Run the allure server, to check the results:
    allure serve allure-results


💡 Credentials Used for Testing

Saucedemo provides built-in user accounts for testing purposes:
