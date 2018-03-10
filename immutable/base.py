class ImmutableObject():
    def __setitem__(self, key, new):
        raise TypeError('{} does not support item assignment'.format(
            self.__class__.__name__))
