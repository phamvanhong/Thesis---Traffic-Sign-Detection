import os

def rename_files_in_folder(folder_path: str, file_name: str, new_character: str) -> None:
    """
    Rename files in a folder by adding a new character to the file name
    Args:
        folder_path (str): The path to the folder to rename files
        file_name (str): The name of the file to rename
        new_character (str): The new character to add to the file name"""
    for filename in os.listdir(folder_path):
        if filename.endswith(file_name):
            # Add a '.' before the file extension
            new_filename = filename.rsplit('.', 1)[0] + new_character + '.' + filename.rsplit('.', 1)[1]
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
