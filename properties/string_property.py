from properties.property import Property


class StringProperty(Property):
    value = ''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
