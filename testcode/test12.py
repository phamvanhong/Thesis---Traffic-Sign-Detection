import os

def count_all_files(directory):
    return sum([len(files) for r, d, files in os.walk(directory)])

# Replace 'your_directory_path' with the path to the directory you want to count files in
directory = r'split\train\images'
print(f'Total files in directory (including subdirectories): {count_all_files(directory)}')
