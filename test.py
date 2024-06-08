import cv2
import numpy as np
import sys
sys.path.append(r"E:\Traffic_Sign_Detection Thesis\Thesis---Traffic-Sign-Detection")

image = r"final_image_dataset\test\images\image_4_jpg.rf.082ed89f248aaf391eab467aa834f5acresize.jpg"
label = r"final_image_dataset\test\labels\image_4_jpg.rf.082ed89f248aaf391eab467aa834f5acresize.txt"

# Đọc ảnh
img = cv2.imread(image)

# Kích thước ảnh
h_img, w_img, _ = img.shape
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



