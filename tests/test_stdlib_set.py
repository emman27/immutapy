"""
Tests for the stdlib Set class
"""
from immutable.stdlib import Set


def test_init():
    s = set()
    assert Set(s)._internal == s
    t = set({2, 5, 88, 9})
    assert Set(t)._internal == t


def test__eq():
    assert Set({1, 2, 3}) == Set({3, 2, 1})
    assert Set({}) == Set()


def test__ne():
    assert Set({1, 2}) != Set({1})


def test_add():
    s = Set()
    t = s.add(1)
    assert s == Set()
    assert t == Set({1})
