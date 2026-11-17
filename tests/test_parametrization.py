import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert  number > 0
    print(f'Number: {number}')

@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browsers', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browsers: str):
    assert len(os + browsers) > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browsers(request: SubRequest):
    return request.param

def test_open_browsers(browsers: str):
    print(f'Running test on browsers: {browsers}')

@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'User with operations: {user}, {account}')


    def test_user_without_operations(self,  user: str):
        print(f'User without operations: {user}')


users = {
    '+7111222333': 'User with money on bank account',
    '+7111222444': 'User without money on bank account',
    '+7111222555': 'User with operations on bank account'
}

@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
     ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    ...