import customtkinter as ctk


class InputField(ctk.CTkFrame):
    def __init__(self, master, label, text_var, **kwargs):
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

        field_entry = ctk.CTkEntry(
            self,
            corner_radius=0,
            fg_color="#B6B6B6",
            text_color="#000000",
            font=ctk.CTkFont(family="Inter", size=16),
            textvariable=text_var,
            height=40,
        )

        field_label.grid(row=0, column=0, sticky="ew", pady=(0, 2))
        field_entry.grid(row=1, column=0, sticky="ew", pady=(2, 0))
