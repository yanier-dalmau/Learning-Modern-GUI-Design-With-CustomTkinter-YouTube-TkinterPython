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



def get_rad():
    if radio_var.get() == "other":
        my_label2.configure(text="Please Make a Selection")
    elif radio_var.get() == "Yes":
        my_label2.configure(text="Of Course You Like Pizza!")
    else:
        my_label2.configure(text="What's Wrong With You?!")


my_label = customtkinter.CTkLabel(root, text="Do you like Pizza?!", font=("Helvetica", 18))
my_label.pack(pady=40)

radio_var = customtkinter.StringVar(value="other")
# Radio Button 1
my_rad1 = customtkinter.CTkRadioButton(root, 
    text="Yes I Do", 
    value= "Yes", 
    variable=radio_var,
    # width=50,
    # height=50,
    radiobutton_width=50,
    radiobutton_height=50,
    corner_radius=1,
    border_width_unchecked=2,
    border_width_checked=5,
    border_color="red",
    hover_color="pink",
    fg_color="green",
    hover=True,
    text_color="red",
    font=("Helvetica", 18),
    state="disable",
)
my_rad1.pack(pady=10)
# Radio Button 2
my_rad2 = customtkinter.CTkRadioButton(root, text="No I Don't", value= "No", variable=radio_var)
my_rad2.pack(pady=10)

my_button = customtkinter.CTkButton(root, text="Select", command=get_rad)
my_button.pack(pady=10)

my_label2 = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
my_label2.pack(pady=10)


root.mainloop()