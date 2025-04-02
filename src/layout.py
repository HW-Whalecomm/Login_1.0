import flet as ft
import datetime
#from pages.dashboard.monitor import Tabla
from pages.mapa import Mapa

def main (page:ft.Page):

    update_height= page.height-20

    def resize_page(event):
        global update_height
        update_height = page.height-20
        
        main_container.height=update_height
        sidebar.height=update_height
        sidebar.update()
        main_container.update()
        page.update()

    
    page.on_resized = resize_page

    page.bgcolor= "#fdfdfd"

    header = ft.Container(       
        expand=True,
        bgcolor="#cb2b2b",
        height=60,
        border_radius=ft.border_radius.only(bottom_left=15,bottom_right=15),
        padding=ft.padding.only(left=15,right=15),
        content=(
            ft.Row(alignment="spaceBetween",
                controls=[
                ft.Text("Sistema de monitoreo de medidores de agua Colinas de San Javier", color = "white", weight="bold",size=36),
                ft.Text(str(datetime.datetime.now()))
            ]
            )
        )
    )

    sidebar = ft.Container(    
        bgcolor="#cb2b2b",
        col=1,
        height=update_height,
        border_radius=ft.border_radius.only(top_left=0,top_right=15,bottom_right=15,bottom_left=0),
        padding=ft.padding.only(left=15,right=15),   
        content=(
            ft.Column(
                expand=True,
                
                alignment="spaceBetween",
                controls=[
                    ft.Row(expand=True,controls=[ft.Column(
                        controls=[
                        ft.IconButton(icon=ft.Icons.HOME,icon_color="white"),
                        ft.IconButton(icon=ft.Icons.TABLE_VIEW,icon_color="white"),
                        ft.IconButton(icon=ft.Icons.MAP,icon_color="white"),
                        ft.IconButton(icon=ft.Icons.APP_REGISTRATION,icon_color="white"),
                        ft.IconButton(icon=ft.Icons.REPORT,icon_color="white")
                        ]
                    )                
                    ]),
                    ft.Row(alignment="end",expand=True,controls=[
                        ft.Column(alignment="end",expand=True,
                            controls=[
                                ft.IconButton(icon=ft.Icons.EXIT_TO_APP,icon_color="white")
                            ]
                        )
                    ])
                        
                ],
                
            )
        )
    )



    main_container = ft.Container(
        height= update_height,
        expand=True,
        border_radius=ft.border_radius.all(15),
        border=ft.border.all(2,"#ebebeb"),
        padding=ft.padding.all(5),
        content=(
            #ft.Text("Hola")
            #Tabla()
            Mapa(page)
        )
    )

    page.add(ft.Column(controls=[
        #ft.Row(controls=[header]),
        ft.Row(controls=[sidebar, main_container])
    ]))


    page.update()


ft.app(target=main)