import flet as ft

puestos_Kirlian = {
    "Programación": ["Jefe", "Programador Senior", "Programador Junior"],
    "Ingeniería": ["Jefe", "Eléctrico Senior", "Eléctrico Junior"],
    "Mecánica": ["Jefe", "Mecánico Senios", "Mecánico Junior"],
    "Adiminstración": ["Administradora", "Contadora", "Director"],
    "Recursos Humanos": ["Licenciada"] 
}

# ----- MENÚ 3
def sub_gestion_huellas():
    def digitalizar_huella(e):
        pass
    def eliminar_plantilla(e):
        pass
    def eliminar_baseData(e):
        pass
    def restaurar_baseData(e):
        pass

    titulo_menu3 = ft.Container(
        content = ft.Text(
            "Registro de Personal",
            color = ft.Colors.LIGHT_BLUE_500,
            weight = ft.FontWeight.BOLD,
            size = 30
        )
    )

    def boton_generic(texto_in, funcion_in, icono_in, bgcolor_in):
        control = ft.ElevatedButton(
            text = texto_in,
            width = 200,
            height = 40,
            on_click = funcion_in,
            icon = icono_in,
            color = ft.Colors.WHITE,
            style = ft.ButtonStyle(
                bgcolor = bgcolor_in,
                text_style = ft.TextStyle(size = 16, weight = ft.FontWeight.BOLD)
            )
        )
        return control

    Registrar_boton = boton_generic(
        "Registrar", 
        digitalizar_huella, 
        ft.Icons.FINGERPRINT_SHARP, 
        ft.Colors.LIGHT_BLUE_ACCENT_700
    )

    Eliminar_boton = boton_generic(
        "Eliminar Plantilla",
        eliminar_plantilla,
        ft.Icons.DELETE,
        ft.Colors.RED_600
    )

    Eliminar_Todo_boton = boton_generic(
        "Eliminar todo",
        eliminar_baseData,
        ft.Icons.DELETE_FOREVER,
        ft.Colors.RED_600
    )

    Restaurar_boton = boton_generic(
        "Restaurar datos", # Cargar Respaldo
        restaurar_baseData,
        ft.Icons.FILE_PRESENT,
        ft.Colors.LIGHT_BLUE_600
    )

    def icono_leyenda(texto_in, bgcolor_in):
        simbologia = ft.Row(
            controls = [
                ft.Container(
                    width = 18,
                    height = 18,
                    border = ft.border.all(1, color = "black"),
                    bgcolor = bgcolor_in
                ),
                ft.Text(texto_in)
            ]
        )
        return simbologia

    icono1 = icono_leyenda("Disponible", ft.Colors.YELLOW)
    icono2 = icono_leyenda("Utilizado", ft.Colors.PURPLE)

    leyenda = ft.Container(
        content = ft.Row(
            controls = [icono1, icono2],
            alignment = ft.MainAxisAlignment.CENTER,
            spacing = 75
        )
    )
    
    normal_radius = 70
    estacionario_radius = 80

    titulo_normal = ft.TextStyle(
        size = 16, 
        color = ft.Colors.WHITE,
        weight = ft.FontWeight.BOLD
    )

    titulo_estacionario = ft.TextStyle(
        size = 22,
        color = ft.Colors.WHITE,
        weight = ft.FontWeight.BOLD,
        shadow = ft.BoxShadow(blur_radius = 2, color = ft.Colors.BLACK54)
    )

    def animacion_estacionario(e: ft.PieChartEvent):
        for idx, section in enumerate(grafica.sections):
            if idx == e.section_index:
                section.radius = estacionario_radius
                section.title_style = titulo_estacionario
            else:
                section.radius = normal_radius
                section.title_style = titulo_normal
        grafica.update()

    
    grafica = ft.PieChart(
        sections = [
            ft.PieChartSection(
                40, 
                title = "40%",
                title_style = titulo_normal,
                color = ft.Colors.YELLOW,
                radius = normal_radius
            ),
            ft.PieChartSection(
                60,
                title = "60%",
                title_style = titulo_normal,
                color = ft.Colors.PURPLE,
                radius = normal_radius
            )
        ],
        sections_space = 0,
        center_space_radius = 40,
        on_chart_event = animacion_estacionario,
    )

    lector_control = ft.Container(
        content = ft.Column(
            controls = [
                ft.Row(
                    controls = [Registrar_boton, Restaurar_boton], 
                    alignment = ft.MainAxisAlignment.CENTER,
                    spacing = 20
                ),
                ft.Row(
                    controls = [Eliminar_boton, Eliminar_Todo_boton], 
                    alignment = ft.MainAxisAlignment.CENTER,
                    spacing = 20
                ),
                ft.Column(
                    controls = [
                        leyenda, 
                        ft.Container(content = grafica, width = 220, height = 200)
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                    spacing = 35,
                    expand = True
                ),
            ],
            spacing = 20,
        ),
        border = ft.border.all(1, "blue"),
        border_radius = 5,
        width = 500,
        padding = ft.padding.only(top = 30),
    )

    titulo_formulario = ft.Row(
        controls = [
            ft.Text(
                "FORMULARIO",
                size = 24,
                weight = ft.FontWeight.BOLD,
                color = ft.Colors.LIGHT_BLUE_500
            ),
            ft.Icon(ft.Icons.PERSON),
        ],
        alignment = ft.MainAxisAlignment.CENTER
    )
    nombre_indicador = ft.Text("Nombre (s)", weight = ft.FontWeight.BOLD)
    ID_indicador = ft.Text("No. de ID", weight = ft.FontWeight.BOLD)
    apellido1_indicador = ft.Text("Apellido Paterno", weight = ft.FontWeight.BOLD)
    apellido2_indicador = ft.Text("Apellido Materno", weight = ft.FontWeight.BOLD)
    departamento_indicador = ft.Text("Departamento", weight = ft.FontWeight.BOLD)
    cargo_indicador = ft.Text("Cargo", weight = ft.FontWeight.BOLD)

    posiciones = list()
    rango = list(range(0, 10))
    for id in rango:
        posiciones.append(ft.dropdown.Option(id))

    ID_control = ft.Dropdown(
        width = 200,
        options = posiciones,
        border_radius = 15,
        border_color = "blue",
    )

    def TextField_generic():
        control = ft.TextField(
            border_color = "blue",
            width = 200,
            border_radius = 15,
            border = ft.border.all(1, "#44f4f4f4"),
            bgcolor = "transparent"
        )
        return control

    nombre_Field = TextField_generic()
    apellido1_Field = TextField_generic()
    apellido2_Field = TextField_generic()

    def activar_submenu(e):
        cargos_list.clear()
        for cargo in puestos_Kirlian[departamentos_control.value]:
            cargos_list.append(ft.dropdown.Option(cargo))
        cargos_control.update()

    departamentos_list = list()

    for departamento in puestos_Kirlian:
        departamentos_list.append(ft.dropdown.Option(departamento))

    departamentos_control = ft.Dropdown(
        width = 200,
        options = departamentos_list,
        on_change = activar_submenu,
        border_radius = 15,
        border_color = "blue",
    )

    cargos_list = list()
    
    if departamentos_control.value != None:
        for departamento_valor in puestos_Kirlian.values():
            for cargo in departamento_valor:
                cargos_list.append(ft.dropdown.Option(cargo))

    cargos_control = ft.Dropdown(
        width = 200,
        options = cargos_list,
        border_radius = 15,
        border_color = "blue",
    )

    def lector_registrar(e):
        pass
    def guardar_formulario(e):
        pass 

    digitalizar_boton = ft.ElevatedButton(
        text = "PROCESAR HUELLA",
        on_click = lector_registrar,
        width = 175,
        height = 40,
        style = ft.ButtonStyle(
            text_style = ft.TextStyle(size = 16, weight = ft.FontWeight.BOLD)
        )
    )

    guardar_boton = ft.ElevatedButton(
        text = "FINALIZAR",
        on_click = guardar_formulario,
        width = 175,
        height = 40,
        style = ft.ButtonStyle(
            text_style = ft.TextStyle(size = 16, weight = ft.FontWeight.BOLD)
        )
    )

    columna1 = ft.Column(
        controls = [
            ft.Column(controls = [nombre_indicador, nombre_Field]),
            ft.Column(controls = [apellido1_indicador, apellido1_Field]),
            ft.Column(controls = [departamento_indicador, departamentos_control]),
            digitalizar_boton
        ],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        spacing = 30
    )

    columna2 = ft.Column(
        controls = [
            ft.Column(controls = [ID_indicador, ID_control]),
            ft.Column(controls = [apellido2_indicador, apellido2_Field]),
            ft.Column(controls = [cargo_indicador, cargos_control]),
            guardar_boton
        ],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        spacing = 30
    )
    formulario = ft.Container(
        content = ft.Column(
            controls = [
                titulo_formulario,
                ft.Row(
                    controls = [columna1, columna2], 
                    alignment = ft.MainAxisAlignment.CENTER,
                    spacing = 30,
                ),
            ],
            spacing = 30,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        ),
        border = ft.border.all(1, "blue"),
        border_radius = 5,
        width = 500,
        padding = ft.padding.only(top = 30)
    )

    Gestion_Huellas = ft.Container(
        content = ft.Column(
            controls = [
                titulo_menu3,
                ft.Row(
                    controls = [lector_control, formulario],
                    alignment = ft.MainAxisAlignment.CENTER,
                    spacing = 35,
                    expand = True
                )
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        ),
        padding = ft.padding.only(bottom = 20),
        margin = ft.margin.all(20),
        expand = True
    )
    
    return Gestion_Huellas