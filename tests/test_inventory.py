from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect
from playwright.sync_api import sync_playwright

def test_get_item_names(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    names = inventory_page.get_item_names()
    assert len(names) == 6

def test_get_item_prices(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    prices = inventory_page.get_item_prices()
    assert len(prices) == 6
    assert all(isinstance(p, float) for p in prices)

def test_add_item(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item("Sauce Labs Backpack")
    expect(inventory_page.cart_count).to_have_text("1")

def test_sortprice_low_high(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_by("lohi")
    prices = inventory_page.get_item_prices()

    assert prices == sorted(prices)

def test_sortprice_high_low(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_by("hilo")
    prices = inventory_page.get_item_prices()
    assert prices == sorted(prices, reverse=True)

def test_sortname_a_z(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_by("az")
    names = inventory_page.get_item_names()

    assert names == sorted(names)

def test_sortname_z_a(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_by("za")
    names = inventory_page.get_item_names()

    assert names == sorted(names, reverse=True)
    
