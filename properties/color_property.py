from typing import List

from properties.property import Property


class ColorProperty(Property):
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
        if 1 >= red > 0:
            red = int(red * 255.0)
        if 1 >= green > 0:
            green = int(green * 255.0)
        if 1 >= blue > 0:
            blue = int(blue * 255.0)
        if 1 >= opacity > 0:
            opacity = int(opacity * 255.0)

        self.red = red
        self.green = green
        self.blue = blue
        self.opacity = opacity

    def process(self) -> List[str]:
        return ['{0} {1} {2} {3}'.format(self.red, self.green, self.blue, self.opacity)]
