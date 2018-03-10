"""
Data Types dealing with the standard library
Namely lists, dicts and tuples
"""
import copy


class List(list):
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

    def __getitem__(self, idx):
        return self._internal[idx]
