from tkinter import PhotoImage
import customtkinter as ctk
from components.header_frame import HeaderFrame
from components.sidebar_frame import SidebarFrame
from PIL import Image

ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Locksmith Password Manager")
        # Set a fixed window size since scaling widgets in Tkinter is a pain to handle
        self.geometry("1340x710")
        self.resizable(False, False)

        # Configure grid for resizing
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Set the app's icon
        try:
            icon = PhotoImage(file="./assets/app_icon.png")
            self.wm_iconphoto(True, icon)
        except Exception as e:
            print(f"Error loading icon: {e}")

        # Header
        self.header_frame = HeaderFrame(self, fg_color="#222222")
        self.header_frame.grid(row=0, column=0, sticky="ew")

        # Body
        self.body_frame = ctk.CTkFrame(self, border_width=2)
        self.body_frame.grid(row=1, column=0, sticky="nsew")
        self.body_frame.grid_columnconfigure((1, 2), weight=3)
        self.body_frame.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar_frame = SidebarFrame(self.body_frame, fg_color="#222222", width=180)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        # Sidebar - Icon and Title
        icon_and_title_frame = ctk.CTkFrame(
            self.sidebar_frame, fg_color="transparent"
        )
        try:
            lock_image = ctk.CTkImage(
                light_image=Image.open("./assets/app_icon.png"),
                dark_image=Image.open("./assets/app_icon.png"),
                size=(48, 48),
            )
        except Exception as e:
            print(f"Error loading lock image: {e}")
            lock_image = None

        # Create image and title labels
        image_label = ctk.CTkLabel(icon_and_title_frame, image=lock_image, text="")
        title = ctk.CTkLabel(
            icon_and_title_frame,
            text="Locksmith\nPassword Manager",
            justify="left",
            font=ctk.CTkFont(family="Arial", size=18, weight="bold"),
        )

        # Layout the frame and ensure the icon and text are in the same row and next to each other
        icon_and_title_frame.grid(row=0, column=0, pady=8)
        icon_and_title_frame.grid_columnconfigure(0, weight=0)  # Prevent stretching of the columns
        icon_and_title_frame.grid_columnconfigure(1, weight=1)  # Let the text column take remaining space

        # Place image and text next to each other
        image_label.grid(row=0, column=0, padx=8)
        title.grid(row=0, column=1, padx=8,)  # Title text next to the image

app = App()
app.mainloop()