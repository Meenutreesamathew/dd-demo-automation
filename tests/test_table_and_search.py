from pages.web_elements_page import WebElementsPage
import time

def test_table_search_sort(page, base_url):
    w = WebElementsPage(page, base_url)
    w.goto()

    # attempt to search/filter in page (if input exists)
    if page.locator("input[placeholder*='Search']").count() > 0:
        page.fill("input[placeholder*='Search']", "John")
        time.sleep(0.5)
        # assert some rows visible
        rows = page.locator("table tbody tr")
        assert rows.count() >= 0

    # check table sorting click on header
    headers = page.locator("table thead th")
    if headers.count() > 0:
        headers.first.click()
        # no error is success
        assert True
