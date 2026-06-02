from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")