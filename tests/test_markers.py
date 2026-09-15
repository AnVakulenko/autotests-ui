import pytest

@pytest.mark.smoke
def test_some_case():
    ...

@pytest.mark.regression
def test_regression_case():
    ...


@pytest.mark.smoke
class TestSute:
    def test_case1(self):
        ...

    def test_case2(self):
        ...