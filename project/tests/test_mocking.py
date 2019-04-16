import os.path

def getssh():
    return os.path.join(os.path.expanduser("~admin"), '.ssh')

def test_mocking(monkeypatch):

    def mockreturn(path):
        return '/abc'

    monkeypatch.setattr(os.path, 'expanduser', mockreturn)
    assert getssh() == '/abc/.ssh'
