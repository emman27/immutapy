import immutable
import pytest


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


def test_index():
    """
    Can index and retrieve an item
    """
    assert immutable.List([1])[0] == 1
    assert immutable.List([1, 2])[-1] == 2


def test_slice():
    """
    Can slice a list
    """
    assert immutable.List([1, 2, 3])[1:] == immutable.List([2, 3])


def test_str():
    """
    Will print the list instead of <class List>
    """
    assert str(immutable.List([1, 2, 3])) == '[1, 2, 3]'


def test_extend():
    """
    Can extend with a regular iterable
    """
    lst = immutable.List()
    new = lst.extend([1, 2])
    assert lst == immutable.List()
    assert new == immutable.List([1, 2])


def test_repr():
    """
    Should implement similar to list repr
    """
    assert immutable.List(['a', 1]).__repr__() == list(['a', 1]).__repr__()


def test_set_raises_typeerror():
    with pytest.raises(TypeError):
        immutable.List([1, 2])[0] = 3


def test_pop():
    lst = immutable.List([1, 2, 3])
    val, new_list = lst.pop(1)
    assert val == 2
    assert new_list == immutable.List([1, 3])
    assert lst == immutable.List([1, 2, 3])


def test_pop_default():
    lst = immutable.List([1, 2, 3])
    val, new_list = lst.pop()
    assert val == 3
    assert new_list == immutable.List([1, 2])
    assert lst == immutable.List([1, 2, 3])


def test_pop_zero():
    lst = immutable.List([1, 2, 3])
    val, new_list = lst.pop(0)
    assert val == 1
    assert new_list == immutable.List([2, 3])
    assert lst == immutable.List([1, 2, 3])


def test_in():
    assert 1 in immutable.List([1, 2, 3])
    assert immutable.List([1]) in immutable.List([
        immutable.List([1])
    ])


def test_sort():
    lst = immutable.List([3, 2, 1])
    assert lst.sort() == immutable.List([1, 2, 3])
    assert lst == immutable.List([3, 2, 1])


def test_sort_with_key():
    lst = immutable.List([1, 2, 3])
    # Fake reverse sorting for integers!
    assert lst.sort(key=lambda x: -x) == immutable.List([3, 2, 1])


def test_sort_with_reverse():
    lst = immutable.List([1, 2, 3])
    assert lst.sort(reverse=True) == immutable.List([3, 2, 1])


def test_count():
    lst = [1, 2, 3, 4]
    im = immutable.List(lst)
    assert lst.count(1) == im.count(1)
    assert lst.count('a') == im.count('a')


def test_insert_start_and_end():
    im = immutable.List([])
    new = im.insert(0, 'a')
    assert im == immutable.List()
    assert new == immutable.List(['a'])


def test_insert_middle():
    im = immutable.List([1, 2, 3, 4])
    new = im.insert(1, 'b')
    assert im == immutable.List([1, 2, 3, 4])
    assert new == immutable.List([1, 'b', 2, 3, 4])
