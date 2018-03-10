import immutable


def test_empty_list_creation():
    assert immutable.List()._internal == []


def test_list_with_items_creation():
    original = list([1, 2, 3])
    immut = immutable.List(original)
    assert immut._internal == original
    assert immut._internal is not original


def test_list_is_true_deepcopy():
    original = list([[{'a': 1}]])
    immut = immutable.List(original)
    assert immut._internal[0][0] is not original[0][0]
