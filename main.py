from tkinter import PhotoImage
import customtkinter
from components.header_frame import HeaderFrame
from components.sidebar_frame import SidebarFrame
from PIL import Image

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
        self.header_frame = HeaderFrame(self, fg_color="#222222")
        self.header_frame.grid(row=0, column=0, sticky="ew")

        # Body
        self.body_frame = customtkinter.CTkFrame(self, border_width=2)
        self.body_frame.grid(row=1, column=0, sticky="nsew")
        self.body_frame.grid_columnconfigure(0, weight=1)
        self.body_frame.grid_columnconfigure((1, 2), weight=3)
        self.body_frame.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar_frame = SidebarFrame(self.body_frame, fg_color="#222222")
        self.sidebar_frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
        )
        
        # Sidebar - Icon and Title
        icon_and_title_frame = customtkinter.CTkFrame(
            self.sidebar_frame, fg_color="transparent"
        )
        lock_image = customtkinter.CTkImage(
            light_image=Image.open("./assets/app_icon.png"),
            dark_image=Image.open("./assets/app_icon.png"),
            size=(48, 48),
        )
        image_label = customtkinter.CTkLabel(
            icon_and_title_frame, image=lock_image, text=""
        )
        title = customtkinter.CTkLabel(
            icon_and_title_frame,
            text="Locksmith\nPassword Manager",
            justify="left",
            font=customtkinter.CTkFont(family="Inter", size=18, weight="bold"),
        )
        icon_and_title_frame.grid(row=0, column=0)
        image_label.grid(row=0, column=0, pady=8)
        title.grid(row=0, column=1)


app = App()
app.mainloop()

# Got icon from https://icons8.com/icon/15437/lock
