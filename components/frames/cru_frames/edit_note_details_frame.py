import customtkinter as ctk

from backend.models import NoteItemModel
from backend.storage import delete_permanently, update_item
from components.buttons.button import Button
from components.frames.cru_frames.components.input_field import InputField
from components.frames.cru_frames.components.textbox_field import TextboxField


class EditNoteDetailsFrame(ctk.CTkFrame):
    def __init__(self, master, item: NoteItemModel, event_handlers, **kwargs):
        super().__init__(master, **kwargs)

        self.item = item
        self.on_update_event = event_handlers["on_update"]
        self.on_cancel_event = event_handlers["on_cancel"]

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
        )

        self.content_textbox_field = TextboxField(
            self.note_form_frame,
            label="Content*",
        )
        self.content_textbox_field.field_textbox.insert("0.0", note_item_data["note"])

        self.note_form_error_label = ctk.CTkLabel(
            self.note_form_frame,
            text="",
            fg_color="transparent",
            text_color="#C92929",
        )

        update_btn = Button(
            self.note_form_frame,
            text="Update",
            corner_radius=2,
            font=ctk.CTkFont(family="Inter", size=16),
            height=45,
            command=self.update_note,
        )

        cancel_update_btn = ctk.CTkButton(
            self.note_form_frame,
            text="Cancel",
            corner_radius=2,
            font=ctk.CTkFont(family="Inter", size=16),
            height=45,
            fg_color="#761E1E",
            hover_color="#631A1A",
            command=lambda: self.on_cancel_event(self.item),
        )

        # Grid placement for secure note form items
        self.note_form_frame.grid(row=2, column=0, sticky="ew", padx=32, pady=(0, 16))
        note_name_input_field.grid(row=0, column=0, sticky="ew", padx=6, pady=4)
        self.content_textbox_field.grid(
            row=1, column=0, sticky="ew", padx=6, pady=(4, 0)
        )
        self.note_form_error_label.grid(row=2, column=0, sticky="w", padx=6)
        update_btn.grid(row=3, column=0, sticky="ew", padx=6, pady=(0, 6))
        cancel_update_btn.grid(row=4, column=0, sticky="ew", padx=6, pady=(0, 6))

    def __notify_about_errors(self, message):
        self.note_form_error_label.configure(text=message)
        self.after(3000, lambda: self.note_form_error_label.configure(text=""))

    def get_form_values(self):
        name = self.form_data["note"]["name"].get().strip()
        content = self.content_textbox_field.get_content().strip()
        return {"name": name, "note": content}

    def update_note(self):
        # Validate the inputs, show error if not valid
        # Save if all inputs are valid
        form_values = self.get_form_values()
        inputs_are_valid = True

        if len(form_values["name"]) == 0 or len(form_values["note"]) == 0:
            inputs_are_valid = False

        if inputs_are_valid:
            try:
                update_item(self.item.id, form_values)
                self.on_update_event()
            except Exception as e:
                self.__notify_about_errors("login", f"Error updating note: {e}")
        else:
            # Show errors in the form
            self.__notify_about_errors("login", "Name and Content are required fields.")

    def move_to_bin(self):
        try:
            update_item(self.item.id, {"is_in_bin": True})
            self.on_update_event()
        except Exception as e:
            self.__notify_about_errors(f"Failed to move item to bin: {e}")

    def delete_permanently(self):
        try:
            delete_permanently(self.item.id)
            self.on_delete_event()
        except Exception as e:
            self.__notify_about_errors(f"Failed to delete item: {e}")
