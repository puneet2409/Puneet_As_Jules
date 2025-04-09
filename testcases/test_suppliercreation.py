import time
from datetime import datetime

import pytest
from playwright.sync_api import Page, expect, Playwright

from  page_objects.LoginPage import LoginPage
from  page_objects.Supplier_Sites import Supplier_Sites
from config_read import RJson


test_data = RJson.readjson('data/master_data.json')
users = test_data["user"]


@pytest.mark.parametrize("user_l",users)

def test_testcase1(playwright: Playwright,user_l,setup):


    #Login Object from  page_objects
    log = LoginPage(setup)
    # Login
    log.login(user_l["username"],user_l["password"])

    # Supplier Page Object from page_objects
    supplier = Supplier_Sites(setup)
    # Navigation to the Suppliers and Sites
    supplier.navigate_Supplier_page()

    # Add a new Supplier
    supp = user_l["supplier details"]

    for sp in supp:
        # Supplier Name
        current_time = datetime.now().strftime("%H:%M:%S")
        value_to_fill = (f"{current_time}Supplier")

        supplier.add_newSupplier(value_to_fill,sp)

        #Validate that the supplier was created and added into the table
        setup.get_by_placeholder("Search by company name").fill(value_to_fill)
        time.sleep(5)
        value = setup.locator("tr[class = 'MuiTableRow-root'] td").nth(2).text_content()
        value = value.replace(" ","")
        assert value_to_fill == value,"The Supplier is not created"

    #Logout
    log.logout()
