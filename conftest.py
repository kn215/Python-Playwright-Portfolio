import sys
import os
from playwright.sync_api import expect

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.login_page import LoginPage

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    expect(page.locator(".inventory_item").first).to_be_visible()
    return page