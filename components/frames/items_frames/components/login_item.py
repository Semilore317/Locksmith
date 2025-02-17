import customtkinter as ctk

from backend.models import LoginItemModel


class LoginItem(ctk.CTkFrame):
    def __init__(self, master, login_data: LoginItemModel, controllers, **kwargs):
        super().__init__(master, **kwargs)

        # Configurations
        self.configure(fg_color="#464646")
        self.grid_columnconfigure((0, 1), weight=1)

        # Frame for showing the name and username
        data_frame = ctk.CTkFrame(self, fg_color="transparent")
        name_label = ctk.CTkLabel(
            data_frame,
            text=login_data.name,
            font=ctk.CTkFont(family="Inter", weight="bold", size=16),
        )
        username_label = ctk.CTkLabel(
            data_frame,
            text=login_data.username,
            text_color="#D7D7D7",
            font=ctk.CTkFont(family="Inter", size=14),
        )

        data_frame.grid(row=0, column=0, sticky="w", padx=(10, 0), pady=10)
        name_label.grid(row=0, column=0, sticky="w")
        username_label.grid(row=1, column=0, sticky="w")

        # Button for viewing the full details of the login item
        view_details_button = ctk.CTkButton(
            self,
            text="View details",
            fg_color="#222222",
            hover_color="#383838",
            font=ctk.CTkFont(family="Inter", size=16),
            command=lambda: controllers["view_item_details"](login_data),
        )
        view_details_button.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="nse")
