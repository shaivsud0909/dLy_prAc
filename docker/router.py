from fastapi import APIRouter
from schema import UserCreate
from service import get_users_service,create_users_service

router = APIRouter()


@router.get("/")
def get_users():
    return get_users_service()

@router.post("/insert")
def create_users(user: UserCreate):
    return create_users_service(user)


