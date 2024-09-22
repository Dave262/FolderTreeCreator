import customtkinter as ctk
from tkinter import messagebox
from BackendScript import create_folders, open_file, parent_directory

# Initialize the app window using customtkinter
ctk.set_appearance_mode("dark")  # Can be "light" or "dark"
ctk.set_default_color_theme("green")  # You can set different color themes here
app = ctk.CTk()  # Create the main window
app.geometry("700x450")
app.title("AGH Folder Maker")

# Add the main label
label = ctk.CTkLabel(app, text="AGH Folder Maker", font=("Inclusive Sans", 30, "bold"))
label.pack(pady=20)

# Add the chosen directory label
directory_label = ctk.CTkLabel(app, text="Select a directory", font=("Inclusive Sans", 15, "bold"))
directory_label.pack(pady=10, side="bottom")

# Input Field for Top Folder
name_frame = ctk.CTkFrame(app)
name_frame.pack(pady=15, padx=10, fill="x")
ctk.CTkLabel(name_frame, text="What's the Top level folder called?").pack(side="left", padx=5)
top_entry = ctk.CTkEntry(name_frame)
top_entry.pack(side="left", fill="x", expand=True, padx=5)

# Input Field for Number of Days
days_frame = ctk.CTkFrame(app)
days_frame.pack(pady=15, padx=10, fill="x")
ctk.CTkLabel(days_frame, text="How many days are you shooting for?").pack(side="left", padx=5)
days_entry = ctk.CTkEntry(days_frame)
days_entry.pack(side="left", fill="x", expand=True, padx=5)

# Input Field for Talent Names
talent_frame = ctk.CTkFrame(app)
talent_frame.pack(pady=15, padx=10, fill="x")
ctk.CTkLabel(talent_frame, text="What are the talent names? (comma separated)").pack(side="left", padx=5)
talent_entry = ctk.CTkEntry(talent_frame)
talent_entry.pack(side="left", fill="x", expand=True, padx=5)

# Update the directory label with the selected directory
def update_directory_label():
    print(f"Updating label with: {parent_directory}")
    directory_label.configure(text=f"Selected: {parent_directory}")
    app.update_idletasks()

# Handle folder selection and update the directory label
def on_choose_folder():
    global parent_directory
    parent_directory = open_file()
    update_directory_label()
    app.update_idletasks()

# Submit function to trigger folder creation
def on_submit():
    top_folder = top_entry.get()
    days = days_entry.get()
    talent_names = talent_entry.get()
    create_folders(top_folder, days, talent_names)

# Choose directory button
directory_button = ctk.CTkButton(app, text="Choose Directory", command=on_choose_folder)
directory_button.pack(side="left", padx=80, pady=10)

# Submit Button to trigger folder creation
submit_button = ctk.CTkButton(app, text="Create Folders", command=on_submit)
submit_button.pack(side="right", padx=80, pady=10)

# Start the main loop
app.mainloop()
