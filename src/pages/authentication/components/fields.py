import flet as ft
from pages.authentication.components.colors import customBgColor,customBorderColor,customDashboardBG,customPrimaryColor,customSideBarIconColor,customTextColor

class CustomTextField(ft.TextField):
    def __init__(
            self,
            label,
            icon = None,
            password = False,
            border = ft.InputBorder.NONE,
            can_reveal_password = False,
            error_text = None,
            input_filter = None,
            **kwargs
            ):
        
        super().__init__(
            label = label,
            border = border,
            error_text = error_text,
            color = customTextColor,
            password = password,
            can_reveal_password=can_reveal_password,
            content_padding=ft.padding.only(top=0,left=20,right=20),
            hint_style=ft.TextStyle(size=14,color=customTextColor),
            input_filter=input_filter,
            focus_color=customTextColor,
            **kwargs
        )