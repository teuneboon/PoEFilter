from properties.property import Property


class Color(Property):
    red = 0
    green = 0
    blue = 0
    opacity = 255

    def __init__(self, red, green, blue, opacity=255):
        """
        If the value of one of the colors is equal or less than 1, we assume you pass it as a percentage(0.0 -> 1.0) and
        multiply it by 255
        :param red:
        :param green:
        :param blue:
        :param opacity:
        :return:
        """
        if 1.0 >= red >= 0.0:
            red = int(red * 255.0)
        if 1.0 >= green >= 0.0:
            green = int(green * 255.0)
        if 1.0 >= blue >= 0.0:
            blue = int(blue * 255.0)
        if 1.0 >= opacity >= 0.0:
            opacity = int(opacity * 255.0)

        self.red = red
        self.green = green
        self.blue = blue
        self.opacity = opacity

    def __str__(self):
        return '{0} {1} {2} {3}'.format(self.red, self.green, self.blue, self.opacity)
