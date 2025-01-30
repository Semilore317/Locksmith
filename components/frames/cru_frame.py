# CRU - Create, Read, Update
import customtkinter as ctk

from components.frames.cru_frames.add_items_frame import AddItemsFrame


class CRUFrame(ctk.CTkFrame):
    def __init__(self, master, event_handlers, **kwargs):
        super().__init__(master, **kwargs)

        self.event_handlers = event_handlers
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="#464646")

        # Show add items frame by default
        self.current_frame = AddItemsFrame(
            self, fg_color="transparent", event_handlers=event_handlers
        )
        self.current_frame.grid(row=0, column=0, sticky="ew")

    def __switch_frame(self, frame: ctk.CTkFrame):
        self.current_frame.destroy()
        self.current_frame = frame(
            self, fg_color="transparent", event_handlers=self.event_handlers
        )
        self.current_frame.grid(row=0, column=0)

    def show_add_items_frame(self):
        self.__switch_frame(AddItemsFrame)
