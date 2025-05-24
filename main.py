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


def clicker():
    my_progressbar.step()
    my_label.configure(text=(my_progressbar.get()*100))

my_progressbar = customtkinter.CTkProgressBar(root, orientation="horizontal")
my_progressbar.pack(pady=40)

# Set the default progess starting point
my_progressbar.set(0)

my_button = customtkinter.CTkButton(root, text="Click me", command=clicker)
my_button.pack(pady=10)

my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
my_label.pack(pady=10)


root.mainloop()