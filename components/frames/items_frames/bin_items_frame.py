import customtkinter as ctk

from backend.models import NoteItemModel
from backend.storage import get_items_by_bin_status


class BinItemsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configurations
        self.grid_columnconfigure(0, weight=1)

        # UI Components
        title_label = ctk.CTkLabel(
            self,
            text="BIN",
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
        )
        title_label.grid(row=0, column=0, sticky="ew")

        # Retrieve items and display them sorted by timestamp - descending order
        bin_items = get_items_by_bin_status()
        if len(bin_items) > 0:
            for item in bin_items:
                if isinstance(item, NoteItemModel):
                    # Display login items
                    login_item = NoteItemModel(self, login_data=item)
                    login_item.grid(sticky="ew", pady=(6, 0))
                else:
                    # Display secure notes
                    note_item = NoteItemModel(self, note_data=item, height=80)
                    note_item.grid(sticky="ew", pady=(6, 0))
        else:
            # If no items have been created, display a message saying so
            no_items_label = ctk.CTkLabel(
                self,
                text="NO ITEMS IN THE BIN",
                font=ctk.CTkFont(family="Arial", size=36, weight="bold"),
            )
            no_items_label.grid(row=1, column=0, sticky="ew", pady=(240, 0))
            desc_label = ctk.CTkLabel(
                self,
                text="You haven't moved any item to the bin",
                font=ctk.CTkFont(family="Arial", size=16),
            )
            desc_label.grid(row=2, column=0, sticky="ew", pady=(10, 0))
