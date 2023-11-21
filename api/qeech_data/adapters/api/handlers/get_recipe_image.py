from qeech_data.core.repositories.recipe import RecipeRepository
import requests
from fastapi import APIRouter
from pydantic import BaseModel
from bs4 import BeautifulSoup

get_recipe_image_router = APIRouter(prefix="/get-recipe-image")


class GetRecipeImageBody(BaseModel):
    recipe_id: int


@get_recipe_image_router.post("")
def get_recipe(body: GetRecipeImageBody):
    recipe = RecipeRepository.get_by_id(body.recipe_id)

    recipe_html = requests.get(recipe.url).text
    recipe_soup = BeautifulSoup(recipe_html, "html.parser")
    
    recipe_image = recipe_soup.select_one(".primary-image img")
    recipe_image_url = None
    if recipe_image is not None:
        recipe_image_url = recipe_image.attrs["src"]

    return {
        "recipe_image_url": recipe_image_url,
    }
