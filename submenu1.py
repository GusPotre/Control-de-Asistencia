import flet as ft

# ----- MENÚ 1
def sub_asistencia():
    def save_document(e):
        pass

    def load_document(e):
        pass

    titulo_menu1 = ft.Container(
        content = ft.Text(
            "Registro de Entradas y Salidas",
            size = 30,
            weight = ft.FontWeight.BOLD,
            color = ft.Colors.LIGHT_BLUE_500
        ),
        margin = ft.margin.only(bottom = 20)
    )

    Guardar1_Boton = ft.ElevatedButton(
        text = "Descargar registro",
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

    Guardar2_Boton = ft.ElevatedButton(
        text = "Descargar Asistencias",
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

    Subir_Boton = ft.ElevatedButton(
        text = "Subir al servidor",
        icon = ft.Icons.BACKUP_OUTLINED,
        color = ft.Colors.WHITE,
        on_click = load_document,
        width = 225,
        height = 40,
        style = ft.ButtonStyle(
            bgcolor = ft.Colors.LIGHT_BLUE_700,
            text_style = ft.TextStyle(size = 16, weight = ft.FontWeight.BOLD)
        )
    )

    estado_IO = ft.Container(
        content = ft.Text(
            "Entradas:           Salidas:            Asistencias:",
            size = 16,
        ),
        margin = ft.margin.only(top = 5)
    )

    tabla_IO = ft.Container(
        content = ft.Column(
            controls = [
                ft.DataTable(
                    columns = [
                        ft.DataColumn(ft.Text("ID", color = ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text("Nombre", color = ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text("Siglas", color = ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text("Departamento", color = ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text("Cargo", color = ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text("Estado", color = ft.Colors.LIGHT_BLUE_600)),
                        ft.DataColumn(ft.Text("Hora", color = ft.Colors.LIGHT_BLUE_600))
                    ],
                    rows = [
                        ft.DataRow(
                            cells = [
                                ft.DataCell(ft.Text("3")),
                                ft.DataCell(ft.Text("Denise Aldama Tello")),
                                ft.DataCell(ft.Text("DAT")),
                                ft.DataCell(ft.Text("Programación")),
                                ft.DataCell(ft.Text("Patrona")),
                                ft.DataCell(ft.Text("Entrada")),
                                ft.DataCell(ft.Text("8:50 hrs.")),
                            ]
                        ),
                        ft.DataRow(
                            cells = [
                                ft.DataCell(ft.Text("18")),
                                ft.DataCell(ft.Text("Samantha Ramos de Aldama")),
                                ft.DataCell(ft.Text("SSRA")),
                                ft.DataCell(ft.Text("Administración")),
                                ft.DataCell(ft.Text("Administradora")),
                                ft.DataCell(ft.Text("Entrada")),
                                ft.DataCell(ft.Text("9:10 hrs.")),
                            ]
                        ),
                        ft.DataRow(
                            cells = [
                                ft.DataCell(ft.Text("24")),
                                ft.DataCell(ft.Text("Mario Aldama Tello")),
                                ft.DataCell(ft.Text("MAT")),
                                ft.DataCell(ft.Text("Ingenieria")),
                                ft.DataCell(ft.Text("Eléctrico")),
                                ft.DataCell(ft.Text("Salida")),
                                ft.DataCell(ft.Text("16:50 hrs.")),
                            ]
                        ) # Ultima fila
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
    ) #Contenedor

    Asistencia = ft.Container(
        content = ft.Column( 
            controls = [
                titulo_menu1,
                ft.Row(controls = [Guardar1_Boton, Guardar2_Boton, Subir_Boton], tight = False),
                estado_IO,
                tabla_IO
            ],
        ),
        padding = 20,
        width = 1000,
        expand = True
    )

    return Asistencia
    