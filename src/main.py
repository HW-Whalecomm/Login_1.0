import flet as ft
from pages.authentication.login import Login
from pages.dashboard.components.mapa import Mapa
from pages.dashboard.dashboard_interface import Dashboard
import pages.dashboard.components.utils.data_request as datos
# from pages.dashboard.monitor import Tabla
# from pages.mapa import Mapa
from router import views_handler
from pages.authentication.utils.colors import customBgColor,customBorderColor,customDashboardBG,customPrimaryColor,customSideBarIconColor,customTextColor,customtextHeaderColor




def main(page:ft.Page):
    datos.request_data()
    def route_change(route):
        # page.views.clear()
        # page.views.append(views_handler(page)[page.route])
        # page.update()
        page.clean()
        page.bgcolor = customBgColor
        page.padding = ft.padding.all(0)
        if page.route == "/login":
            page.add(Login(page))
        if page.route == "/dashboard":
            page.add(Dashboard(page))
        if page.route == "/mapa":
            page.add(Mapa(page))
        if page.route == "/":
             page.add(Login(page))

    page.on_route_change = route_change
  
    page.go("/dashboard")
    


ft.app(main)