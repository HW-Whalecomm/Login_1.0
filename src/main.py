import flet as ft
import threading
import datetime
import time
from pages.authentication.login import Login
from pages.dashboard.components.mapa import Mapa
from pages.dashboard.dashboard_interface import Dashboard
import pages.dashboard.components.utils.data_request as datos
# from pages.dashboard.monitor import Tabla
# from pages.mapa import Mapa
from router import views_handler
from pages.authentication.utils.colors import customBgColor,customBorderColor,customDashboardBG,customPrimaryColor,customSideBarIconColor,customTextColor,customtextHeaderColor




def main(page:ft.Page):
    # datos.request_data()
    # datos.historicos()
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
    
    # def actualizar_data():
    #     t0 = datetime.datetime.now()
    #     t0 = int(t0.timestamp())
    #     t_now = t0
    #     while(1):
    #         if t_now-t0 > 3600:
    #             datos.request_data()
    #             datos.historicos()
    #             datos.historicos()
    #             t0 = t_now
    #             page.go("/dashboard")
    #         time.sleep(1)
    #         t_now = datetime.datetime.now()
    #         t_now = int(t_now.timestamp())


             

    page.on_route_change = route_change
  
    page.go("/")

    # t_update = threading.Thread(target=actualizar_data)
    # t_update.start()


    


ft.app(main)