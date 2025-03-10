import flet as ft

class SignUp(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()

        self.content = ft.Column(
            controls = [
                ft.Text("Hello signup", color = "white"),
                ft.ElevatedButton(text="login", on_click=lambda e: page.go("/login"))
            ]
        )