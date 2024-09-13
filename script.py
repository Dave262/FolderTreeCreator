import os
import tkinter



#input
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
