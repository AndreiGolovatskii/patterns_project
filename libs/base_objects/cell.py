import attr


@attr.s(frozen=True)
class Cell:
    x = attr.ib(converter=int)
    y = attr.ib(converter=int)

    def __add__(self, other):
        return Cell(self.x + other.x, self.y + other.y)


