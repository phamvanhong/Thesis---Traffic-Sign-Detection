import cv2
import numpy as np
import pybboxes as pbx
# Load your image
image = cv2.imread(r'split\valid\images\image_26resize.jpg')

# Define your bounding box coordinates
# These are in the format: [x, y, width, height]
bbox = [0.615625, 0.840625, 0.64375, 0.9015625]

# Convert bbox coordinates to pixel values
bbox_pixel = np.array(bbox) * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
bbox_pixel = bbox_pixel.astype(int)

# Draw the bounding box on the image
cv2.rectangle(image, (bbox_pixel[0], bbox_pixel[1]), (bbox_pixel[2], bbox_pixel[3]), (0, 255, 0), 2)

# Display the image
cv2.imshow('Image with Bounding Box', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


voc_bbox = (bbox_pixel[0], bbox_pixel[1], bbox_pixel[2], bbox_pixel[3])
W, H = 640, 640  # WxH of the image
list = [pbx.convert_bbox(voc_bbox, from_type="voc", to_type="yolo", image_size=(W,H))]
print(list)

