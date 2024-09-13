import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from folder_creation import create_folders
from folder_creation import open_file

# Initialize the app window with ttkbootstrap's 'superhero' theme
app = ttk.Window(themename="superhero")
app.geometry("700x350")
app.title("AGH Folder Maker")

# Add the main label
label = ttk.Label(app, text="AGH Folder Maker", style='Inverse.TLabel', bootstyle=DARK,)
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
ttk.Label(days_frame, text="How many days are you shooting for?", bootstyle=LIGHT).pack(side="left", padx=5)
days_entry = ttk.Entry(days_frame)
days_entry.pack(side="left", fill="x", expand=True, padx=5)

# Input Field for Talent Names
talent_frame = ttk.Frame(app)
talent_frame.pack(pady=15, padx=10, fill="x")
ttk.Label(talent_frame, text="What are the talent names? (comma separated)").pack(side="left", padx=5)
talent_entry = ttk.Entry(talent_frame)
talent_entry.pack(side="left", fill="x", expand=True, padx=5)

def on_submit():
    top_folder = top_entry.get()
    days = days_entry.get()
    talent_names = talent_entry.get()
    create_folders(top_folder, days, talent_names)

button_frame = ttk.Frame(app)
button_frame.pack(pady=0, padx=0, side="bottom")

directory_button = ttk.Button(app, text="Choose Folder", command=open_file)
directory_button.pack(side=LEFT, padx=120, pady=10)
    
# Submit Button to trigger folder creation
submit_button = ttk.Button(app, text="Create Folders", command=on_submit)
submit_button.pack(side=RIGHT, padx=120, pady=10)

app.mainloop()
