from properties.property import Property


class Comparer(Property):
    comparer = '='
    value = ''

    def __init__(self, value, comparer='='):
        self.comparer = comparer
        self.value = value

    def __str__(self):
        return '{0} {1}'.format(self.comparer, self.value)
