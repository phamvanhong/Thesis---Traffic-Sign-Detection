from chitra.image import Chitra
import matplotlib.pyplot as plt


class AdjustBoundingBoxes:
    def __init__(self, img_paths: list, annotation_paths: list, image_width, image_height):
        """
        Initialize the AdjustBoundingBoxes class with the image and annotation paths"""
        self.img_paths = img_paths
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

    def convert_bboxes_to_standard(self):
        """
        Convert the bounding boxes to standard format"""
        bboxes = []
        labels = []

        for annotation_file_path in self.annotation_paths:
            with open(annotation_file_path, 'r') as file:
                lines = file.readlines()

            for line in lines:
                elements = line.strip().split()
                label = elements[0]
                yolo_annotation = list(map(float, elements[1:]))

                center_x, center_y, box_width, box_height = self.calculate_center_and_size(
                    yolo_annotation)
                standard_annotation = self.calculate_corners(
                    center_x, center_y, box_width, box_height)

                bboxes.append(standard_annotation)
                labels.append(label)

        return bboxes, labels

    def adjust_bboxes_resize_img(self):
        """
        Adjust the bounding boxes of resize the images"""
        bboxes, labels = self.convert_bboxes_to_standard()

        for img_path in self.img_paths:
            image = Chitra(img_path, bboxes, labels)
            image.resize_image_with_bbox((640, 640))
            print('Rescaled bboxes:', image.bboxes)

if __name__ == "__main__":
    img_paths = [r'data/VN_traffic_sign_frames_video/Frames-Video for YOLO/Vietnam_video_traffic_sign/train/images/image_484.jpg']
    annotation_paths = [r'data\VN_traffic_sign_frames_video\Frames-Video for YOLO\Vietnam_video_traffic_sign\train\labels\image_484.txt']
    image_width = 1280
    image_height = 720

    adjust_bboxes = AdjustBoundingBoxes(img_paths, annotation_paths, image_width, image_height)
    adjust_bboxes.adjust_bboxes_resize_img()
