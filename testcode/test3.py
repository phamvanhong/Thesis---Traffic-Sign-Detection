import cv2
import os
import numpy as np

# Đường dẫn đến thư mục chứa ảnh và annotation
image_dir = r'data\test_new_dataset\test\images'
annotation_dir = r'data\test_new_dataset\test\labels'

for filename in os.listdir(annotation_dir):
    if filename.endswith('.txt'):
        # Đọc file annotation
        with open(os.path.join(annotation_dir, filename), 'r') as f:
            lines = f.readlines()

        # Đọc ảnh tương ứng
        image = cv2.imread(os.path.join(image_dir, filename.replace('.txt', '.jpg')))

        # Tạo một hình ảnh trắng có cùng kích thước với hình ảnh gốc
        white_image = np.ones_like(image) * 255

        # Duyệt qua tất cả các dòng trong file annotation
        for line in lines:
            # Mỗi dòng trong file annotation gồm: class x_center y_center width height
            parts = line.strip().split()
            class_id, x_center, y_center, width, height = map(float, parts)

            # Chỉ visualize object có label là 0
            if int(class_id) == 0:
                # Chuyển đổi tọa độ từ định dạng YOLO về pixel
                x_center *= image.shape[1]
                y_center *= image.shape[0]
                width *= image.shape[1]
                height *= image.shape[0]

                # Tính toán tọa độ góc trên bên trái và góc dưới bên phải của bounding box
                x1 = int(x_center - width / 2)
                y1 = int(y_center - height / 2)
                x2 = int(x_center + width / 2)
                y2 = int(y_center + height / 2)

                # Cắt (crop) phần của hình ảnh bên trong bounding box
                cropped = image[y1:y2, x1:x2]

                # Dán phần hình ảnh đã cắt lên hình ảnh trắng
                white_image[y1:y2, x1:x2] = cropped

        # Hiển thị hình ảnh
        cv2.imshow('Image', white_image)
        cv2.waitKey(0)