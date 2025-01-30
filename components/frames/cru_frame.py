# CUR - Create, Update, Read
import customtkinter as ctk

from components.frames.cur_frames.add_login_frame import AddLoginCredentialsFrame
from components.frames.cur_frames.add_note_frame import AddNotesFrame


class CRUFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configurations
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="#464646")

        # Show add login credentials frame by default
        self.current_frame = AddLoginCredentialsFrame(self, fg_color="transparent")
        self.current_frame.grid(row=0, column=0)

    def __switch_frame(self, frame: ctk.CTkFrame):
        self.current_frame.destroy()
        self.current_frame = frame(self, fg_color="transparent")
        self.current_frame.grid(row=0, column=0)

    def show_add_login_frame(self):
        self.__switch_frame(AddLoginCredentialsFrame)

    def show_add_notes_frame(self):
        self.__switch_frame(AddNotesFrame)
