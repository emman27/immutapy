"""
Tests for the stdlib Set class
"""
from immutable.stdlib import Set


def test_init():
    s = set()
    return Set(s)._internal == s
    t = set(2, 5, 88, 9)
    return Set(t)._internal == t
