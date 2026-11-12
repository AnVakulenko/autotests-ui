import pytest

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