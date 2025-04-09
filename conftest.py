import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def supp_l(request):
    return request.param


@pytest.fixture()
def setup(playwright: Playwright, request):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    # setting up for tracing start
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page
    context.tracing.stop(path='Results/trace.zip')
    context.close()
    browser.close()
