import flet as ft
from utils.colors import customBgColor,customBorderColor,customDashboardBG,customPrimaryColor,customSideBarIconColor,customTextColor,customtextHeaderColor


class Dashboard(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.expand = True

        self.content = ft.Row(
            controls = [
                ft.Container(
                    expand = 4,
                    padding = ft.padding.all(40),
                    content=ft.Column(
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment =ft.CrossAxisAlignment.CENTER,
                        controls =[
                            ft.Text("Bienvenido al dashboard", color=customtextHeaderColor, size = 30, weight=ft.FontWeight.BOLD)
                        ]
                    )
                )
            ]
        )