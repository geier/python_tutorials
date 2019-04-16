import pytest

def test_with_file(tmpdir):
    """tmpdir is a built-in fixture, provide a temporary directory"""
    assert str(tmpdir).startswith('/tmp')


@pytest.fixture
def smtp():
    import smtplib
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


def test_fixture(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert 1


@pytest.fixture
def smtp2():
    """use yield if you need to tear something down"""
    import smtplib
    smtp = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp
    print('tear down')
    smtp.close()


def test_fixture2(smtp2):
    response, msg = smtp2.ehlo()
    assert response == 250
    assert 1
