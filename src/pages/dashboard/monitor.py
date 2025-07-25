import flet as ft


#Define class to handle data between controls

#Some dummy data

dummy_data={
    0:{"encoder":"232006626",
       "cuenta":"04356",
       "consumo":46.8463,
       "status":"OK",
       "detalles":"Dashboard"},
    1:{"encoder":"232006627",
        "cuenta":"04357",
        "consumo":6.8463,
        "status":"OK",
        "detalles":"Dashboard"},
    2:{"encoder":"232006628",
       "cuenta":"04358",
       "consumo":12.6532,
       "status":"OK",
       "detalles":"Dashboard"},
    3:{"encoder":"232006629",
       "cuenta":"04359",
       "consumo":1.3114,
       "status":"OK",
       "detalles":"Dashboard"},
    4:{"encoder":"232006630",
       "cuenta":"04360",
       "consumo":23.6423,
       "status":"OK",
       "detalles":"Dashboard"},
    5:{"encoder":"232006631",
       "cuenta":"04361",
       "consumo":3.0987,
       "status":"OK",
       "detalles":"Dashboard"},
    6:{"encoder":"232006632",
       "cuenta":"04362",
       "consumo":0.6345,
       "status":"OK",
       "detalles":"Dashboard"},
    
}

class Controller:
    items: dict = dummy_data
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
    "bgcolor": "#cb2b2b",
    "border_radius": ft.border_radius.only(top_left=15, top_right=15),
    "padding": ft.padding.only(left=15,right=15),
}

#Method that creat and return a textfield

def search_field(function: callable):
    return ft.TextField(
        border_color="transparent",
        height=20,
        text_size=14,
        content_padding=0,
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
                ft.Icon(name=ft.Icons.SEARCH,
                        size=17,
                        opacity=0.85,
                        color="#cb2b2b"
                        ),
                        control,
            ],
        ),
    )


#define header class

class Header(ft.Container):
    def __init__(self, dt: ft.DataTable) -> None:
        super().__init__(**header_style, 
                         on_hover=self.toogle_search)
        
        #create a dt attribute
        self.dt= dt

        #create a textfield for search/filter
        self.search_value = search_field(self.filter_dt_rows)

        #create a searchbox
        self.search = search_bar(self.search_value)

        #define other class atributes
        self.name = ft.Text("Monitor medidores de agua", color="white", weight="bold")
        self.avatar = ft.IconButton("person",icon_color="white")

        #compile the attributyes inside the header container
        self.content = ft.Row(
            alignment="spaceBetween",
            controls=[self.name, self.search, self.avatar]
        )

    #define method that toggles search box visibility
    def toogle_search(self, e: ft.HoverEvent):
        self.search.opacity = 1 if e.data == "true" else 0
        self.search.update()

    #define a placeholder methor for tiltering data
    def filter_dt_rows(self,e):
        for data_rows in self.dt.rows:
            data_col1 = data_rows.cells[0]
            data_col2 = data_rows.cells[1]
            data_col3 = data_rows.cells[2]
            data_col4 = data_rows.cells[3]
            data_rows.visible=(True if (e.control.value.lower() in data_col1.content.value.lower()) or
                                 (e.control.value.lower() in data_col2.content.value.lower()) or 
                                 (e.control.value.lower() in str(data_col3.content.value).lower()) or 
                                 (e.control.value.lower() in str(data_col4.content.value).lower()) 
                                 else False)
            
            data_rows.update()


#define form class styling and attributes
form_style: dict[str, any] = {
    "border_radius":8,
    "border": ft.border.all(1,"#ebebeb"),
    "bgcolor":"white10",
    "padding":15,
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

        #define the 4 row textfields
        self.row1_value = text_field()
        self.row2_value = text_field()
        self.row3_value = text_field()
        self.row4_value = text_field()

        #define and wrap each inside container
        self.row1 = text_field_container(True, "Row One", self.row1_value)
        self.row2 = text_field_container(3, "Row Two", self.row2_value)
        self.row3 = text_field_container(1, "Row Three", self.row3_value)
        self.row4 = text_field_container(1, "Row Four", self.row4_value)

        #define a button to submit the data
        self.submit = ft.ElevatedButton(
            text="Submit",
            style=ft.ButtonStyle(shape={"":ft.RoundedRectangleBorder(radius=8)}),
            on_click=self.submit_data,
        )

        #compile all the atributes into the class container
        self.content=ft.Column(
            expand=True,
            controls=[
                ft.Row(controls=[self.row1]),
                ft.Row(controls=[self.row2,self.row3,self.row4]),
                ft.Row(controls=[self.submit],alignment="end"),
            ]
        )

    def submit_data (self,e:ft.TapEvent):
        data={
            "Encoder":self.row1_value.value,
            "Cuenta":self.row2_value.value,
            "Consumo":self.row3_value.value,
            "Status":self.row4_value.value,
            "Detalles":"Dashboard",
            }
        Controller.add_item(data)
        self.clear_entries()
        self.dt.fill_data_table()

    #define a method to clear entries post-submit
    def clear_entries(self):
        self.row1_value.value=""
        self.row2_value.value=""
        self.row3_value.value=""
        self.row4_value.value=""

        self.content.update()

#define data table style, attributes and columns
column_names =["Encoder", "Cuenta", "Consumo", "Status", "Detalles"]

data_table_style={
    "expand":True,
    "border_radius":8,
    "border": ft.border.all(2,"#ebebeb"),
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

def Tabla(page:ft.Page) -> None:
    page.bgcolor= "#fdfdfd"

    table = DataTable()
    
    header = Header(dt=table)
    form = Form(dt=table)

    page.add(
        ft.Column(
            expand=True,
            controls=[
                #header....
                header,
                # ft.Divider(height=2, color="transparent"),
                # #form
                # form,
                ft.Column(
                    scroll="hidden",
                    expand=True,
                    controls=[ft.Row(controls=[table])]
                )
            ]
        )
    )
    

    page.update()
    
    #It's possible fill out the dt after add the control to the page
    table.fill_data_table()
    


ft.app(target=Tabla)