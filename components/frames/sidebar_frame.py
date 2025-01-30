import customtkinter as ctk
from components.buttons.button import Button


class SidebarFrame(ctk.CTkFrame):
    def __init__(self, master, controllers, **kwargs):
        super().__init__(master, **kwargs)

        # Define some constants for the sidebar components
        self.BUTTON_WIDTH = 140
        self.BUTTON_HEIGHT = 45
        self.BUTTON_CORNER_RADIUS = 2

        # Define a smaller font size for the buttons
        button_font = ctk.CTkFont(size=14, weight="bold")

        # All Items Button
        all_items_button = Button(
            self,
            width=self.BUTTON_WIDTH,
            height=self.BUTTON_HEIGHT,
            corner_radius=self.BUTTON_CORNER_RADIUS,
            text="All Items",
            font=button_font,
            command=controllers["show_all_items"],
        )

        # Bin Button
        bin_button = Button(
            self,
            text="Bin",
            width=self.BUTTON_WIDTH,
            height=self.BUTTON_HEIGHT,
            corner_radius=self.BUTTON_CORNER_RADIUS,
            font=button_font,
            command=controllers["show_bin_items"],
        )

        # Section Label ("Types")
        types_label = ctk.CTkLabel(
            self,
            text="Types",
            font=ctk.CTkFont(size=24, weight="bold"),
            anchor="w",
            padx=100,
        )

        # Login Button
        login_button = Button(
            self,
            text="Logins",
            width=self.BUTTON_WIDTH,
            height=self.BUTTON_HEIGHT,
            corner_radius=self.BUTTON_CORNER_RADIUS,
            font=button_font,
            command=controllers["show_logins"],
        )

        # Secure Note Button
        secure_note_button = Button(
            self,
            text="Secure Notes",
            width=self.BUTTON_WIDTH,
            height=self.BUTTON_HEIGHT,
            corner_radius=self.BUTTON_CORNER_RADIUS,
            font=button_font,
            command=controllers["show_notes"],
        )

        # Layout the elements with reduced padding and width
        all_items_button.grid(row=1, column=0, pady=(30, 10))
        bin_button.grid(row=2, column=0, pady=(20, 10), padx=15)

        types_label.grid(row=3, column=0, pady=(50, 20), padx=15, sticky="w")

        login_button.grid(row=4, column=0, pady=(10, 10), padx=15)
        secure_note_button.grid(row=5, column=0, pady=(10, 20), padx=15)
