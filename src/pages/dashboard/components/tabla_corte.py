import flet as ft
import pages.dashboard.components.utils.data_request as datos
#from pages.dashboard.components.utils.mqtt_data import * 

class Controller:
    items: dict = datos.medidores_corte

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

        def corte_periodo(e):
            datos.corte_periodo()
            print("Se hace el corte del periodo")
            self.dt.fill_data_table()
        
        #create a dt attribute
        self.dt= dt

        # #create a textfield for search/filter
        # self.search_value = search_field(self.filter_dt_rows)

        # #create a searchbox
        # self.search = search_bar(self.search_value)

        # #define other class atributes
        # self.avatar = ft.IconButton(icon=ft.Icons.SEARCH,icon_color="#cb2b2b")

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

    # #define method that toggles search box visibility
    # def toogle_search(self, e: ft.HoverEvent):
    #     self.search.opacity = 1 if e.data == "true" else 0
    #     self.search.update()

    # #define a placeholder methor for filtering data
    # def filter_dt_rows(self,e):
    #     for data_rows in self.dt.rows:
    #         data_col1 = data_rows.cells[0]
    #         data_col2 = data_rows.cells[1]
    #         data_col3 = data_rows.cells[2]
    #         data_col4 = data_rows.cells[3]
    #         data_col5 = data_rows.cells[4]
    #         data_col6 = data_rows.cells[5]
    #         data_col7 = data_rows.cells[6]

    #         data_rows.visible=(True if (e.control.value.lower() in data_col1.content.value.lower()) or
    #                              (e.control.value.lower() in data_col2.content.value.lower()) or 
    #                              (e.control.value.lower() in data_col3.content.value.lower()) or 
    #                              (e.control.value.lower() in data_col4.content.value.lower()) or
    #                              (e.control.value.lower() in data_col5.content.value.lower()) or 
    #                              (e.control.value.lower() in data_col6.content.value.lower()) or 
    #                              (e.control.value.lower() in data_col7.content.value.lower()) 
    #                              else False)
            
    #         data_rows.update()


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

        #define a button to submit the data
        self.corte_perioodo = ft.ElevatedButton(
            text="Corte",
            style=ft.ButtonStyle(shape={"":ft.RoundedRectangleBorder(radius=8)}),
            on_click=self.corte,
        )


    def corte (self,e:ft.TapEvent):
        datos.corte_periodo()
        self.clear_entries()
        self.dt.fill_data_table()

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
        #self.update()


class Tabla_corte(ft.Container):

    def __init__(self, page:ft.Page):
        super().__init__()

        self.table = DataTable()
        self.table.fill_data_table()
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