from datetime import datetime
import networkx as nx

from qeech_data.application.services.create_recipes_graph import create_recipes_graph
from qeech_data.core.database.database import database
from qeech_data.application.services.global_score import global_score
from qeech_data.core.entities.recipe import Recipe
from qeech_data.core.entities.user import User
from qeech_data.core.logger.logger import Logger
from qeech_data.core.utils.nx_knn import nx_knn

__cache = {}


def recommend_recipes(user: User, date: datetime):
    Logger.log_info(f"Searching for recipe recommendations for {date}")

    if (
        "recipes_graph" not in __cache
        or __cache["recipes_graph"]["users"] != database.users
        or __cache["recipes_graph"]["recipes"] != database.recipes
    ):
        recipes_graph = create_recipes_graph(
            recipes=database.recipes, users=database.users
        )

        __cache["recipes_graph"] = {
            "recipes": database.recipes,
            "users": database.users,
            "graph": recipes_graph,
        }
    else:
        Logger.log_info("Using cached recipes graph")
        recipes_graph: nx.Graph = __cache["recipes_graph"]["graph"]

    k_nearest_recipes_count = 5000
    Logger.log_info(f"Searching for {k_nearest_recipes_count} nearest recipes")
    recipes_to_search = list(map(
        lambda node: next(recipe for recipe in database.recipes if recipe.id == node[0]),
        nx_knn(recipes_graph, user.id, k_nearest_recipes_count, label="recipe")
    ))
    Logger.log_info(f"Found {len(recipes_to_search)} recipes")

    Logger.log_info("Calculating best recipes")
    start_time_score_recipes = datetime.now()
    bo5_recipes: list[tuple[float, Recipe]] = []
    for recipe in recipes_to_search:
        score = global_score(
            recipe,
            forbidden_ingredients=user.forbidden_ingredients,
            user=user,
            recipes_graph=recipes_graph,
            available_ingredients=user.available_ingredients,
            date=date,
        )

        if len(bo5_recipes) < 5:
            bo5_recipes.append((score, recipe))
        else:
            for bo_recipe in bo5_recipes:
                if score > bo_recipe[0]:
                    bo5_recipes.insert(bo5_recipes.index(bo_recipe), (score, recipe))
                    break
    
    Logger.log_info(f"Found top 5 recipes in {(datetime.now() - start_time_score_recipes).total_seconds()} seconds among {len(recipes_to_search)} recipes")

    return sorted(bo5_recipes, key=lambda x: x[0], reverse=True)[:5]
