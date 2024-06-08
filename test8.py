import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread(r'speedlitmit80\valid\images\p179_jpg.rf.f6a146d8750ca391e0440bb6e995bec8.jpg')
# Kích thước ảnh
h_img, w_img, _ = img.shape

# YOLO annotations
annotations = [
[0,0.34375, 0.48214285714285715, 0.015625, 0.05357142857142857],
[0 ,0.49107142857142855 ,0.4375, 0.017857142857142856, 0.05357142857142857],
[0, 0.6651785714285714 ,0.3861607142857143 ,0.020089285714285716 ,0.060267857142857144],
#[0 ,0.875, 0.3236607142857143, 0.029017857142857144, 0.07366071428571429],
]

for ann in annotations:
    class_id, x_center, y_center, w, h = ann
    x_center *= w_img
    y_center *= h_img
    w *= w_img
    h *= h_img

    # Tính toán tọa độ góc trên bên trái và góc dưới bên phải
    x1 = int(x_center - w / 2)
    y1 = int(y_center - h / 2)
    x2 = int(x_center + w / 2)
    y2 = int(y_center + h / 2)

    # Vẽ bounding box
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Hiển thị ảnh
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
