import flet as ft
from pages.authentication.login import Login
from pages.authentication.signup import SignUp
from pages.dashboard.dashboard_interface import Dashboard
#from pages.dashboard.monitor import main
from pages.dashboard.components.mapa import Mapa
from styles.colors import *

def views_handler(page):
    return{
        "/login": ft.View(route = "/login" , bgcolor = customBgColor , padding = ft.padding.all(0) , controls = [Login(page)]),
        "/signup": ft.View(route = "/signup" , bgcolor=customBgColor , padding = ft.padding.all(0) ,controls = [SignUp(page)]),
 #       "/monitor": ft.View(route = "/monitor" , bgcolor = customBgColor , padding = ft.padding.all(0) , controls = [main(page)]),
        "/mapa": ft.View(route = "/mapa" , bgcolor=customBgColor , padding = ft.padding.all(0) ,controls = [Mapa(page)]),
        "/dashboard": ft.View(route = "/dashboard" , bgcolor=customBgColor , padding = ft.padding.all(20) ,controls = [Dashboard(page)]),
    } 