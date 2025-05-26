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


# Create Tabview
my_tab = customtkinter.CTkTabview(root, 
    width=600,
    height=250,
    corner_radius=10,
    fg_color="silver",
    segmented_button_fg_color="red",
    segmented_button_selected_color="green",
    segmented_button_selected_hover_color="pink",
    segmented_button_unselected_hover_color="purple",
    segmented_button_unselected_color="yellow",
)
my_tab.pack(pady=10)

# Create tabs
tab_1 = my_tab.add("Tab 1")
tab_2 = my_tab.add("Tab 2")

# Put stuff in tabs
my_button = customtkinter.CTkButton(tab_1)
my_button.pack(pady=40)

root.mainloop()