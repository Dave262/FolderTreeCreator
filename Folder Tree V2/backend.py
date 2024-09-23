import os
from tkinter import messagebox, filedialog

DirPath = ""

def user_select_dir():
    global DirPath
    DirPath = filedialog.askdirectory(initialdir="/home", title="please select a directory for your folder tree")
    if DirPath:
        print(f"The directory has been set to: {DirPath}")
    else:
        print("No directory selected")
    return DirPath

def create_folders(projectinput, daily_name, days_number_input, bodypack_name, optional_folder_name, talent_folder):
    global DirPath
    if not projectinput or not daily_name or not days_number_input or not bodypack_name or not optional_folder_name or not talent_folder:
        messagebox.showerror("Input Error, please fill in all fields")
        return
    
    try:
        days = int(days_number_input)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of days")
        return
    
    names = [name.strip() for name in talent_folder.split(',')]
    # bodypack_name = "Bodypack Recorders"

    top_folder = os.path.join(DirPath, projectinput)

    try:
        os.makedirs(top_folder)
        print(f"Created top level folder: {projectinput}")
    except FileExistsError:
        messagebox.showwarning(f"Top Level Folder'{projectinput}' already exists")
        return
    
    for number in range(1, days + 1):
        daily_folder = f"Day_{number}"
        daily_folder_path = os.path.join(top_folder, daily_folder)
    
        try:
            os.makedirs(daily_folder_path)
            print(f"Created folder: {daily_folder}")
        
            bodypack_path = os.path.join(daily_folder_path, bodypack_name)
            os.makedirs(bodypack_path)
            print(f"Created folder: {daily_folder}:{bodypack_name}")
            
            if optional_folder_name:
                optional_folder_path = os.path.join(daily_folder_path, optional_folder_name)
                os.makedirs(optional_folder_path)
                print(f"Created optional folder: {daily_folder}:{optional_folder_name}")


            for name in names:
                talent_folder_path = os.path.join(bodypack_path, name)
                os.makedirs(talent_folder_path)
                print(f"Created folder: {daily_folder}:{bodypack_name}:{name}")
            
        except FileExistsError:
            messagebox.showwarning("Folder Exists", f"Folder '{daily_folder_path}' already exists")

    messagebox.showinfo("Success", "Folders created successfully")
