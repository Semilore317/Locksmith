from tkinter import PhotoImage
import customtkinter
from components.header_frame import HeaderFrame

customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Locksmith Password Manager")
        self.minsize(900, 500)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Set the app's icon
        icon = PhotoImage(file="./assets/app_icon.png")
        self.wm_iconphoto(True, icon)

        # header
        self.header = HeaderFrame(self)
        self.header.grid(row=0, column=0, sticky="ew")

        # Body
        self.body = customtkinter.CTkFrame(self)
        self.body.grid(row=1, column=0, sticky="nsew")


app = App()
app.mainloop()

# Got icon from https://icons8.com/icon/15437/lock