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


# Create function
def color_picker(choice):
    my_label.configure(text=choice, text_color=choice)

def color_picker2():
    my_label.configure(text=my_option.get(), text_color=my_option.get())

def yellow():
    my_option.set("Yellow")
    my_label.configure(text=my_option.get(), text_color=my_option.get())

# Set the options for our OptionMenu
colors = ["Red", "Green", "Blue"]

# Create OptionMenu
my_option = customtkinter.CTkComboBox(
    root, 
    values=colors,
    # command=color_picker,
)
my_option.pack(pady=40)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=10)

pick_button = customtkinter.CTkButton(root, text="Make Choice", command=color_picker2)
pick_button.pack(pady=10)

yellow_button = customtkinter.CTkButton(root, text="Pick Yellow", command=yellow)
yellow_button.pack(pady=10)

root.mainloop()