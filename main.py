import os
import platform
from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter Buttons')
root.geometry('700x450')

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
    
def game():
    my_label.configure(text="You clicked the thing!")

check_var = customtkinter.StringVar(value="off")
my_check = customtkinter.CTkCheckBox(root, 
    text="Would you like to play a game?",
    variable=check_var,
    onvalue="on", 
    offvalue="off"
)
my_check.pack(pady=40)

my_button = customtkinter.CTkButton(root, text="Submit", command=game)
my_button.pack(pady=20)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)


root.mainloop()
