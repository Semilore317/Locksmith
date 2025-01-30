import customtkinter as ctk


class NoteItemsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        title_label = ctk.CTkLabel(
            self,
            text="Secure Notes",
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
        )
        title_label.grid(row=0, column=0, sticky="ew")

        # Retrieve items and display them sorted by timestamp - descending order
        all_items = []
        if len(all_items) > 0:
            # If items are found, display them
            pass
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
