import flet as ft
from pages.authentication.login import Login
from pages.dashboard.components.mapa import Mapa
from pages.dashboard.dashboard_interface import Dashboard
import pages.dashboard.components.utils.data_request as datos
import datetime
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
            dt_object = datetime.datetime.fromtimestamp(datos.t0 + 3600)
            hora = dt_object.strftime("%H:%M:%S")
            hora_actualizacion = "Próxima actualización a las "+hora
            page.open(ft.SnackBar(ft.Text(hora_actualizacion,color="white"),bgcolor="#cb2b2b"))
        if page.route == "/mapa":
            page.add(Mapa(page))
        if page.route == "/":
             page.add(Login(page))

    page.on_route_change = route_change
  
    page.go("/")

    # t_update = threading.Thread(target=actualizar_data)
    # t_update.start()


    


ft.app(main)