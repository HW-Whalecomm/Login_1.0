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
        status = datos.medidores_data[medidor]["status"]
        historico = datos.medidor_historico[medidor]

        if status == "disconnected":
            fondo=ft.Colors.RED_300
        elif status == "telemetry":
            fondo=ft.Colors.AMBER_300
        else:
            fondo=ft.Colors.WHITE
        
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
                            ft.Row(controls=[ft.Text("Batería ",size=18, weight=ft.FontWeight.BOLD ,color=ft.Colors.BLACK),ft.Text(bateria,size=14 ,color=ft.Colors.BLACK),ft.Text(" V",size=14 ,color=ft.Colors.BLACK)]),                           
                            ft.Row(controls=[ft.Text("Status ",size=18, weight=ft.FontWeight.BOLD ,color=ft.Colors.BLACK,bgcolor=fondo),ft.Text(status,size=14 ,color=ft.Colors.BLACK,bgcolor=fondo)])
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        )

        llave = list(historico.keys())
        filas=[]
        for registro in llave:
            #print(registro)
            per_con = ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(historico[registro]["periodo"]),size=12 ,color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text(str(historico[registro]["consumo"]),size=12 ,color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text(str(historico[registro]["inicio"]),size=12 ,color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text(str(historico[registro]["corte"]),size=12 ,color=ft.Colors.BLACK))
            ])
            filas.append(per_con)

        self.historicos = ft.DataTable(
                                        horizontal_lines=ft.border.BorderSide(1, ft.Colors.RED_200),
                                        columns=[
                                            ft.DataColumn(ft.Text("Período",size=14 ,color=ft.Colors.BLACK)),
                                            ft.DataColumn(ft.Text("Consumo m³",size=14 ,color=ft.Colors.BLACK)),
                                            ft.DataColumn(ft.Text("L. Inicial m³",size=14 ,color=ft.Colors.BLACK)),
                                            ft.DataColumn(ft.Text("L. Final m³",size=14 ,color=ft.Colors.BLACK)),
                                        ],
                                        rows=filas
                                    )

        


        self.content = ft.Row(
            alignment="start",
            controls=[
                ft.Column(controls=[self.data_meter],scroll="hidden"),
                ft.VerticalDivider(width=1, color=ft.Colors.RED_100),
                ft.Column(controls=[self.historicos],scroll="hidden")
            ]
        )