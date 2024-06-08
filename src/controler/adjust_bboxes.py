import sys
sys.path.append(r'E:\Traffic_Sign_Detection Thesis\Thesis---Traffic-Sign-Detection')
from src.common.constans import *
from src.common.configs import *
from src.model.resize_bboxes import AdjustBoundingBoxes
from src.model.get_path import FilePathCollector

def main():

    # set up 
    train_annotation_folder = r"speedlitmit80\labels"
    test_annotation_folder = r"data\VN_Traffic_Sign_Robo\test\labels"
    valid_annotation_folder = r"data\VN_Traffic_Sign_Robo\valid\labels"
    image_folder = r"data\VN_Traffic_Sign_Robo\train\images"
    # get annotation file paths
    annotations = FilePathCollector(image_folder, train_annotation_folder).get_annotation_path()
    
    # set up path
    resize = r"adjust_annotation\resize"
    blur = r"adjust_annotation\blur"
    noise = r"adjust_annotation\noise"
    high_contrast = r"adjust_annotation\high_contrast"
    low_contrast = r"adjust_annotation\low_contrast"
    darkness = r"adjust_annotation\darkness"
    brightness = r"adjust_annotation\brightness"

    #create annotation
    resize_adjust = AdjustBoundingBoxes(resize, annotations, 224, 224)
    resize_adjust.write_new_bboxes_to_annotations_file()

    blur_adjust = AdjustBoundingBoxes(blur, annotations, 224, 224)
    blur_adjust.write_new_bboxes_to_annotations_file()

    noise_adjust = AdjustBoundingBoxes(noise, annotations, 224, 224)
    noise_adjust.write_new_bboxes_to_annotations_file()

    high_contrast_adjust = AdjustBoundingBoxes(high_contrast, annotations, 224, 224)
    high_contrast_adjust.write_new_bboxes_to_annotations_file()

    low_contrast_adjust = AdjustBoundingBoxes(low_contrast, annotations, 224, 224)
    low_contrast_adjust.write_new_bboxes_to_annotations_file()

    darkness_adjust = AdjustBoundingBoxes(darkness, annotations, 224, 224)
    darkness_adjust.write_new_bboxes_to_annotations_file()

    brightness_adjust = AdjustBoundingBoxes(brightness, annotations, 224, 224)
    brightness_adjust.write_new_bboxes_to_annotations_file()


if __name__ == "__main__":
    main()
