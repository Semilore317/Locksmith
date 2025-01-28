import customtkinter as ctk


class SidebarFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create both button frames
        buttonFrame1 = ctk.CTkButtonFrame()
