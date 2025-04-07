import flet as ft
from typing import Any
from styles.colors import *

class CustomDisplayCard(ft.Container):
    def __init__(self, iconbg=None, title=None, value=None, color=None, icon=None):
        super().__init__()

        self.iconbg = iconbg
        self.title = title
        self.value = value
        self.color = color
        self.icon = icon

        self.shadow = ft.BoxShadow(spread_radius=3, blur_radius=6, color=self.color)

        self.width = 250
        self.height = 80
        self.bgcolor = "white"

        self.card = ft.Row(
            controls=[
                ft.Container(
                    height=100,
                    width=80,
                    bgcolor = self.iconbg,
                    content=ft.Icon(
                        name=self.icon,
                        color="white",
                        size=50,
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(left=5,right=5),
                    content = ft.Column(
                        controls = [
                            ft.Text(
                                self.title,
                                color = customTextColor,
                                size=15,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                self.value,
                                color = customTextColor,
                                size=12,
                                weight=ft.FontWeight.BOLD
                            )
                        ]
                    )
                )
            ]
        )

    
        self.content = self.card