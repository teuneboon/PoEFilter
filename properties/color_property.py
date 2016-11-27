from properties.property import Property


class ColorProperty(Property):
    red = 0
    green = 0
    blue = 0
    opacity = 255

    def __init__(self, red, green, blue, opacity=255):
        self.red = red
        self.green = green
        self.blue = blue
        self.opacity = opacity

    def __str__(self):
        return '{0} {1} {2} {3}'.format(self.red, self.green, self.blue, self.opacity)
