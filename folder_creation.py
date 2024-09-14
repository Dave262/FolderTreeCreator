import os
from tkinter import messagebox, filedialog


#Global variable to pass to the AppInterface script
parent_directory = ""

#set the directory where the folders will be credated

def open_file():
    global parent_directory #this means the parent_directory variables are NOT local to the function but reference the global variable
    parent_directory = filedialog.askdirectory(initialdir="/home", title="Select a Parent Directory")
    print(f"Parent directory set to: {parent_directory}")
    if parent_directory:
        print(f"Parent directory set to: {parent_directory}")
    else:
        print("No Directory")
    return parent_directory # this passes the variable after exiting the function and lets the app update the label with the directory
    


def create_folders(top_folder_name, days, talent_names):
    global parent_directory
    if not top_folder_name or not days or not talent_names:
        messagebox.showerror("Input Error, please fill in all fields")
        return

# Get user input for days and show error if they dont enter a valid input 
    try:
        days = int(days)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of days")
        return
    
# create list from the comma seaprated names entered
    names = [name.strip() for name in talent_names.split(',')]
    BodypackName = "Bodypack Recorders"

# Create the top level folder
    top_folder_path = os.path.join(parent_directory, top_folder_name)   
    try:
        os.makedirs(top_folder_path)
        print(f"Created top level folder: {top_folder_name}")
    except FileExistsError:
        messagebox.showwarning("Folder Exists", f"Top Level Folder'{top_folder_name}' already exists")
        return

# Create the rest of the fodler structure in a loop inside daily folders
    for number in range(1, days + 1):
        daily_folder = f"Day_{number}"
        subfolder_path = os.path.join(top_folder_path, daily_folder)

        try:
# daily folders
            os.makedirs(subfolder_path)
            print(f"Created folder: {daily_folder}")

# bodypack recorder folder
            bodypack_path = os.path.join(subfolder_path, BodypackName)
            os.makedirs(bodypack_path)
            print(f"Created folder: {daily_folder}:{BodypackName}")
# talent name folders
            for name in names:
                talent_folder_path = os.path.join(bodypack_path, name)
                os.makedirs(talent_folder_path)
                print(f"Created folder: {daily_folder}:{BodypackName}:{name}")

        except FileExistsError:
            messagebox.showwarning("Folder Exists", f"Folder '{subfolder_path}' already exists")

    messagebox.showinfo("Success", "Folders created successfully")