import os
import platform
from tkinter import *
import customtkinter

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



def change():
    my_font.configure(underline=False, overstrike=False, size=22, slant="roman")


my_font = customtkinter.CTkFont(family="Helvetica", 
    size=44,
    weight="bold",  # bold/normal
    slant="italic",   # italic/roman
    underline=True,
    overstrike=True,
)

my_label = customtkinter.CTkLabel(root, text="This is Text", font=my_font)
my_label.pack(pady=40)

my_button = customtkinter.CTkButton(root, text="Change text", command=change)
my_button.pack(pady=10)

root.mainloop()