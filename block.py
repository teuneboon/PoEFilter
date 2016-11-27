from collections import OrderedDict

from filter_part import FilterPart
from properties.boolean_property import BooleanProperty
from properties.property import Property
from properties.string_property import StringProperty
from theme import Theme


class Block(FilterPart):
    show = True  # if show is false we'll make it a hide block
    properties = {}

    def __init__(self, show=True, theme: Theme=None, **kwargs):
        self.show = show

        if theme is not None:
            theme.process(self.properties)

        for key, value in kwargs.items():
            self.set_property(self.__translate_property_key(key), value)

    @staticmethod
    def __translate_property_key(key):
        """
        This changes a property key like this_is_a_test to ThisIsATest
        :param key:
        :return:
        """
        return ''.join([word.capitalize() for word in key.split('_')])

    def set_property(self, key, value):
        if not isinstance(value, Property):
            # not already passed as a property, we'll try to guess what the user intended
            if isinstance(value, bool):
                value = BooleanProperty(value)
            else:
                # we'll assume it's wanted as a string
                value = StringProperty(value)

        self.properties[key] = value

    def __str__(self):
        if self.show:
            keyword = 'Show:'
        else:
            keyword = 'Hide:'

        property_string = ''
        for key, value in self.properties.items():
            property_string += '    {0} {1}\n'.format(key, str(value))

        result = '{0}\n{1}'.format(keyword, property_string)
        return result
