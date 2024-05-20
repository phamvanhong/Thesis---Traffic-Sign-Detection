import cv2

img = cv2.imread(r'data\VN_traffic_sign_frames_video\Frames-Video for YOLO\frames\image537.jpg', cv2.IMREAD_UNCHANGED)

# Print the original image size
print('Original Dimensions : ', img.shape)
