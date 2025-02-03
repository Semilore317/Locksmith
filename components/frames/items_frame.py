import customtkinter as ctk
from backend.models import LoginItemModel, NoteItemModel
from components.frames.items_frames.all_items_frame import AllItemsFrame
from components.frames.items_frames.bin_items_frame import BinItemsFrame
from components.frames.items_frames.logins_frame import LoginItemsFrame
from components.frames.items_frames.notes_frame import NoteItemsFrame
from components.frames.items_frames.search_results_frame import SearchResultsFrame


class ItemsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, controllers, **kwargs):
        super().__init__(master, **kwargs)

        self.controllers = controllers
        # Configurations
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.configure(fg_color="#2F2F2F")

        # Show all items by default
        self.current_frame = AllItemsFrame(
            self, fg_color="transparent", controllers=self.controllers
        )
        self.current_frame.grid(row=0, column=0, sticky="nsew", padx=6, pady=6)

    def __switch_frame(self, frame: ctk.CTkFrame, **kwargs):
        self.current_frame.destroy()
        self.current_frame = frame(
            self, fg_color="transparent", controllers=self.controllers, **kwargs
        )
        self.current_frame.grid(row=0, column=0, sticky="nsew", padx=6, pady=6)

    # Move these controllers to main.py
    def show_all_items(self):
        self.__switch_frame(AllItemsFrame)

    def show_bin_items(self):
        self.__switch_frame(BinItemsFrame)

    def show_logins(self):
        self.__switch_frame(LoginItemsFrame)

    def show_secure_notes(self):
        self.__switch_frame(NoteItemsFrame)

    def show_search_results(self, results: list[LoginItemModel | NoteItemModel]):
        self.__switch_frame(SearchResultsFrame, search_results=results)
