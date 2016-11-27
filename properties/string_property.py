from typing import List

from properties.property import Property


class StringProperty(Property):
    value = ''

    def __init__(self, value):
        self.value = value

    def process(self) -> List[str]:
        return [str(self.value)]
