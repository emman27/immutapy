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

    def __getslice__(self, start, end):
        return self.__getitem__(slice(start, end))

    def __str__(self):
        return self._internal.__str__()

    def __repr__(self):
        return self._internal.__repr__()

    def extend(self, iterable):
        return self.__class__(self._internal + iterable)

    def pop(self, idx=-1):
        """
        Warning: This method behaves differently from the standard library's pop

        This is due to the fact that the stdlib's pop actually achieves 2 things at once:
            1. Returns the element at idx (or the last element if idx is not specified)
            2. Removes that element from the list
               (side-effect that should not happen in an immutable structure)

        :args idx(int): The index to pop, defaults to the last item in the list
        :returns (<T>, immutable.List): Returns a two-tuple of the item popped, as well as the
            new list after popping. The original list remains unmodified

        >>> item, new_list = immutable.List([1, 2, 3]).pop()
        >>> item
        3
        >>> new_list
        [1, 2]
        """
        if idx == -1:
            idx = len(self._internal) - 1
        new_list = self.__class__(self._internal[:idx] + self._internal[idx + 1:])
        value = self._internal[idx]
        return (value, new_list)
