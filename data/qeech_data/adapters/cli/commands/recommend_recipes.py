import sys
from datetime import datetime

from qeech_data.application.usecases.recommend_recipes import recommend_recipes as _recommend_recipes
from qeech_data.core.repositories.user import UserRepository

def recommend_recipes():
    username = sys.argv[sys.argv.index("--username") + 1]
    password = sys.argv[sys.argv.index("--password") + 1]

    user = UserRepository.login(username, password)

    date = datetime.now()
    if "--date" in sys.argv:
        date = datetime.fromisoformat(sys.argv[sys.argv.index("--date") + 1])

    print(_recommend_recipes(user, date))
