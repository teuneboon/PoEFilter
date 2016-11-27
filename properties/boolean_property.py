from typing import List

from properties.property import Property


class BooleanProperty(Property):
    value = None

    def __init__(self, value):
        self.value = value

    def process(self) -> List[str]:
        if self.value:
            return ['True']
        else:
            return ['False']
