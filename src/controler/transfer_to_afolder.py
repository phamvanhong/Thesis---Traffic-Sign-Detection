import shutil
import os

# Danh sách các thư mục nguồn
annotation = [r'adjust_annotation\resize', 
                  r'adjust_annotation\blur', 
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
destination_folder = r'Test_data\train\images'

# Đảm bảo thư mục đích tồn tại
os.makedirs(destination_folder, exist_ok=True)

# Di chuyển tất cả các tệp từ thư mục nguồn đến thư mục đích
for folder in image:
    for file_name in os.listdir(folder):
        shutil.move(os.path.join(folder, file_name), destination_folder)
