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


def color_picker(choice):
    output_label.configure(text=choice, text_color=choice)

def color_picker2():
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())
    
def color_picker_yellow():
    # Set de combo box option
    my_combo.set("Yellow")
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())



my_label = customtkinter.CTkLabel(root, text="Pick a color", font=("Helvetica", 18))
my_label.pack(pady=40)

# Set the options for our combobox 
colors = ["Red", "Green", "Blue"]
# Create combobox
my_combo = customtkinter.CTkComboBox(root, 
    values=colors,
    height=50,
    width=200,
    font=("Helvetica", 18),
    dropdown_font=("Helvetica", 18),
    corner_radius=50,
    border_width=2,
    border_color="red",
    button_color="red",
    button_hover_color="green",
    dropdown_hover_color="green"
)
my_combo.pack(pady=0)

# Create a button
my_button = customtkinter.CTkButton(root, text="Pick a color", command=color_picker2)
my_button.pack(pady=20)

# Yellow button
yellow_button = customtkinter.CTkButton(root, text="Pick yellow!", command=color_picker_yellow)
yellow_button.pack(pady=20)

# Create output label
output_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
output_label.pack(pady=20)

root.mainloop()