import flet as ft
from utils.colors import customBgColor,customBorderColor,customDashboardBG,customPrimaryColor,customSideBarIconColor,customTextColor,customtextHeaderColor



class Dispositivos(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True
        self.bgcolor = customDashboardBG

        self.dispositivo1 = ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Dispositivo 1", color="black")),
                                    ft.DataCell(ft.Text("00001", color="black")),
                                    ft.DataCell(ft.Text("12.5647", color="black")),
                                    ft.DataCell(ft.Text("ok", color="black")),
                                    ft.DataCell(ft.Text("Details", color="black")),
                                ],
                            )

        self.main_content = ft.Column(
            spacing=20,
            controls=[
                ft.Container(
                    bgcolor="white",
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        controls=[ft.Row(
                            controls=[
                                ft.Text("Medidores de Agua",size=20,weight=ft.FontWeight.BOLD,color=customTextColor),
                                ft.IconButton(icon=ft.Icons.SEARCH,icon_color="blue",icon_size=30,tooltip="Buscar medidor")
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Divider(color="black",height=0.5, thickness=0.7),
                        ]
                    )

                ),
                ft.Container(
                        expand=True,
                        content=ft.Column(
                            expand=True,
                            controls = [
                            ft.Row(
                                controls=[
                                    ft.DataTable(
                                        expand=5, 
                                        columns = [
                                            ft.DataColumn(ft.Text("ID Encoder")),
                                            ft.DataColumn(ft.Text("Cuenta")),
                                            ft.DataColumn(ft.Text("Consumo")),
                                            ft.DataColumn(ft.Text("Status")),
                                            ft.DataColumn(ft.Text("Detalles")),
                                        ],
                                        rows=[
                                            self.dispositivo1,
                                        ],

                                    )
                                ]
                            )
                        ]
                        )
                ),
            ],
        )

        self.content = ft.Row(
            spacing=0,
            controls=[
                ft.Container(
                    expand=True,
                    content=self.main_content
                ),
            ]
        )
