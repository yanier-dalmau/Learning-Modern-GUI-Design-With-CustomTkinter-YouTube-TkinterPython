import os
import platform
from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

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
  
# Variables globales para los widgets  
my_text = None  
my_button = None  
my_option = None  
  
def change():
    global mode
    if mode == "dark":
        customtkinter.set_appearance_mode("light")
        mode = "light"
        # Sintaxis correcta para CTkTextbox
        my_text.delete("1.0", "end")  
        my_text.insert("1.0", "This is Light Mode...")
    else:  
        customtkinter.set_appearance_mode("dark")
        mode = "dark"  
        # Sintaxis correcta para CTkTextbox
        my_text.delete("1.0", "end")
        my_text.insert("1.0", "This is Dark Mode...")


def change_colors_dynamic(choice):  
    global my_text, my_button, my_option  
      
    # Cambiar el tema  
    customtkinter.set_default_color_theme(choice)  
      
    # Guardar contenido actual del textbox  
    current_content = my_text.get("1.0", "end-1c")  # end-1c para evitar el salto de línea extra  
      
    # Destruir widgets existentes  
    my_text.destroy()  
    my_button.destroy()  
    my_option.destroy()  
      
    # Recrear widgets con el nuevo tema  
    my_text = customtkinter.CTkTextbox(root, width=600, height=300)  
    my_text.pack(pady=20)  
    my_text.insert("1.0", current_content)  
      
    my_button = customtkinter.CTkButton(root, text="Change Light/Dark", command=change)  
    my_button.pack(pady=20)  
      
    colors = ["blue", "dark-blue", "green"]  
    my_option = customtkinter.CTkOptionMenu(root, values=colors, command=change_colors_dynamic)  
    my_option.pack(pady=10)  
    my_option.set(choice)  # Mantener la selección actual  
  
# Crear widgets iniciales  
my_text = customtkinter.CTkTextbox(root, width=600, height=300)
my_text.pack(pady=20)
my_text.insert("1.0", "This is Dark Mode...")  
  
my_button = customtkinter.CTkButton(root, text="Change Light/Dark", command=change)
my_button.pack(pady=20)

colors = ["blue", "dark-blue", "green"]
my_option = customtkinter.CTkOptionMenu(root, values=colors, command=change_colors_dynamic)  
my_option.pack(pady=10)
my_option.set("dark-blue")  # Establecer el tema inicial  
  
root.mainloop()