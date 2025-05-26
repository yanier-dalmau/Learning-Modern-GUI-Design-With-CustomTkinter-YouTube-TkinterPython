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


# Create funtion
def switcher():
    my_label.configure(text=switch_var.get())

# Create toggle function
def clicker():
    # my_switch.deselect()
    # my_switch.select()
    my_switch.toggle()
    

# Create a StringVar
switch_var = customtkinter.StringVar(value="on")
# Create Switch
my_switch = customtkinter.CTkSwitch(root, 
    text="Switch", 
    command=switcher,
    variable=switch_var,
    onvalue="on",
    offvalue="off",
    # width=200,
    # height=100,
    switch_width=200,
    switch_height=25,
    # corner_radius=15,
    border_color="orange",
    border_width=5,
    fg_color="red",
    progress_color="green",
    button_color="pink",
    button_hover_color="yellow",
    font=("Helvetica", 24),
    text_color="blue",
    state="disabled",
)
my_switch.pack(pady=40)

# Create a label
my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=10)

# Create a button
my_button = customtkinter.CTkButton(root, text="Click Me!", command=clicker)
my_button.pack(pady=10)

root.mainloop()