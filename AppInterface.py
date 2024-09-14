import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from folder_creation import create_folders, open_file, parent_directory

# Initialize the app window with ttkbootstrap's 'superhero' theme
app = ttk.Window(themename="superhero")
app.geometry("700x450")
app.title("AGH Folder Maker")

# Add the main label
label = ttk.Label(app, text="AGH Folder Maker", style='Inverse.TLabel', bootstyle=DARK,)
label.config(font=("Inclusive Sans", 30, "bold"))
label.pack(pady=20)

#Add the chosen directory label
directory_label = ttk.Label(app, text="Select a directory")
directory_label.config(font=("Inclusive Sans", 15, "bold"))
directory_label.pack(pady=10, side="bottom")

# Input Field for Top Folder
name_frame = ttk.Frame(app)
name_frame.pack(pady=15, padx=10, fill="x")
ttk.Label(name_frame, text="What's the Top level folder called?").pack(side="left", padx=5,)
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

def update_directory_label():
# Update the directory label with the selected directory.
    print(f"Updating label with: {parent_directory}")
    directory_label.config(text=f"Selected: {parent_directory}")
    app.update_idletasks()

def on_choose_folder():
# Handle folder selection and update the directory label.
    global parent_directory
    parent_directory = open_file()
    update_directory_label()
    app.update_idletasks()

def on_submit():
    top_folder = top_entry.get()
    days = days_entry.get()
    talent_names = talent_entry.get()
    create_folders(top_folder, days, talent_names)

# Choose directory button
directory_button = ttk.Button(app, text="Choose Directory", command=on_choose_folder)
directory_button.pack(side=LEFT, padx=80, pady=10)
    
# Submit Button to trigger folder creation
submit_button = ttk.Button(app, text="Create Folders", command=on_submit)
submit_button.pack(side=RIGHT, padx=80, pady=10)

app.mainloop()
