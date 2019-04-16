import pytest

# usually, the code to test would be imported
def increment(x):
    return x + 1


def test_increment():
    assert increment(2) == 3


def test_increment_negative():
    assert increment(-1) == 3


def get_list():
    return range(1, 10)

def test_list():
    assert get_list() == range(12)


def test_strings():
    assert 'Hello World!' == 'Helo World!'


def inverse(x):
    return 1.0 / x


def test_raises():
    with pytest.raises(ZeroDivisionError, message="We expect a Zero Division Error"):
        inverse(0)


def test_fails_to_raise():
    with pytest.raises(ZeroDivisionError, message="We expect a Zero Division Error"):
        inverse(1)
