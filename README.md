# Playwright Python Demo Project

This project is a small project for using **Playwright with Python** for UI automation testing. It specifically targets the popular practice website: [Sauce Demo](https://www.saucedemo.com/).

The framework integrates **Cucumber Gherkin** syntax for behavior-driven development (BDD) and generates detailed test reports using **Allure**.

---

## 🛠️ Features
* **UI Automation:** Powered by Playwright (Python).
* **BDD Syntax:** Structured with Cucumber Gherkin.
* **Reporting:** Visual and interactive reports via Allure.

---

## 🚀 How to Run the Project

Follow these steps to execute the tests and view the results.

### 1. Run the tests
Execute the test suite with the following command (take into account that this command cleans the previous report data)
```bash
pytest --alluredir=allure-results --clean-alluredir
```

### 2. Generate the report
Generate the Allure report with the following command:
```bash
allure serve allure-results
```