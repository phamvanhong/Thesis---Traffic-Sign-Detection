import sys
sys.path.append(r'E:\Traffic_Sign_Detection Thesis\Thesis---Traffic-Sign-Detection')
from src.common.constans import *
from src.common.configs import *
from src.model.data_augment import DataAugment


def main():
    train_data_folder = "data/VN_traffic_sign_frames_video/Frames-Video for YOLO/Vietnam_video_traffic_sign/train"
