import time


class Side_Menu_Bar:

    def __init__(self,page):
        self.page = page

    def navigate_Supplier_sites(self):
        self.page.get_by_test_id("LibraryBooksIcon").click()
        self.page.get_by_role("link", name="Suppliers & Sites").click()
        time.sleep(5)

    def navigate_Purchases_Trading(self):
        self.page.get_by_test_id("ShoppingCartIcon").click()
        self.page.get_by_role("link", name="Purchases (Trading)").click()
        time.sleep(5)

    def navigate_Sales(self):
        self.page.get_by_test_id("LocalOfferIcon").click()
        self.page.get_by_role("link", name="Sales").click()
        time.sleep(5)

    def navigate_Inbound_loads(self):
        self.page.get_by_test_id("WarehouseIcon").click()
        self.page.get_by_role("link", name="Inbound loads").click()
        time.sleep(5)

    def navigate_Hedging_contracts(self):
        self.page.get_by_test_id("VerifiedUserIcon").click()
        self.page.get_by_role("link", name="Hedging contracts").click()
        time.sleep(5)

    def navigate_Planning_Booking(self):
        self.page.get_by_test_id("HeadsetMicIcon").click()
        self.page.get_by_role("link", name="Planning/Booking").click()
        time.sleep(5)

    def navigate_Rate_management(self):
        self.page.get_by_test_id("LocalShippingIcon").click()
        self.page.get_by_role("link", name="Rate management").first.click()
        time.sleep(5)

    def navigate_Invoices(self):
        self.page.get_by_test_id("RequestQuoteIcon").click()
        self.page.get_by_role("link", name="Invoices").click()
        time.sleep(5)

    def navigate_Notes(self):
        self.page.get_by_test_id("CheckBoxIcon").click()
        self.page.get_by_role("link", name="Notes").click()
        time.sleep(5)
