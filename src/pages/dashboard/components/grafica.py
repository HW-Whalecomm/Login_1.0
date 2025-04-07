import flet as ft


class Grafica(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()

        self.expand = True


        self.data_consumption = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1,1),
                    ft.LineChartDataPoint(2,2.5),
                    ft.LineChartDataPoint(3,6.8),
                    ft.LineChartDataPoint(4,3.5),
                    ft.LineChartDataPoint(5,0.3),
                    ft.LineChartDataPoint(6,9.4),
                    ft.LineChartDataPoint(7,11.1),
                    ft.LineChartDataPoint(8,1.4),
                    ft.LineChartDataPoint(9,14.8),
                    ft.LineChartDataPoint(10,3.7),
                    ft.LineChartDataPoint(11,2.1),
                    ft.LineChartDataPoint(12,1.2)
                ],
                stroke_width = 5,
                color = "red",
                below_line_bgcolor = ft.Colors.with_opacity(0.3, ft.Colors.RED_200),
                curved = True,
                stroke_cap_round = True,
            )
        ]

        self.chart = ft.LineChart(
            data_series = self.data_consumption,
            border = ft.Border(
                bottom= ft.BorderSide(4, ft.Colors.with_opacity(0.9, ft.Colors.ON_SURFACE))
            ),
            horizontal_grid_lines = ft.ChartGridLines(
                interval = 1,
                color = ft.Colors.with_opacity(0.2, ft.Colors.BLUE_GREY_900),
                width = 1
            ),
            vertical_grid_lines = ft.ChartGridLines(
                interval = 1, 
                color = ft.Colors.with_opacity(0.2, ft.Colors.BLUE_GREY_900),
                width = 1
            ),
            left_axis = ft.ChartAxis(
                labels = [
                    ft.ChartAxisLabel(
                        value = 1,
                        label = ft.Text("1m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 2,
                        label = ft.Text("2m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 3,
                        label = ft.Text("3m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 4,
                        label = ft.Text("4m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 5,
                        label = ft.Text("5m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 6,
                        label = ft.Text("6m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 7,
                        label = ft.Text("7m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 8,
                        label = ft.Text("8m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 9,
                        label = ft.Text("9m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 10,
                        label = ft.Text("10m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 11,
                        label = ft.Text("11m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 12,
                        label = ft.Text("12m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 13,
                        label = ft.Text("13m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 14,
                        label = ft.Text("14m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value = 15,
                        label = ft.Text("15m³", size = 14, weight = ft.FontWeight.BOLD, color="black"),
                    ),
                ],
                labels_size=40,
                
            ),
            bottom_axis = ft.ChartAxis(
                labels = [
                    ft.ChartAxisLabel(
                        value = 1,
                        label = ft.Text("Ene", size = 16, weight = ft.FontWeight.BOLD, color = "black")
                    ),
                    ft.ChartAxisLabel(
                        value = 2,
                        label = ft.Text("Feb", size = 16, weight = ft.FontWeight.BOLD, color = "black")
                    ),
                    ft.ChartAxisLabel(
                        value = 3,
                        label = ft.Text("Mar", size = 16, weight = ft.FontWeight.BOLD, color = "black")
                    ),
                    ft.ChartAxisLabel(
                        value = 4,
                        label = ft.Text("Abr", size = 16, weight = ft.FontWeight.BOLD, color = "black")
                    ),
                    ft.ChartAxisLabel(
                        value = 5,
                        label = ft.Text("May", size = 16, weight = ft.FontWeight.BOLD, color = "black")
                    ),
                    ft.ChartAxisLabel(
                        value = 6,
                        label = ft.Text("Jun", size = 16, weight = ft.FontWeight.BOLD, color = "black")
                    ),
                    ft.ChartAxisLabel(
                        value = 7,
                        label = ft.Text("Jul", size = 16, weight = ft.FontWeight.BOLD, color = "black")
                    ),
                    ft.ChartAxisLabel(
                        value = 8,
                        label = ft.Text("Ago", size = 16, weight = ft.FontWeight.BOLD, color = "black")
                    ),
                    ft.ChartAxisLabel(
                        value = 9,
                        label = ft.Text("Sep", size = 16, weight = ft.FontWeight.BOLD, color = "black")
                    ),
                    ft.ChartAxisLabel(
                        value = 10,
                        label = ft.Text("Oct", size = 16, weight = ft.FontWeight.BOLD, color = "black")
                    ),
                    ft.ChartAxisLabel(
                        value = 11,
                        label = ft.Text("Nov", size = 16, weight = ft.FontWeight.BOLD, color = "black")
                    ),
                    ft.ChartAxisLabel(
                        value = 12,
                        label = ft.Text("Dic", size = 16, weight = ft.FontWeight.BOLD, color = "black")
                    ),
                ],
                labels_size = 20,
            ),
            tooltip_bgcolor=ft.Colors.with_opacity(0.7, ft.Colors.WHITE12),
            min_x=0,
            min_y=0,
            max_x=13,
            max_y=16,
            expand=True,
            animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
        )



        self.chart.data_series = self.data_consumption
        self.chart.interactive = True
        self.content = self.chart 