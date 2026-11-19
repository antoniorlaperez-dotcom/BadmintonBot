import re
from playwright.sync_api import Playwright, sync_playwright, expect

# testing
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


# Attempted to do a auto regesteration bot
website = "https://reservation-cf.frontdeskqms.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"

def run(playwright: Playwright) -> None: 
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(website)
    page.get_by_text("Badminton").click()
    page.get_by_role("button", name="Confirm").click()
    page.locator("summary").filter(has_text="Thursday November 19ᵗʰ,").click() # change date to desired day
    page.locator("summary").filter(has_text="Thursday November 19ᵗʰ,").click() # change time to desired time
    page.get_by_role("button", name="1:30 p.m. Thursday November 19ᵗʰ,").click()
    page.get_by_role("textbox", name="Phone number (please enter").click()
    page.get_by_role("textbox", name="Phone number (please enter").fill("3432024780")
    page.get_by_role("textbox", name="Email address: *").click()
    page.get_by_role("textbox", name="Email address: *").fill("perez.o.antonio@gmail.com")
    page.get_by_role("textbox", name="Name *").click()
    page.get_by_role("textbox", name="Name *").fill("Antonio")
    page.wait_for_timeout(50000)


with sync_playwright() as playwright:
    run(playwright)




