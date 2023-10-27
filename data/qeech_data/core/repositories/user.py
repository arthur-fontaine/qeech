from qeech_data.core.database.database import database
from qeech_data.core.entities.user import User


class UserRepository:
    @staticmethod
    def login(username: str, password: str) -> User:
        for user in database.users:
            if user.username == username and user.password == password:
                return user
            
        raise Exception("User not found")
