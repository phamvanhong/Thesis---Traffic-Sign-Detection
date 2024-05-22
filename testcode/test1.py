import os
import matplotlib.pyplot as plt
# Đường dẫn đến thư mục chứa các file annotation
folder_path = r'data\test_new_dataset\train\labels'

# Đường dẫn đến file labels.txt
labels_file_path = r'data\test_new_dataset\labels.txt'

# Đọc file labels.txt và lưu vào list
with open(labels_file_path, 'r', encoding='utf-8') as f:
    labels = f.read().splitlines()


# Khởi tạo dict để đếm số lượng mỗi label
label_counts = {label: 0 for label in labels}

# Duyệt qua tất cả các file trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Kiểm tra nếu là file .txt
        with open(os.path.join(folder_path, filename), 'r') as f:
            for line in f:
                label_index = int(line.split()[0])  # Lấy index của label từ dòng đầu tiên
                label = labels[label_index]  # Tìm label tương ứng trong file labels.txt
                label_counts[label] += 1  # Tăng số lượng của label này lên 1

labels = list(label_counts.keys())
counts = list(label_counts.values())

# Tạo biểu đồ cột
plt.figure(figsize=(10, 6))  # Tạo figure với kích thước phù hợp
plt.barh(labels, counts, color='skyblue')  # Vẽ biểu đồ cột ngang
plt.xlabel('Số lượng')  # Đặt tên cho trục x
plt.title('Số lượng các loại biển báo')  # Đặt tiêu đề cho biểu đồ
plt.show()  # 
