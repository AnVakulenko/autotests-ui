from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login") #переход на страницу по ссылке

    email_input = page.get_by_test_id('login-form-email-input').locator('input') #найдет поле с таким локатором
    email_input.fill('user.name@gmail.com') #вводит в найденное поле имя пользователя user.name@gmail.com

    password_input = page.get_by_test_id('login-form-password-input').locator('input') #найдет поле с таким локатором
    password_input.fill('Password') #вводит в найденное поле пароль Password

    login_button = page.get_by_test_id('login-page-login-button') #найдет кнопку
    login_button.click() #нажать на кнопку

    wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert') #находит алерт
    expect(wrong_email_or_password_alert).to_be_visible() #проверяет что отображается
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password') #проверяет что отображается именно этот текст

    page.wait_for_timeout(5000) #это не нужная вещь, просто ждем 5 секунд