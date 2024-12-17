import flet as ft
from menu import menu

# ----- CONTRASEÑA
usuarios = {
    "DeniseAT": "Kirlian123",
    "Alejandra": "KIRLIAN123",
    "Israel": "KirlianAutomation",
    "" : ""
}

# ----- VENTANA LOGIN
def login(page):
    page.padding = 0
    page.window.width = 1120
    page.window.height = 630
    page.window.resizable = False
    page.vertical_alignmet = "center"
    page.horizontal_alignmet = "center"
    page.title = "Inicio de sesión"

    def autenticacion(e):
        flag1 = False
        flag2 = False
        input_usuario = usuario_Field.value
        input_contraseña = contraseña_Field.value

        for username, password in usuarios.items():
            if username == input_usuario and password == input_contraseña:
                flag1 = True
                flag2 = True
            if username == input_usuario and password != input_contraseña:
                flag1 = True
                flag2 = False
            if username != input_usuario and password == input_contraseña:
                flag1 = False
                flag2 = True
        
        if flag1 == True and flag2 == True:
            page.controls.clear()
            menu(page)
        if flag1 == True and flag2 == False:
            contraseña_Field.error_text = "Contraseña incorrecto"        
        if flag1 == False and flag2 == True:
            usuario_Field.error_text = "Usuario incorrecto"        
        if flag1 == False and flag2 == False:
            usuario_Field.error_text = "Usuario incorrecto"
            contraseña_Field.error_text = "Contraseña incorrecto"

        usuario_Field.value = None
        contraseña_Field.value = None
        page.update()

    def limpiar_usuario(e):
        usuario_Field.error_text = None
        page.update()
    def limpiar_contraseña(e):
        contraseña_Field.error_text = None
        page.update()


    fondo = ft.Image(
        src = "Temas/theme3.jpg", 
        width = 1120,
        height = 630
    )
    
    avatar = ft.Image(
        src = "Logos/logo1.png", 
        width = 110
    )

    encabezado = ft.Text(
        "Welcome to Kirlian Automation",
        color = "blue", 
        weight = "w700", 
        size = 26
    )

    usuario_Field = ft.TextField(
        label = "Usuario",
        border_color = "blue",
        prefix_icon = ft.Icons.PERSON, 
        width = 275,
        border_radius = 18,
        border = ft.border.all(1, "#44f4f4f4"),
        bgcolor = "transparent",
        on_focus = limpiar_usuario
    )

    contraseña_Field = ft.TextField(
        label = "Contraseña",
        border_color = "blue",
        password = True,
        can_reveal_password = True,
        prefix_icon = ft.Icons.LOCK_ROUNDED,
        width = 275,
        border_radius = 18,
        border = ft.border.all(1, "#44f4f4f4"),
        bgcolor = "transparent",
        on_focus = limpiar_contraseña
    )

    entrar_Button = ft.ElevatedButton(
        text = "LOGIN", 
        on_click = autenticacion,
        width = 200,
        height=50,
        style = ft.ButtonStyle(
            color = "white", 
            bgcolor = ft.Colors.BLUE_400,
            text_style = ft.TextStyle(size = 20, weight = ft.FontWeight.BOLD)
            )
    )

    controles = ft.Column(
        [avatar, encabezado, usuario_Field, contraseña_Field, entrar_Button],
        alignment = ft.MainAxisAlignment.SPACE_EVENLY,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER
    )

    body = ft.Stack([
            fondo,
            ft.Container(                
                controles,
                width = 450,
                height = 500,
                left = 335,
                top = 50,
                border_radius = 18,
                blur = ft.Blur(10, 12, ft.BlurTileMode.MIRROR),
                border = ft.border.all(1, "blue"),
            ),
        ]
    )

    page.add(body)