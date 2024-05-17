from src.common.constans import READ, WRITE
import os

class ReadWriteFile:
    def __init__(self, file_path, folder_path):
        self.file_path = file_path
        self.folder_path = folder_path

    def read_lines_in_file(self):
        with open(self.file_path, READ) as file:
            lines = file.readlines()
        return lines

    def write_to_file(self, data):
        with open(self.file_path, WRITE) as file:
            file.write(data)
    
    def write_to_file_into_folder(self):
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        
        base_name = os.path.basename(self.file_path)
        new_file_path = os.path.join(self.folder_path, base_name)
        return new_file_path