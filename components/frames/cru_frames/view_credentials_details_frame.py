import customtkinter as ctk

from backend.models import LoginItemModel
from components.buttons.button import Button
from components.frames.cru_frames.components.input_field import InputField


class ViewCredentialsDetailsFrame(ctk.CTkFrame):
    def __init__(self, master, item: LoginItemModel, **kwargs):
        super().__init__(master, **kwargs)

        login_item_data = item.get_decrypted_data()
        self.form_data = {
            "login": {
                "name": ctk.StringVar(value=login_item_data["name"]),
                "username": ctk.StringVar(value=login_item_data["username"]),
                "password": ctk.StringVar(value=login_item_data["password"]),
            }
        }
        self.password_switch_var = ctk.StringVar(value="off")

        # Configurations
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="VIEW ITEM DETAILS",
            font=ctk.CTkFont(family="Arial", size=28),
        )
        self.title_label.grid(row=0, column=0, sticky="ew", padx=16, pady=(32, 16))

        # ----------------- Login Credentials Form
        self.login_form_frame = ctk.CTkFrame(self, fg_color="#B6B6B6", corner_radius=2)
        self.login_form_frame.grid_columnconfigure(0, weight=1)

        credentials_name_input_field = InputField(
            self.login_form_frame,
            "Name*",
            text_var=self.form_data["login"]["name"],
            is_readonly=True,
        )

        username_input_field = InputField(
            self.login_form_frame,
            "Username*",
            text_var=self.form_data["login"]["username"],
            is_readonly=True,
        )

        self.password_input_field = InputField(
            self.login_form_frame,
            "Password",
            text_var=self.form_data["login"]["password"],
            is_readonly=True,
        )
        self.password_input_field.field_entry.configure(show="*")

        show_password_switch = ctk.CTkSwitch(
            self.login_form_frame,
            text="Show password",
            variable=self.password_switch_var,
            onvalue="on",
            offvalue="off",
            text_color="#000000",
            command=self.show_password,
        )

        self.login_form_error_label = ctk.CTkLabel(
            self.login_form_frame,
            text="",
            fg_color="transparent",
            text_color="#C92929",
        )

        edit_credentials_button = Button(
            self.login_form_frame,
            text="Edit",
            corner_radius=2,
            font=ctk.CTkFont(family="Inter", size=16),
            height=45,
            command=self.update_login_credentials,
        )

        softdelete_credentials_button = Button(
            self.login_form_frame,
            text="Move to Bin",
            corner_radius=2,
            font=ctk.CTkFont(family="Inter", size=16),
            height=45,
            command=self.move_to_bin,
        )

        # Grid placement for login credentials form items
        self.login_form_frame.grid(row=2, column=0, sticky="ew", padx=32, pady=(0, 16))

        credentials_name_input_field.grid(row=0, column=0, sticky="ew", padx=6, pady=4)
        username_input_field.grid(row=1, column=0, sticky="ew", padx=6, pady=4)
        self.password_input_field.grid(
            row=2, column=0, sticky="ew", padx=6, pady=(4, 0)
        )
        show_password_switch.grid(row=3, column=0, sticky="w", padx=6)
        self.login_form_error_label.grid(row=4, column=0, sticky="w", padx=6)
        edit_credentials_button.grid(row=5, column=0, sticky="ew", padx=6, pady=(0, 6))
        softdelete_credentials_button.grid(
            row=6, column=0, sticky="ew", padx=6, pady=(0, 6)
        )

    def update_login_credentials(self):
        print("Updating Login Credentials")

    def move_to_bin(self):
        print("Moving to bin")

    def show_password(self):
        if self.password_switch_var.get() == "on":
            self.password_input_field.field_entry.configure(show="")
        else:
            self.password_input_field.field_entry.configure(show="*")
