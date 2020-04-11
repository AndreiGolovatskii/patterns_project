import attr


@attr.s
class ResourceWallet:
    money = attr.ib(default=0)
    oil = attr.ib(default=0)
    electricity = attr.ib(default=0)

    def __add__(self, other):
        return ResourceWallet(
            money=self.money + other.money,
            oil=self.oil + other.oil,
            electricity=self.electricity + other.electricity,
        )

    def __sub__(self, other):
        return ResourceWallet(
            money=self.money - other.money,
            oil=self.oil - other.oil,
            electricity=self.electricity - other.electricity,
        )

    def __lt__(self, other):
        return (
            self.money < other.money
            and self.oil < other.oil
            and self.electricity < other.electricity
        )

    def __le__(self, other):
        return (
            self.money <= other.money
            and self.oil <= other.oil
            and self.electricity <= other.electricity
        )

    def __eq__(self, other):
        return (
            self.money == other.money
            and self.oil == other.oil
            and self.electricity == other.electricity
        )
