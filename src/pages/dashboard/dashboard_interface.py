import flet as ft
import time
import datetime
import asyncio
from pages.dashboard.components.tabla import Tabla
from pages.dashboard.components.tabla_corte import Tabla_corte
from pages.dashboard.components.mapa import Mapa
from pages.dashboard.components.register import Register
from pages.authentication.access import token
import pages.dashboard.components.utils.data_request as datos
from styles.colors import *


class Dashboard(ft.Container):

    def __init__(self, page:ft.Page):
        super().__init__()
        
        # self.page.run_thread(self.actualizar_data)
        self.padding_ok = 10
        self.update_height= page.height - (2*self.padding_ok)

        if token[0] == "WH_OK":
            def resize_page(event):
                self.update_height = page.height - (2*self.padding_ok)
                
                self.main_container.height=self.update_height 
                self.sidebar.height=self.update_height
                self.sidebar.update()
                self.main_container.update()
                page.update()
            
            def home_function(e):
                dt_object = datetime.datetime.fromtimestamp(datos.t0 +3600)
                hora = dt_object.strftime("%H:%M:%S")
                hora_actualizacion = "Próxima actualización a las "+hora
                t1 = datetime.datetime.now()
                t1 = int(t1.timestamp())
                if(t1 - datos.t0 >3600):
                    datos.request_data()
                    datos.historicos()
                    datos.historicos()
                self.main_container.content=Mapa(page)
                self.main_container.update()
                page.open(ft.SnackBar(ft.Text(hora_actualizacion,color="white"),bgcolor="#cb2b2b"))
                        
            def table_function(e):
                t1 = datetime.datetime.now()
                t1 = int(t1.timestamp())
                if(t1 - datos.t0 >3600):
                    datos.request_data()
                    datos.historicos()
                    datos.historicos()
                self.main_container.content=Tabla(page)
                self.main_container.update()

            # def map_function(e):
            #     self.main_container.content=Mapa(page)
            #     self.main_container.update()

            def register_function(e):
                t1 = datetime.datetime.now()
                t1 = int(t1.timestamp())
                if(t1 - datos.t0 >3600):
                    datos.request_data()
                    datos.historicos()
                    datos.historicos()
                self.main_container.content=Register(page)
                self.main_container.update()

            def invoice_function(e):
                t1 = datetime.datetime.now()
                t1 = int(t1.timestamp())
                if(t1 - datos.t0 >3600):
                    datos.request_data()
                    datos.historicos()
                    datos.historicos()
                self.main_container.content=Tabla_corte(page)
                self.main_container.update()

            def logout(e):
                global token
                
                token=[]
                datos.medidor_historico={}
                datos.medidor_historico_desor={}
                datos.medidores_consumos={}
                datos.medidores_corte={}
                datos.medidores_data={}
                datos.medidores_historico={}
                datos.mes={}
                datos.mes_num={}

                self.page.go("/")
            
            

            # def dashboard_function(e):
            #     self.main_container.content = ft.Container(
            #         content = (
            #             ft.Row(
            #                 controls = [
            #                     ft.Container(
            #                         expand = True,
            #                         content=(Mapa(page))
            #                     ),
            #                     ft.VerticalDivider(width=1, color=ft.Colors.RED_100),
            #                     ft.Container(
            #                         expand=True,
            #                         content=(
            #                             ft.Column(
            #                                 controls=[
            #                                     Grafica(page),
            #                                     ft.Divider(height=5, color=ft.Colors.RED_100),
            #                                     Telemetry(page)
            #                                 ]
            #                             )
            #                         )
            #                     )
            #                 ]
            #             )
            #         )
            #     )
                self.main_container.update()

            page.on_resized = resize_page
            
            self.expand = True

            self.sidebar=ft.Container(    
                bgcolor="#cb2b2b",
                col=1,
                height=self.update_height,
                border_radius=ft.border_radius.only(top_left=0,top_right=15,bottom_right=15,bottom_left=0),
                padding=ft.padding.only(left=15,right=15),   
                content=(
                    ft.Column(
                        expand=True,
                        
                        alignment="spaceBetween",
                        controls=[
                            ft.Row(expand=True,controls=[ft.Column(
                                controls=[
                                ft.IconButton(icon=ft.Icons.HOME,icon_color="white", on_click=home_function),
                                ft.IconButton(icon=ft.Icons.TABLE_VIEW,icon_color="white", on_click=table_function),
                                ft.IconButton(icon=ft.Icons.APP_REGISTRATION,icon_color="white", on_click=register_function),
                                ft.IconButton(icon=ft.Icons.REPORT,icon_color="white", on_click=invoice_function)
                                # ft.IconButton(icon=ft.Icons.ADDCHART,icon_color="white", on_click=dashboard_function)
                                ]
                            )                
                            ]),
                            ft.Row(alignment="end",expand=True,controls=[
                                ft.Column(alignment="end",expand=True,
                                    controls=[
                                        ft.IconButton(icon=ft.Icons.EXIT_TO_APP,icon_color="white", on_click=logout)
                                    ]
                                )
                            ])
                                
                        ],
                        
                    )
                )
            )
            self.main_container=ft.Container(
                height= self.update_height,
                expand=True,
                border_radius=ft.border_radius.all(15),
                border=ft.border.all(2,"#ebebeb"),
                padding=ft.padding.all(5),
                content=(
                    Mapa(page)
                )
            )

            self.content = ft.Container(
                padding = ft.padding.all(self.padding_ok),
                content= ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                self.sidebar,
                                self.main_container
                            ]
                        )
                    ]
                )
            )
        
            # async def actualizar_data():
            #     t0 = datetime.datetime.now()
            #     t0 = int(t0.timestamp())
            #     t_now = t0
            #     while(1):
            #         if t_now-t0 > 36:
            #             datos.request_data()
            #             datos.historicos()
            #             datos.historicos()
            #             t0 = t_now
            #             home_func()
            #         time.sleep(1)
            #         t_now = datetime.datetime.now()
            #         t_now = int(t_now.timestamp())
                
            # t_update = mp.Process(target=actualizar_data)
            # t_update.start()
            
        
        else:
            self.main_container=ft.Container(
                height= self.update_height,
                expand=True,
                border_radius=ft.border_radius.all(15),
                border=ft.border.all(2,"#ebebeb"),
                padding=ft.padding.all(5),
                content=(
                    ft.Text("Sitio sin aceso")
                )
            )

            self.content = ft.Container(
                padding = ft.padding.all(self.padding_ok),
                content= ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                self.main_container
                            ]
                        )
                    ]
                )
            )
        