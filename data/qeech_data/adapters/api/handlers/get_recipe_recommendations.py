from typing import Annotated
from fastapi import APIRouter, Header
from pydantic import BaseModel, Field, validator
from datetime import datetime

from qeech_data.adapters.api.utils.auth import auth
from qeech_data.application.usecases.recommend_recipes import recommend_recipes

get_recipe_recommentations_router = APIRouter(prefix="/get-recipe-recommendations")


class GetRecipeRecommendationsBody(BaseModel):
    date: datetime = Field(default_factory=datetime.now)

    @validator("date")
    def should_not_be_offset_awared(cls, v):
        if v.tzinfo is not None:
            raise ValueError("Date should not be offset aware")
        return v


@get_recipe_recommentations_router.post("")
def get_recipe_recommendations(
    body: GetRecipeRecommendationsBody, token: Annotated[str | None, Header(alias="Authorization")]
):
    user = auth(token)
    assert user is not None

    recommended_recipes = recommend_recipes(user, body.date)

    return {
        "recommended_recipes": [
            {
                "name": recipe.name,
                "id": recipe.id,
                "score": score,
            }
            for score, recipe in recommended_recipes
        ],
    }
