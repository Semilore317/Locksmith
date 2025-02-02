import customtkinter as ctk

from backend.models import LoginItemModel
from backend.storage import delete_permanently, update_item
from components.buttons.button import Button
from components.frames.cru_frames.components.input_field import InputField


class ViewCredentialsDetailsFrame(ctk.CTkFrame):
    def __init__(self, master, item: LoginItemModel, event_handlers, **kwargs):
        super().__init__(master, **kwargs)

        self.item = item
        self.on_update_event = event_handlers["on_update"]
        self.on_delete_event = event_handlers["on_delete"]

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

        self.delete_btn = ctk.CTkButton(
            self.login_form_frame,
            text="Move to Bin",
            corner_radius=2,
            font=ctk.CTkFont(family="Inter", size=16),
            height=45,
            fg_color="#761E1E",
            hover_color="#631A1A",
            command=self.move_to_bin,
        )

        if self.item.is_in_bin:
            self.delete_btn = ctk.CTkButton(
                self.login_form_frame,
                text="Delete Permanently",
                corner_radius=2,
                font=ctk.CTkFont(family="Inter", size=16),
                height=45,
                fg_color="#761E1E",
                hover_color="#631A1A",
                command=self.delete_permanently,
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
        self.delete_btn.grid(row=6, column=0, sticky="ew", padx=6, pady=(0, 6))

    def get_form_values(self):
        name = self.form_data["login"]["name"].get().strip()
        username = self.form_data["login"]["username"].get().strip()
        password = self.form_data["login"]["password"].get().strip()
        return {"name": name, "username": username, "password": password}

    def __notify_about_errors(self, message):
        self.login_form_error_label.configure(text=message)
        self.after(3000, lambda: self.login_form_error_label.configure(text=""))

    def update_login_credentials(self):
        print("Updating Login Credentials")

    def move_to_bin(self):
        try:
            update_item(self.item.id, {"is_in_bin": True})
            self.on_update_event()
        except Exception as e:
            self.__notify_about_errors(f"Failed to move item to bin: {e}")

    def delete_permanently(self):
        try:
            delete_permanently(self.item.id)
            self.on_delete_event()
        except Exception as e:
            self.__notify_about_errors(f"Failed to delete item: {e}")

    def show_password(self):
        if self.password_switch_var.get() == "on":
            self.password_input_field.field_entry.configure(show="")
        else:
            self.password_input_field.field_entry.configure(show="*")
