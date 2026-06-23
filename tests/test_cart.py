from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_add_one_item(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item("Sauce Labs Backpack")
    inventory_page.cart_button.click()
    cart_page = CartPage(logged_in_page)
    
    assert cart_page.get_item_count() == 1

def test_add_multiple_items(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item("Sauce Labs Backpack")
    inventory_page.add_item("Sauce Labs Bike Light")
    inventory_page.cart_button.click()
    cart_page = CartPage(logged_in_page)
    
    assert cart_page.get_item_count() == 2

def test_remove_item(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item("Sauce Labs Backpack")
    inventory_page.cart_button.click()
    cart_page = CartPage(logged_in_page)
    cart_page.remove_item("Sauce Labs Backpack")

    assert cart_page.get_item_count() == 0

def test_correct_item(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item("Sauce Labs Backpack")
    inventory_page.cart_button.click()
    
    cart_page = CartPage(logged_in_page)

    assert cart_page.check_item_in_cart("Sauce Labs Backpack")