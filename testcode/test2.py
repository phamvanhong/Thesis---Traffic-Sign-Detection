import os
import cv2
import numpy as np
from albumentations import Compose, Resize, Rotate
from albumentations.pytorch.transforms import ToTensorV2

# Đường dẫn đến thư mục chứa hình ảnh và annotation
image_folder = 'path_to_your_image_folder'
annotation_folder = 'path_to_your_annotation_folder'

# Khởi tạo biến đổi
transform = Compose([
    Resize(640, 640),  # Thay đổi kích thước hình ảnh
    Rotate(limit=45),  # Quay hình ảnh 45 độ
    ToTensorV2()  # Chuyển hình ảnh thành tensor
])

# Duyệt qua tất cả các hình ảnh trong thư mục
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg'):  # Kiểm tra nếu là file .jpg
        # Đọc hình ảnh
        image = cv2.imread(os.path.join(image_folder, filename))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Đọc file annotation tương ứng
        with open(os.path.join(annotation_folder, filename.replace('.jpg', '.txt')), 'r') as f:
            annotations = [line.strip().split() for line in f]

        # Chuyển đổi annotations thành dạng phù hợp cho Albumentations
        bboxes = [list(map(float, ann[1:])) for ann in annotations]
        class_labels = [int(ann[0]) for ann in annotations]

        # Áp dụng biến đổi cho hình ảnh và bounding box
        transformed = transform(image=image, bboxes=bboxes, class_labels=class_labels)
        transformed_image = transformed['image']
        transformed_bboxes = transformed['bboxes']

        # Cập nhật file annotation
        with open(os.path.join(annotation_folder, filename.replace('.jpg', '.txt')), 'w') as f:
            for bbox, label in zip(transformed_bboxes, class_labels):
                f.write(f"{label} {' '.join(map(str, bbox))}\n")
