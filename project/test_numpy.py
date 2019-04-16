import numpy as np


def normalize(data):
    """normalize data to mean=0 and var=1"""
    return (data - data.mean(axis=0)) / data.std(axis=0)


def test_normalize():
    """This test will fail, because the mean isn't exactly 0,
    same goes for the variance"""
    data = np.random.random(10)
    normalized = normalize(data)
    assert normalized.mean() == 0
    assert normalized.var() == 1


def test_normalize_close():
    data = np.random.random(10)
    normalized = normalize(data)
    assert np.allclose(normalized.mean(), np.array([0]))
    assert np.allclose(normalized.var(), 1)


def test_normalize_two_dim():
    data = np.random.random(100).reshape(10, 10)
    normalized = normalize(data)
    assert np.allclose(normalized.mean(), np.array([0] * 10))
    assert np.allclose(normalized.var(), np.array([1] * 10))
