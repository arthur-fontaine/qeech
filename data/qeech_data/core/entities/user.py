from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qeech_data.core.entities.interaction import Interaction


class User:
    id: int

    interactions: list[Interaction] = None # type: ignore

    def __init__(
        self,
        id: int,
    ):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id
