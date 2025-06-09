import os
import platform
from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # root = customtkinter.CTk()

        self.title('Tkinter.com - Custom Tkinter Buttons')
        self.geometry('700x450')

        # Verificar el sistema operativo
        if platform.system() == 'Windows':
            self.iconbitmap('images/codemy.ico')  # Usar icono ICO en Windows
        else:
            self.iconphoto(True, 
                PhotoImage(
                    file=os.path.join(os.path.dirname(__file__), 
                    'images', 
                    'codemy.png')
                )
            )  # Usar icono PNG en otros sistemas operativos

        self.my_text = customtkinter.CTkTextbox(self, width=600, height=300)
        self.my_text.pack(pady=20)

        self.my_button = customtkinter.CTkButton(self, text="Clear Box", command=self.clear)
        self.my_button.pack(pady=20)

    def clear(self):
        self.my_text.delete('0.0', END)


# Create app and create our app's mainloop
app = App()
app.mainloop()