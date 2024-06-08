import cv2
import numpy as np

image = r"add data\speed limit 50\train\images\004_0001_j-Copy-2-_png_jpg.rf.50783e2be4b2f99d30313e12ae7a3424.jpg"
label = r"data\VN_Traffic_Sign_Robo\test\labels\image59_jpg.rf.08449a8fb703386b97460054f5503c8e.txt"

# Đọc ảnh
img = cv2.imread(image)

# Kích thước ảnh
h_img, w_img, _ = img.shape
print(f'Kích thước ảnh: {w_img} x {h_img}')



