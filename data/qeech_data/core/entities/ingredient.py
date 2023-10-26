class Ingredient:
    id: int

    def __eq__(self, other):
        return self.id == other.id
