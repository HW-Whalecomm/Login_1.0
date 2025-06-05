import flet as ft
import pages.dashboard.components.utils.data_request as datos
#from pages.dashboard.components.utils.mqtt_data import * 

class Controller:
    items: dict = datos.medidores_corte
    counter: int = len(items)

    @staticmethod
    def get_items():
        return Controller.items
    
    @staticmethod
    def add_item(data : dict):
        Controller.items[Controller.counter] = data
        Controller.counter +=1
        


#define stule and attributes for header class

header_style: dict[str, any]={
    "height":60,
    #"bgcolor": "#cb2b2b",
    #"border_radius": ft.border_radius.only(top_left=15, top_right=15),
    #"padding": ft.padding.only(left=15,right=15),
}

#Method that creat and return a textfield

def search_field(function: callable):
    return ft.TextField(
        border_color="#cb2b2b",
        height=40,
        text_size=14,
        content_padding=5,
        cursor_color="black",
        cursor_width=1,
        color="black",
        hint_text="Buscar",
        on_change=function,
    )

#Method that adds a container to the search_field

def search_bar(control: ft.TextField):
    return ft.Container(
        width=350,
        bgcolor="white",
        border_radius=6,
        opacity=0,
        animate_opacity=300,
        padding=8,
        content=ft.Row(
            spacing=10,
            vertical_alignment="center",
            controls=[
                        control,
            ],
        ),
    )




#define header class

class Header(ft.Container):
    def __init__(self, dt: ft.DataTable)-> None:
        super().__init__(**header_style)

        #create a dt attribute
        self.dt= dt

        def corte_periodo(e):
            datos.corte_periodo()
            datos_corte = datos.medidores_corte
            llaves = datos_corte.keys()
            for factura in datos_corte:
                Controller.add_item(datos_corte[factura])
                self.dt.fill_data_table()

        #compile the attributyes inside the header container

        self.boton_corte = ft.ElevatedButton("Corte",
                                             style=ft.ButtonStyle(
                                                 color=ft.Colors.WHITE,
                                                 bgcolor="#cb2b2b",
                                             ),
                                             on_click=corte_periodo,
                                             width=120
                                             )
        self.content = ft.Row(
            alignment="end",
            controls=[self.boton_corte]
        )




#define form class styling and attributes
form_style: dict[str, any] = {
    "border_radius":8,
    #"border": ft.border.all(1,"#ebebeb"),
    #"bgcolor":"white10",
    "padding":5,
}

#Define method that create and return a textfield
def text_field():
    return ft.TextField(
        border_color="transparent",
        height=20,
        text_size=13,
        content_padding=0,
        cursor_color="black",
        cursor_width=1,
        cursor_height=18,
        color="black",
    )

#define a container to wrap the textfield in
def text_field_container(
        expand: bool | int, name: str, control:ft.TextField
):
    return ft.Container(
        expand=expand,
        height=45,
        bgcolor="#ebebeb",
        border_radius=6,
        padding=8,
        content=ft.Column(
            controls=[
                ft.Text(
                    value=name,
                    size=9,
                    color="black",
                    weight="bold"
                ),
                control
            ]
        )
    )

#Define a Form Class
class Form(ft.Container):
    def __init__(self, dt: ft.DataTable):
        super().__init__(**form_style)

        #create a dt attribute
        self.dt = dt

    #define a method to clear entries post-submit
    def clear_entries(self):
        self.content.update()

#define data table style, attributes and columns
column_names =["Encoder", "Cuenta", "L. Inicial", "L. Final", "Consumo", "Periodo", "Hora"]

data_table_style={
    "expand":True,
    "border_radius":8,
    #"border": ft.border.all(2,"#ebebeb"),
    "horizontal_lines":ft.border.BorderSide(1,"#ebebeb"),
    "columns":[
        ft.DataColumn(ft.Text(index,size=12, color="black",weight="bold"))
        for index in column_names
    ]
}



#Class for the data table
class DataTable(ft.DataTable):
    def __init__(self):
        super().__init__(**data_table_style)

        #create an attribute to get items
        self.df = Controller.get_items()
    
    def fill_data_table(self):
        #clear the data table rows for new/update batch
        self.rows = []
        #check dict data type to understand followinf loop
        for values in self.df.values():
            #create a new DataRow
            data = ft.DataRow(cells = [
                ft.DataCell(ft.Text(value,color="black", ))
                for value in values.values()
            ])
            self.rows.append(data)
        self.update()


class Tabla_corte(ft.Container):

    def __init__(self, page:ft.Page):
        super().__init__()

        self.table = DataTable()
        #self.table.fill_data_table()
        self.header = Header(dt=self.table)
        self.expand = True
        self.content= ft.Container(
            expand=True,
            content=(
                ft.Column(
                    expand=True,
                    controls=[
                        self.header,
                        ft.Column(
                            scroll="hidden",
                            expand=True,
                            controls=[ft.Row(controls=[self.table])]
                        )
                    ]
                )
            )
        )
        
        
        # self.update()
    

#     page.update()
    
#     #It's possible fill out the dt after add the control to the page
    
    


# ft.app(target=Tabla)