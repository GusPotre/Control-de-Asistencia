import flet as ft
from submenu1 import sub_asistencia
from submenu2 import sub_registro
from submenu3 import sub_gestion_huellas
from submenu4 import sub_dispositivos
from submenu5 import sub_configuraciones

# ----- VENTANA INTERFAZ PRINCIPAL
def menu(page):
    # Creación de las instancias de los submenús
    Asistencia = sub_asistencia()
    Registro = sub_registro()
    Gestion_Huellas = sub_gestion_huellas()
    Dispositivos = sub_dispositivos()
    Configuraciones = sub_configuraciones()
    
    page.window.maximized = True
    page.title = "Menú principal"

    Menu_boton = ft.Container(
        ft.IconButton(
            icon = ft.Icons.MENU_ROUNDED,
            tooltip = "Ocultar",
            icon_color = ft.Colors.WHITE, 
            width = 150
            #on_click = ocultar_riel
        ),
    )

    App_barra  = ft.AppBar(
        title = ft.Text(
            "CONTROL DE ASISTENCIA", 
            size = 28, 
            text_align = "center",
            color = ft.Colors.WHITE,
            weight = ft.FontWeight.BOLD,
            style = ft.TextStyle(letter_spacing = 5)
        ),
        actions = [Menu_boton],
        center_title = True,
        toolbar_height = 70,
        bgcolor = ft.Colors.BLACK,        
    )

    def ventana(e):
        index = e.control.selected_index
        content.controls.clear()
        if index == 0:
            content.controls.append(Asistencia)
        elif index == 1:
            content.controls.append(Registro)
        elif index == 2:
            content.controls.append(Gestion_Huellas)
        elif index == 3:
            content.controls.append(Dispositivos)
        elif index == 4:
            content.controls.append(Configuraciones)
        page.update()

    Menu_Barra = ft.NavigationRail(
        selected_index = 0,
        label_type = ft.NavigationRailLabelType.ALL,
        min_width = 150,
        min_extended_width = 300,
        destinations = [
            ft.NavigationRailDestination(
                icon = ft.Icon(ft.Icons.GROUP), 
                label = "Asistencia",
            ),
            ft.NavigationRailDestination(
                icon = ft.Icon(ft.Icons.BOOK), 
                label = "Registros"
            ),
            ft.NavigationRailDestination(
                icon = ft.Icon(ft.Icons.FINGERPRINT), 
                label = "Gestión de Huellas"
            ),
            ft.NavigationRailDestination(
                icon = ft.Icon(ft.Icons.USB), 
                label = "Dispositivos"
            ),
            ft.NavigationRailDestination(
                icon = ft.Icon(ft.Icons.SETTINGS_OUTLINED), 
                selected_icon = ft.Icon(ft.Icons.SETTINGS),
                label =  "Configuraciones"
            ),
        ], 
        on_change = ventana,
        group_alignment=-0.9
    ) 

    content = ft.Column(
        [Asistencia], 
        expand = True,
        alignment = ft.MainAxisAlignment.SPACE_EVENLY,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER
    )

    divisor = ft.VerticalDivider(width = 5)

    body = ft.Row(
        [Menu_Barra, divisor, content], 
        expand = True
    )

    page.add(App_barra, body)
