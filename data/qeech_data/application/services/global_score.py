import networkx as nx
from datetime import datetime

from qeech_data.application.services.diet_score import diet_score
from qeech_data.application.services.habits_score import habits_score
from qeech_data.application.services.ingredients_score import ingredients_score
from qeech_data.application.services.season_score import season_score
from qeech_data.core.entities.ingredient import Ingredient
from qeech_data.core.entities.recipe import Recipe
from qeech_data.core.entities.user import User


def global_score(
    recipe: Recipe,
    *,
    forbidden_ingredients: list[Ingredient],
    user: User,
    recipes_graph: nx.Graph,
    available_ingredients: list[Ingredient],
    date: datetime,
):
    diet_score_value = diet_score(recipe, forbidden_ingredients=forbidden_ingredients)
    habits_score_value = habits_score(recipe, user=user, recipes_graph=recipes_graph)
    ingredients_score_value = ingredients_score(
        recipe, available_ingredients=available_ingredients
    )
    season_score_value = season_score(recipe, date=date)

    return (
        habits_score_value + ingredients_score_value + season_score_value
    ) * diet_score_value
