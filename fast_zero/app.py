import flet as ft
import flet.fastapi as flet_fastapi
from fast_zero.routers import users, auth
from fast_zero.routers.users import UserController
from fast_zero.routers.auth import AuthController

app = flet_fastapi.FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

def main(page: ft.Page):
    
    def route_change(e):
        page.clean()
        if page.route == '/login':
            AuthController(page).login()
        elif page.route == '/users/':
            UserController(page).start()
        else:
            AuthController(page).login()

    page.on_route_change = route_change
    page.go('/login')

app.mount(path='/', app=flet_fastapi.app(main))