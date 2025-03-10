import flet as ft
from pages.authentication.login import Login
from pages.authentication.signup import SignUp
from utils.colors import customBgColor,customBorderColor,customDashboardBG,customPrimaryColor,customSideBarIconColor,customTextColor


def views_handler(page):
    return{
        "/login": ft.View(route = "/login" , bgcolor = customBgColor , padding = ft.padding.all(0) , controls = [Login(page)]),
        "/signup": ft.View(route = "/signup" , bgcolor=customBgColor , padding = ft.padding.all(0) ,controls = [SignUp(page)]),
    } 