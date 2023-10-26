from __future__ import annotations

from datetime import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qeech_data.core.entities.ingredient import Ingredient
    from qeech_data.core.entities.interaction import Interaction


class Recipe:
    id: int
    name: str

    ingredients: list[Ingredient]
    interactions: list[Interaction]

    def get_expected_period(self) -> tuple[int, int]:
        season_ranges: list[tuple[int, int]] = [
            (354, 365),
            (1, 78),  # Winter: 21 December - 31 December & 1 January - 20 March
            (79, 170),  # Spring: 21 March - 20 June
            (171, 262),  # Summer: 21 June - 20 September
            (263, 353),  # Autumn: 21 September - 20 December
        ]

        average_interaction_period = self.get_average_interaction_period()

        for season_range in season_ranges:
            if season_range[0] <= average_interaction_period <= season_range[1]:
                return season_range

        raise Exception(
            f"Unexpected average interaction period: {average_interaction_period}"
        )

    def get_average_interaction_period(self) -> float:
        average_interaction_period = 0
        for interaction in self.interactions:
            interaction_year_datetime = datetime(interaction.date.year, 1, 1)
            average_interaction_period += (
                interaction.date - interaction_year_datetime
            ).days
        average_interaction_period /= len(self.interactions)

        return average_interaction_period
    
    def __eq__(self, other):
        return self.id == other.id
