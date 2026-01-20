from fastapi import APIRouter
from schema import user
from service import home, creating_user, login, dashboard, logout

router = APIRouter()

router.get("/")(home)
router.post("/create_user")(creating_user)
router.post("/login")(login)
router.get("/dashboard")(dashboard)
router.get("/logout")(logout)
