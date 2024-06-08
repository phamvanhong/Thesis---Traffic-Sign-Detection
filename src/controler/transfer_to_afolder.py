import shutil
import os

# Danh sách các thư mục nguồn
annotation = [r'adjust_annotation\blur', 
                r'adjust_annotation\resize',
                r'adjust_annotation\noise',
                r'adjust_annotation\high_contrast',
                r'adjust_annotation\low_contrast',
                r'adjust_annotation\darkness',
                r'adjust_annotation\brightness']

image = [r'augment_image\resize',
             r'augment_image\blur',
             r'augment_image\noise',
             r'augment_image\high_contrast',
             r'augment_image\low_contrast',
             r'augment_image\darkness',
             r'augment_image\brightness']
# Thư mục đích
image_folder = r"FINISH_IMAGE\80\images"
annotation_folder = r"FINISH_IMAGE\80\labels"

# Đảm bảo thư mục đích tồn tại
os.makedirs(image_folder, exist_ok=True)
os.makedirs(annotation_folder, exist_ok=True)

# Di chuyển tất cả các tệp từ thư mục nguồn đến thư mục đích
for folder in image:
    for file_name in os.listdir(folder):
        shutil.move(os.path.join(folder, file_name), image_folder)
for folder in annotation:
    for file_name in os.listdir(folder):
        shutil.move(os.path.join(folder, file_name), annotation_folder)