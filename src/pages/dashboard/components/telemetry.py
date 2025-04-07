import flet as ft 

class Telemetry(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()

        self.expand = True

        self.timestamp = ft.Container(
            expand=True,
            padding= ft.padding.all(10),
            content=(
                ft.Row(
                    alignment="start",
                    controls=[
                        ft.Container(
                            col = 1,
                            expand = True,
                            content = (
                                ft.Icon(name=ft.Icons.CALENDAR_MONTH_OUTLINED, color="red",size=32)
                                )
                        ),
                        ft.Container(
                            expand = True,
                            content = (
                                ft.Column(
                                    controls = [
                                        ft.Text("Hora y fecha de la última lectura recibida", color="black"),
                                        ft.Text("4 de Abril de 2025 12:35:56", color=ft.Colors.BLACK26)
                                        ]
                                    )
                            )
                        ),
                    ]
                )
            )
        )


        self.bateria = ft.Container(
            # height=100,
            # width=160,
            expand=True,
            padding= ft.padding.all(20),
            content=(
                ft.Row(
                    alignment="start",
                    controls=[
                        ft.Container(
                            expand = True,
                            content=(
                                ft.Icon(name=ft.Icons.BATTERY_5_BAR, color="green",size=32)
                            )
                        ),
                        ft.Container(
                            expand = True,
                            content = (
                                ft.Column(
                                    controls = [
                                        ft.Text("Voltaje en batería:", color="black"),
                                        ft.Text("3.8", color=ft.Colors.BLACK38)
                                    ]
                                )
                            )
                        )
                        
                    ]
                )
            )
        )


        self.lectura = ft.Container(
            # height=250,
            # width=190,
            expand=True,
            padding= ft.padding.all(20),
            content=(
                ft.Row(
                    alignment="start",
                    controls=[
                        ft.Container(
                            expand=True,
                            content=(
                                ft.Icon(name=ft.Icons.WATER_DROP, color="blue", size=56)
                            )
                        ),
                        ft.Container(
                            expand = True,
                            content = (
                                ft.Column(
                                    controls=[
                                        ft.Text("Número de cuenta: 23017"),
                                        ft.Text("Titular: Fulanito Goméz"),
                                        ft.Text("Domicilio: P. Noria 1234"),
                                        ft.Text("Medidor: 230671816"),
                                        ft.Text("Lectura del medidor"),
                                        ft.Text("86.4637 m³")
                                    ]
                                )
                            )
                        )
                        
                    ]
                )
            )
        )
        

        self.content = ft.Row(
            alignment="start",
            controls=[
                ft.Container(
                    expand = True,
                    content=(
                        ft.Column(
                        alignment="start",
                        controls=[
                            self.timestamp,
                            ft.Divider(height=5, color=ft.Colors.RED_100),
                            self.bateria
                            ]
                        )
                    )
                ),
                ft.VerticalDivider(width=1, color=ft.Colors.RED_100),
                self.lectura
            ]
        )