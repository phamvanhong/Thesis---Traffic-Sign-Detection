import cv2
import numpy as np
import matplotlib.pyplot as plt

# Your original YOLO annotation
bbox = [1044.3558400000002,222.11568, 103.9936 ,155.76912000000002]

# Load your image
image = cv2.imread(r"data\VN_traffic_sign_frames_video\Frames-Video for YOLO\Vietnam_video_traffic_sign\test\images\image_548.jpg")

# Calculate the actual x, y, w, h from YOLO annotation
h, w = image.shape[:2]
x = int(bbox[0])
y = int(bbox[1])
bw = int(bbox[2])
bh = int(bbox[3])

# Rotate the image
M = cv2.getRotationMatrix2D((w/2, h/2), 45, 1.0)
rotated_image = cv2.warpAffine(image, M, (w, h))

# Adjust the annotation for the rotated image
center = np.array([x + bw / 2, y + bh / 2, 1])
rotated_center = M @ center
rx, ry = rotated_center[:2]
rw, rh = bw, bh  # Assuming the bounding box dimensions don't change after rotation

# Draw the adjusted bounding box on the rotated image
cv2.rectangle(rotated_image, (int(rx - rw / 2), int(ry - rh / 2)), (int(rx + rw / 2), int(ry + rh / 2)), (0, 255, 0), 2)

# Display the rotated image with the adjusted bounding box
plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.show()
