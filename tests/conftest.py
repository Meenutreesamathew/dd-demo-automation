import pytest
from playwright.sync_api import sync_playwright
import os

BASE_URL = os.getenv("BASE_URL", "https://dd-demo-tau.vercel.app/web_elements.html")

def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default="true", help="headless true/false")

@pytest.fixture(scope="session")
def browser_context():
    headless = True
    # plugin option override
    # if pytest -k something with --headless=false, it's handled below
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL
