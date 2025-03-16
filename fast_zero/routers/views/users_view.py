import flet as ft

class UserView:
    def __init__(self, page):
        self.page = page

    def show_register(self, register):
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