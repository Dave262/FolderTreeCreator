import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from tkinter import filedialog

#Global variable to store the selected directory
parent_directory = ""

def open_file():
    global parent_directory
    selected_directory = filedialog.askdirectory(initialdir="/home", title="Select a Parent Directory")
    if selected_directory:
        parent_directory = selected_directory
        print(f"Parent directory set to: {parent_directory}")
    else:
        print("No fucking directories")
    return parent_directory

def create_folders(top_folder_name, days, talent_names):
    global parent_directory
    if not talent_names or not parent_directory:
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


# Create the top level folder

    top_folder_path = os.path.join(parent_directory, top_folder_name)
    
    try:
        os.makedirs(top_folder_path)
        print(f"Created top level folder: {top_folder_name}")
    except FileExistsError:
        messagebox.showwarning("Folder Exists", f"Top Level Folder'{top_folder_name}' already exists")
        return

# Create the rest of the fodler structure
    for i in range(1, days + 1):
        daily_folder = f"Day_{i}"
        path = os.path.join(top_folder_path, daily_folder)

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



