import customtkinter as ctk

from components.buttons.button import Button
from components.frames.cru_frames.components.input_field import InputField
from components.frames.cru_frames.components.textbox_field import TextboxField


class AddItemsFrame(ctk.CTkFrame):
    def __init__(self, master, event_handlers, **kwargs):
        super().__init__(master, **kwargs)

        self.on_save_event = event_handlers["on_save"]
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
            "Name*",
            text_var=self.form_data["login"]["name"],
        )

        username_input_field = InputField(
            self.add_login_form_frame,
            "Username*",
            text_var=self.form_data["login"]["username"],
        )

        password_input_field = InputField(
            self.add_login_form_frame,
            "Password",
            text_var=self.form_data["login"]["password"],
        )

        self.login_form_error_label = ctk.CTkLabel(
            self.add_login_form_frame,
            text="",
            fg_color="transparent",
            text_color="#000000",
        )

        save_credentials_button = Button(
            self.add_login_form_frame,
            text="Save",
            corner_radius=2,
            font=ctk.CTkFont(family="Inter", size=16),
            height=45,
            command=self.save_login_credentials,
        )

        # Grid placement for login credentials form items
        credentials_name_input_field.grid(row=0, column=0, sticky="ew", padx=6, pady=4)
        username_input_field.grid(row=1, column=0, sticky="ew", padx=6, pady=4)
        password_input_field.grid(row=2, column=0, sticky="ew", padx=6, pady=(4, 0))
        self.login_form_error_label.grid(row=3, column=0, sticky="w", padx=6)
        save_credentials_button.grid(row=4, column=0, sticky="ew", padx=6, pady=(0, 6))
        # --------------------------------------------------------------------------

        # ----------------- Secure Note Form
        self.add_note_form_frame = ctk.CTkFrame(
            self, fg_color="#B6B6B6", corner_radius=2
        )
        self.add_note_form_frame.grid_columnconfigure(0, weight=1)

        note_name_input_field = InputField(
            self.add_note_form_frame,
            label="Name*",
            text_var=self.form_data["note"]["name"],
        )

        self.content_textbox_field = TextboxField(
            self.add_note_form_frame,
            label="Content*",
        )

        self.note_form_error_label = ctk.CTkLabel(
            self.add_note_form_frame,
            text="",
            fg_color="transparent",
            text_color="#000000",
        )

        save_note_button = Button(
            self.add_note_form_frame,
            text="Save",
            corner_radius=2,
            font=ctk.CTkFont(family="Inter", size=16),
            height=45,
            command=self.save_note,
        )

        # Grid placement for secure note form items
        note_name_input_field.grid(row=0, column=0, sticky="ew", padx=6, pady=4)
        self.content_textbox_field.grid(
            row=1, column=0, sticky="ew", padx=6, pady=(4, 0)
        )
        self.note_form_error_label.grid(row=2, column=0, sticky="w", padx=6)
        save_note_button.grid(row=3, column=0, sticky="ew", padx=6, pady=(0, 6))
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

    def __notify_about_errors(self, type):
        if type == "login":
            self.login_form_error_label.configure(
                text="Name and Username are required fields."
            )
            self.after(3000, lambda: self.login_form_error_label.configure(text=""))
        elif type == "note":
            self.note_form_error_label.configure(
                text="Name and Content are required fields."
            )
            self.after(3000, lambda: self.note_form_error_label.configure(text=""))
        else:
            print("Unknown type")

    def save_login_credentials(self):
        # Validate the inputs, show error if not valid
        # Save if all inputs are valid
        name = self.form_data["login"]["name"].get().strip()
        username = self.form_data["login"]["username"].get().strip()
        password = self.form_data["login"]["password"].get().strip()
        inputs_are_valid = True

        if len(name) == 0 or len(username) == 0:
            inputs_are_valid = False

        if inputs_are_valid:
            # Save the data
            # TODO
            self.on_save_event()
        else:
            # Show errors in the form
            self.__notify_about_errors("login")

    def save_note(self):
        # Validate the inputs, show error if not valid
        # Save if all inputs are valid
        name = self.form_data["note"]["name"].get().strip()
        content = self.content_textbox_field.get_content().strip()
        inputs_are_valid = True

        if len(name) == 0 or len(content) == 0:
            inputs_are_valid = False

        if inputs_are_valid:
            # Save the data
            # TODO
            self.on_save_event()
        else:
            # Show errors in the form
            self.__notify_about_errors("note")
