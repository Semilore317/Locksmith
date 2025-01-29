import customtkinter as ctk


class Button(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configure the button's appearance
        self.configure(fg_color="#464646", hover_color="#383838")
