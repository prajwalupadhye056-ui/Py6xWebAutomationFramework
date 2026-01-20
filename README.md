Tech Stack

#Python
#Selenium
#Pytest
#Allure Report
#Data Driven Testing[openpyxl,csv]
#Git ignore
#Pytest HTML Report
#Page Object Model and Page Factory
#Highlight element while run
#Parallel Run with xdist
#Jenkins(to run our framework on different machines)
#faker-Test data generation(FakeData Generation)


#All the dependencies used

pip install allure-pytest selenium
pip install pytest selenium pytest-html openpyxl
pip install selenium-page-factory
pip install pyyaml faker openpyxl
pip install pytest-xdist
pip install mysql-connector-python
pip install pytest-reportportal
pip install python-dotenv(#store your credentials)


# Python Selenium Web Automation Framework

A robust, scalable, and maintainable **Python-based Selenium Automation Framework** built using industry best practices. This framework is designed for UI test automation with support for **data-driven testing, parallel execution, rich reporting, CI/CD integration**, and **clean project architecture**.

---

## 🚀 Tech Stack

* **Programming Language:** Python
* **Automation Tool:** Selenium WebDriver
* **Test Framework:** Pytest
* **Reporting:**

  * Allure Report
  * Pytest HTML Report
* **Design Pattern:**

  * Page Object Model (POM)
  * Page Factory
* **Test Data Handling:**

  * Data Driven Testing using **openpyxl** (Excel)
  * CSV file support
  * Fake test data generation using **Faker**
* **Parallel Execution:** Pytest-xdist
* **CI/CD Integration:** Jenkins
* **Configuration Management:** YAML & dotenv
* **Database Connectivity:** MySQL
* **Version Control:** Git (.gitignore configured)

---

## 📁 Framework Features

* ✅ Modular and scalable framework structure
* ✅ Page Object Model with Page Factory implementation
* ✅ Data-driven testing (Excel & CSV)
* ✅ Parallel test execution using Pytest-xdist
* ✅ Element highlighting during execution for better visibility
* ✅ Allure and HTML test reports
* ✅ Faker-based dynamic test data generation
* ✅ Environment-based configuration using YAML & .env files
* ✅ Jenkins integration for execution on multiple machines
* ✅ MySQL database connectivity for data validation

---

## 🧱 Project Structure

```
├── src/
│   ├── pages/              # Page classes (POM)
│   ├── tests/              # Test cases
│   ├── utilities/          # Reusable utilities
│   ├── data/               # Test data (Excel / CSV)
│   ├── config/             # YAML & environment configs
│   └── base/               # Base test & driver setup
│
├── reports/
│   ├── allure-results/     # Allure raw results
│   └── html-report/        # Pytest HTML reports
│
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd python-selenium-framework
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install allure-pytest selenium
pip install pytest pytest-html openpyxl
pip install selenium-page-factory
pip install pyyaml faker openpyxl
pip install pytest-xdist
pip install mysql-connector-python
pip install pytest-reportportal
pip install python-dotenv
```

---

## ▶️ Running Tests

### Run All Tests

```bash
pytest
```

### Run Tests in Parallel

```bash
pytest -n auto
```

### Generate HTML Report

```bash
pytest --html=reports/html-report/report.html
```

### Generate Allure Report

```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## 🎯 Data Driven Testing

* Excel data handled using **openpyxl**
* CSV files supported for lightweight data sources
* Test data located under `src/data/`
* Faker library used for dynamic and random test data generation

---

## 🎨 Element Highlighting

* Web elements are highlighted during execution
* Helps in better debugging and demo visibility

---

## 🔁 CI/CD Integration (Jenkins)

* Jenkins job can be configured to:

  * Pull latest code from Git
  * Install dependencies
  * Execute tests
  * Generate Allure / HTML reports
* Supports execution on different machines

---

## 🧪 Reporting

* **Allure Report** for detailed, interactive test results
* **Pytest HTML Report** for lightweight execution summaries

---

## 📌 Version Control

* `.gitignore` configured for:

  * Virtual environments
  * Reports
  * Cache files

---

## 👤 Author

**Prajwal Upadhye**
QA Automation Engineer

---

## ⭐ Contribution & Feedback

Contributions, issues, and feature requests are welcome!
If you find this framework useful, don’t forget to ⭐ the repository.



