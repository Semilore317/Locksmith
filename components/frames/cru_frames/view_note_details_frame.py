import customtkinter as ctk

from backend.models import NoteItemModel
from components.buttons.button import Button
from components.frames.cru_frames.components.input_field import InputField
from components.frames.cru_frames.components.textbox_field import TextboxField


class ViewNoteDetailsFrame(ctk.CTkFrame):
    def __init__(self, master, item: NoteItemModel, **kwargs):
        super().__init__(master, **kwargs)

        note_item_data = item.get_decrypted_data()
        self.form_data = {
            "note": {
                "name": ctk.StringVar(value=note_item_data["name"]),
            },
        }

        # Configurations
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="VIEW ITEM DETAILS",
            font=ctk.CTkFont(family="Arial", size=28),
        )
        self.title_label.grid(row=0, column=0, sticky="ew", padx=16, pady=(32, 16))

        # ----------------- Secure Note Form
        self.note_form_frame = ctk.CTkFrame(self, fg_color="#B6B6B6", corner_radius=2)
        self.note_form_frame.grid_columnconfigure(0, weight=1)

        note_name_input_field = InputField(
            self.note_form_frame,
            label="Name*",
            text_var=self.form_data["note"]["name"],
            is_readonly=True,
        )

        self.content_textbox_field = TextboxField(
            self.note_form_frame,
            label="Content*",
        )
        self.content_textbox_field.field_textbox.insert("0.0", note_item_data["note"])
        self.content_textbox_field.field_textbox.configure(state="disabled")

        self.note_form_error_label = ctk.CTkLabel(
            self.note_form_frame,
            text="",
            fg_color="transparent",
            text_color="#C92929",
        )

        edit_note_button = Button(
            self.note_form_frame,
            text="Edit",
            corner_radius=2,
            font=ctk.CTkFont(family="Inter", size=16),
            height=45,
            command=self.update_note,
        )

        softdelete_note_button = Button(
            self.note_form_frame,
            text="Move to Bin",
            corner_radius=2,
            font=ctk.CTkFont(family="Inter", size=16),
            height=45,
            command=self.move_to_bin,
        )

        # Grid placement for secure note form items
        self.note_form_frame.grid(row=2, column=0, sticky="ew", padx=32, pady=(0, 16))
        note_name_input_field.grid(row=0, column=0, sticky="ew", padx=6, pady=4)
        self.content_textbox_field.grid(
            row=1, column=0, sticky="ew", padx=6, pady=(4, 0)
        )
        self.note_form_error_label.grid(row=2, column=0, sticky="w", padx=6)
        edit_note_button.grid(row=5, column=0, sticky="ew", padx=6, pady=(0, 6))
        softdelete_note_button.grid(row=6, column=0, sticky="ew", padx=6, pady=(0, 6))

    def update_note(self):
        print("Updating Login Credentials")

    def move_to_bin(self):
        print("Moving to bin")
