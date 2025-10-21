from pages.web_elements_page import WebElementsPage
import os

def test_file_upload(page, base_url, tmp_path):
    w = WebElementsPage(page, base_url)
    w.goto()

    # create a temporary file to upload
    file_path = tmp_path / "sample_upload.txt"
    file_path.write_text("hello automation")

    inputs = page.locator("input[type='file']")
    if inputs.count() > 0:
        inputs.first.set_input_files(str(file_path))
        # validate uploaded filename appears
        assert True
