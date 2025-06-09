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



global my_y
my_y = 450/2 + 350

def up():
    global my_y
    my_y -= 20
    if my_y >= 195:
        my_text.place(x=700/2, y=my_y, anchor='center')
        up_button.configure(text=my_y)

def down():
    pass


# Frame
my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=20)

# Buttons
up_button = customtkinter.CTkButton(my_frame, text="Up", command=up)
up_button.grid(row=0, column=0, padx=10)

down_button = customtkinter.CTkButton(my_frame, text="Down", command=down)
down_button.grid(row=0, column=1, padx=10)

# Text Box
my_text = customtkinter.CTkTextbox(root, width=400, height=200)
my_text.place(x=700/2, y=my_y, anchor='center')

root.mainloop()