import os
import platform
from tkinter import *
import customtkinter
from PIL import Image

# Set the theme and color options
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter Buttons')
root.geometry('700x350')

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



my_image = customtkinter.CTkImage(
    light_image=Image.open('images/little_bird.png'),
    dark_image=Image.open('images/little_bird.png')
)

my_label = customtkinter.CTkLabel(root, text="", image=my_image)
my_label.pack(pady=10)


root.mainloop()