import os
import shutil
import random


def split_dataset(input_folder, output_folder, train_ratio=0.7, test_ratio=0.15, valid_ratio=0.15):
    """Split a dataset into train, test, and validation sets

    Args:
        input_folder (_type_): input folder containing the dataset
        output_folder (_type_): output folder where the split datasets will be saved
        train_ratio (float, optional): ratio of the dataset to be used for training. Defaults to 0.7.
        test_ratio (float, optional): ratio  of the dataset to be used for testing. Defaults to 0.15.
        valid_ratio (float, optional): ratio of the dataset to be used for validation. Defaults to 0.15.
    """
    # Create output folders if they don't exist
    for folder in ['train', 'test', 'valid']:
        os.makedirs(os.path.join(output_folder, folder), exist_ok=True)

    # Get the list of image files
    image_files = [f for f in os.listdir(
        input_folder) if f.endswith('.jpg') or f.endswith('.png')]

    # Shuffle the list of image files
    random.shuffle(image_files)

    # Calculate the number of images for each split
    num_images = len(image_files)
    num_train = int(train_ratio * num_images)
    num_test = int(test_ratio * num_images)
    num_valid = num_images - num_train - num_test

    # Split the image files into train, test, and validation sets
    train_images = image_files[:num_train]
    test_images = image_files[num_train:num_train + num_test]
    valid_images = image_files[num_train + num_test:]

    # Copy images to their respective folders
    for img_file in train_images:
        shutil.copy(os.path.join(input_folder, img_file),
                    os.path.join(output_folder, 'train', img_file))
    for img_file in test_images:
        shutil.copy(os.path.join(input_folder, img_file),
                    os.path.join(output_folder, 'test', img_file))
    for img_file in valid_images:
        shutil.copy(os.path.join(input_folder, img_file),
                    os.path.join(output_folder, 'valid', img_file))

if __name__ == '__main__':
    input_folder = 'VN_traffic_sign_vid_data/Video for R-CNN/frames'
    output_folder = 'VN_traffic_sign_vid_data/Video for R-CNN/Vietnam_video_traffic_sign_rcnn'
    split_dataset(input_folder, output_folder)
