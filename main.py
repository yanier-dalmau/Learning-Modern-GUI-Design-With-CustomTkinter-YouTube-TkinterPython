from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter Buttons')
root.iconbitmap('images/codemy.ico')
root.geometry('600x350')


def hello():
    pass

# Use CTkButton instead of tkinter Button
my_button = customtkinter.CTkButton(root, text="Hello World!!!", command=hello)
my_button.pack(pady = 80)

root.mainloop()