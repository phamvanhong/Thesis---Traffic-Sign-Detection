from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np

def rotate(img_path: str) -> Image.Image:
        """
        Rotate the input image by 45 degrees
        Args:
            img_path (str): The path to the input image
        Returns:
            PIL.Image.Image: The rotated image
        """
        img = Image.open(img_path)
        return img.rotate(45)

def rotate_(image_path):
    """
    Rotates an image (angle in degrees) and expands image to avoid cropping
    """
    image = cv2.imread(image_path)
    height, width = image.shape[:2]  # image shape has 3 dimensions
    image_center = (width / 2,
                    height / 2)  # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

    rotation_mat = cv2.getRotationMatrix2D(image_center, 45, 1.)

    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0, 0])
    abs_sin = abs(rotation_mat[0, 1])

    # find the new width and height bounds
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # subtract old image center (bringing image back to origin) and adding the new image center coordinates
    rotation_mat[0, 2] += bound_w / 2 - image_center[0]
    rotation_mat[1, 2] += bound_h / 2 - image_center[1]

    # rotate image with the new bounds and translated rotation matrix
    rotated_mat = cv2.warpAffine(image, rotation_mat, (bound_w, bound_h))
    return rotated_mat

image_path = r"testdata\frames\image19.jpg"
image = rotate(image_path)
image.save("rotated_image1.jpg")
image2 = rotate_(image_path)
cv2.imwrite("rotated_image2.jpg", image2)