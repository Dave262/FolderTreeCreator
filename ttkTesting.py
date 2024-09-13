import tkinter as tk
from tkinter import ttk, font

window = tk.Tk()
window.title("My Cool Title")
window.geometry("400x400")

style = ttk.Style()
style.configure('TButton', font = ("Inclusive Sans", 30))
style.map("new.TButton")
# print(style.theme_names())
label = ttk.Label(
    window,
    text = "A Label",
    background = "red",
    foreground = "white",
    font = ("Inclusive Sans", 30)
)
label.pack()

button = ttk.Button(
    window, 
    text = "A Button0",

    )
button.pack()

window.mainloop()