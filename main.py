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


# Funtion
def sliding(value):
    my_label.configure(text=int(value))


my_slider = customtkinter.CTkSlider(root, 
    from_=0,
    to=100,
    command=sliding,
    orientation="horizontal",
    number_of_steps=10,
    width=400,
    height=50,
    border_width=10,
)
my_slider.pack(pady=40)

# Define starting point
my_slider.set(0)

my_label = customtkinter.CTkLabel(root, text=my_slider.get(), font=("Helvetica", 18))
my_label.pack(pady=20)


root.mainloop()