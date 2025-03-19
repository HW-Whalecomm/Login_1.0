import flet as ft
from components.cards import CustomDisplayCard
from utils.colors import customBgColor,customBorderColor,customDashboardBG,customPrimaryColor,customSideBarIconColor,customTextColor,customtextHeaderColor
import time
import _thread




class Dashboard(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.expand = True
        self.bgcolor = customDashboardBG


        verde1 = "#40e019"
        verde2 ="#70e019"
        verde3 ="#9ee019"
        amarillo1 ="#eef110"
        amarillo2 ="#f1d910"
        amarillo3 ="#f1be10"
        naranja1 ="#f19c10"
        naranaj2 ="#f17d10"
        naranja3 ="#f13910"

        #self.nodo = ft.Text(value="Hola", color="red",size=12, weight=ft.FontWeight.BOLD)
        self.nodo = CustomDisplayCard(iconbg=verde1,title="Nodo 1",value=0.0,color=verde1,icon=ft.Icons.BATTERY_FULL) 
        self.nodo1 = CustomDisplayCard(verde2,"Nodo 2",0.0,verde2,ft.Icons.BATTERY_6_BAR_SHARP)
        self.nodo2 = CustomDisplayCard(verde3,"Nodo 3",0.0,verde3,ft.Icons.BATTERY_5_BAR)
        self.nodo3 = CustomDisplayCard(amarillo1,"Nodo 4",0.0,amarillo1,ft.Icons.BATTERY_4_BAR)
        self.nodo4 = CustomDisplayCard(amarillo2,"Nodo 5",0.0,amarillo2,ft.Icons.BATTERY_3_BAR)
        self.nodo5 = CustomDisplayCard(amarillo3,"Nodo 6",0.0,amarillo3,ft.Icons.BATTERY_2_BAR)
        self.nodo6 = CustomDisplayCard(naranja1,"Nodo 2",0.0,naranja1,ft.Icons.BATTERY_1_BAR)
        self.nodo7 = CustomDisplayCard(naranaj2,"Nodo 3",0.0,naranaj2,ft.Icons.BATTERY_0_BAR)
        self.nodo8 = CustomDisplayCard(naranja3,"Nodo 4",0.0,naranja3,ft.Icons.BATTERY_ALERT_ROUNDED)
 

        

        self.contenedor_master = ft.Column(
            controls=[
                ft.Container(
                    padding=ft.padding.all(30),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[self.nodo,
                                  self.nodo1,
                                  self.nodo2,
                                  self.nodo3]
                                )
                ),
                ft.Container(
                    padding=ft.padding.all(30),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[self.nodo4,
                                  self.nodo5,
                                  self.nodo6,
                                  self.nodo7]
                                )
                ),
                ft.Container(
                    padding=ft.padding.all(30),
                    on_click= self.actualizar,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[self.nodo8,
                                  #self.nodo9,
                                  #self.nodo10,
                                  #self.nodo11,
                                  ]
                        
                                )
                ),
            ]
            
        )

        self.main_content = ft.Column(
            controls= [
                ft.Container(
                    #alignment = ft.alignment.center,
                    bgcolor="white",
                    padding = ft.padding.all(20),
                    content= ft.Text("Dashboard",
                                     color=customtextHeaderColor,
                                     size=20,
                                     weight=ft.FontWeight.BOLD,)
                ),
                ft.Divider(color="black", height=0.5,thickness=0),
                self.contenedor_master, 
            ]
        )
        self.content = ft.Row(
            spacing=0,
            controls=[
                ft.Container(
                    expand=True,
                    content=self.main_content
                )
            ]
        )

        page.update()

    def actualizar(self,e):
        i=0
    #     while(1):
    #         print("Actualizando")
    #         #time.sleep(2)
    #         i = i+1
    #         self.nodo.title = str(i)
    #         self.nodo.update()
    #         time.sleep(2)

    # _thread.start_new_thread(actualizar,(None,None))

    