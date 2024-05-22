import os
import shutil

def merge_folders(source_folders, destination_folder):
    """
    Hàm này gộp tất cả các file từ danh sách thư mục nguồn vào thư mục đích.

    :param source_folders: Danh sách các thư mục nguồn.
    :param destination_folder: Thư mục đích.
    """
    # Tạo thư mục đích nếu nó không tồn tại
    os.makedirs(destination_folder, exist_ok=True)

    for folder in source_folders:
        for filename in os.listdir(folder):
            source_file = os.path.join(folder, filename)
            destination_file = os.path.join(destination_folder, filename)

            # Di chuyển file từ thư mục nguồn đến thư mục đích
            shutil.move(source_file, destination_file)

# Sử dụng hàm
image_folders = [r'augment_image\blur',
                  r'augment_image\brightness', 
                  r'augment_image\darkness',
                  r"augment_image\high_contrast",
                  r"augment_image\low_contrast",
                  r"augment_image\noise",
                  r"augment_image\resize"]  # Thay đổi này thành danh sách thư mục nguồn của bạn\
annotation_folder = [r'adjust_annotation\blur',
                     r'adjust_annotation\brightness', 
                  r'adjust_annotation\darkness',
                  r"adjust_annotation\high_contrast",
                  r"adjust_annotation\low_contrast",
                  r"adjust_annotation\noise",
                  r"adjust_annotation\resize"]  # Thay đổi này thành danh sách thư mục nguồn của bạn
destination_folder = r'split\train\labels'  # Thay đổi này thành thư mục đích của bạn
merge_folders(annotation_folder, destination_folder)
