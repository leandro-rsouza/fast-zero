import flet as ft
import requests

class UserView:
    def __init__(self, page):
        self.page = page
        self.user_id = self.page.session.get("user_id")
        self.access_token = self.page.session.get("access_token")

    def show_register(self, register):
        def register(e):
            user_data = {
                "username": username.value,
                "email": email.value,
                "password": password.value,
            }
            headers = {
                'Authorization': f'Bearer {self.access_token}'
            }
            requests.post(f"http://127.0.0.1:8000/users/create/{self.user_id}", json=user_data, headers=headers)
            
        user = ft.Text(
            value=self.user_id
        )
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
            user,
            username,
            email,
            password,
            ft.ElevatedButton(
                text='Cadastrar',
                on_click=register
            )
        )
        self.page.update()