from typing import List

from properties.property import Property


class StringList(Property):
    values = None

    def __init__(self, values: List[str]=None):
        if values is None:
            values = []
        self.values = values

    def add_value(self, value):
        self.values.append(value)

    def __str__(self):
        return ' '.join(['"{0}"'.format(value) for value in self.values])
