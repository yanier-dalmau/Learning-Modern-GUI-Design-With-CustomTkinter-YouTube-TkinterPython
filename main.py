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


# Create a Function
def input():
    dialog = customtkinter.CTkInputDialog(
        text="What is your name?", 
        title="Hello There!",
        fg_color="white",
        button_fg_color="red",
)
    thing = dialog.get_input()
    if thing:
        my_label.configure(text=f"Hello {thing}")
    else:
        my_label.configure(text=f"Yout Forgot To Type Anything!")

# Create a Button
my_button = customtkinter.CTkButton(root, text="Click Me!", command=input)
my_button.pack(pady=40)

# Create a Label
my_label = customtkinter.CTkLabel(root, text='')
my_label.pack(pady=10)

root.mainloop()

