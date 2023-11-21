from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qeech_data.core.entities.interaction import Interaction
    from qeech_data.core.entities.ingredient import Ingredient


class User:
    id: int
    username: str
    password: str

    interactions: list[Interaction] = None # type: ignore
    forbidden_ingredients: list[Ingredient] = None # type: ignore
    available_ingredients: list[Ingredient] = None # type: ignore

    def __init__(
        self,
        id: int,
        username: str,
        password: str,
    ):
        self.id = id
        self.username = username
        self.password = password

    def __eq__(self, other):
        return self.id == other.id
