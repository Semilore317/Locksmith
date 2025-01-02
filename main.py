# TODO 1: add a functioning side bar
# TOOD 2: add a functioning menu bar 
# TODO 3 : add the main app GUI for creating custom fields for passwords
# TODO 4: add the file handling logic to store the passwords
# TODO 5: use cryptography module to store the credentials as hashes

import tkinter as tk
import customtkinter as ctk

# functions
def close_welcome_screen():
    root.destroy()  # Closes the welcome screen

# Basic theming
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("700x480")
root.title("Locksmith")
root.resizable(width=False, height=False)

frame = ctk.CTkFrame(master=root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Add content to the welcome screen
welcome_label = ctk.CTkLabel(
    root, 
    text="Welcome to My Application", 
    font=ctk.CTkFont("Arial", size=24, weight="bold")
)
welcome_label.pack(pady=100)

loading_label = ctk.CTkLabel(
    root, 
    text="Loading, please wait...", 
    font=ctk.CTkFont("Arial", size=16, weight="normal")
)
loading_label.pack(pady=10)

# Schedule the screen to close after 3 seconds (3000 milliseconds)
root.after(3000, close_welcome_screen)


root.mainloop()

# this is a comment