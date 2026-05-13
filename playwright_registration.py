from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username = page.get_by_test_id('registration-form-username-input').locator('input')
    username.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    login_button = page.get_by_test_id('registration-page-registration-button')
    login_button.click()

    test_text = page.get_by_test_id('dashboard-toolbar-title-text')  # тут я понятия не имею как назвать переменную
    expect(test_text).to_be_visible()
    expect(test_text).to_have_text('Dashboard')
    page.wait_for_timeout(5000)