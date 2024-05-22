import cv2
import numpy as np

# Load the input image
image = cv2.imread(r'new_image\image27resize_crop_7.jpg')

# Create the sharpening kernel
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

# Apply the sharpening kernel to the image using filter2D
sharpened = cv2.filter2D(image, -1, kernel)

# Save the output image
cv2.imwrite('sharpened_image.jpg', sharpened)
