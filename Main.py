import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    page.get_by_role("link", name="English 7,261,000+ articles").click()
    page.get_by_role("link", name="Jensen Huang", exact=True).click()
    page.wait_for_timeout(2000)


    # ---------------------
    context.close()
    browser.close()


website = "https://reservation-cf.frontdeskqms.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"
def run(playwright: Playwright) -> None: 
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(website)
    page.wait_for_timeout(2000)

with sync_playwright() as playwright:
    run(playwright)

