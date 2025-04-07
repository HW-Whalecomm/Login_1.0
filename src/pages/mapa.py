import flet as ft
from pages.components.cards import CustomDisplayCard
from styles.colors import *
import flet_map as map

class Mapa(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()

        self.expand=True
        self.bgcolor = customDashboardBG
        self.marker_layer_ref = ft.Ref[map.MarkerLayer]()
        self.circle_layer_ref = ft.Ref[map.CircleLayer]()



        self.data_1 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 1.5),
                    ft.LineChartDataPoint(5, 1.4),
                    ft.LineChartDataPoint(7, 3.4),
                    ft.LineChartDataPoint(10, 2),
                    ft.LineChartDataPoint(12, 2.2),
                    ft.LineChartDataPoint(13, 1.8),
                ],
                stroke_width=8,
                color=ft.Colors.LIGHT_GREEN,
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 2.8),
                    ft.LineChartDataPoint(7, 1.2),
                    ft.LineChartDataPoint(10, 2.8),
                    ft.LineChartDataPoint(12, 2.6),
                    ft.LineChartDataPoint(13, 3.9),
                ],
                color=ft.Colors.PINK,
                below_line_bgcolor=ft.Colors.with_opacity(0, ft.Colors.PINK),
                stroke_width=8,
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 2.8),
                    ft.LineChartDataPoint(3, 1.9),
                    ft.LineChartDataPoint(6, 3),
                    ft.LineChartDataPoint(10, 1.3),
                    ft.LineChartDataPoint(13, 2.5),
                ],
                color=ft.Colors.CYAN,
                stroke_width=8,
                curved=True,
                stroke_cap_round=True,
            ),
        ]

        self.data_2 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 4),
                    ft.LineChartDataPoint(5, 1.8),
                    ft.LineChartDataPoint(7, 5),
                    ft.LineChartDataPoint(10, 2),
                    ft.LineChartDataPoint(12, 2.2),
                    ft.LineChartDataPoint(13, 1.8),
                ],
                stroke_width=4,
                color=ft.Colors.with_opacity(0.5, ft.Colors.LIGHT_GREEN),
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 2.8),
                    ft.LineChartDataPoint(7, 1.2),
                    ft.LineChartDataPoint(10, 2.8),
                    ft.LineChartDataPoint(12, 2.6),
                    ft.LineChartDataPoint(13, 3.9),
                ],
                color=ft.Colors.with_opacity(0.5, ft.Colors.PINK),
                below_line_bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.PINK),
                stroke_width=4,
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 3.8),
                    ft.LineChartDataPoint(3, 1.9),
                    ft.LineChartDataPoint(6, 5),
                    ft.LineChartDataPoint(10, 3.3),
                    ft.LineChartDataPoint(13, 4.5),
                ],
                color=ft.Colors.with_opacity(0.5, ft.Colors.CYAN),
                stroke_width=4,
                stroke_cap_round=True,
            ),
        ]

        self.chart = ft.LineChart(
            data_series=self.data_1,
            border=ft.Border(
                bottom=ft.BorderSide(4, ft.Colors.with_opacity(0.9, ft.Colors.ON_SURFACE))
            ),
            horizontal_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.Colors.with_opacity(0.2, ft.Colors.BLUE_GREY_900), width=1
            ),
            vertical_grid_lines=ft.ChartGridLines(
                interval=1, color=ft.Colors.with_opacity(0.2, ft.Colors.BLUE_GREY_900), width=1
            ),
            left_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=1,
                        label=ft.Text("1m", size=14, weight=ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value=2,
                        label=ft.Text("2m", size=14, weight=ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value=3,
                        label=ft.Text("3m", size=14, weight=ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value=4,
                        label=ft.Text("4m", size=14, weight=ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value=5,
                        label=ft.Text("5m", size=14, weight=ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value=6,
                        label=ft.Text("6m", size=14, weight=ft.FontWeight.BOLD, color="black"),
                    ),
                ],
                labels_size=40,
            ),
            right_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=1,
                        label=ft.Text("2.0", size=14, weight=ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value=2,
                        label=ft.Text("2.5", size=14, weight=ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value=3,
                        label=ft.Text("3.0", size=14, weight=ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value=4,
                        label=ft.Text("3.5", size=14, weight=ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value=5,
                        label=ft.Text("4.0", size=14, weight=ft.FontWeight.BOLD, color="black"),
                    ),
                    ft.ChartAxisLabel(
                        value=6,
                        label=ft.Text("4.5", size=14, weight=ft.FontWeight.BOLD, color="black"),
                    ),
                ],
                labels_size=40,
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=2,
                        label=ft.Container(
                            ft.Text(
                                "SEP",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color="black",
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=7,
                        label=ft.Container(
                            ft.Text(
                                "OCT",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color="black",
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=12,
                        label=ft.Container(
                            ft.Text(
                                "DEC",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color="black",
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                ],
                labels_size=32,
            ),
            tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.BLUE_GREY),
            min_y=0,
            max_y=4,
            min_x=0,
            max_x=14,
            animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
            expand=True,
        )

        self.chart.data_series = self.data_2
        self.chart.data_series[2].point = True
        self.chart.max_y = 6
        self.chart.interactive = True

    # def toggle_data(self, e):
    #     if s.toggle:
    #         self.chart.data_series = self.data_2
    #         self.chart.data_series[2].point = True
    #         self.chart.max_y = 6
    #         self.chart.interactive = False
    #     else:
    #         chart.data_series = data_1
    #         chart.max_y = 4
    #         chart.interactive = True
    #     s.toggle = not s.toggle
    #     chart.update()

        self.graph_content = ft.Container(
            expand=True,
            content=self.chart
        )

        self.data_node = ft.Container(
            expand=True,
            content= ft.Column(
                controls=[
                    self.graph_content,
                    ft.Text("Datos del encoder", color="black"),
                    ft.Text("Encoder: 123123123", color="black"),
                    ft.Text("Lectura: 12.4332", color="black"),
                    ft.Text("Fecha: 23 Marzo 2025 14:45:34", color="black"),
                    ft.Text("Batería: 3.6", color="black"),
                    ft.Text("Consumo instantáneo: 12.45354", color="black"),
                    ft.Text("Históricos", color="black"),
                    
                ]
            )
        )

        self.map_content = map.Map(
            expand=True,
            initial_center=map.MapLatitudeLongitude(20.699628629282913, -103.39913551264735),
            initial_zoom=15,
            interaction_configuration=map.MapInteractionConfiguration(
                flags=map.MapInteractiveFlag.ALL
            ),
            #on_init=lambda e: print(f"Initialized Map"),
            #on_tap=handle_tap,
            #on_secondary_tap=handle_tap,
            #on_long_press=handle_tap,
            #on_event=lambda e: print(e),
            layers=[
                map.TileLayer(
                    url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                    on_image_error=lambda e: print("TileLayer Error"),
                ),
                # map.RichAttribution(
                #     attributions=[
                #         map.TextSourceAttribution(
                #             text="OpenStreetMap Contributors",
                #             on_click=lambda e: e.page.launch_url(
                #                 "https://openstreetmap.org/copyright"
                #             ),
                #         ),
                #         # map.TextSourceAttribution(
                #         #     text="Flet",
                #         #     on_click=lambda e: e.page.launch_url("https://flet.dev"),
                #         # ),
                #     ]
                # ),
                # map.SimpleAttribution(
                #     text="Whalecomm",fl
                #     alignment=ft.alignment.bottom_right,
                #     on_click=lambda e: print("Clicked SimpleAttribution"),
                # ),
                map.MarkerLayer(
                    ref=self.marker_layer_ref,
                    markers=[
                        map.Marker(
                            content=ft.Container(
                                ft.Row(
                                    controls=[ft.Icon(ft.Icons.LOCATION_ON, color="red"),
                                              ft.Text("Encoder: 2300435335", color="black"),
                                              ft.Text("Consumo: 23.53456", color="black")]
                                    )),
                            coordinates=map.MapLatitudeLongitude(20.70305024580718, -103.39748599554488),
                        ),
                        map.Marker(
                            content=ft.Container(
                                ft.Row(
                                    controls=[ft.Icon(ft.Icons.LOCATION_ON, color="red"),
                                              ft.Text("Encoder: 2300435335", color="black"),
                                              ft.Text("Consumo: 23.53456", color="black")]
                                    )),
                            coordinates=map.MapLatitudeLongitude(20.697161589491337, -103.40061442723625),
                        ),
                        map.Marker(
                            content=ft.Container(
                                ft.Row(
                                    controls=[ft.Icon(ft.Icons.LOCATION_ON, color="red"),
                                              ft.Text("Encoder: 2300435335", color="black"),
                                              ft.Text("Consumo: 23.53456", color="black")]
                                    )),
                            coordinates=map.MapLatitudeLongitude(20.703924227502664, -103.39754642404671),
                        ),
                    ],
                ),
                map.CircleLayer(
                    ref=self.circle_layer_ref,
                    circles=[
                        map.CircleMarker(
                            radius=10,
                            coordinates=map.MapLatitudeLongitude(16, 24),
                            color=ft.Colors.RED,
                            border_color=ft.Colors.BLUE,
                            border_stroke_width=4,
                        ),
                    ],
                ),
                
                
            ],
        )
    
        self.content = ft.Row(spacing=0,
                            controls=[self.map_content,self.data_node])
        
        page.update()