# CUR - Create, Update, Read
import customtkinter as ctk


class CRUFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configurations
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="#464646")
