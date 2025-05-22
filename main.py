import os
from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter Buttons')
root.geometry('600x350')

icon_path = os.path.join(os.path.dirname(__file__), 'images', 'codemy.png')   # Construir ruta absoluta al archivo codemy.png
icono = PhotoImage(file=icon_path)   # Cargar el icono en formato PNG

root.iconphoto(True, icono)

root.mainloop()