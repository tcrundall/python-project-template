from example import add


def test_something():
    assert 5 == 5, "If this fails, display this message"


def test_add():
    expected_result = 4
    assert expected_result == add(2, 2), "Add broke"
