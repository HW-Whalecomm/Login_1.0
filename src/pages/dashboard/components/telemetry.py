import flet as ft 
import pages.dashboard.components.utils.data_request as datos

class Telemetry(ft.Container):
    def __init__(self,page:ft.Page, medidor):
        super().__init__()

        self.expand = True

        medidor = medidor
        cuenta = datos.medidores_data[medidor]["cuenta"]
        titular = datos.medidores_data[medidor]["titular"]
        direccion = datos.medidores_data[medidor]["direccion"]
        lectura = datos.medidores_data[medidor]["lectura"]
        fecha = datos.medidores_data[medidor]["fecha"]
        bateria = datos.medidores_data[medidor]["batería"]
        
        self.data_meter = ft.Container(
            expand = True,
            padding = ft.padding.all(15),
            content=(
                ft.Column(controls=[
                            ft.Row(controls=[ft.Text("Medidor ",size=18, weight=ft.FontWeight.BOLD ,color=ft.Colors.BLACK ),ft.Text(medidor,size=14 ,color=ft.Colors.BLACK)]),
                            ft.Row(controls=[ft.Text("Cuenta ",size=18, weight=ft.FontWeight.BOLD ,color=ft.Colors.BLACK),ft.Text(cuenta,size=14 ,color=ft.Colors.BLACK)]),
                            ft.Row(controls=[ft.Text("Titular ",size=18, weight=ft.FontWeight.BOLD ,color=ft.Colors.BLACK),ft.Text(titular,size=14 ,color=ft.Colors.BLACK)]),
                            ft.Row(controls=[ft.Text("Dirección ",size=18, weight=ft.FontWeight.BOLD ,color=ft.Colors.BLACK),ft.Text(direccion,size=14 ,color=ft.Colors.BLACK)]),
                            ft.Row(controls=[ft.Text("Lectura ",size=18, weight=ft.FontWeight.BOLD ,color=ft.Colors.BLACK),ft.Text(lectura,size=14 ,color=ft.Colors.BLACK),ft.Text(" m³",size=14 ,color=ft.Colors.BLACK)]),
                            ft.Row(controls=[ft.Text("Fecha ",size=18, weight=ft.FontWeight.BOLD ,color=ft.Colors.BLACK),ft.Text(fecha,size=14 ,color=ft.Colors.BLACK)]),
                            ft.Row(controls=[ft.Text("Batería ",size=18, weight=ft.FontWeight.BOLD ,color=ft.Colors.BLACK),ft.Text(bateria,size=14 ,color=ft.Colors.BLACK),ft.Text(" V",size=14 ,color=ft.Colors.BLACK)])
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        )

        self.historicos = ft.DataTable(
                    horizontal_lines=ft.border.BorderSide(1, ft.Colors.RED_200),
                    columns=[
                        ft.DataColumn(ft.Text("Período",size=14 ,color=ft.Colors.BLACK)),
                        ft.DataColumn(ft.Text("Consumo m³",size=14 ,color=ft.Colors.BLACK))
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("Agosto 2024",size=12 ,color=ft.Colors.BLACK)),
                                ft.DataCell(ft.Text("12.7654",size=12 ,color=ft.Colors.BLACK))
                            ]
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("Septiembre 2024",size=12 ,color=ft.Colors.BLACK)),
                                ft.DataCell(ft.Text("5.7564",size=12 ,color=ft.Colors.BLACK))
                            ]
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("Octubre 2024",size=12 ,color=ft.Colors.BLACK)),
                                ft.DataCell(ft.Text("3.9837",size=12 ,color=ft.Colors.BLACK))
                            ]
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("Noviembre 2024",size=12 ,color=ft.Colors.BLACK)),
                                ft.DataCell(ft.Text("0.6754",size=12 ,color=ft.Colors.BLACK))
                            ]
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("Diciembre 2024",size=12 ,color=ft.Colors.BLACK)),
                                ft.DataCell(ft.Text("19.0763",size=12 ,color=ft.Colors.BLACK))
                            ]
                        )
                    ]
                )
       

        self.content = ft.Row(
            alignment="start",
            controls=[
                self.data_meter,
                ft.VerticalDivider(width=1, color=ft.Colors.RED_100),
                self.historicos
            ]
        )