import zipfile
import tkinter as tk
import customtkinter

# Basic theming
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("600x600")
root.title("ZipWizard!")
root.resizable(width=False, height=False)

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Welcome-label
welcomeLabel = customtkinter.CTkLabel(master=frame, text="Welcome to ZipWizard!", font=("Roboto", 40))
welcomeLabel.pack(padx=10, pady=10, fill="both", expand=True)

# Select Operation Label
selectionLabel = customtkinter.CTkLabel(master=frame, text="Select Operation", font=("Roboto", 20))
selectionLabel.pack(padx=10, pady=10, fill="both", expand=True)

# Create a multi-stage app with buttons
buttonFrame = customtkinter.CTkFrame(master=frame)
buttonFrame.pack(padx=10, pady=10, fill="both", expand=True)

# Inner frame to center the buttons
innerButtonFrame = customtkinter.CTkFrame(master=buttonFrame)
innerButtonFrame.pack(expand=True)

# Buttons for "Zip" and "Unzip"
zipButton = customtkinter.CTkButton(master=innerButtonFrame, text="Zip", font=("Roboto", 20))
zipButton.grid(row=0, column=0, padx=10, pady=10)

unzipButton = customtkinter.CTkButton(master=innerButtonFrame, text="Unzip", font=("Roboto", 20))
unzipButton.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()