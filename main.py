import os
import platform
from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("themes/red.json")  # Themes: blue (default), dark-blue, green
# Turn off scaling
customtkinter.deactivate_automatic_dpi_awareness()

root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter Buttons')
root.geometry('700x500')

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



mode = "dark"
def change():
    global mode
    if mode == "dark":
        customtkinter.set_appearance_mode("light")
        mode = "light"
        # Clear text box
        my_text.delete(0.0, END)
        my_text.insert(END, "This is Light Mode...")
    else:
        customtkinter.set_appearance_mode("dark")
        mode = "dark"
        # Clear text box
        my_text.delete(0.0, END)
        my_text.insert(END, "This is Dark Mode...")


def change_colors(choice):
    customtkinter.set_default_color_theme(choice)


my_text = customtkinter.CTkTextbox(root, width=600, height=300)
my_text.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Change Light/Dark", command=change)
my_button.pack(pady=20)

colors = ["blue", "dark-blue", "green"]
my_option = customtkinter.CTkOptionMenu(root, values=colors, command=change_colors)
my_option.pack(pady=10)

my_progress = customtkinter.CTkProgressBar(root, orientation="horizontal", )
my_progress.pack(pady=20)

root.mainloop()