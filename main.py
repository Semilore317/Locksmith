from tkinter import PhotoImage
import customtkinter as ctk
from backend.models import LoginItemModel, NoteItemModel
from components.frames.cru_frames.add_items_frame import AddItemsFrame
from components.frames.cru_frames.edit_credentials_details_frame import EditCredentialsDetailsFrame
from components.frames.cru_frames.edit_note_details_frame import EditNoteDetailsFrame
from components.frames.cru_frames.view_credentials_details_frame import ViewCredentialsDetailsFrame
from components.frames.cru_frames.view_note_details_frame import ViewNoteDetailsFrame
from components.frames.header_frame import HeaderFrame
from components.frames.sidebar_frame import SidebarFrame
from components.frames.items_frame import ItemsFrame
from PIL import Image
from backend.storage import init_appdata
from backend.utils import resource_path

import sys
import os

ctk.set_appearance_mode("dark")


def resource_path(relative_path):
    """Get the absolute path to the resource (works for dev and for PyInstaller)."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        init_appdata()

        self.title("Locksmith Password Manager")
        self.geometry("1340x710")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Set the app's icon
        try:
            icon = PhotoImage(file=resource_path("assets/app_icon.png"))
            self.wm_iconphoto(True, icon)
        except Exception as e:
            print(f"Error loading icon: {e}")

        # Body
        self.body_frame = ctk.CTkFrame(self, border_width=2)
        self.body_frame.grid_columnconfigure((1, 2), weight=1)
        self.body_frame.grid_rowconfigure(0, weight=1)
        self.body_frame.grid(row=1, column=0, sticky="nsew")

        # Items Frame
        self.items_frame = ItemsFrame(
            self.body_frame,
            controllers={"view_item_details": self.view_item_details},
        )
        self.items_frame.grid(row=0, column=1, sticky="nsew")

        # Header with search field
        self.header_frame = HeaderFrame(
            self,
            event_handlers={"on_search": self.items_frame.show_search_results},
            controllers={"show_all_items": self.items_frame.show_all_items},
        )
        self.header_frame.grid(row=0, column=0, sticky="ew")

        # CRU Frame
        self.cru_frame = ctk.CTkFrame(self.body_frame, fg_color="#464646")
        self.cru_frame.grid_columnconfigure(0, weight=1)
        self.cru_frame.grid_propagate(False)
        self.cru_frame.grid(row=0, column=2, sticky="nsew")

        self.show_add_items_frame()

        # Sidebar
        self.sidebar_frame = SidebarFrame(
            self.body_frame,
            width=180,
            controllers={
                "show_add_items": self.show_add_items_frame,
                "show_all_items": self.items_frame.show_all_items,
                "show_bin_items": self.items_frame.show_bin_items,
                "show_logins": self.items_frame.show_logins,
                "show_notes": self.items_frame.show_secure_notes,
            },
        )
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        # Sidebar - Icon and Title
        icon_and_title_frame = ctk.CTkFrame(self.sidebar_frame, fg_color="transparent")
        icon_and_title_frame.grid(row=0, column=0, pady=8)
        icon_and_title_frame.grid_columnconfigure(0, weight=0)
        icon_and_title_frame.grid_columnconfigure(1, weight=1)

        try:
            lock_image = ctk.CTkImage(
                light_image=Image.open(resource_path("assets/app_icon.png")),
                dark_image=Image.open(resource_path("assets/app_icon.png")),
                size=(48, 48),
            )
        except Exception as e:
            print(f"Error loading lock image: {e}")
            lock_image = None

        image_label = ctk.CTkLabel(icon_and_title_frame, image=lock_image, text="")
        title = ctk.CTkLabel(
            icon_and_title_frame,
            text="Locksmith\nPassword Manager",
            justify="left",
            font=ctk.CTkFont(family="Arial", size=18, weight="bold"),
        )

        image_label.grid(row=0, column=0, padx=8)
        title.grid(row=0, column=1, padx=8)

    def refresh(self):
        self.show_add_items_frame()
        self.items_frame.show_all_items()

    def on_delete_event(self):
        self.show_add_items_frame()
        self.items_frame.show_bin_items()

    def view_item_details(self, item_data):
        self.cru_frame.grid_remove()
        if isinstance(item_data, LoginItemModel):
            view_frame = ViewCredentialsDetailsFrame(
                self.cru_frame,
                fg_color="#464646",
                item=item_data,
                event_handlers={
                    "on_update": self.refresh,
                    "on_delete": self.on_delete_event,
                    "on_edit_btn_clicked": self.show_edit_items_frame,
                },
            )
        elif isinstance(item_data, NoteItemModel):
            view_frame = ViewNoteDetailsFrame(
                self.cru_frame,
                fg_color="#464646",
                item=item_data,
                event_handlers={
                    "on_update": self.refresh,
                    "on_delete": self.on_delete_event,
                    "on_edit_btn_clicked": self.show_edit_items_frame,
                },
            )
        view_frame.grid(row=0, column=0, sticky="nsew")
        self.cru_frame.grid_propagate(False)
        self.cru_frame.grid(row=0, column=2, sticky="nsew")

    def show_add_items_frame(self):
        self.cru_frame.grid_remove()
        add_items_frame = AddItemsFrame(
            self.cru_frame,
            fg_color="#464646",
            event_handlers={"on_save": self.items_frame.show_all_items},
        )
        add_items_frame.grid(row=0, column=0, sticky="nsew")
        self.cru_frame.grid_propagate(False)
        self.cru_frame.grid(row=0, column=2, sticky="nsew")

    def show_edit_items_frame(self, item_data):
        self.cru_frame.grid_remove()
        if isinstance(item_data, LoginItemModel):
            edit_frame = EditCredentialsDetailsFrame(
                self.cru_frame,
                fg_color="#464646",
                item=item_data,
                event_handlers={
                    "on_update": self.refresh,
                    "on_cancel": self.view_item_details,
                },
            )
        elif isinstance(item_data, NoteItemModel):
            edit_frame = EditNoteDetailsFrame(
                self.cru_frame,
                fg_color="#464646",
                item=item_data,
                event_handlers={
                    "on_update": self.refresh,
                    "on_cancel": self.view_item_details,
                },
            )
        edit_frame.grid(row=0, column=0, sticky="nsew")
        self.cru_frame.grid_propagate(False)
        self.cru_frame.grid(row=0, column=2, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
