from chitra.image import Chitra
import matplotlib.pyplot as plt

# Assuming 'img_path' is the path to your image,
# 'box' is the bounding box, and 'label' is the label for the bounding box
img_path = r'data/VN_traffic_sign_frames_video/Frames-Video for YOLO/Vietnam_video_traffic_sign/train/images/image_484.jpg'
yolo_annotation = [0.741141, 0.311699, 0.030251,0.062500]

# Image dimensions
image_width = 1280
image_height = 720

# Convert YOLO annotation to standard format
center_x = yolo_annotation[0] * image_width
center_y = yolo_annotation[1] * image_height
box_width = yolo_annotation[2] * image_width
box_height = yolo_annotation[3] * image_height

top_left_x = center_x - box_width / 2
top_left_y = center_y - box_height / 2
bottom_right_x = center_x + box_width / 2
bottom_right_y = center_y + box_height / 2

# Standard format annotation
standard_annotation = [top_left_x, top_left_y, bottom_right_x, bottom_right_y]
label = ["ANH"]
image = Chitra(img_path, standard_annotation, label)

# Chitra can rescale your bounding box automatically based on the new image size.
image.resize_image_with_bbox((640, 640))

print('rescaled bbox:', image.bboxes)

# Display the image with the rescaled bounding box
plt.imshow(image.draw_boxes())
plt.show()
