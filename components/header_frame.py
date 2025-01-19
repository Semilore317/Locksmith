import customtkinter

class HeaderFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        search_bar = customtkinter.CTkEntry(
            master=self, placeholder_text="Search by Username or Website", width=300
        )
        search_bar.grid(row=0, column=0, padx=10, pady=10)
