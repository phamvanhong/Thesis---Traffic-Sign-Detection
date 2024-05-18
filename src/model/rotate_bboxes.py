from src.model.resize_bboxes import AdjustBoundingBoxes
from src.model.read_write import ReadWriteFile
import numpy as np
import cv2
import sys
sys.path.append(
    r'E:\Traffic_Sign_Detection Thesis\Thesis---Traffic-Sign-Detection')


class RotateBoundingBoxes:
    def __init__(self,
                 folder_path: str,
                 annotation_paths: list,
                 rotated_img_paths: list,
                 origin_img_paths: list) -> None:
        """
        Initialize the RotateBoundingBoxes object
        Args:
            folder_path (str): The path to the folder to create new anntation files
            annotation_paths (list): The list of paths to the annotation files
            rotated_img_paths (list): The list of paths to the rotated image files
            origin_img_paths (list): The list of paths to the original image files
        """
        self.folder_path = folder_path
        self.annotation_paths = annotation_paths
        self.rotated_img_paths = rotated_img_paths
        self.origin_img_paths = origin_img_paths

        # create a 2D-rotation matrix
        self.rotation_angle = 45 * np.pi / 180
        self.rot_matrix = np.array(
            [[np.cos(self.rotation_angle), -np.sin(self.rotation_angle)],
             [np.sin(self.rotation_angle), np.cos(self.rotation_angle)]])

    def open_image(self, img_path: str) -> cv2.typing.MatLike:
        """
        Open an image from the file path
        Args:
            img_path (str): The path to the image file
        Returns:
            Image.Image: The image object
        """
        return cv2.imread(img_path)

    def get_size(self, img: cv2.typing.MatLike) -> tuple:
        """
        Get the size of the image
        Args:
            img (Image.Image): The image object
        Returns:
            tuple: The size of the image (width, height)
        """
        height, width = img.shape[:2]
        return height, width

    def get_size_all_images(self, img_paths: list) -> list:
        """
        Get the size of all images
        Args:
            img_paths (list): The list of paths to the images (rotated or original)
        Returns:
            list: The list of sizes of the images [(height1, width1), (height2, width2), ...]
        """
        img_size = []
        for img_path in img_paths:
            height, width = self.get_size(self.open_image(img_path))
            img_size.append((height, width))
        return img_size

    def calculate_coners(self,
                         center_x: float,
                         center_y: float,
                         box_width: float,
                         box_height: float) -> tuple:
        """
        Calculate the corners of the bounding box from its center and size
        Shift the origin to the center of the image
        Args:
            center_x (float): The x-coordinate of the center of the bounding box
            center_y (float): The y-coordinate of the center of the bounding box
            box_width (float): The width of the bounding box
            box_height (float): The height of the bounding box
        Returns:
            list: The corners of the bounding box [top_left_x, top_left_y, bottom_right_x, bottom_right_y]
        """
        origin_height, origin_width = self.get_size(
            self.open_image(self.origin_img_paths))
        upper_left_corner_shift = (
            center_x - origin_width / 2, -origin_height / 2 + center_y)
        upper_right_corner_shift = (
            box_width - origin_width / 2, -origin_height / 2 + center_y)
        lower_left_corner_shift = (
            center_x - origin_width / 2, -origin_height / 2 + box_height)
        lower_right_corner_shift = (
            box_width - origin_width / 2, -origin_height / 2 + box_height)
        return (upper_left_corner_shift, upper_right_corner_shift, lower_left_corner_shift, lower_right_corner_shift)

    def rotate_coners(self, corners_shift: list) -> list:
        """
        Rotate the corners of the bounding box
        Args:
            corners_shift (list): The corners of the bounding box after shifting the origin [upper_left_corner_shift, upper_right_corner_shift, lower_left_corner_shift, lower_right_corner_shift]
        Returns:
            list: The corners of the bounding box after rotating
        """
        new_lower_right_corner = [-1, -1]
        new_upper_left_corner = []
        rotate_width, rotate_height = self.get_size(
            self.open_image(self.rotated_img_paths))
        for i in (upper_left_corner_shift, upper_right_corner_shift, lower_left_corner_shift,
                  lower_right_corner_shift):
            new_coords = np.matmul(self.rot_matrix, np.array((i[0], -i[1])))
            x_prime, y_prime = rotate_width / 2 + \
                new_coords[0], rotate_height / 2 - new_coords[1]
            if new_lower_right_corner[0] < x_prime:
                new_lower_right_corner[0] = x_prime
            if new_lower_right_corner[1] < y_prime:
                new_lower_right_corner[1] = y_prime

            if len(new_upper_left_corner) > 0:
                if new_upper_left_corner[0] > x_prime:
                    new_upper_left_corner[0] = x_prime
                if new_upper_left_corner[1] > y_prime:
                    new_upper_left_corner[1] = y_prime
            else:
                new_upper_left_corner.append(x_prime)
                new_upper_left_corner.append(y_prime)

    def rotate_bboxes(self):
        """
        Rotate the bounding boxes
        """
        img_rotate_size = self.get_size_all_images(self.rotated_img_paths)
        img_origin_size = self.get_size_all_images(self.origin_img_paths)
        adjust_bboxes = AdjustBoundingBoxes(
            self.folder_path, self.annotation_paths, img_origin_size[0][1], img_origin_size[0][0]
        )
        for annotation_file_path in self.annotation_paths:
            lines = ReadWriteFile(annotation_file_path).read_lines_in_file()
            for line in lines:
                bbox = line.strip('\n').split(' ')
                yolo_annotation = list(map(float, bbox[1:]))
                if len(bbox) > 1:
                    (center_x, center_y, box_width, box_height) = adjust_bboxes.calculate_center_and_size(
                        yolo_annotation)
                    (upper_left_corner_shift, upper_right_corner_shift, lower_left_corner_shift,
                     lower_right_corner_shift) = self.calculate_coners(center_x, center_y, box_width, box_height)
                    
