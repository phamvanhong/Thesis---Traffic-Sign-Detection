import cv2
import numpy as np

# Đường dẫn đến hình ảnh của bạn
image_path = r'data\VN_traffic_sign_frames_video\Frames-Video for YOLO\Vietnam_video_traffic_sign\test\images\image_380.jpg'

# Tọa độ bounding box
bbox = [1194.81472, 228.4614, 1231.32288, 299.99988]

# Chuyển đổi tọa độ bounding box thành kiểu int
bbox = [int(b) for b in bbox]

# Load hình ảnh
image = cv2.imread(image_path)

# Lấy kích thước gốc của hình ảnh
original_height, original_width = image.shape[:2]

# Kích thước mới bạn muốn thay đổi
new_width = 640
new_height = 640

# Tính toán hệ số tỷ lệ
width_scale = new_width / original_width
height_scale = new_height / original_height

# Thay đổi kích thước hình ảnh
resized_image = cv2.resize(image, (new_width, new_height))

# Điều chỉnh tọa độ của bounding box
resized_bbox = [int(bbox[0]*width_scale), int(bbox[1]*height_scale), int(bbox[2]*width_scale), int(bbox[3]*height_scale)]
print(int(bbox[0]*width_scale))
# Vẽ bounding box lên hình ảnh mới
cv2.rectangle(resized_image, (resized_bbox[0], resized_bbox[1]), (resized_bbox[2], resized_bbox[3]), (0, 255, 0), 2)

# Hiển thị hình ảnh
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
