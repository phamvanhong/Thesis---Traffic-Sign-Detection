import os
import cv2
import numpy as np
import random

# Đường dẫn đến thư mục chứa hình ảnh và annotation
image_folder = r'split\train\images'
annotation_folder = r'split\train\labels'

# Đường dẫn đến thư mục mới để lưu hình ảnh đã crop
new_image_folder = 'new_image'

# Số lượng crop tùy chỉnh
num_crops = 300

# Tạo thư mục mới nếu chúng chưa tồn tại
os.makedirs(new_image_folder, exist_ok=True)

# Duyệt qua tất cả các hình ảnh trong thư mục
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg'):  # Kiểm tra nếu là file .jpg
        # Đọc hình ảnh
        image = cv2.imread(os.path.join(image_folder, filename))

        # Đọc file annotation tương ứng
        with open(os.path.join(annotation_folder, filename.replace('.jpg', '.txt')), 'r') as f:
            annotations = [line.strip().split() for line in f]

        # Chuyển đổi annotations thành dạng phù hợp cho Albumentations
        bboxes = [list(map(float, ann[1:])) for ann in annotations]
        labels = [int(ann[0]) for ann in annotations]

        # Duyệt qua tất cả các bounding box
        for bbox, label in zip(bboxes, labels):
            if label == 0:  # Kiểm tra nếu label là 0
                x_center, y_center, width, height = bbox

                # Tính toạ độ của bounding box
                x_min = int((x_center - width / 2) * image.shape[1])
                x_max = int((x_center + width / 2) * image.shape[1])
                y_min = int((y_center - height / 2) * image.shape[0])
                y_max = int((y_center + height / 2) * image.shape[0])

                # Crop hình ảnh
                cropped_image = image[y_min:y_max, x_min:x_max]

                # Thay đổi kích thước hình ảnh thành 640x640
                resized_image = cv2.resize(cropped_image, (640, 640))

                # Lưu hình ảnh mới
                cv2.imwrite(os.path.join(new_image_folder, f"{filename.replace('.jpg', '')}_crop_{random.randint(0, num_crops)}.jpg"), resized_image)
