from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime

    from qeech_data.core.entities.user import User
    from qeech_data.core.entities.recipe import Recipe


class Interaction:
    date: datetime

    user: User
    recipe: Recipe
