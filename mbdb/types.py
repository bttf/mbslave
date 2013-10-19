
class PartialDate(object):

    __slots__ = ('year', 'month', 'day')

    def __init__(self, year=None, month=None, day=None):
        self.year = year
        self.month = month
        self.day = day

    def __composite_values__(self):
        return self.year, self.month, self.day

    def __iter__(self):
        yield self.year
        yield self.month
        yield self.day

    def __repr__(self):
        return "{0.__class__.__name__}(year={0.year}, month={0.month}, day={0.day})".format(self)

    def __eq__(self, other):
        return isinstance(other, PartialDate) and \
            other.year == self.year and \
            other.month == self.month and \
            other.day == self.day

    def __ne__(self, other):
        return not self.__eq__(other)

    def __nonzero__(self):
        return bool(self.year or self.month or self.day)
