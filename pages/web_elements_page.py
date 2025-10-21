from playwright.sync_api import Page

class WebElementsPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = base_url

        # text fields
        self.input_text = "input#text"         # example id - adjust if different
        self.input_email = "input#email"
        self.input_pass = "input#password"
        # buttons
        self.submit_btn = "button#submit"
        self.toggle_btn = "button#toggle"
        # checkboxes / radios
        self.checkbox_all = "input[type='checkbox']"
        self.radio_options = "input[type='radio']"
        # selects
        self.single_select = "select#select"
        # alerts / modals - selectors may vary; use text match for alerts/confirm
        self.alert_trigger = "button#alertBtn"
        self.confirm_trigger = "button#confirmBtn"
        self.prompt_trigger = "button#promptBtn"
        # table
        self.table = "table#table"
        self.table_rows = "table#table tbody tr"
        # drag & drop
        self.drag_src = "#draggable"
        self.drop_target = "#droppable"
        # file upload
        self.file_input = "input[type='file']"
        # date / time
        self.date_input = "input[type='date']"

    def goto(self):
        self.page.goto(self.url)
