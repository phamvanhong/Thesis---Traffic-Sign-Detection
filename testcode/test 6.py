import cv2
import numpy as np

# Đường dẫn đến hình ảnh của bạn
image_path = r'data\VN_traffic_sign_frames_video\Frames-Video for YOLO\Vietnam_video_traffic_sign\test\images\image_380.jpg'

# Tọa độ bounding box
bbox = [597, 203, 615, 266]

# Chuyển đổi tọa độ bounding box thành kiểu int
bbox = [int(b) for b in bbox]

# Load hình ảnh
image = cv2.imread(image_path)
resized_image = cv2.resize(image, (640, 640))
# Vẽ bounding box lên hình ảnh
cv2.rectangle(resized_image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)

# Hiển thị hình ảnh
cv2.imshow('Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
