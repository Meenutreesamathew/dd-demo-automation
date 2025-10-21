# import pytest
# from playwright.sync_api import Page, expect
#
# def test_alerts_and_modals(page: Page):
#     # Navigate to the test page
#     page.goto("https://dd-demo-tau.vercel.app/web_elements.html")
#
#     # -------- Handle Alert --------
#     def handle_alert(dialog):
#         print(f"Alert text: {dialog.message}")
#         dialog.accept()
#
#     page.once("dialog", handle_alert)
#     page.locator("#alertBtn").click()
#
#     # -------- Handle Confirm --------
#     def handle_confirm(dialog):
#         print(f"Confirm text: {dialog.message}")
#         dialog.accept()
#
#     page.once("dialog", handle_confirm)
#     page.locator("#confirmBtn").click()
#
#     # -------- Handle Prompt --------
#     def handle_prompt(dialog):
#         print(f"Prompt text: {dialog.message}")
#         dialog.accept("Playwright QA Test")
#
#     page.once("dialog", handle_prompt)
#     page.locator("#promptBtn").click()
#
#     # Verify page loaded correctly
#     expect(page).to_have_url("https://dd-demo-tau.vercel.app/web_elements.html")
