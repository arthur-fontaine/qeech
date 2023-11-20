from qeech_data.core.database.database import database
from qeech_data.core.entities.user import User
from qeech_data.core.logger.logger import Logger


class UserRepository:
    @staticmethod
    def login(username: str, password: str) -> User:
        Logger.log_info(f"Logging in with username {username} and password {password}")

        for user in database.users:
            if user.username == username and user.password == password:
                Logger.log_info(f"Logged in as {user.username}")
                return user
            
        raise Exception("User not found")
    
    @staticmethod
    def get_by_id(user_id: int) -> User:
        Logger.log_info(f"Getting user with id {user_id}")

        for user in database.users:
            if user.id == user_id:
                Logger.log_info(f"Found user with id {user_id}")
                return user
            
        raise Exception("User not found")
