from fastapi import FastAPI
import uvicorn

from qeech_data.adapters.api.handlers.get_recipe_recommendations import (
    get_recipe_recommentations_router,
)
from qeech_data.adapters.api.handlers.login import login_router

app = FastAPI()


app.include_router(login_router)
app.include_router(get_recipe_recommentations_router)


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
