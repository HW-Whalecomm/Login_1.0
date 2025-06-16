import flet as ft
import flet_map as map
import pages.dashboard.components.utils.data_request as datos
from pages.dashboard.components.grafica import Grafica
from pages.dashboard.components.telemetry import Telemetry


class Mapa(ft.Container):

    def __init__(self, page:ft.Page):
        super().__init__()
        
        self.pines = datos.medidores_data

        self.marcadores = []

        
        def Summary_Meter(data,e):
            datos_pin = data
            data_ubicacion=self.pines[datos_pin]["ubicacion"].split(",")
            texto = "Encoder: {encoder}\nCuenta: {cuenta}\nLectura: {lectura}\nFecha: {fecha}\nBatería: {bat}\nStatus: {status}".format(encoder=datos_pin, cuenta=self.pines[datos_pin]["cuenta"],lectura=self.pines[datos_pin]["lectura"],fecha=self.pines[datos_pin]["fecha"],bat = self.pines[datos_pin]["batería"],status=self.pines[datos_pin]["status"])
            leyenda = ft.Tooltip(message=texto,text_style=ft.TextStyle(size=18, color=ft.Colors.WHITE),gradient=ft.LinearGradient(
                                                                                                                begin=ft.alignment.top_left,
                                                                                                                end=ft.alignment.Alignment(0.8, 1),
                                                                                                                colors=["#cb2b2b",
                                                                                                                        "#B48484",
                                                                                                                ],
                                                                                                             tile_mode=ft.GradientTileMode.MIRROR
                                                                                                            ))
            self.content=ft.Container(content=ft.Container(
                content = (
                    ft.Row(
                        controls = [
                            ft.Container(
                                expand = True,
                                content=(map.Map(
                                                expand = True,
                                                initial_center = map.MapLatitudeLongitude(float(data_ubicacion[0]), float(data_ubicacion[1])),
                                                initial_zoom = 18,
                                                interaction_configuration = map.MapInteractionConfiguration(
                                                    flags = map.MapInteractiveFlag.ALL
                                                ),
                                                layers = [
                                                    map.TileLayer(
                                                        url_template = "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                                                        on_image_error = lambda e: print("TileLayer Error"),
                                                    ),
                                                    map.MarkerLayer(
                                                        ref = self.marker_layer_ref,
                                                        markers = [
                                                            map.Marker(
                                                            content=ft.Icon(ft.Icons.LOCATION_ON, color="#58A0DB",tooltip=leyenda),
                                                            coordinates=map.MapLatitudeLongitude(float(data_ubicacion[0]), float(data_ubicacion[1])) )
                                                        ]
                                                    )          
                                                ],
                                            )
                                         )
                            ),
                            ft.VerticalDivider(width=1, color=ft.Colors.RED_100),
                            ft.Container(
                                expand=True,
                                content=(
                                    ft.Column(
                                        controls=[
                                            Grafica(page),
                                            ft.Divider(height=5, color=ft.Colors.RED_100),
                                            Telemetry(page,datos_pin)
                                        ]
                                    )
                                )
                            )
                        ]
                    )
                )
            )
            )
            page.update()



        

        for pin in self.pines:
            #linea de cambio
            data_ubicacion=self.pines[pin]["ubicacion"].split(",")
            if self.pines[pin]["status"]=="telemetry" or (float(self.pines[pin]["batería"])>3.0 and float(self.pines[pin]["batería"])<3.5):
                color = ft.Colors.ORANGE
            elif self.pines[pin]["status"]=="disconnected" or float(self.pines[pin]["batería"])<3.0:
                color = ft.Colors.RED
            else:
                color = ft.Colors.GREEN
            
            texto = "Encoder: {encoder}\nCuenta: {cuenta}\nLectura: {lectura}\nFecha: {fecha}\nBatería: {bat}\nStatus: {status}".format(encoder=pin, cuenta=self.pines[pin]["cuenta"],lectura=self.pines[pin]["lectura"],fecha=self.pines[pin]["fecha"],bat = self.pines[pin]["batería"],status=self.pines[pin]["status"])

            self.leyenda = ft.Tooltip(message=texto,text_style=ft.TextStyle(size=18, color=ft.Colors.WHITE),gradient=ft.LinearGradient(
                                                                                                                begin=ft.alignment.top_left,
                                                                                                                end=ft.alignment.Alignment(0.8, 1),
                                                                                                                colors=["#cb2b2b",
                                                                                                                        "#B48484",
                                                                                                                ],
                                                                                                             tile_mode=ft.GradientTileMode.MIRROR
                                                                                                            )
                                    )
            self.boton_marcador = ft.IconButton(icon=ft.Icons.LOCATION_ON, icon_color = color, tooltip = self.leyenda, data=pin, on_click=lambda pin=pin,event=pin: Summary_Meter(event, pin))
            self.marcadores.append(map.Marker(
                content=ft.Container(self.boton_marcador),
                coordinates=map.MapLatitudeLongitude(float(data_ubicacion[0]), float(data_ubicacion[1]))
            ))
            
            
        

        self.expand = True
        
        self.marker_layer_ref = ft.Ref[map.MarkerLayer]()
        
        self.mapa = map.Map(
            expand = True,
            initial_center = map.MapLatitudeLongitude(20.699615, -103.39853),
            initial_zoom = 16,
            interaction_configuration = map.MapInteractionConfiguration(
                flags = map.MapInteractiveFlag.ALL
            ),
            layers = [
                map.TileLayer(
                    url_template = "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                    on_image_error = lambda e: print("TileLayer Error"),
                ),
                map.MarkerLayer(
                    ref = self.marker_layer_ref,
                    markers = self.marcadores,
                )          
            ],
        )

        self.content = self.mapa