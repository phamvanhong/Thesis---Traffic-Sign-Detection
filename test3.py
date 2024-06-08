import os

# Đường dẫn tới thư mục chứa các file annotation
folder_path = r'speedlitmit50\labels'

# Duyệt qua từng file trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Kiểm tra xem file có phải là file .txt không
        file_path = os.path.join(folder_path, filename)
        
        # Đọc file
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        # Thay đổi class thành số 7
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            parts[0] = '7'  # Thay đổi class thành số 7
            new_line = ' '.join(parts)
            new_lines.append(new_line)
        
        # Cập nhật lại file
        with open(file_path, 'w') as f:
            f.write('\n'.join(new_lines))
