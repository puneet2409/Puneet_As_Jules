import time


class Supplier_Sites:

        def __init__(self,page):
            self.page = page

        def navigate_Supplier_page(self):
            self.page.get_by_test_id("LibraryBooksIcon").click()
            self.page.get_by_role("link", name="Suppliers & Sites").click()
            time.sleep(5)

        def add_newSupplier(self,value_to_fill,supp_l):

            buyer = "Akhil Harold"
            purchase = "1 week max Arrival date +5"

            # Add a new Supplier
            self.page.get_by_role("button", name="Add a new supplier").click()
            # Usual Name
            self.page.locator("div[data-test-id='Company.companyName'] input").fill(value_to_fill)
            # Legal Entity Name
            self.page.locator("div[data-test-id='Company.companyLegalName'] input").fill(supp_l["Legal_Entity_Name"])
            time.sleep(5)
            # ERP Id
            self.page.locator("div[data-test-id='Company.erpId'] input").fill("ERP1234")
            # Legal Form
            self.page.locator("div[data-test-id='Company.legalForm'] input").fill("CompanyLegal1")

            # Purchase Payment terms
            self.page.locator("div[data-test-id='Company.paymentTerms'] input").click()
            self.page.get_by_role("option", name=purchase).click()
            time.sleep(3)

            # Buyer
            self.page.locator("div[data-test-id='Company.defaultUser'] input").click()
            self.page.get_by_role("option", name=buyer).click()

            # Navigate to Next page
            self.page.get_by_role("button", name="Next").click()

            # Billing And Financial Address 1
            self.page.locator("div[data-test-id='AddressForm.address'] input").fill("Address of the Bill")

            # Billing And Financial Address 2
            self.page.locator("div[data-test-id='AddressForm.address2'] input").fill("Address2")

            # Save the Supplier details
            self.page.get_by_role("button", name="Save").click()
            time.sleep(5)