from comment import Comment
from filter_part import FilterPart
from properties.boolean import Boolean
from properties.comparer import Comparer
from properties.property import Property
from properties.string_list import StringList
from theme import Theme


# properties that we always want to add as a comparer
COMPARER_PROPERTIES = ['Rarity', 'ItemLevel', 'DropLevel', 'LinkedSockets', 'Sockets', 'Quality', 'Width', 'Height']


class Block(FilterPart):
    show = True  # if show is false we'll make it a hide block
    properties = None
    comment = None

    def __init__(self, show=True, theme: Theme=None, comment=None, **kwargs):
        """

        :param show: if this is false we explicitly make it a Hide: block
        :param theme: a Theme object, this will get overwritten by kwargs if you use them
        :param comment: optional comment we want to attach, this is just a shorthand since you can also add it manually
        :param kwargs:
        :return:
        """
        self.properties = {}
        self.show = show
        if comment is not None:
            if isinstance(comment, Comment):
                self.comment = comment
            else:
                self.comment = Comment(comment)

        self.set_theme(theme)

        for key, value in kwargs.items():
            self.set_property(key, value)

    def set_theme(self, theme: Theme):
        if theme is not None:
            theme.process(self)

    @staticmethod
    def __translate_property_key(key):
        """
        This changes a property key like this_is_a_test to ThisIsATest
        :param key:
        :return:
        """
        if key == '_class':
            key = 'class'

        return ''.join([word.capitalize() for word in key.split('_')])

    def set_property(self, key, value):
        key = self.__translate_property_key(key)
        if value is None:
            if key in self.properties:
                del self.properties[key]
        else:
            if not isinstance(value, Property):
                # not already passed as a property, we'll try to guess what the user intended
                if isinstance(value, bool):
                    value = Boolean(value)
                elif key in COMPARER_PROPERTIES:
                    value = Comparer(value)
                else:
                    # we'll assume it's wanted as a string with "" around it
                    value = StringList(value)

            self.properties[key] = value

    def __str__(self):
        if self.show:
            keyword = 'Show:'
        else:
            keyword = 'Hide:'

        property_string = ''
        for key, value in self.properties.items():
            property_string += '    {0} {1}\n'.format(key, str(value))

        result = ''
        if self.comment is not None:
            result += '{0}\n'.format(str(self.comment))

        result += '{0}\n{1}'.format(keyword, property_string)
        return result
