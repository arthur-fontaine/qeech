from fastapi import APIRouter
from pydantic import BaseModel

from qeech_data.adapters.api.utils.auth import encode_token
from qeech_data.core.repositories.user import UserRepository

login_router = APIRouter(prefix="/login")


class LoginBody(BaseModel):
    username: str
    password: str


@login_router.post("")
def login(body: LoginBody):
    user = UserRepository.login(body.username, body.password)

    token = encode_token(user_id=user.id)

    return {
        "token": token,
    }
