import flet as ft
import requests

API_URL = "http://127.0.0.1:8000/auth/token"

class LoginView:
    def __init__(self, page):
        self.page = page

    def show_login(self, login):
        def login(e):
            user_data = {
                "username": email.value,
                "password": password.value,
            }
            requests.post(API_URL, data=user_data)

        email = ft.TextField(
            hint_text='Email'
        )
        password = ft.TextField(
            hint_text='Senha'
        )

        self.page.add(
            email,
            password,
            ft.ElevatedButton(
                text='Login',
                on_click=login
            )
        )
        
        self.page.update()