"""
Data Types dealing with the standard library
Namely lists, dicts and tuples
"""
import copy

from .base import ImmutableObject


class List(ImmutableObject, list):
    """
    Replaces the list structure in the standard library
    """

    def __init__(self, iterable=[]):
        self._internal = list(copy.copy(iterable))

    def append(self, new_item):
        return self.__class__(self._internal + [new_item])

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self._internal == other._internal

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.__class__(self._internal[key])
        return self._internal[key]

    def __str__(self):
        return self._internal.__str__()

    def __repr__(self):
        return self._internal.__repr__()

    def extend(self, iterable):
        return self.__class__(self._internal + iterable)
