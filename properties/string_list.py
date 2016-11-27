from typing import List

from properties.property import Property


class StringList(Property):
    values = None

    def __init__(self, values: List[str]=None):
        if values is None:
            values = []
        if not isinstance(values, list):
            values = [values]

        self.values = values

    def add_value(self, value):
        self.values.append(value)

    def __str__(self):
        # please don't kill me for this code
        return ' '.join([str(value) if isinstance(value, int) else '"{0}"'.format(value) for value in self.values])
