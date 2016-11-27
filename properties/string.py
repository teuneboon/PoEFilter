from properties.property import Property


class String(Property):
    value = ''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
