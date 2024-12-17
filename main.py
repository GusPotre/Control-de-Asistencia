import flet as ft
from login import login

'''
main                            # Archivo principal que se ejecuta
├── login                       # Archivo con los controles de login
    ├── menu                    # Archivo con los controles de la interfaz
        ├── Asistencia          
        ├── Registros
        ├── Dispositivos
        └── Configuraciones
'''

    # ----- VENTANA ORIGEN
def main(page: ft.Page):
    login(page)

ft.app(main)