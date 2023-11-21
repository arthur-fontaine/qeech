from fastapi import APIRouter
from pydantic import BaseModel
from qeech_data.core.repositories.recipe import RecipeRepository

get_recipe_router = APIRouter(prefix="/get-recipe")


class GetRecipeBody(BaseModel):
    recipe_id: int


@get_recipe_router.post("")
def get_recipe(body: GetRecipeBody):
    recipe = RecipeRepository.get_by_id(body.recipe_id)

    return {
        "name": recipe.name,
        "ingredients": [
            {
                "name": ingredient.name,
            }
            for ingredient in recipe.ingredients
        ],
    }
