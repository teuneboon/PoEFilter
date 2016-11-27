from filter_part import FilterPart


class Filter(object):
    parts = None

    def __init__(self, parts=None):
        if parts is None:
            parts = []

        self.parts = parts

    def add_part(self, part: FilterPart):
        self.parts.append(part)

    def __str__(self):
        result = ''
        for part in self.parts:
            result += '{0}\n'.format(str(part))

        return result
