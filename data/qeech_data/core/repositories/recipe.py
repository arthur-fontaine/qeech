from qeech_data.core.database.database import database
from qeech_data.core.entities.recipe import Recipe
from qeech_data.core.logger.logger import Logger


class RecipeRepository:
    @staticmethod
    def get_by_id(recipe_id: int) -> Recipe:
        Logger.log_info(f"Getting recipe with id {recipe_id}")

        for recipe in database.recipes:
            if recipe.id == recipe_id:
                Logger.log_info(f"Found recipe with id {recipe_id}")
                return recipe

        raise Exception("Recipe not found")
