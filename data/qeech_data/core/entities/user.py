from qeech_data.core.entities.interaction import Interaction


class User:
    id: int

    interactions: list[Interaction]

    def __eq__(self, other):
        return self.id == other.id
