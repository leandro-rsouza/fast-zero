import flet as ft
import flet.fastapi as flet_fastapi
from fast_zero.routers import users, auth
from fast_zero.routers.users import UserController

app = flet_fastapi.FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

def main(page: ft.Page):
    UserController(page).start()

app.mount(path='/users', app=flet_fastapi.app(main))