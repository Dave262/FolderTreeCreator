import customtkinter as ctk
import colour
from backend import DirPath, user_select_dir, create_folders
# from backend import open_file

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

# FUNCTION CALLS
# NOTE - make the folder label scrollable for long ass folder paths
        
        def update_directory_label():      
                print(f"Your folder tree will be in: {DirPath}")
                directory_label.configure(text=f"Your folder tree will be in: {DirPath}")
                app.update_idletasks()

        def user_dir():
                global DirPath
                DirPath = user_select_dir()
                update_directory_label()
                app.update_idletasks()

##### ------ GUI STUFF ------- #

# GEOMETRY      
        self.geometry("800x450")
        self.minsize(width=800, height=450)

        self.title("Production Audio Folder Tree Creator")

        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
# FRAMES
        frame_right = ctk.CTkFrame(self)
        frame_right.grid(row=0, column=1, rowspan=7, padx=10, pady=10, sticky="nswe")
        frame_right.configure(fg_color=colour.BACKGROUND_COLOR)
        
        frame_left = ctk.CTkFrame(self)
        frame_left.grid(row=0, column=0, rowspan=7, padx=10, pady=10, sticky="nswe")
        frame_left.configure(fg_color=colour.BACKGROUND_COLOR)

# Heading
        label = ctk.CTkLabel(frame_left, text="Production Audio Folder Tree Creator", 
                             font=("Inclusive Sans", 30, "bold"), text_color=colour.GREEN)


        label.pack(side = "top", anchor = "w", pady = (20, 10), padx = (10, 20))             
     
# GREETING

        greeting = ctk.CTkLabel(frame_left, 
                                text="Pick a directory, name the folders and hit create!", 
                                font=("Inclusive Sans", 15, "bold"), text_color=colour.OFF_WHITE)
        greeting.pack(side = "top", anchor = "w", pady = (0, 20), padx = 15)

        subframe = ctk.CTkFrame(frame_left)
        subframe.pack(side = "top", fill = "x", padx = 10, pady = 10, anchor="nw")
        subframe.configure(fg_color=colour.BLUE)
        subframe.grid_columnconfigure((0, 1), weight=1)

# RIGHT FRAME 

        choosebutton = ctk.CTkButton(frame_right, text="choose directory", command=user_dir)
        choosebutton.pack(side = "top", pady = 30)
        choosebutton.configure(fg_color = colour.BLUE, text_color=colour.OFF_WHITE)

        chosendirectory_label = ctk.CTkLabel(frame_right, text="Project Folder", text_color=colour.GREEN)
        chosendirectory_label.pack(side = "top", pady = 5)

        chosendirectory_label = ctk.CTkLabel(frame_right, text="Daily Folders", text_color=colour.GREEN)
        chosendirectory_label.pack(side = "top", pady = 5)

        chosendirectory_label = ctk.CTkLabel(frame_right, text="BodyPacks", text_color=colour.GREEN)
        chosendirectory_label.pack(side = "top", pady = 5)

        chosendirectory_label = ctk.CTkLabel(frame_right, text="Optional Folder", text_color=colour.GREEN)
        chosendirectory_label.pack(side = "top", pady = 5)

        chosendirectory_label = ctk.CTkLabel(frame_right, text="Talent Folders", text_color=colour.GREEN)
        chosendirectory_label.pack(side = "top", pady = 5)

        gotofolder_button = ctk.CTkButton(frame_right, text="Go to folder")
        gotofolder_button.pack(side = "top", pady = (10, 30))
        gotofolder_button.configure(fg_color = colour.BLUE, text_color=colour.OFF_WHITE)

# FOLDER ENTRIES        
        folder1_entry = ctk.CTkEntry(subframe, placeholder_text="Project folder name?", 
                                       font=("Inclusive Sans", 12, "bold"), placeholder_text_color=colour.OFF_WHITE)
        folder1_entry.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = (20, 10), sticky = "ew")

        folder2_entry = ctk.CTkEntry(subframe, placeholder_text="Daily folder names?",
                                     font=("Inclusive Sans", 12, "bold"), placeholder_text_color=colour.OFF_WHITE)
        folder2_entry.grid(row = 1, column = 0, padx = 5, pady = 10, sticky = "ew")

        folder2_amount_entry = ctk.CTkEntry(subframe, placeholder_text="How many shooting days?",
                                          font=("Inclusive Sans", 12, "bold"), placeholder_text_color=colour.OFF_WHITE)
        folder2_amount_entry.grid(row = 1, column = 1, padx = 5, pady = 10, sticky ="ew")

        folder3_entry = ctk.CTkEntry(subframe, placeholder_text="Bodypack folder name?",
                                     font=("Inclusive Sans", 12, "bold"), placeholder_text_color=colour.OFF_WHITE)
        folder3_entry.grid(row = 2, column = 0,columnspan = 2, padx = 5, pady = 10, sticky = "ew")

        folder4_entry = ctk.CTkEntry(subframe, placeholder_text="Optional folder inside each daily?",
                                     font=("Inclusive Sans", 12, "bold"), placeholder_text_color=colour.OFF_WHITE)
        folder4_entry.grid(row = 3, column = 0,columnspan = 2, padx = 5, pady = 10, sticky = "ew")

        folder5_entry = ctk.CTkEntry(subframe, placeholder_text="Talent names (comma separated)?",
                                     font=("Inclusive Sans", 12, "bold"), placeholder_text_color=colour.OFF_WHITE)
        folder5_entry.grid(row = 4, column = 0,columnspan = 2, padx = 5, pady = (10, 20), sticky = "ew")

        directory_label = ctk.CTkLabel(frame_left, 
                                text=f"Your folder tree will be in: ", 
                                font=("Inclusive Sans", 15, "bold"), text_color=colour.OFF_WHITE)
        directory_label.pack(anchor = "w", padx = "15", pady = (0, 15))


        def on_submit():
                project_folder = folder1_entry.get()
                daily_folder = folder2_amount_entry.get()
                days_number_input = folder2_amount_entry.get()
                bodypack_name = folder3_entry.get()
                optional_folder_name = folder4_entry.get()
                talent_folder = folder5_entry.get()
                
                create_folders(project_folder, 
                               daily_folder, 
                               days_number_input, 
                               bodypack_name, 
                               optional_folder_name, 
                               talent_folder
                               )


        create_button = ctk.CTkButton(frame_right, text="Create Folder Tree", command=on_submit)
        create_button.pack(side = "top", pady = (10, 30))
        create_button.configure(fg_color = colour.BLUE, text_color=colour.OFF_WHITE)


if __name__ == "__main__":
        app = App()
        app.mainloop()