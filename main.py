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


# Create a scrollable frame
my_frame = customtkinter.CTkScrollableFrame(root,
    orientation="vertical",
    width=300,
    height=200,
    label_text="Hello World!",
    label_fg_color="blue",
    label_text_color="yellow",
    label_font=("Helvetica", 18),
    label_anchor="center", # "w", "n", "ne", "e", "se", "s", "sw", "w", "nw", center
    border_width=3,
    border_color="green",
    fg_color="red",
    scrollbar_fg_color="yellow",
    scrollbar_button_color="pink",
)
my_frame.pack(pady=40)

for x in range(20):
    customtkinter.CTkButton(my_frame, text="This is a button!!").pack(pady=10)

root.mainloop()