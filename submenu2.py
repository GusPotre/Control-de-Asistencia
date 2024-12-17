import flet as ft

def sub_registro():
    # ----- MENÚ 2
    def save_document(e):
        pass

    def editar_usuario(e):
        pass

    titulo_menu2 = ft.Container(
        content = ft.Text(
            "Plantilla de Empleados",
            color = ft.Colors.LIGHT_BLUE_500,
            weight = ft.FontWeight.BOLD,
            size = 30
        ),
        margin = ft.margin.only(bottom = 20)
    )

    Guardar_boton = ft.ElevatedButton(
        text = "Guardar plantilla",
        icon = ft.Icons.SAVE,
        color = ft.Colors.WHITE,
        on_click = save_document,
        width = 225,
        height = 40,
        style = ft.ButtonStyle(
            bgcolor = ft.Colors.GREEN,
            text_style = ft.TextStyle(size = 16, weight = ft.FontWeight.BOLD)
        )
    )

    Tabla_plantilla = ft.Container(
        content = ft.Column(
            controls = [
                ft.DataTable(
                    columns = [
                        ft.DataColumn(ft.Text("No.", color = ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text("Nombre", color =  ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text("Siglas", color = ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text("Departamento", color = ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text("Cargo", color = ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text("ID", color = ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text("Huella Digital", color = ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text(None, color = ft.Colors.LIGHT_BLUE_600))
                    ],
                    rows = [
                        ft.DataRow(
                            cells = [
                                ft.DataCell(ft.Text("1")),
                                ft.DataCell(ft.Text("Denise Aldama Tello")),
                                ft.DataCell(ft.Text("DAT")),
                                ft.DataCell(ft.Text("Programación")),
                                ft.DataCell(ft.Text("Patrona")),
                                ft.DataCell(ft.Text("3")),
                                ft.DataCell(ft.Text("CARGADA")),
                                ft.DataCell(
                                    ft.Text(None), 
                                    on_tap = editar_usuario,
                                    show_edit_icon = True
                                )
                            ]
                        )
                    ]
                ) # Tabla de datos
            ],
            auto_scroll = "always",
            scroll = ft.ScrollMode.ADAPTIVE
        ), # Columna
        border_radius = 10,
        border = ft.border.all(2, ft.Colors.LIGHT_BLUE_600),
        margin = ft.margin.only(top = 10),
        expand = True
    ) # Contenedor

    Registro = ft.Container(
        content = ft.Column(
            controls = [
                titulo_menu2,
                Guardar_boton,
                Tabla_plantilla
            ]
        ),
        padding = 20,
        expand = True
    )

    return Registro