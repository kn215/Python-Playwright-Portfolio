from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item("Sauce Labs Backpack")

    cart_page = CartPage(logged_in_page)
    cart_page.goto_cart()
    cart_page.goto_checkout()


    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_form('mike','ryan','18902')
    checkout_page.finish()
  
    assert checkout_page.order_confirmation()

def test_checkout_error(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item("Sauce Labs Backpack")
    
    cart_page = CartPage(logged_in_page)
    cart_page.goto_cart()
    cart_page.goto_checkout()
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_form('','ryan','18902')

    assert checkout_page.get_error_message()


