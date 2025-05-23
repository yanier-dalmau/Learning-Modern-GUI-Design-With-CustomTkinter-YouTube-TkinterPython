import os
import platform
from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter Buttons')
root.geometry('600x350')

# Verificar el sistema operativo
if platform.system() == 'Windows':
    root.iconbitmap('images/codemy.ico')  # Usar icono ICO en Windows
else:
    root.iconphoto(True, 
        PhotoImage(
            file=os.path.join(os.path.dirname(__file__), 
            'images', 
            'codemy.png')
        )
    )  # Usar icono PNG en otros sistemas operativos

my_label = customtkinter.CTkLabel(root, text="Pick a color", font=("Helvetica", 18))
my_label.pack(pady=40)

# Set the options for our combobox 
colors = ["Red", "Green", "Blue"]
# Create combobox
my_combo = customtkinter.CTkComboBox(root, values=colors)
my_combo.pack(pady=20)

root.mainloop()