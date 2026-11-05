import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправка данных в сервис аналитики")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициалиация настройки автотестов")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")

@pytest.fixture(scope="function") #можно не указывать function т.к используетя по умолчанию
def browser():
    print("[FUNCTION] Открываем в браузере каждый автотест")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...
    def test_user_can_create_course(self, settings, user, browser):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...