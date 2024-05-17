import sys
sys.path.append(r'E:\Traffic_Sign_Detection Thesis\Thesis---Traffic-Sign-Detection')
from src.model.read_write import ReadWriteFile
from src.common.constans import WRITE



class AdjustBoundingBoxes:
    def __init__(self, folder_path: str,  annotation_paths: list, image_width: int, image_height: int):
        """
        Initialize the AdjustBoundingBoxes object
        Args:
            folder_path (str): The path to the folder
            annotation_paths (list): The list of paths to the annotation files
            image_width (int): The original width of the image
            image_height (int): The original height of the image

        """
        self.folder_path = folder_path
        self.annotation_paths = annotation_paths
        self.image_width = image_width
        self.image_height = image_height

    def calculate_center_and_size(self, yolo_annotation: list) -> tuple:
        """
        Calculate the center and size of the bounding box from YOLO annotation
        Args:
            yolo_annotation (list): The YOLO annotation to convert
        Returns:
            tuple: The center and size of the bounding box (center_x, center_y, box_width, box_height)
        """
        center_x = yolo_annotation[0] * self.image_width
        center_y = yolo_annotation[1] * self.image_height
        box_width = yolo_annotation[2] * self.image_width
        box_height = yolo_annotation[3] * self.image_height

        return (center_x, center_y, box_width, box_height)

    def calculate_corners(self, center_x, center_y, box_width, box_height):
        """
        Calculate the corners of the bounding box from its center and size
        Args:
            center_x (float): The x-coordinate of the center of the bounding box
            center_y (float): The y-coordinate of the center of the bounding box
            box_width (float): The width of the bounding box
            box_height (float): The height of the bounding box
        Returns:
            list: The corners of the bounding box [top_left_x, top_left_y, bottom_right_x, bottom_right_y]
        """
        top_left_x = center_x - box_width / 2
        top_left_y = center_y - box_height / 2
        bottom_right_x = center_x + box_width / 2
        bottom_right_y = center_y + box_height / 2

        return [top_left_x, top_left_y, bottom_right_x, bottom_right_y]

    def calculate_ratio(self) -> float:
        """
        Calculate the ratio of the width and height after resizing the image to 640x640

        Returns:
            float: The ratio of the width and height
        """
        width_scale = 640 / image_width
        height_scale = 640 / image_height
        return width_scale, height_scale

    def resize_bboxes_adjust(self, lines: list) -> list:
        """
        Save the adjust annotations to a list
        Args:
            lines (list): The list of lines in the annotation file
        Returns:
            list: The list of annotations
        """
        annotations = []
        for line in lines:
            elements = line.strip().split()
            label = elements[0]
            yolo_annotation = list(map(float, elements[1:]))
            center_x, center_y, box_width, box_height = self.calculate_center_and_size(
                yolo_annotation)
            
            standard_annotation = self.calculate_corners(
                center_x, center_y, box_width, box_height)
            
            width_scale, height_scale = self.calculate_ratio()
            
            resize_bboxes = [int(standard_annotation[0]*width_scale),
                             int(standard_annotation[1]*height_scale),
                             int(standard_annotation[2]*width_scale),
                             int(standard_annotation[3]*height_scale)]
            annotations.append([label, resize_bboxes])
        return annotations

    def write_new_bboxes_to_annotations_file(self):
        """
        Convert the bounding boxes to standard format"""
        for annotation_file_path in self.annotation_paths:
            lines = ReadWriteFile(annotation_file_path,
                                  self.folder_path).read_lines_in_file()
            annotations = self.resize_bboxes_adjust(lines)
            new_file_path = ReadWriteFile(
                annotation_file_path, self.folder_path).create_new_file_path()
            with open(new_file_path, WRITE) as file:
                for annotation in annotations:
                    label = annotation[0]
                    center_x, center_y, box_width, box_height = annotation[1]
                    file.write(f"{label} {center_x} {center_y} {
                               box_width} {box_height}\n")


if __name__ == "__main__":

    annotation_paths = [r'data\VN_traffic_sign_frames_video\Frames-Video for YOLO\Vietnam_video_traffic_sign\train\labels\image_484.txt',
                        r"data\VN_traffic_sign_frames_video\Frames-Video for YOLO\Vietnam_video_traffic_sign\test\labels\image_470.txt",
                        r"data\VN_traffic_sign_frames_video\Frames-Video for YOLO\Vietnam_video_traffic_sign\test\labels\image_380.txt"]
    folder_path = "tessttxt"
    image_width = 1280
    image_height = 720

    adjust_bboxes = AdjustBoundingBoxes(
        folder_path, annotation_paths, image_width, image_height)
    adjust_bboxes.write_new_bboxes_to_annotations_file()
