import os
import ttkbootstrap as ttk
import tkinter as tk
from tkinter import messagebox

# Function to create folders based on user input
def create_folders():
    # Get user input
    top_folder = top_entry.get()
    try:
        days = int(days_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of days")
        return

    talent_names = talent_entry.get()
    if not talent_names or not top_folder:
        messagebox.showerror("Input Error", "Please fill in all fields")
        return

    names = [name.strip() for name in talent_names.split(',')]
    string2 = "Bodypack Recorders"

    # Create folders
    for i in range(1, days + 1):
        daily_folder = f"Day_{i}"
        path = os.path.join(top_folder, daily_folder)

        try:
            os.makedirs(path)
            print(f"Created folder: {daily_folder}")

            bodypack_path = os.path.join(path, string2)
            os.makedirs(bodypack_path)
            print(f"Created folder: {daily_folder}:{string2}")

            for name in names:
                subfolder_path = os.path.join(bodypack_path, name)
                os.makedirs(subfolder_path)
                print(f"Created folder: {daily_folder}:{string2}:{name}")

        except FileExistsError:
            messagebox.showwarning("Folder Exists", f"Folder '{path}' already exists")

    messagebox.showinfo("Success", "Folders created successfully")

# Initialize the app window with ttkbootstrap's 'darkly' theme
app = ttk.Window(themename="superhero")
app.geometry("800x300")
app.title("Folder Structure Creator")

# Add the main label
label = ttk.Label(app, text="Folder Structure Creator")
label.config(font=("Arial", 20, "bold"))
label.pack(pady=20)

# Input Field for Top Folder
name_frame = ttk.Frame(app)
name_frame.pack(pady=15, padx=10, fill="x")
ttk.Label(name_frame, text="What's the Top level folder called?").pack(side="left", padx=5)
top_entry = ttk.Entry(name_frame)
top_entry.pack(side="left", fill="x", expand=True, padx=5)

# Input Field for Number of Days
days_frame = ttk.Frame(app)
days_frame.pack(pady=15, padx=10, fill="x")
ttk.Label(days_frame, text="How many days are you shooting for?").pack(side="left", padx=5)
days_entry = ttk.Entry(days_frame)
days_entry.pack(side="left", fill="x", expand=True, padx=5)

# Input Field for Talent Names
talent_frame = ttk.Frame(app)
talent_frame.pack(pady=15, padx=10, fill="x")
ttk.Label(talent_frame, text="What are the talent names? (comma separated)").pack(side="left", padx=5)
talent_entry = ttk.Entry(talent_frame)
talent_entry.pack(side="left", fill="x", expand=True, padx=5)

# Submit Button to trigger folder creation
submit_button = ttk.Button(app, text="Create Folders", command=create_folders)
submit_button.pack(pady=20)

app.mainloop()

