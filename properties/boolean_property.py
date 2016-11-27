from properties.property import Property


class BooleanProperty(Property):
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value:
            return 'True'
        else:
            return 'False'
