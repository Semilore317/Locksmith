import customtkinter as ctk


class AddItemsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="ADD LOGIN CREDENTIALS",
            font=ctk.CTkFont(family="Arial", size=28),
        )
        self.title_label.grid(row=0, column=0, sticky="ew", padx=16, pady=(32, 16))

        # ----------------- Options Menu for selecting the type of item - Note or Login
        select_item_type_frame = ctk.CTkFrame(
            self,
            fg_color="#B6B6B6",
            corner_radius=2,
        )
        select_item_type_frame.grid_columnconfigure(0, weight=1)
        select_item_type_label = ctk.CTkLabel(
            select_item_type_frame,
            text="Type",
            text_color="#000000",
            anchor="w",
            font=ctk.CTkFont(family="Arial", size=16),
        )

        # OptionMenu doesn't allow borders so I'll wrap it in a frame and add a border to the frame
        options_menu_frame = ctk.CTkFrame(
            select_item_type_frame,
            border_width=2,
            border_color="#000000",
            corner_radius=1,
            fg_color="transparent",
        )
        options_menu_frame.grid_columnconfigure(0, weight=1)

        item_type_options_menu = ctk.CTkOptionMenu(
            options_menu_frame,
            corner_radius=0,
            fg_color="#B6B6B6",
            button_color="#B6B6B6",
            button_hover_color="#AFAEAE",
            text_color="#000000",
            font=ctk.CTkFont(family="Inter", size=16),
            dropdown_font=ctk.CTkFont(family="Inter", size=16),
            values=["Login", "Secure Note"],
            command=self.on_item_type_change,
        )
        select_item_type_frame.grid(row=1, column=0, sticky="ew", padx=32, pady=(0, 16))
        select_item_type_label.grid(row=0, column=0, sticky="ew", padx=4, pady=(4, 2))
        options_menu_frame.grid(row=1, column=0, sticky="ew", padx=4, pady=(0, 4))
        item_type_options_menu.grid(row=0, column=0, sticky="ew", padx=(2, 3), pady=2)
        # --------------------------------------------------------------------------

        # ----------------- Form for the user to enter the login credentials/note

    def on_item_type_change(self, choice):
        item_type = choice.lower().replace(" ", "_")
        if item_type == "login":
            self.title_label.configure(text="ADD LOGIN CREDENTIALS")
        elif item_type == "secure_note":
            self.title_label.configure(text="ADD SECURE NOTE")
        else:
            print("Unknown type")
