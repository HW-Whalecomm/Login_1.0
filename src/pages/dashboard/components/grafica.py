import flet as ft
import pages.dashboard.components.utils.data_request as datos


class Grafica(ft.Container):
    def __init__(self,page:ft.Page,medidor):
        super().__init__()

        self.expand = True
        medidor = medidor
        historico = datos.medidor_historico[medidor]

        puntos = []
        etiquetas_x=[]
        etiquetas_y=[]
        consumos=[]

        llaves = list(historico.keys())
        consumo_fecha = {}
        for llave in llaves:
            consumo_fecha[historico[llave]["periodo"]] = historico[llave]["consumo"]
        fechas=list(consumo_fecha.keys())
        aux_punto=1
        for consumo in fechas:
            volumen = float(consumo_fecha[consumo])
            punto= ft.LineChartDataPoint(aux_punto,volumen)
            etiquetax=ft.ChartAxisLabel(
                        value = aux_punto,
                        label = ft.Text(consumo, size = 12, weight = ft.FontWeight.BOLD, color = "black")
                    )         
            puntos.append(punto)
            etiquetas_x.append(etiquetax)
            
            consumos.append(float(consumo_fecha[consumo]))
            aux_punto=aux_punto+1

        consumos.sort(reverse=True)
        intervalo = 0
        etiquetas_y=[]
        maximo_y = 0
        if consumos[0] < 5.0:
            intervalo = 0.5
            maximo_y = 5.5
            etiquetas_y=[
                ft.ChartAxisLabel(value = 0.5,
                        label = ft.Text("0.5 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 1.0,
                        label = ft.Text("1.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 1.5,
                        label = ft.Text("1.5 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 2.0,
                        label = ft.Text("2.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 2.5,
                        label = ft.Text("2.5 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 3.0,
                        label = ft.Text("3.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 3.5,
                        label = ft.Text("3.5 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 4.0,
                        label = ft.Text("4.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 4.5,
                        label = ft.Text("4.5 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 5.0,
                        label = ft.Text("5.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black"))             
            ]
        elif consumos[0] < 10.0:
            intervalo = 1
            maximo_y = 11
            etiquetas_y=[
                ft.ChartAxisLabel(value = 1.0,
                        label = ft.Text("1.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 2.0,
                        label = ft.Text("2.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 3.0,
                        label = ft.Text("3.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 4.0,
                        label = ft.Text("4.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 5.0,
                        label = ft.Text("5.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 6.0,
                        label = ft.Text("6.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 7.0,
                        label = ft.Text("7.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 8.0,
                        label = ft.Text("8.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 9.0,
                        label = ft.Text("9.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 10.0,
                        label = ft.Text("10.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black"))             
            ]
        elif consumos[0] < 100.0:
            intervalo = 10
            maximo_y = 110
            etiquetas_y=[
                ft.ChartAxisLabel(value = 10.0,
                        label = ft.Text("10.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 20.0,
                        label = ft.Text("20.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 30.0,
                        label = ft.Text("30.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 40.0,
                        label = ft.Text("40.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 50.0,
                        label = ft.Text("50.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 60.0,
                        label = ft.Text("60.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 70.0,
                        label = ft.Text("70.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 80.0,
                        label = ft.Text("80.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 90.0,
                        label = ft.Text("90.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 100.0,
                        label = ft.Text("100.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black"))             
            ]
        else:
            intervalo = 50
            maximo_y = 550
            etiquetas_y=[
                ft.ChartAxisLabel(value = 50.0,
                        label = ft.Text("50.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 100.0,
                        label = ft.Text("100.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 150.0,
                        label = ft.Text("150.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 200.0,
                        label = ft.Text("200.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 250.0,
                        label = ft.Text("250.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 300.0,
                        label = ft.Text("300.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 350.0,
                        label = ft.Text("350.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 400.0,
                        label = ft.Text("400.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 450.0,
                        label = ft.Text("450.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black")),
                ft.ChartAxisLabel(value = 500.0,
                        label = ft.Text("500.0 m³", size = 10, weight = ft.FontWeight.BOLD, color="black"))             
            ]

        


        self.data_consumption = [
            ft.LineChartData(
                data_points=puntos,
                stroke_width = 5,
                color = "red",
                below_line_bgcolor = ft.Colors.with_opacity(0.3, ft.Colors.RED_200),
                curved = False,
                stroke_cap_round = False,
            )
        ]

        self.chart = ft.LineChart(
            data_series = self.data_consumption,
            border = ft.Border(
                bottom= ft.BorderSide(4, ft.Colors.with_opacity(0.9, ft.Colors.ON_SURFACE))
            ),
            horizontal_grid_lines = ft.ChartGridLines(
                interval = intervalo,
                color = ft.Colors.with_opacity(0.2, ft.Colors.BLUE_GREY_900),
                width = 1
            ),
            vertical_grid_lines = ft.ChartGridLines(
                interval = 1, 
                color = ft.Colors.with_opacity(0.2, ft.Colors.BLUE_GREY_900),
                width = 1
            ),
            left_axis = ft.ChartAxis(
                labels=etiquetas_y,
                labels_size=45,
                
            ),
            bottom_axis = ft.ChartAxis(
                labels = etiquetas_x,
                labels_size = 20,
            ),
            tooltip_bgcolor=ft.Colors.with_opacity(0.7, ft.Colors.WHITE12),
            min_x=0,
            min_y=0,
            max_x=len(fechas)+1,
            max_y=maximo_y,
            expand=True,
            animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
        )



        self.chart.data_series = self.data_consumption
        self.chart.interactive = True
        self.content = self.chart 