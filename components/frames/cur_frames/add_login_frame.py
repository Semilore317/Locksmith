import customtkinter as ctk


class AddLoginCredentialsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        title_label = ctk.CTkLabel(
            self,
            text="ADD LOGIN CREDENTIALS",
            font=ctk.CTkFont(family="Arial", size=32),
        )
        title_label.grid(row=0, column=0, sticky="ew", padx=16, pady=(32, 0))
