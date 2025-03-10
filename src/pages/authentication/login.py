import flet as ft
from components.fields import CustomTextField
from utils.colors import customBgColor,customBorderColor,customDashboardBG,customPrimaryColor,customSideBarIconColor,customTextColor,customtextHeaderColor

class Login(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()

        self.expand = True

        self.usuario =  ft.Container(
            content=CustomTextField(label="Usuario",border=ft.border.all(width=1,color="black"))
        )

        self.password =  ft.Container(
            content=CustomTextField(label="Contraseña",border=ft.border.all(width=1,color="black"),password=True,can_reveal_password=True)
        )

        self.content = ft.Row(
            controls = [
                ft.Container(
                    expand = 4,
                    padding = ft.padding.all(40),
                    content=ft.Column(
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment =ft.CrossAxisAlignment.CENTER,
                        controls =[
                            ft.Text("Bienvenido", color=customtextHeaderColor, size = 30, weight=ft.FontWeight.BOLD),
                            self.usuario,
                            self.password,
                            ft.Container(
                                alignment=ft.alignment.center,
                                height=40,
                                bgcolor=customPrimaryColor,
                                content=ft.Text("Ingresar", size = 20, weight=ft.FontWeight.BOLD),
                            )
                        ]
                    )
                ),
                ft.Container(
                    expand = 3,
                    content=ft.Column(
                        alignment = ft.MainAxisAlignment.CENTER,
                        controls =[
                            ft.Image(src=f"Login.png", fit="cover")
                        ]
                    )
                )
            ]
        )