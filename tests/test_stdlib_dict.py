from immutable import Dict


def test_str():
    """
    Renders correctly on str
    """
    assert str(Dict({'a': 1})) == "{'a': 1}"
