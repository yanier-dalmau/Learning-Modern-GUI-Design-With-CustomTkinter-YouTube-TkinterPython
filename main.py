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



# Functions
def delete():
    pass

def copy():
    pass

def paste():
    pass


my_text = customtkinter.CTkTextbox(root)
my_text.pack(pady=20)

my_fame = customtkinter.CTkFrame(root)
my_fame.pack(pady=10)

delete_button = customtkinter.CTkButton(my_fame, text="Delete", command=delete)
copy_button = customtkinter.CTkButton(my_fame, text="Copy", command=copy)
paste_button = customtkinter.CTkButton(my_fame, text="Paste", command=paste)

delete_button.grid(row=0, column=0)
copy_button.grid(row=0, column=1)
paste_button.grid(row=0, column=2)


root.mainloop()