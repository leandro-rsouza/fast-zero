import flet as ft
import requests

API_URL = "http://127.0.0.1:8000/users/create"

class UserView:
    def __init__(self, page):
        self.page = page

    def show_register(self, register):
        def register(e):
            user_data = {
                "username": username.value,
                "email": email.value,
                "password": password.value,
            }
            requests.post(API_URL, json=user_data)
            
        username = ft.TextField(
            hint_text='Nome de Usuário'
        )
        email = ft.TextField(
            hint_text='Email'
        )
        password = ft.TextField(
            hint_text='Senha'
        )
        self.page.add(
            username,
            email,
            password,
            ft.ElevatedButton(
                text='Cadastrar',
                on_click=register
            )
        )
        self.page.update()