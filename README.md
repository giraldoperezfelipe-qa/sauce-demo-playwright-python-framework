# Sauce demo playwright python framework

This is a small, end-to-end automation testing demo built using Python and Playwright, targeting the demo e-commerce store SauceDemo.

🚀 Features

    Automated Login Flow: Tests standard users, locked-out users, and performance glitch users.

    Shopping Cart Operations: Adds items to the cart, verifies item details, and removes items.

    Checkout Process: Fills out checkout information and completes a successful order.

    Cross-Browser Testing: Runs tests effortlessly across Chromium, Firefox, and WebKit.

🛠️ Prerequisites

Make sure you have the following installed on your machine:

    Python (version 3.8 or higher)

    pip (Python package manager)

📦 Installation & Setup

    Clone the repository:
    Bash

    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME

    Create and activate a virtual environment (recommended):
    Bash

    python -m venv venv

    # On Windows:
    venv\Scripts\activate

    # On macOS/Linux:
    source venv/bin/activate

    Install dependencies:
    Bash

    pip install pytest playwright

    Install Playwright browsers:
    Bash

    playwright install

🏃‍♂️ Running the Tests

To run the demo script or test suite, use the following commands:

    Run all tests (headless mode):
    Bash

    pytest

    Run tests with the browser UI visible (headed mode):
    Bash

    pytest --headed

    Run a specific test file:
    Bash

    pytest tests/test_checkout.py

📂 Project Structure
Plaintext

YOUR_REPOSITORY_NAME/
│
├── tests/                  # Test files directory
│   ├── __init__.py
│   └── test_saucedemo.py   # Main test scripts
│
├── .gitignore              # Files to ignore in git
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies

💡 Credentials Used for Testing

Saucedemo provides built-in user accounts for testing purposes:

    Standard User: standard_user / secret_sauce

    Locked Out User: locked_out_user / secret_sauce

    Problem User: problem_user / secret_sauce

🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
📝 License

This project is open-source and available under the MIT License.
Quick Tip before you save:

Make sure to replace YOUR_USERNAME and YOUR_REPOSITORY_NAME with your actual GitHub username and repo name!

Let me know if you want to add specific test scenarios or structure details to this file.
