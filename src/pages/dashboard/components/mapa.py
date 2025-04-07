import flet as ft
import flet_map as map



class Mapa(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()

        self.expand = True
        
        self.marker_layer_ref = ft.Ref[map.MarkerLayer]()
        
        self.mapa = map.Map(
            expand = True,
            initial_center = map.MapLatitudeLongitude(20.699628629282913, -103.39913551264735),
            initial_zoom = 15,
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
                            content = ft.Container(
                                ft.IconButton(icon=ft.Icons.LOCATION_ON, icon_color = "red", tooltip = "Desconectado")
                            ),
                            coordinates=map.MapLatitudeLongitude(20.70305024580718, -103.39748599554488),
                        ),
                        map.Marker(
                            content = ft.Container(
                                ft.IconButton(icon=ft.Icons.LOCATION_ON, icon_color = "yellow", tooltip = "Batería baja")
                            ),
                            coordinates=map.MapLatitudeLongitude(20.697161589491337, -103.40061442723625),
                        ),
                        map.Marker(
                            content = ft.Container(
                                ft.IconButton(icon=ft.Icons.LOCATION_ON, icon_color = "yellow", tooltip = "No envió telemetría")
                            ),
                            coordinates=map.MapLatitudeLongitude(20.703924227502664, -103.39754642404671),
                        ),
                        map.Marker(
                            content = ft.Container(
                                ft.IconButton(icon=ft.Icons.LOCATION_ON, icon_color = "green", tooltip = "113.2654")
                            ),
                            coordinates=map.MapLatitudeLongitude(20.695594107739243, -103.40181090213704),
                        ),
                        map.Marker(
                            content = ft.Container(
                                ft.IconButton(icon=ft.Icons.LOCATION_ON, icon_color = "green", tooltip = "34.0956")
                            ),
                            coordinates=map.MapLatitudeLongitude(20.696890958189897, -103.40092491258665),
                        ),
                    ],
                )
            ],
        )

        self.content = self.mapa