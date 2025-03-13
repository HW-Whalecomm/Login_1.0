import flet as ft
from pages.authentication.login import Login
from router import views_handler
from utils.colors import customBgColor,customBorderColor,customDashboardBG,customPrimaryColor,customSideBarIconColor,customTextColor,customtextHeaderColor


def main(page:ft.Page):
    def route_change(route):
        # page.views.clear()
        # page.views.append(views_handler(page)[page.route])
        # page.update()
        page.clean()
        page.bgcolor = customBgColor
        page.padding = ft.padding.all(0)
        if page.route == "/login":
            page.add(Login(page))

    page.on_route_change = route_change
  
    page.go("/login")



ft.app(target=main, assets_dir = "assets")