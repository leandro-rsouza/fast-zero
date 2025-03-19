import flet as ft
import flet.fastapi as flet_fastapi
from fast_zero.routers import users, auth
from fast_zero.routers.users import UserController
from fast_zero.routers.auth import AuthController

app = flet_fastapi.FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

def register(page: ft.Page):
    UserController(page).start()

def login(page: ft.Page):
    AuthController(page).login()

app.mount(path='/users', app=flet_fastapi.app(register))
app.mount(path='/login', app=flet_fastapi.app(login))