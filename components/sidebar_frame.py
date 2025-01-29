import customtkinter as ctk

class SidebarFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Define a smaller font size for the buttons
        button_font = ctk.CTkFont(size=14, weight="bold")

        # All Items Button
        all_items_button = ctk.CTkButton(
            self, text="All Items", width=120, height=36, corner_radius=8, font=button_font
        )
        # Bin Button
        bin_button = ctk.CTkButton(
            self, text="Bin", width=120, height=36, corner_radius=8, font=button_font
        )
        # Section Label ("Types")
        types_label = ctk.CTkLabel(
            self, text="Types", font=ctk.CTkFont(size=24, weight="bold"), anchor="w", padx=100
        )
        # Login Button
        login_button = ctk.CTkButton(
            self, text="Login", width=120, height=36, corner_radius=8, font=button_font
        )
        # Secure Note Button
        secure_note_button = ctk.CTkButton(
            self, text="Secure Note", width=120, height=36, corner_radius=8, font=button_font
        )

        # Layout the elements with reduced padding and width
        all_items_button.grid(row=1, column=0, pady=(30, 10), padx=15)
        bin_button.grid(row=2, column=0, pady=(30, 20), padx=15)
        types_label.grid(row=3, column=0, pady=(30, 10), padx=15, sticky="w")
        login_button.grid(row=4, column=0, pady=(30, 10), padx=15)
        secure_note_button.grid(row=5, column=0, pady=(30, 20), padx=15)

        # Configure extra row for spacing if needed
        self.grid_rowconfigure(5, weight=1)

        # Optionally, you can set the width of the SidebarFrame itself
        self.grid_columnconfigure(0, weight=1)
        self.configure(width=180)  # Adjust this to control the width of the frame