from playwright.sync_api import expect


class LoginPage:

        def __init__(self,page):
            self.page = page

        def login(self,username,password):
            self.page.goto("https://demo.haroldwaste.com/")
            self.page.locator("input[name=email]").fill(username)
            self.page.locator("input[name=password]").fill(password)
            self.page.get_by_role("button", name="Log in").click()

            # Home page loaded Check
            expect(self.page.get_by_text("Summary")).to_be_visible()

        def logout(self):
            # Logout
            self.page.locator("div[style*='align-items: center; display: inline-grid'] div").get_by_text("Qa JULES").click()
            self.page.get_by_role("menuitem", name="Log out").click()

