import customtkinter as ctk
from components.frames.all_items_frame import AllItemsFrame


class ItemsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configurations
        self.grid_columnconfigure(0, weight=1)

        self.all_items_frame = AllItemsFrame(
            self,
            fg_color="#2F2F2F",
        )
        self.all_items_frame.grid(row=0, column=0)
