import customtkinter as ctk
from backend.storage import search_items


class HeaderFrame(ctk.CTkFrame):
    def __init__(self, master, event_handlers, controllers, **kwargs):
        super().__init__(master, **kwargs)

        self.show_search_results = event_handlers["on_search"]
        self.show_all_items = controllers["show_all_items"]

        # Configurations
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="#222222")

        self.search_field_val = ctk.StringVar()
        search_field = ctk.CTkEntry(
            master=self,
            placeholder_text="Search by Username or Website",
            width=600,
            height=30,
            corner_radius=3,
            textvariable=self.search_field_val,
        )
        search_field.bind("<KeyPress>", self.search_for_items)
        search_field.grid(row=0, column=0, padx=10, pady=10)

    def search_for_items(self, event):
        keyword = self.search_field_val.get().strip()
        # Search only if there's a char in the input field
        if event.keysym == "Return":
            if len(keyword) > 0:
                results = search_items(keyword)
                self.show_search_results(results)
            else:
                self.show_all_items()
