import time
from datetime import datetime
from playwright.sync_api import Page, expect


def test_testcase1(page:Page):
    #Login
    current_time = datetime.now().strftime("%H:%M:%S")
    value_to_fill = (f"{current_time}ABCD")
    page.goto("https://demo.haroldwaste.com/")
    page.locator("input[name=email]").fill("qa@julesai.com")
    page.locator("input[name=password]").fill("QaJULES2023!")
    page.get_by_role("button",name="Log in").click()
    # Home page
    expect(page.get_by_text("Summary")).to_be_visible()

    #Navigation to the Suppliers and Sites
    page.get_by_test_id("LibraryBooksIcon").click()
    page.get_by_role("link", name="Suppliers & Sites").click()
    time.sleep(5)
    page.get_by_role("button",name="Add a new supplier").click()

    page.locator("div[data-test-id='Company.companyName'] input").fill(value_to_fill)
    page.locator("div[data-test-id='Company.companyLegalName'] input").fill("Agarwal")

    page.get_by_role("button",name="Next").click()
    page.get_by_role("button", name="Save").click()
    time.sleep(5)
    page.get_by_placeholder("Search by company name").fill(value_to_fill)
    time.sleep(5)
    value = page.locator("tr[class = 'MuiTableRow-root'] td").nth(2).text_content()

    value = value.replace(" ","")
    print(value)
    print(value_to_fill)
    assert value_to_fill == value,"The Supplier is not created"
    #Logout

    page.get_by_text("Qa JULES").click()
    page.get_by_role("menuitem",name="Log out").click()


#def test_logout(page: Page):
