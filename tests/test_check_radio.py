from pages.web_elements_page import WebElementsPage

def test_checkboxes_and_radios(page, base_url):
    w = WebElementsPage(page, base_url)
    w.goto()

    # check all checkboxes
    checkboxes = page.locator("input[type='checkbox']")
    for i in range(checkboxes.count()):
        checkbox = checkboxes.nth(i)
        if not checkbox.is_checked():
            checkbox.check()
            assert checkbox.is_checked()

    # uncheck first checkbox if exists
    if checkboxes.count() > 0:
        first = checkboxes.first
        if first.is_checked():
            first.uncheck()
            assert not first.is_checked()

    # radios - select each option
    radios = page.locator("input[type='radio']")
    for i in range(radios.count()):
        radios.nth(i).check()
        assert radios.nth(i).is_checked()
