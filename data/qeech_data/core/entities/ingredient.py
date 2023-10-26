class Ingredient:
    name: str

    def __init__(
        self,
        name: str,
    ):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
