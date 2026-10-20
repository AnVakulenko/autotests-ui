import pytest

@pytest.mark.skip(reason="тестирую")
def test_feature_in_development():
    ...

@pytest.mark.skip(reason="тестирую класс")
class TestSuiteSkip:
    def test_feature_in_development_1():
        ...

    def test_feature_in_development_2():
        ...