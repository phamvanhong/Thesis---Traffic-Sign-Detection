import os

# Đường dẫn tới thư mục chứa các ảnh và thư mục chứa các file annotation
image_folder_path = r'FINISH_IMAGE\50\images'
annotation_folder_path = r'FINISH_IMAGE\50\labels'
image_files = set(os.path.splitext(filename)[0] for filename in os.listdir(image_folder_path) if filename.endswith('.jpg'))

# Lấy danh sách tên file (không kèm đuôi) trong thư mục annotation
annotation_files = set(os.path.splitext(filename)[0] for filename in os.listdir(annotation_folder_path) if filename.endswith('.txt'))

# Tìm các file có trong thư mục ảnh nhưng không có trong thư mục annotation
missing_in_annotations = image_files - annotation_files

# Tìm các file có trong thư mục annotation nhưng không có trong thư mục ảnh
missing_in_images = annotation_files - image_files

# In ra danh sách các file khác nhau
# print("Các file có trong thư mục ảnh nhưng không có trong thư mục annotation:", missing_in_annotations)
print("Các file có trong thư mục annotation nhưng không có trong thư mục ảnh:", missing_in_images)
