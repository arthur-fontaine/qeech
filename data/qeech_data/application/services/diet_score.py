from qeech_data.core.entities.ingredient import Ingredient
from qeech_data.core.entities.recipe import Recipe

def diet_score(recipe: Recipe, *, forbidden_ingredients: list[Ingredient]):
    recipe_ingredients = recipe.ingredients

    for recipe_ingredient in recipe_ingredients:
        for forbidden_ingredient in forbidden_ingredients:
            if recipe_ingredient.id == forbidden_ingredient.id:
                return 0
            
    return 1
