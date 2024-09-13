import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from tkinter import filedialog

# Function to create folders based on user input

def open_file():
    filepath = filedialog.askdirectory(initialdir="/", title="Select a File")
    print(filepath)

def create_folders(top_folder, days, talent_names):
    if not talent_names or not top_folder:
        messagebox.showerror("Input Error, please fill in all fields")
        return

    # Get user input for days
    try:
        days = int(days)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of days")
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



