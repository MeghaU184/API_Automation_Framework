
# 🚀 Python API Automation Framework

A **Hybrid Custom API Automation Framework** built with **Python** and **PyTest**, designed for **scalable, maintainable, and enterprise-grade API testing**. This framework follows **industry best practices** with a modular folder structure, support for parallel execution, rich reporting, and easy integration into CI/CD pipelines.

---

## 📌 Key Highlights

* Modular and scalable folder structure
* Supports **CRUD-based API testing**
* Parallel execution using **PyTest xdist**
* **JSON schema validation** for advanced API testing
* Rich reporting with **Allure** and **PyTest HTML**
* Easy to extend for **CI/CD pipelines** (GitHub Actions, Jenkins, GitLab CI)

---

## 📂 Project Structure

```
python-api-automation-framework/
│
├── config/              # Environment & configuration files
├── data/                # Test data (CSV, Excel, JSON)
├── helpers/             # Utility & helper functions
├── payloads/            # Request payloads
├── schemas/             # JSON schema validations
├── tests/
│   ├── crud/            # CRUD-based API tests
│   └── conftest.py      # PyTest fixtures
├── reports/             # Test execution reports
├── requirements.txt     # Project dependencies
└── README.md
```

---

## 🛠 Tech Stack

| Component            | Technology              |
| -------------------- | ----------------------- |
| Language             | Python 3.12             |
| HTTP Client          | `requests`              |
| Test Framework       | `pytest`                |
| Reporting            | Allure, `pytest-html`   |
| Test Data Management | CSV, Excel, JSON, Faker |
| API Validation       | `jsonschema`            |
| Parallel Execution   | `pytest-xdist`          |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/python-api-automation-framework.git
cd python-api-automation-framework
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install requests pytest pytest-html faker allure-pytest jsonschema
```

### 3️⃣ Install Parallel Execution Support

```bash
pip install pytest-xdist
```

---

## ▶️ Running Tests

### Run a Single Test with Allure Report

```bash
pytest tests/crud/test_create_booking.py --alluredir=reports/allure_results -s
```

### Run All Tests

```bash
pytest tests/ --alluredir=reports/allure_results -s
```

### Run Tests in Parallel

```bash
pytest tests/ -n auto --alluredir=reports/allure_results
```

### Generate Allure Report

```bash
allure serve reports/allure_results
```

---

## 🧪 Supported Test Scenarios

* CRUD API testing
* JSON schema validation
* Data-driven testing (CSV, Excel, JSON, Faker)
* Negative & edge-case testing
* Parallel test execution
* CI/CD-friendly execution

---

## 👨‍💻 Author

**Megha U** – QA Tester | SDET | API Automation Tester

---

## 🤝 Contributions

Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes
4. Push the branch and open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it **with attribution**.

