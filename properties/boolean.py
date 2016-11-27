from properties.property import Property


class Boolean(Property):
    value = False

    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value:
            return 'True'
        else:
            return 'False'
