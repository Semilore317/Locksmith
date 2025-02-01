from tkinter import PhotoImage
import customtkinter as ctk
from components.frames.header_frame import HeaderFrame
from components.frames.sidebar_frame import SidebarFrame
from backend.models import LoginItem, SecureNoteItem
from backend.storage import save_data, load_data, move_to_bin, delete_permanently, search_items, filter_by_type, filter_by_bin_status, return_all_items, edit_credential
from backend.utils import check_password_strength, generate_password
from PIL import Image

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

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
        self.header_frame = HeaderFrame(self, fg_color="#222222")
        self.header_frame.grid(row=0, column=0, sticky="ew")

        # Body
        self.body_frame = ctk.CTkFrame(self, border_width=2)
        self.body_frame.grid(row=1, column=0, sticky="nsew")
        self.body_frame.grid_columnconfigure((1, 2), weight=3)
        self.body_frame.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar_frame = SidebarFrame(
            self.body_frame, fg_color="#222222", width=180
        )
        self.sidebar_frame.grid_columnconfigure(0, weight=1)
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

        '''BACKEND BS & TESTING'''

        # Create sample LoginItem and SecureNoteItem objects
        login1 = LoginItem(name="nigger", username="cotton picker", _password="i_am_a_nigger")
        login2 = LoginItem(name="diddy", username="oiler", _password="oil_me_up")
        login3 = LoginItem(name="Semilore", username="semilore", _password="peekaboo")
        note1 = SecureNoteItem(name="Private Note", _note="the younger the soul...")
        note2 = SecureNoteItem(name="Another Note", _note="...the tighter the...")

        # Save data
        save_data([login1, login2, login3, note1, note2])

        # Load and print decrypted data
        loaded_data = load_data()
        for item in loaded_data:
            print(item)
            if isinstance(item, LoginItem):
                print("Decrypted Password:", item.password)
            elif isinstance(item, SecureNoteItem):
                print("Decrypted Note:", item.note)

        # Test: Move a login item to bin
        item_id = login1.id
        if move_to_bin(item_id):
            print("Item moved to bin successfully!")
        else:
            print("Item not found.")

        # Test: Permanently delete an item
        if delete_permanently(item_id):
            print("Item permanently deleted!")
        else:
            print("Item not found.")

        # Test for searching
        results = search_items("semilore")
        print("Search Results:", results)

        # Test filter by type
        logins = filter_by_type("login")
        print("Login Items:", logins)

        notes = filter_by_type("note")
        print("Secure Notes:", notes)

        # Test filtering by bin status
        move_to_bin(logins[0].id)  # Move first login item

        # Get deleted items
        deleted_items = filter_by_bin_status(True)
        print("Items in Bin:", deleted_items)

        # Test returning all items in chronological order
        return_all_items()

        # Test password strength checker
        new_password = "ffFe625abeN2N46f6e58VF81651a7392A1"
        strength = check_password_strength(new_password)

        print(f"Password strength: {strength}")

        # Test password generator
        print("Random Password is: "+generate_password())

        # Test editing existing credentials
        # Update only the password of a login item
        updated_login = edit_credential(login2.id, {"_password": "new_secure_pass"})
        print(updated_login)

        # Update both username and name of a login item
        updated_login = edit_credential(login3.id, {"username": "new_user", "name": "Updated Site"})
        print(updated_login)

        # Update note content of a secure note
        updated_note = edit_credential(note1.id, {"_note": "This is the updated content."})
        print(updated_note)

app = App()
app.mainloop()