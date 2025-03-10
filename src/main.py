import flet as ft

def main(page:ft.Page):
    def route_change(route):
        pass

    page.on_route_change = route_change


ft.app(target=main, assets_dir = "assets")