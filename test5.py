import os

# Đường dẫn tới thư mục chứa các file annotation
folder_path = r'speedlitmit60\labels'

# Duyệt qua từng file trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Kiểm tra xem file có phải là file .txt không
        file_path = os.path.join(folder_path, filename)
        
        # Đọc file
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        # Kiểm tra xem file có đúng 2 dòng không
        if len(lines) == 2:
            print(filename)
