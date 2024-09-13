import os
import ttkbootstrap as ttk
import tkinter as tk
from tkinter import filedialog, simpledialog

app = ttk.Window(themename="darkly")
app.geometry("600x500")

label = ttk.Label(app, text="Whatever")
label.config(font=("Arial", 20, "bold"))


#Input Field Top
name_frame = ttk.Frame(app)
name_frame.pack(pady=15, padx=10, fill="x")
ttk.Label(name_frame, text="What's the Top level folder called?").pack(side="left", padx=5)
ttk.Entry(name_frame).pack(side="left", fill="x", expand=True, padx=5)

#Input Field Days
name_frame = ttk.Frame(app)
name_frame.pack(pady=15, padx=10, fill="x")
ttk.Label(name_frame, text="How many days are you shooting for?").pack(side="left", padx=5)
ttk.Entry(name_frame).pack(side="left", fill="x", expand=True, padx=5)




Top = input("Top level folder?: ")
Days = int(input("How many days will you be shooting for?: "))
TalentNames = input("What are the talent names? - comma separated: " )

Names = [name.strip() for name in TalentNames.split(',')]

String2 = "Bodypack Recorders"

for i in range(1, Days + 1):
    DailyFolder = f"Day_{i}"

    path = os.path.join(Top, DailyFolder)

    try:
        os.makedirs(path)
        print(f"created folder: {DailyFolder}")

        BodypackPath = os.path.join(path, String2 )
        os.makedirs(BodypackPath)
        print(f"created folder: {DailyFolder}:{String2}")

        for Name in Names:
            SubFolderPath = os.path.join(path, String2, Name)
            os.makedirs(SubFolderPath)
            print(f"created folder: {DailyFolder}:{String2}:{Name}")
        
    except FileExistsError:
        print(f"could not creat folder {path} already exists")
