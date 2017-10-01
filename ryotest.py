def test_are_equal(a, b):
    assert a == b, "Expected {0}, got {1}.".format(b, a)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}.".format(b, a)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)


def test_not_in(collection, item):
    assert item not in collection, "{0} contains {1}".format(collection, item)


def test_is_greater_than(a, b):
    assert a > b, "{0} is not greater than {1}".format(a, b)


def test_is_between(a, b, c):
    assert a <= c <= b, "{0} is not between {1} and {2}".format(c, a, b)