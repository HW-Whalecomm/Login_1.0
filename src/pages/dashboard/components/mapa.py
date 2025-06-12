import flet as ft
import flet_map as map
import pages.dashboard.components.utils.data_request as datos




class Mapa(ft.Container):

    def __init__(self, page:ft.Page):
        super().__init__()
        
        self.pines = datos.medidores_data

        self.marcadores = []

        
        def  click_boton(e,self):
            datos_pin = self
            print(datos_pin)
        

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

            self.leyenda = ft.Tooltip(message=texto)
            self.boton_marcador = ft.IconButton(icon=ft.Icons.LOCATION_ON, icon_color = color, tooltip = self.leyenda)
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