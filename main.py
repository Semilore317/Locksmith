from tkinter import PhotoImage
import customtkinter as ctk
from backend.models import LoginItemModel, NoteItemModel
from components.frames.cru_frames.add_items_frame import AddItemsFrame
from components.frames.cru_frames.edit_credentials_details_frame import (
    EditCredentialsDetailsFrame,
)
from components.frames.cru_frames.edit_note_details_frame import EditNoteDetailsFrame
from components.frames.cru_frames.view_credentials_details_frame import (
    ViewCredentialsDetailsFrame,
)
from components.frames.cru_frames.view_note_details_frame import ViewNoteDetailsFrame
from components.frames.header_frame import HeaderFrame
from components.frames.sidebar_frame import SidebarFrame
from components.frames.items_frame import ItemsFrame
from PIL import Image
from backend.storage import init_appdata

ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        init_appdata()

        self.title("Locksmith Password Manager")
        # Set a fixed window size since scaling widgets in Tkinter is a pain to handle
        self.geometry("1340x710")
        self.resizable(False, False)

        # Configure grid for resizing
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Set the app's icon
        try:
            icon = PhotoImage(file="./assets/app_icon.png")
            self.wm_iconphoto(True, icon)
        except Exception as e:
            print(f"Error loading icon: {e}")

        # Header
        self.header_frame = HeaderFrame(self)
        self.header_frame.grid(row=0, column=0, sticky="ew")

        # Body
        self.body_frame = ctk.CTkFrame(self, border_width=2)
        # Body grid configuration
        self.body_frame.grid_columnconfigure((1, 2), weight=1)
        self.body_frame.grid_rowconfigure(0, weight=1)

        self.body_frame.grid(row=1, column=0, sticky="nsew")

        # Items Frame
        self.items_frame = ItemsFrame(
            self.body_frame,
            controllers={"view_item_details": self.view_item_details},
        )
        self.items_frame.grid(row=0, column=1, sticky="nsew")

        # CRU (Create, Read, Update) Frame
        self.cru_frame = ctk.CTkFrame(self.body_frame, fg_color="#464646")
        self.cru_frame.grid_columnconfigure(0, weight=1)

        add_items_frame = AddItemsFrame(
            self.cru_frame,
            fg_color="#464646",
            event_handlers={
                "on_save": self.items_frame.show_all_items,
            },
        )

        self.cru_frame.grid_propagate(False)
        add_items_frame.grid(row=0, column=0, sticky="nsew")
        self.cru_frame.grid(row=0, column=2, sticky="nsew")

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
        try:
            lock_image = ctk.CTkImage(
                light_image=Image.open("./assets/app_icon.png"),
                dark_image=Image.open("./assets/app_icon.png"),
                size=(48, 48),
            )
        except Exception as e:
            print(f"Error loading lock image: {e}")
            lock_image = None

        # Create image and title labels
        image_label = ctk.CTkLabel(icon_and_title_frame, image=lock_image, text="")
        title = ctk.CTkLabel(
            icon_and_title_frame,
            text="Locksmith\nPassword Manager",
            justify="left",
            font=ctk.CTkFont(family="Arial", size=18, weight="bold"),
        )

        # Layout the frame and ensure the icon and text are in the same row and next to each other
        icon_and_title_frame.grid(row=0, column=0, pady=8)
        # Prevent stretching of the columns
        icon_and_title_frame.grid_columnconfigure(0, weight=0)
        # Let the text column take remaining space
        icon_and_title_frame.grid_columnconfigure(1, weight=1)

        # Place image and text next to each other
        image_label.grid(row=0, column=0, padx=8)
        title.grid(
            row=0,
            column=1,
            padx=8,
        )

    def refresh(self):
        self.show_add_items_frame()
        self.items_frame.show_all_items()

    def on_delete_event(self):
        self.show_add_items_frame()
        self.items_frame.show_bin_items()

    def view_item_details(self, item_data):
        self.cru_frame.grid_remove()
        if isinstance(item_data, LoginItemModel):
            view_items_frame = ViewCredentialsDetailsFrame(
                self.cru_frame,
                fg_color="#464646",
                item=item_data,
                event_handlers={
                    "on_update": self.refresh,
                    "on_delete": self.on_delete_event,
                    "on_edit_btn_clicked": self.show_edit_items_frame,
                },
            )
            view_items_frame.grid(row=0, column=0, sticky="nsew")
        elif isinstance(item_data, NoteItemModel):
            note_details_frame = ViewNoteDetailsFrame(
                self.cru_frame,
                fg_color="#464646",
                item=item_data,
                event_handlers={
                    "on_update": self.refresh,
                    "on_delete": self.on_delete_event,
                    "on_edit_btn_clicked": self.show_edit_items_frame,
                },
            )
            note_details_frame.grid(row=0, column=0, sticky="nsew")
        self.cru_frame.grid_propagate(False)
        self.cru_frame.grid(row=0, column=2, sticky="nsew")

    def show_add_items_frame(self):
        self.cru_frame.grid_remove()
        add_items_frame = AddItemsFrame(
            self.cru_frame,
            fg_color="#464646",
            event_handlers={
                "on_save": self.items_frame.show_all_items,
            },
        )
        self.cru_frame.grid_propagate(False)
        add_items_frame.grid(row=0, column=0, sticky="nsew")
        self.cru_frame.grid(row=0, column=2, sticky="nsew")

    def show_edit_items_frame(self, item_data):
        self.cru_frame.grid_remove()
        if isinstance(item_data, LoginItemModel):
            view_items_frame = EditCredentialsDetailsFrame(
                self.cru_frame,
                fg_color="#464646",
                item=item_data,
                event_handlers={
                    "on_update": self.refresh,
                    "on_cancel": self.view_item_details,
                },
            )
            view_items_frame.grid(row=0, column=0, sticky="nsew")
        elif isinstance(item_data, NoteItemModel):
            note_details_frame = EditNoteDetailsFrame(
                self.cru_frame,
                fg_color="#464646",
                item=item_data,
                event_handlers={
                    "on_update": self.refresh,
                    "on_cancel": self.view_item_details,
                },
            )
            note_details_frame.grid(row=0, column=0, sticky="nsew")
        self.cru_frame.grid_propagate(False)
        self.cru_frame.grid(row=0, column=2, sticky="nsew")


app = App()
app.mainloop()
