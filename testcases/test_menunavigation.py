import pytest

from  page_objects.LoginPage import LoginPage
from page_objects.Side_Menu_Bar import Side_Menu_Bar
from config_read import RJson


test_data = RJson.readjson('data/master_data.json')
users = test_data["user"]

@pytest.mark.parametrize("user_l",users)
def test_menunavigation(user_l,setup):

    # Login Object from  page_objects
    log = LoginPage(setup)
    # Login
    log.login(user_l["username"], user_l["password"])


    # Supplier Page Object from page_objects
    sdMBar = Side_Menu_Bar(setup)

    # Navigation to the Suppliers and Sites
    setup.evaluate("document.body.style.zoom='80%'")
    sdMBar.navigate_Supplier_sites()

    # Navigation to the Sales
    sdMBar.navigate_Sales()

    # Navigation to Purchases Trading
    sdMBar.navigate_Purchases_Trading()

    # Navigate to the Invoices section
    sdMBar.navigate_Invoices()

    # Navigate to the Rate Management section
    sdMBar.navigate_Rate_management()

    # Navigate to the Hedging Contracts section
    sdMBar.navigate_Hedging_contracts()

    # Navigate to the Inbound Loads section
    sdMBar.navigate_Inbound_loads()

    # Navigate to the Planning & Booking section
    sdMBar.navigate_Planning_Booking()

    # Navigate to the Notes section
    sdMBar.navigate_Notes()

    setup.evaluate("document.body.style.zoom='100%'")
    # Logout
    log.logout()