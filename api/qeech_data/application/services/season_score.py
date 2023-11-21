from __future__ import annotations

from datetime import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qeech_data.core.entities.recipe import Recipe

def season_score(recipe: Recipe, *, date: datetime):
    average_recipe_date = recipe.get_average_interaction_period()

    days_since_start_of_year = (date - datetime(date.year, 1, 1)).days

    # More the dates are close to each other, more the score is close to 1
    return 1 - abs(days_since_start_of_year - average_recipe_date) / 365
