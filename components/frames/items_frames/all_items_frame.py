import customtkinter as ctk
from backend.models import LoginItemModel
from backend.storage import get_items_by_bin_status
from components.frames.items_frames.components.login_item import LoginItem
from components.frames.items_frames.components.note_item import NoteItem


# This frame shows all items (passwords, secure notes, etc.)
class AllItemsFrame(ctk.CTkFrame):
    def __init__(self, master, controllers, **kwargs):
        super().__init__(master, **kwargs)

        self.controllers = controllers
        # Configurations
        self.grid_columnconfigure(0, weight=1)

        # UI Components
        title_label = ctk.CTkLabel(
            self,
            text="ALL ITEMS",
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
        )
        title_label.grid(row=0, column=0, sticky="ew")

        # Retrieve items and display them sorted by their time of creation - descending order
        all_items = get_items_by_bin_status(False)
        if len(all_items) > 0:
            for item in all_items:
                if isinstance(item, LoginItemModel):
                    # Display login items
                    login_item = LoginItem(
                        self, login_data=item, controllers=self.controllers
                    )
                    login_item.grid(sticky="ew", pady=(6, 0))
                else:
                    # Display secure notes
                    note_item = NoteItem(
                        self, note_data=item, controllers=self.controllers
                    )
                    note_item.grid(sticky="ew", pady=(6, 0))
        else:
            # If no items have been created, display a message saying so
            no_items_label = ctk.CTkLabel(
                self,
                text="NO ITEMS",
                font=ctk.CTkFont(family="Arial", size=36, weight="bold"),
            )
            no_items_label.grid(row=1, column=0, sticky="ew", pady=(240, 0))
            desc_label = ctk.CTkLabel(
                self,
                text="You haven't saved any note or login credential",
                font=ctk.CTkFont(family="Arial", size=16),
            )
            desc_label.grid(row=2, column=0, sticky="ew", pady=(10, 0))
