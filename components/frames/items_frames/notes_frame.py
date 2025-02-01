import customtkinter as ctk

from backend.storage import get_items_by_type
from components.frames.items_frames.components.note_item import NoteItem


class NoteItemsFrame(ctk.CTkFrame):
    def __init__(self, master, controllers, **kwargs):
        super().__init__(master, **kwargs)

        self.controllers = controllers
        # Configurations
        self.grid_columnconfigure(0, weight=1)

        # UI Components
        title_label = ctk.CTkLabel(
            self,
            text="SECURE NOTES",
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
        )
        title_label.grid(row=0, column=0, sticky="ew")

        # Retrieve items and display them sorted by timestamp - descending order
        note_items = get_items_by_type("note")
        if len(note_items) > 0:
            # Display secure notes
            for item in note_items:
                note_item = NoteItem(self, note_data=item, controllers=self.controllers)
                note_item.grid(sticky="ew", pady=(6, 0))
        else:
            # If no items have been created, display a message saying so
            no_items_label = ctk.CTkLabel(
                self,
                text="NO NOTES",
                font=ctk.CTkFont(family="Arial", size=36, weight="bold"),
            )
            no_items_label.grid(row=1, column=0, sticky="ew", pady=(240, 0))
            desc_label = ctk.CTkLabel(
                self,
                text="You haven't saved any note",
                font=ctk.CTkFont(family="Arial", size=16),
            )
            desc_label.grid(row=2, column=0, sticky="ew", pady=(10, 0))
