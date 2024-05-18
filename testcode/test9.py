import sys
sys.path.append(r'E:\Traffic_Sign_Detection Thesis\Thesis---Traffic-Sign-Detection')
import cv2
import numpy as np
from src.model.read_write import ReadWriteFile
from src.model.resize_bboxes import AdjustBoundingBoxes


annotation_file_paths = [r"data\VN_traffic_sign_frames_video\Frames-Video for YOLO\Vietnam_video_traffic_sign\test\labels\image_4.txt"]
folder_path = "tessttxt"
for file in annotation_file_paths:
    lines = ReadWriteFile(file, folder_path).read_lines_in_file()
    for line in lines:
        bbox = line.strip('\n').split(' ')
        yolo_annotation = list(map(float, bbox[1:]))
        coner = AdjustBoundingBoxes().calculate_center_and_size(yolo_annotation)
        for i in coner:
            print(i)
