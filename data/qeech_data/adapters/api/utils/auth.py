from fastapi import HTTPException

from qeech_data.core.repositories.user import UserRepository
from qeech_data.core.entities.user import User


def decode_token(token: str) -> int:
    return int(token)


def encode_token(*, user_id: int) -> str:
    return str(user_id)


def auth(token: str | None, throw_unauthorized: bool = True) -> User | None:
    if token is None:
        if throw_unauthorized:
            raise HTTPException(
                status_code=401,
                detail="Missing token",
            )
        else:
            return None
        
    if not token.startswith("Bearer "):
        if throw_unauthorized:
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
            )
        else:
            return None
        
    token = token[len("Bearer "):]

    try:
        user_id = decode_token(token)
    except Exception:
        if throw_unauthorized:
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
            )
        else:
            return None

    try:
        user = UserRepository.get_by_id(user_id)
    except Exception:
        if throw_unauthorized:
            raise HTTPException(
                status_code=401,
                detail="User not found",
            )
        else:
            return None

    return user
