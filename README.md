> **Please note this is an in-progress repository that I am creating to learn automation.**

# Python Playwright Portfolio

End-to-end UI test suite for [SauceDemo](https://www.saucedemo.com/) built with Python, Pytest, and Playwright. Covers login, inventory, and checkout flows using the Page Object Model pattern.

---

## Tech Stack

- **Python 3.14.4**
- **Pytest** — test framework
- **Playwright** — browser automation
- **GitHub Actions** — CI/CD 

---

## Project Structure

```
Python-Playwright-Portfolio/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Setup & Installation

**1. Clone the repo**
```bash
git clone https://github.com/kn215/Python-Playwright-Portfolio.git
cd Python-Playwright-Portfolio
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Install Playwright browsers**
```bash
playwright install
```

---

## Running Tests

**Run the full suite**
```bash
pytest
```

**Run with verbose output**
```bash
pytest -v
```

**Run a specific file**
```bash
pytest tests/test_login.py
```

**Run headed (visible browser) with slow motion**
```bash
pytest --headed --slowmo=500
```

---

## Test Coverage

| Area | Tests |
|------|-------|
| Login — valid credentials | ✓ |
| Login — invalid credentials | ✓ |
| Inventory — Get item names | ✓ |
| Inventory — Get item prices | ✓ |
| Inventory — Add items | ✓ |
| Cart — Add Item/Test Cart Count | ✓ |
| Cart — Add multiple items | ✓ |
| Cart — Remove Item/Test Cart Count | ✓ |
| Cart — Test Correct Item | ✓ |
| Checkout — Successful checkout | ✓ |
| Checkout — Error on missing field | ✓ |

More scenarios being added weekly.

---

## Author

Kenneth Navarra · [github.com/kn215](https://github.com/kn215)
