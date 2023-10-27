from __future__ import annotations

from datetime import datetime
import random

from qeech_data.core.entities.ingredient import Ingredient
from qeech_data.core.entities.interaction import Interaction
from qeech_data.core.entities.recipe import Recipe
from qeech_data.core.entities.user import User
from qeech_data.core.utils.load_data import load_data


class Database:
    ingredients: list[Ingredient] = []
    interactions: list[Interaction] = []
    recipes: list[Recipe] = []
    users: list[User] = []

    def __init__(
        self,
        *,
        ingredients: list[Ingredient],
        interactions: list[Interaction],
        recipes: list[Recipe],
        users: list[User],
    ):
        self.ingredients = ingredients
        self.interactions = interactions
        self.recipes = recipes
        self.users = users


def __create_database() -> Database:
    __ingredients: dict[str, Ingredient] = {}
    __interactions: list[Interaction] = []
    __recipes: dict[int, Recipe] = {}
    __users: dict[int, User] = {}

    df_interactions = load_data("RAW_interactions")
    df_recipes = load_data("RAW_recipes")

    for row in df_recipes.iter_rows(named=True):
        recipe = Recipe(
            id=row["id"],
            name=row["name"],
        )
        recipe.interactions = []
        recipe.ingredients = []

        __recipes[row["id"]] = recipe

        recipe_ingredients: list[str] = eval(row["ingredients"])

        for recipe_ingredient in recipe_ingredients:
            if recipe_ingredient not in __ingredients:
                ingredient = Ingredient(
                    name=recipe_ingredient,
                )
                __ingredients[recipe_ingredient] = ingredient

                recipe.ingredients.append(ingredient)

    for row in df_interactions.iter_rows(named=True):
        if row["recipe_id"] not in __recipes:
            continue

        if row["user_id"] not in __users:
            user = User(
                id=row["user_id"],
                username=str(row["user_id"]),
                password=str(row["user_id"]),
            )
            user.interactions = []
            user.available_ingredients = random.sample(
                list(__ingredients.values()), random.randint(1, 50)
            )
            user.forbidden_ingredients = random.sample(
                list(__ingredients.values()), random.randint(1, 50)
            )
            __users[row["user_id"]] = user
        else:
            user = __users[row["user_id"]]

        recipe = __recipes[row["recipe_id"]]

        interaction = Interaction(
            date=datetime.fromisoformat(row["date"]),
            user=user,
            recipe=recipe,
        )
        __interactions.append(interaction)

        user.interactions.append(interaction)
        recipe.interactions.append(interaction)

    return Database(
        ingredients=list(__ingredients.values()),
        interactions=__interactions,
        recipes=list(__recipes.values()),
        users=list(__users.values()),
    )


database = __create_database()
