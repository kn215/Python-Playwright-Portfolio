import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.login_page import LoginPage

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)

    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    return page