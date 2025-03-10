import flet as ft

class Login(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()

        self.content = ft.Column(
            controls = [
                ft.Text("Hello login", color = "white"),
                ft.ElevatedButton(text="signup", on_click=lambda e: page.go("/signup"))
            ]
        )