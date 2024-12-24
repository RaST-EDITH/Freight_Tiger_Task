import os

def check_if_folder_is_empty():

    folder_path = os.getcwd()
    if os.path.exists(folder_path) and os.path.isdir(folder_path):

        files = os.listdir(folder_path)

        if files:
            return True
        else:
            return False
    else:
        return False
