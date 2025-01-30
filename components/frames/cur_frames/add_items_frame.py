import customtkinter as ctk

from components.buttons.button import Button
from components.frames.cur_frames.components.input_field import InputField
from components.frames.cur_frames.components.textbox_field import TextboxField


class AddItemsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.form_data = {
            "login": {
                "name": ctk.StringVar(),
                "username": ctk.StringVar(),
                "password": ctk.StringVar(),
            },
            "note": {
                "name": ctk.StringVar(),
            },
        }

        # Configurations
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
        select_item_type_label.grid(row=0, column=0, sticky="ew", padx=6, pady=(4, 2))
        options_menu_frame.grid(row=1, column=0, sticky="ew", padx=6, pady=(0, 4))
        item_type_options_menu.grid(row=0, column=0, sticky="ew", padx=(2, 3), pady=2)
        # --------------------------------------------------------------------------

        # ----------------- Login Credentials Form
        self.add_login_form_frame = ctk.CTkFrame(
            self, fg_color="#B6B6B6", corner_radius=2
        )
        self.add_login_form_frame.grid_columnconfigure(0, weight=1)

        credentials_name_input_field = InputField(
            self.add_login_form_frame,
            "Name",
            text_var=self.form_data["login"]["name"],
        )

        username_input_field = InputField(
            self.add_login_form_frame,
            "Username",
            text_var=self.form_data["login"]["username"],
        )

        password_input_field = InputField(
            self.add_login_form_frame,
            "Password",
            text_var=self.form_data["login"]["password"],
        )

        save_credentials_button = Button(
            self.add_login_form_frame,
            text="Save",
            corner_radius=2,
            font=ctk.CTkFont(family="Inter", size=16),
            height=45,
        )

        # Grid placement for login credentials form items
        credentials_name_input_field.grid(row=0, column=0, sticky="ew", padx=6, pady=4)
        username_input_field.grid(row=1, column=0, sticky="ew", padx=6, pady=4)
        password_input_field.grid(row=2, column=0, sticky="ew", padx=6, pady=4)
        save_credentials_button.grid(row=3, column=0, sticky="ew", padx=6, pady=6)
        # --------------------------------------------------------------------------

        # ----------------- Secure Note Form
        self.add_note_form_frame = ctk.CTkFrame(
            self, fg_color="#B6B6B6", corner_radius=2
        )
        self.add_note_form_frame.grid_columnconfigure(0, weight=1)

        note_name_input_field = InputField(
            self.add_note_form_frame,
            label="Name",
            text_var=self.form_data["note"]["name"],
        )

        content_textbox_field = TextboxField(
            self.add_note_form_frame,
            label="Content",
        )

        save_note_button = Button(
            self.add_note_form_frame,
            text="Save",
            corner_radius=2,
            font=ctk.CTkFont(family="Inter", size=16),
            height=45,
        )

        # Grid placement for secure note form items
        note_name_input_field.grid(row=0, column=0, sticky="ew", padx=6, pady=4)
        content_textbox_field.grid(row=1, column=0, sticky="ew", padx=6, pady=4)
        save_note_button.grid(row=2, column=0, sticky="ew", padx=6, pady=6)
        # --------------------------------------------------------------------------
        self.current_form = self.add_login_form_frame
        self.current_form.grid(row=2, column=0, sticky="ew", padx=32, pady=(0, 16))

    def on_item_type_change(self, choice):
        item_type = choice.lower().replace(" ", "_")
        if item_type == "login":
            self.show_login_credentials_form()
        elif item_type == "secure_note":
            self.show_secure_note_form()
        else:
            print("Unknown type")
            # Meh, just show the default form
            self.show_login_credentials_form()

    def show_login_credentials_form(self):
        self.title_label.configure(text="ADD LOGIN CREDENTIALS")
        self.current_form.grid_forget()
        self.current_form = self.add_login_form_frame
        self.current_form.grid(row=2, column=0, sticky="ew", padx=32, pady=(0, 16))

    def show_secure_note_form(self):
        self.title_label.configure(text="ADD SECURE NOTE")
        self.current_form.grid_forget()
        self.current_form = self.add_note_form_frame
        self.current_form.grid(row=2, column=0, sticky="ew", padx=32, pady=(0, 16))
