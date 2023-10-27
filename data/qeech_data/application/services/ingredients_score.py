from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qeech_data.core.entities.ingredient import Ingredient
    from qeech_data.core.entities.recipe import Recipe

def ingredients_score(recipe: Recipe, *, available_ingredients: list[Ingredient]):
    recipe_ingredients = recipe.ingredients

    found_ingredients_counter = 0
    for recipe_ingredient in recipe_ingredients:
        for available_ingredient in available_ingredients:
            if recipe_ingredient == available_ingredient:
                found_ingredients_counter += 1
                break

    available_ingredients_ratio = found_ingredients_counter / len(recipe_ingredients)

    return available_ingredients_ratio
