from filter_part import FilterPart


class Comment(FilterPart):
    comment = ''

    def __init__(self, comment):
        self.comment = comment

    def __str__(self):
        return '# {0}'.format(self.comment)
