from cli import punto_medio


def test_success():
    res, i = punto_medio(100, 20, 52.5, 0.05)
    assert res == 52.5
    assert i == 5

