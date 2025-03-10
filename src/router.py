import flet as ft
from pages.authentication.login import Login
from pages.authentication.signup import SignUp


def views_handler(page):
    return{
        "/login": ft.View(route = "/login", controls = [Login(page)]),
        "/signup": ft.View(route = "/signup", controls = [SignUp(page)]),
    } 