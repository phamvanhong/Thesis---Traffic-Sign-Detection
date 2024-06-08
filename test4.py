from PIL import Image
import os

# Đường dẫn tới thư mục chứa các ảnh
folder_path = r'speedlitmit60\images'

# Duyệt qua từng file trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Kiểm tra xem file có phải là file ảnh không
        file_path = os.path.join(folder_path, filename)
        
        # Đọc ảnh
        img = Image.open(file_path)
        
        # Lấy kích thước ảnh
        width, height = img.size
        
        # In ra kích thước ảnh
        print(f'Kích thước của ảnh {filename}: {width} x {height}')
