import flet as ft

# ----- MENÚ 4
def sub_dispositivos():

    titulo_menu4 = ft.Text(
        "Configuración de dispositivos",
        size = 30,
        color = ft.Colors.LIGHT_BLUE_500,
        text_align = ft.TextAlign.CENTER,
        weight = ft.FontWeight.BOLD
    )

    # Titulos 
    def titulo_generic(texto_in):
        titulo = ft.Text(
            texto_in, 
            size = 20,
            weight = ft.FontWeight.BOLD
        )
        return titulo

    titulo_moduloWiFi = titulo_generic("MODULO WIFI ESP")
    titulo_cerradura = titulo_generic("CERRADURA ELÉCTRICA")
    titulo_lector = titulo_generic("LECTOR DE HUELLAS")

    def imagen_generic(ruta):
        imagen = ft.Container(
            content = ft.Image(
                src = f"Dispositivos/{ruta}",
                width = 200,
                height = 200
            ),
            #border = ft.border.all(1, "blue"),
            #border_radius = 5,
            width = 200,
            height = 200
        )
        return imagen
    
    imagen_wifi = imagen_generic("ESP8266_01.png")
    imagen_cerradura = imagen_generic("Door_Close.png")
    imagen_lector = imagen_generic("Lector_AS608.png")

    def reconectar_wifi(e):
        pass
    def cambiar_modo(e):
        pass
    def cerradura_estado(e):
        pass
    def comunicacion_lector(e):
        pass

    def boton_generic(texto_in, evento_in):
        boton = ft.ElevatedButton(
            text = texto_in,
            width = 200,
            height = 40,
            on_click = evento_in,
            style = ft.ButtonStyle(
                text_style = ft.TextStyle(size = 16, weight = ft.FontWeight.BOLD)
            )
        )
        return boton
        
    Conectar_boton = boton_generic("CONECTAR", reconectar_wifi)
    modo_boton = boton_generic("AUTOMATICO", cambiar_modo)
    puerta_boton = boton_generic("ABRIR PUERTA", cerradura_estado)
    lector_boton = boton_generic("CONEXIÓN", comunicacion_lector)

    puertos = list()
    puertos.append(ft.dropdown.Option("Port 80"))
    puertos.append(ft.dropdown.Option("Port 105"))
    puertos.append(ft.dropdown.Option("Port 01"))

    puerto_indicador = ft.Text("Puerto/Red:", weight = ft.FontWeight.BOLD)
    lector_indicador = ft.Text("Estado: ", weight = ft.FontWeight.BOLD)

    puerto_menu = ft.Column(
        controls = [
            puerto_indicador,
            ft.Dropdown(
                width = 200,
                options = puertos,
                border_radius = 15,
                border_color = ft.Colors.BLUE
            )
        ]
    )

    lector_Field = ft.Column(
        controls = [
            lector_indicador,
            ft.TextField(
                border_color = "blue",
                width = 200,
                border_radius = 15,
                border = ft.border.all(1, "#44f4f4f4"),
                bgcolor = "transparent"
            )
        ]
    )

    modulo_wifi = ft.Container(
        content = ft.Column(
            controls = [
                titulo_moduloWiFi,
                imagen_wifi,
                puerto_menu,
                Conectar_boton
            ],
            spacing = 30,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        ),
        width = 325,
        padding = ft.padding.only(top = 20)
    )

    cerradura = ft.Container(
        content = ft.Column(
            controls = [
                titulo_cerradura,
                imagen_cerradura,
                modo_boton,
                puerta_boton
            ],
            spacing = 30,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        ),
        width = 325,
        padding = ft.padding.only(top = 20)
    )

    lector = ft.Container(
        content = ft.Column(
            controls = [
                titulo_lector,
                imagen_lector,
                lector_Field,
                lector_boton
            ],
            spacing = 30,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        ),
        width = 325,
        padding = ft.padding.only(top = 20)
    )

    Dispositivos = ft.Container(
        content = ft.Column(
            controls = [
                titulo_menu4,
                ft.Row(
                    controls =[
                        modulo_wifi, 
                        ft.VerticalDivider(), 
                        cerradura, 
                        ft.VerticalDivider(), 
                        lector
                    ],
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                    expand = True
                )
            ],
            spacing = 20,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        ),
        margin = ft.margin.all(40),
        expand = True
    )

    return Dispositivos