import flet as ft
from pages.authentication.login import Login
from pages.authentication.signup import SignUp
#from pages.dashboard.monitor import main
from pages.mapa import Mapa
from utils.colors import customBgColor,customBorderColor,customDashboardBG,customPrimaryColor,customSideBarIconColor,customTextColor


def views_handler(page):
    return{
        "/login": ft.View(route = "/login" , bgcolor = customBgColor , padding = ft.padding.all(0) , controls = [Login(page)]),
        "/signup": ft.View(route = "/signup" , bgcolor=customBgColor , padding = ft.padding.all(0) ,controls = [SignUp(page)]),
 #       "/monitor": ft.View(route = "/monitor" , bgcolor = customBgColor , padding = ft.padding.all(0) , controls = [main(page)]),
        "/mapa": ft.View(route = "/mapa" , bgcolor=customBgColor , padding = ft.padding.all(0) ,controls = [Mapa(page)]),
    } 