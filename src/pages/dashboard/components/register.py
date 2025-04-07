import flet as ft

#define form class styling and attributes
form_style: dict[str, any] = {
    "border_radius":8,
    #"border": ft.border.all(1,"#ebebeb"),
    "bgcolor":"white10",
    "padding":5,
}

#Define method that create and return a textfield
def text_field():
    return ft.TextField(
        border_color="transparent",
        height=20,
        text_size=20,
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
        height=65,
        bgcolor="#ebebeb",
        border_radius=6,
        padding=8,
        content=ft.Column(
            controls=[
                ft.Text(
                    value=name,
                    size=12,
                    color="black",
                    weight="bold"
                ),
                control
            ]
        )
    )

#Define a Form Class
class Register(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__(**form_style)

        self.expand =True

        #define the 4 row textfields
        self.rowtitular_value = text_field()
        self.rowdireccion_value = text_field()
        self.rowcuenta_value = text_field()
        self.rowlatitud_value = text_field()
        self.rowlongitud_value = text_field()
        self.rowencoder_value = text_field()
        self.rowoffset_value = text_field()
        self.rowoffset_value.value = "0.0"

        #define and wrap each inside container
        self.rowtitular = text_field_container(True, "Titular", self.rowtitular_value)
        self.rowdireccion = text_field_container(3, "Dirección", self.rowdireccion_value)
        self.rowlatitud = text_field_container(1, "Latitud", self.rowlatitud_value)
        self.rowlongitud = text_field_container(1, "Longitud", self.rowlongitud_value)
        self.rowcuenta = text_field_container(2, "Cuenta", self.rowcuenta_value)
        self.rowencoder = text_field_container(2, "ID medidor", self.rowencoder_value)
        self.rowoffset = text_field_container(1, "Consumo pendiente m³", self.rowoffset_value)

        #define a button to submit the data
        self.submit = ft.ElevatedButton(
            text="Submit",
            style=ft.ButtonStyle(bgcolor="red",color = "white",shape={"":ft.RoundedRectangleBorder(radius=8)}),
            on_click=self.submit_data,
        )

        #compile all the atributes into the class container
        self.content=ft.Column(
            expand=True,
            controls=[
                ft.Row(controls=[self.rowtitular]),
                ft.Row(controls=[self.rowdireccion,self.rowlatitud,self.rowlongitud]),
                ft.Row(controls=[self.rowcuenta,self.rowencoder,self.rowoffset]),
                ft.Row(None),
                ft.Row(None),
                ft.Row(None),
                ft.Row(controls=[self.submit],alignment="end"),
            ]
        )

    def submit_data (self,e:ft.TapEvent):

        bandera = True

        titular = self.rowtitular_value.value
        direccion = self.rowdireccion_value.value
        latitud = self.rowlatitud_value.value
        longitud = self.rowlongitud_value.value
        cuenta = self.rowcuenta_value.value
        encoder = self.rowencoder_value.value
        offset = self.rowoffset_value.value

        if titular == "" or titular == "Valor requerido":
            self.rowtitular_value.value = "Valor requerido"
            self.rowtitular_value.color = "red"
            self.rowtitular.update()
            bandera = False
        if direccion == "" or direccion == "Valor requerido":
            self.rowdireccion_value.value = "Valor requerido"
            self.rowdireccion_value.color = "red"
            self.rowdireccion.update()
            bandera = False
        if latitud == "" or latitud == "Valor requerido":
            self.rowlatitud_value.value = "Valor requerido"
            self.rowlatitud_value.color = "red"
            self.rowlatitud.update()
            bandera = False
        if longitud == "" or longitud == "Valor requerido":
            self.rowlongitud_value.value = "Valor requerido"
            self.rowlongitud_value.color = "red"
            self.rowlongitud.update()
            bandera = False
        if cuenta == "" or cuenta == "Valor requerido":
            self.rowcuenta_value.value = "Valor requerido"
            self.rowcuenta_value.color = "red"
            self.rowcuenta.update()
        if encoder == "" or encoder == "Valor requerido":
            self.rowencoder_value.value = "Valor requerido"
            self.rowencoder_value.color = "red"
            self.rowencoder.update()
            bandera = False   
        if bandera:
            data={
                "Titular": titular,
                "Direccion": direccion,
                "Latitud": latitud,
                "Longitud": longitud,
                "Cuenta": cuenta,
                "Encoder": encoder,
                "Offset" : offset
                }
            self.clear_entries()

        bandera = True


    #define a method to clear entries post-submit
    def clear_entries(self):
        self.rowtitular_value.value = ""
        self.rowtitular_value.value = ""
        self.rowdireccion_value.value = ""
        self.rowlatitud_value.value = ""
        self.rowlongitud_value.value = ""
        self.rowcuenta_value.value = ""
        self.rowencoder_value.value = ""
        self.rowoffset_value.value = ""

        self.content.update()