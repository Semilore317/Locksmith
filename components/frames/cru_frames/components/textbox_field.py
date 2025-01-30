import customtkinter as ctk


class TextboxField(ctk.CTkFrame):
    def __init__(self, master, label, **kwargs):
        super().__init__(master, **kwargs)

        # Configurations
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="transparent")

        field_label = ctk.CTkLabel(
            self,
            text=label,
            text_color="#000000",
            anchor="w",
            font=ctk.CTkFont(family="Arial", size=16),
        )

        field_textbox = ctk.CTkTextbox(
            self,
            corner_radius=0,
            fg_color="#B6B6B6",
            text_color="#000000",
            font=ctk.CTkFont(family="Inter", size=16),
            height=100,
            border_width=2,
            border_color="#565B5E",
        )

        field_label.grid(row=0, column=0, sticky="ew", pady=(0, 2))
        field_textbox.grid(row=1, column=0, sticky="ew", pady=(2, 0))
