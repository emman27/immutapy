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
        self._internal = copy.deepcopy(iterable)
