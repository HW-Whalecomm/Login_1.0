import flet as ft
from components.fields import CustomTextField
from utils.colors import customBgColor,customBorderColor,customDashboardBG,customPrimaryColor,customSideBarIconColor,customTextColor,customtextHeaderColor
from utils.validation import Validation
import time
from  pages.authentication.access import hash_verify


class Login(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()

        self.expand = True
        self.validation = Validation()
        self.error_border = ft.border.all(color="red",width=1)
        self.error_field = ft.Text(value="", color="red",size=0, weight=ft.FontWeight.BOLD)

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
                            self.error_field,
                            self.usuario,
                            self.password,
                            ft.Container(
                                alignment=ft.alignment.center,
                                height=40,
                                bgcolor=customPrimaryColor,
                                content=ft.Text("Ingresar", size = 20, weight=ft.FontWeight.BOLD),
                                on_click= self.login,
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

    
    def login (self, e):
        print("Ingresando al sistema")
        usuario_ingreso = self.usuario.content.value
        password_ingreso = self.password.content.value

        if usuario_ingreso and password_ingreso:
            acceso = hash_verify(password_ingreso,usuario_ingreso)
            if acceso:
                print("Bienvenido")
                self.page.go("/")
            else:
                print("Usuario o contraseña equivocados")
        else:
            self.error_field.value = "No pueden existir campos vacíos"
            self.error_field.size = 12
            self.error_field.update()
            time.sleep(3)
            self.error_field.size = 0
            self.error_field.update()