import immutable


def test_empty_list_creation():
    """
    Defaults to initializing with an empty list
    """
    assert immutable.List()._internal == []


def test_list_with_items_creation():
    """
    Can initialize with a list, which will be copied
    """
    original = list([1, 2, 3])
    immut = immutable.List(original)
    assert immut._internal == original
    assert immut._internal is not original


def test_list_append():
    """
    Appending operation does not affect the old list
    """
    lst = immutable.List()
    new_list = lst.append(1)
    assert lst._internal == []
    assert new_list._internal == [1]


def test_equality():
    """
    Only equals other immutable lists of the same value
    """
    assert immutable.List() == immutable.List()
    assert immutable.List([1, 2]) == immutable.List([1, 2])
    assert immutable.List() != []
