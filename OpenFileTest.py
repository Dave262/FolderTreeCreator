import os 
import ttkbootstrap as ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *


# Select path
root = Tk()
def open_file():
    filepath = filedialog.askdirectory(initialdir="/", title="Select a File")
    print(filepath)
button = Button(root, text="Open File", command=open_file)
button.pack()
root.mainloop()


