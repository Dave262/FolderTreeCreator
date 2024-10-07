import os


def get_mounted_drives():
    # This function will return a list of mounted drives
    if os.name == 'nt':  # For Windows
        import string
        drives = [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]
    else:  # For Unix/Linux
        drives = [os.path.join('/mnt', d) for d in os.listdir('/mnt') if os.path.ismount(os.path.join('/mnt', d))]
    return drives

# def update_drive_list():
#     # Get the list of drives and insert them into the textbox
#     drives = get_mounted_drives()
#     print(drives)
#     return drives



