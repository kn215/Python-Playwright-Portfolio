from pages.login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    # Assert correct URL is reached after login
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("wrong_user", "wrong_pass")

    assert page.get_by_text("Epic sadface: Username and password do not match").is_visible()

def test_wrong_password(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "wrong_pass")

    assert page.get_by_text("Epic sadface: Username and password do not match").is_visible()