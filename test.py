import cv2
import numpy as np
import sys
sys.path.append(r"E:\Traffic_Sign_Detection Thesis\Thesis---Traffic-Sign-Detection")

image = r"augment_image\blur\p57_jpg.rf.34c3805aa3308479b86f64c8d28552d7blur.jpg"
label = r"adjust_annotation\blur\p57_jpg.rf.34c3805aa3308479b86f64c8d28552d7blur.txt"

# Đọc ảnh
img = cv2.imread(image)

# Kích thước ảnh
h_img, w_img, _ = img.shape
print(h_img, w_img)
with open(label, 'r') as f:
    lines = f.readlines()

# Chuyển đổi dữ liệu annotation thành numpy array
annotations = [list(map(float, line.strip().split())) for line in lines]
annotations = np.array(annotations)

# Vẽ bounding boxes
for ann in annotations:
    class_id, x_center, y_center, w, h = ann
    x_center *= w_img
    y_center *= h_img
    w *= w_img
    h *= h_img
    x1 = int(x_center - w / 2)
    y1 = int(y_center - h / 2)
    x2 = x1 + int(w)
    y2 = y1 + int(h)
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Hiển thị ảnh
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



