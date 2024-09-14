import os
import tkinter as tk
from tkinter import filedialog, simpledialog

# Create a simple window using Tkinter
root = tk.Tk()
root.withdraw()  # Hide the main Tkinter window as we only need input dialogs

# Ask the user to select a folder
Top = filedialog.askdirectory(title="Select the top-level folder")

# Ask for the number of days
Days = simpledialog.askinteger("Input", "How many days will you be shooting for?", minvalue=1)

# Ask for talent names
TalentNames = simpledialog.askstring("Input", "What are the talent names? (comma separated)")

# Process the talent names
Names = [name.strip() for name in TalentNames.split(',')]

# Create the folder structure
String2 = "Bodypack Recorders"

for i in range(1, Days + 1):
    DailyFolder = f"Day_{i}"

    path = os.path.join(Top, DailyFolder)

    try:
        os.makedirs(path)
        print(f"Created folder: {DailyFolder}")

        BodypackPath = os.path.join(path, String2)
        os.makedirs(BodypackPath)
        print(f"Created folder: {DailyFolder}:{String2}")

        for Name in Names:
            SubFolderPath = os.path.join(path, String2, Name)
            os.makedirs(SubFolderPath)
            print(f"Created folder: {DailyFolder}:{String2}:{Name}")

    except FileExistsError:
        print(f"Could not create folder {path} - already exists")
