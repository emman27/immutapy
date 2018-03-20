from immutable import Dict


def test_str():
    """
    Renders correctly on str
    """
    assert str(Dict({'a': 1})) == "{'a': 1}"


def test_getitem():
    """
    Allows the getting of a key
    """
    d = Dict({'a': 1})
    assert d['a'] == 1


def test_equality():
    """
    Dicts are equal if the underlying dictionaries are equal
    """
    assert Dict() == Dict()
    assert Dict({'a': 1}) == Dict({'a': 1})
    assert Dict() != Dict({'a': 1})


def test_ne():
    """
    Tests non-equality
    """
    assert Dict() != Dict({'a': 2})
    assert {} != Dict()


def test_pop():
    """
    Tests on popping
    """
    d = Dict({'a': 1})
    popped, e = d.pop('a')
    assert popped == 1
    assert e == Dict()


def test_keys():
    o = {'a': 23, 'b': 3}
    assert Dict(o).keys() == o.keys()


def test_values():
    o = {'a': 23, 'b': 3}
    assert sorted(Dict(o).values()) == sorted(o.values())


def items():
    o = {'a': 23, 'b': 3}
    assert Dict(o).items() == o.items()


def test_update():
    d = Dict()
    e = d.update({'b': 3})
    assert d == Dict()
    assert e == Dict({'b': 3})


def test_get():
    d = Dict({'a': 1})
    assert d.get('a') == 1
    assert d.get('a', 23) == 1
    assert d.get('b') is None
    assert d.get('b', 44) == 44
