import customtkinter as ctk

from backend.models import NoteItemModel


class NoteItem(ctk.CTkFrame):
    def __init__(self, master, note_data: NoteItemModel, controllers, **kwargs):
        super().__init__(master, **kwargs)

        # Configurations
        self.configure(fg_color="#464646")
        self.grid_columnconfigure((0, 1), weight=1)

        name_label = ctk.CTkLabel(
            self,
            text=note_data.name,
            font=ctk.CTkFont(family="Inter", weight="bold", size=16),
        )
        name_label.grid(row=0, column=0, sticky="w", padx=(10, 0), pady=10)

        # Button for viewing the full details of the note item
        view_details_button = ctk.CTkButton(
            self,
            text="View details",
            fg_color="#222222",
            hover_color="#383838",
            font=ctk.CTkFont(family="Inter", size=16),
            command=lambda: controllers["view_item_details"](note_data),
        )
        view_details_button.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="nse")
