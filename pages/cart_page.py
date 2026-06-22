from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_name = page.locator('[data-test="inventory-item-name"]')
        self.cart_item = page.locator('[data-test="inventory-item"]')
        self.checkout = page.locator('[data-test="checkout"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')

    def goto(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def remove_item(self, name: str):
        formatted = name.lower().replace(" ", "-")
        self.page.locator(f"[data-test='remove-{formatted}']").click()

    def continue_shopping(self):
        self.page.locator('[data-test="continue-shopping"]').click()

    def goto_checkout(self):
        self.page.locator('[data-test="checkout"]').click()

    def get_item_count(self):
        return self.cart_item.count()
    
    def get_item_names(self):
        return self.item_name.all_text_contents()
    
    def check_item_in_cart(self, name: str):
        return name in self.get_item_names()