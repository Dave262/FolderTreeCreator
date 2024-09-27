import customtkinter as ctk
import colour
from backend import DirPath, user_select_dir, create_folders
from PIL import Image, ImageTk
# from backend import open_file

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()


        def update_directory_label():      
                print(f"Your folder tree will be in: {DirPath}")
                directory_label.configure(text=f"Parent folder: {DirPath}",)
                self.update_idletasks()

        def user_dir():
                global DirPath
                DirPath = user_select_dir()
                update_directory_label()
                self.update_idletasks()


##### ------ GUI STUFF ------- #

# GEOMETRY      
        self.geometry("800x450")
        self.minsize(width=800, height=450)

        self.title("Production Audio Folder Tree Creator - by David Ross")

        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
                
                
        # FRAMES

        frame_right = ctk.CTkFrame(self)
        frame_right.grid(row=0, column=1, rowspan=7, padx=10, pady=10, sticky="nswe")
        frame_right.configure(fg_color=colour.BACKGROUND_COLOR)
        
        frame_left = ctk.CTkFrame(self)
        frame_left.grid(row=0, column=0, rowspan=7, padx=10, pady=10, sticky="nswe")
        frame_left.configure(fg_color=colour.BACKGROUND_COLOR)

        subframe_top = ctk.CTkFrame(frame_left)
        subframe_top.pack(side = "top", fill = "x", padx = 10, pady = 10, anchor="nw")
        subframe_top.configure(fg_color="transparent")
#TEXT INPUT FIELD
        subframe_mid = ctk.CTkFrame(frame_left)
        subframe_mid.pack(side = "top", fill = "x", padx = 10, pady = 10, anchor="nw")
        subframe_mid.configure(fg_color="transparent")
        subframe_mid.grid_columnconfigure((0, 1), weight=1)
        
        subframe_bottom = ctk.CTkFrame(frame_left)
        subframe_bottom.pack(side = "top", fill = "x", padx = 10, pady = 10, anchor="nw")
        subframe_bottom.configure(fg_color="transparent")


# Heading
        label = ctk.CTkLabel(subframe_top, text="Production Audio Folder Tree Creator", 
                        font=("Inclusive Sans", 25, "bold"), text_color=colour.OFF_WHITE)

        label.pack()             

# GREETING

        greeting = ctk.CTkLabel(subframe_top, 
                                text="Pick a directory, name the folders and hit create!", 
                                font=("Inclusive Sans", 15, "bold"), text_color=colour.OFF_WHITE)
        greeting.pack()

# RIGHT FRAME 

        choosebutton = ctk.CTkButton(frame_right, text="choose directory", command=user_dir)
        choosebutton.pack(side = "top", pady = 10)
        choosebutton.configure(fg_color = colour.BLUE, text_color=colour.OFF_WHITE)

        


# FOLDER ENTRIES        
        folder1_entry = ctk.CTkEntry(subframe_mid, placeholder_text="Project folder name?", 
                                font=("Inclusive Sans", 12, "bold"), placeholder_text_color=colour.GREY)
        folder1_entry.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = (20, 10), sticky = "ew")

        folder2_entry = ctk.CTkEntry(subframe_mid, placeholder_text="Daily folder names?",
                                font=("Inclusive Sans", 12, "bold"), placeholder_text_color=colour.GREY)
        folder2_entry.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "ew")

        folder2_amount_entry = ctk.CTkEntry(subframe_mid, placeholder_text="How many shooting days?",
                                        font=("Inclusive Sans", 12, "bold"), placeholder_text_color=colour.GREY)
        folder2_amount_entry.grid(row = 1, column = 1, padx = 10, pady = 10, sticky ="ew")

        folder3_entry = ctk.CTkEntry(subframe_mid, placeholder_text="Bodypack folder name?",
                                font=("Inclusive Sans", 12, "bold"), placeholder_text_color=colour.GREY)
        folder3_entry.grid(row = 2, column = 0,columnspan = 2, padx = 10, pady = 10, sticky = "ew")

        folder4_entry = ctk.CTkEntry(subframe_mid, placeholder_text="Optional folder inside each daily?",
                                font=("Inclusive Sans", 12, "bold"), placeholder_text_color=colour.GREY)
        folder4_entry.grid(row = 3, column = 0,columnspan = 2, padx = 10, pady = 10, sticky = "ew")

        folder5_entry = ctk.CTkEntry(subframe_mid, placeholder_text="Talent names (comma separated)?",
                                font=("Inclusive Sans", 12, "bold"), placeholder_text_color=colour.GREY)
        folder5_entry.grid(row = 4, column = 0,columnspan = 2, padx = 10, pady = (10, 20), sticky = "ew")

        directory_label = ctk.CTkLabel(subframe_bottom, 
                                text=f"No directory selected...", 
                                font=("Inclusive Sans", 15, "bold"), text_color=colour.OFF_WHITE,
                                wraplength=500, justify="center")
        directory_label.pack(padx = "15")


# FUNCTION CALLS
#  make the folder label scrollable for long ass folder paths
        



        def on_submit():
                project_folder = folder1_entry.get()
                daily_folder = folder2_entry.get() or "Day"
                days_number_input = folder2_amount_entry.get()
                bodypack_name = folder3_entry.get() or "Bodypack Recorders"
                optional_folder_name = folder4_entry.get()
                talent_folder = folder5_entry.get()         

                create_folders(project_folder, 
                                daily_folder, 
                                days_number_input, 
                                bodypack_name, 
                                optional_folder_name, 
                                talent_folder
                                )
                
        def copy_path(text):
                self.clipboard_clear()
                self.clipboard_append(text)
                self.update()
                print(f"Copied {text} to the clipboard")

 


        create_button = ctk.CTkButton(frame_right, text="Create folder tree", command=on_submit)
        create_button.pack(side = "top", pady=20)
        create_button.configure(fg_color = colour.YELLOW, text_color=colour.OFF_WHITE)


        copy_button = ctk.CTkButton(frame_right, text="Copy path", command=lambda: copy_path(DirPath))
        copy_button.pack(side="bottom", pady=10)
        copy_button.configure(fg_color = colour.BLUE, text_color=colour.OFF_WHITE)

