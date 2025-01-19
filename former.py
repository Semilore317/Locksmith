# TODO 1: add a functioning side bar
# TODO 2: add a functioning menu bar
# TODO 3 : add the main app GUI for creating custom fields for passwords
# TODO 4: add the file handling logic to store the passwords
# TODO 5: use cryptography module to store the credentials as hashes

from tkinter import PhotoImage
import customtkinter as ctk

# Basic theming
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("950x480")
root.title("Locksmith")
#root.resizable(width=False, height=False)

icon = PhotoImage(file="./shield.png")
root.wm_iconphoto(True, icon)

# Configure root grid to support main_frame resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=2)


# main app frame after welcome screen
main_frame = ctk.CTkFrame(master=root, width=900, height=400)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=15)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure((1,2), weight=2)

main_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")  # Show main frame

# search bar
search_bar = ctk.CTkEntry(master=main_frame, placeholder_text="Search", width=300)
search_bar.grid(row=0, column=0, columnspan=3 , padx=10, pady=10)

# menu bar
menu_bar = ctk.CTkOptionMenu(master=main_frame)
file_menu = ctk.CTkOptionMenu(master=main_frame)
action_menu = ctk.CTkOptionMenu(master=main_frame)

# subframes
subframe_left = ctk.CTkFrame(master=main_frame, corner_radius=10)
subframe_middle = ctk.CTkFrame(master=main_frame, corner_radius=10)
subframe_right = ctk.CTkFrame(master=main_frame, corner_radius=10)

# place subframes side by side
subframe_left.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
subframe_middle.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
subframe_right.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

# add labels to each subframe
label1 = ctk.CTkLabel(master=subframe_left, text="Left Frame", corner_radius=10)
label1.pack(padx=10, pady=10)

label2 = ctk.CTkLabel(master=subframe_middle, text="Middle Frame", corner_radius=10)
label2.pack(padx=10, pady=10)

label3 = ctk.CTkLabel(master=subframe_right, text="Right Frame", corner_radius=10)
label3.pack(padx=10, pady=10)

root.mainloop()

#attribution: https://www.flaticon.com/free-icons/security" Security icons by flaticon.com