from pages.web_elements_page import WebElementsPage

def test_select_single_and_multi(page, base_url):
    w = WebElementsPage(page, base_url)
    w.goto()

    # single select by value/text
    selectors = page.locator("select")
    for i in range(selectors.count()):
        sel = selectors.nth(i)
        # try selecting by index/text
        options = sel.locator("option")
        if options.count() > 1:
            # select the second option (if exists)
            value = options.nth(1).get_attribute("value")
            if value:
                sel.select_option(value=value)
                selected = sel.evaluate("el => el.value")
                assert selected == value
