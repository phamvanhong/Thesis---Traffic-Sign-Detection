import os
from PIL import Image
import numpy as np

class DataAugment:
    def __init__(self, input_folder: str, output_folder: str):
        """
        Initialize the DataAugment class with the input and output folders
        Args:
            input_folder (str): The input folder containing images
            output_folder (str): The output folder to save processed images
        """
        self.input_folder = input_folder
        self.output_folder = output_folder
    
    def process_images(self, operation):
        """
        Process the images in the input folder with the specified operation
        Args:
            operation (function): The operation to apply on each image
        """
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        
        for filename in os.listdir(self.input_folder):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                img_path = os.path.join(self.input_folder, filename)
                
                # Apply the operation to the image
                processed_img = operation(img_path)
                
                output_img_path = os.path.join(self.output_folder, filename)
                processed_img.save(output_img_path)
    
    def resize(self, img_path):
        """
        Resize the input image to a smaller size (640x640)
        Args:
            img_path (str): The path to the input image
        Returns:
            PIL.Image.Image: The resized image
        """
        img = Image.open(img_path)
        return img.resize((640, 640))
    
    def add_noise(self, img_path):
        """
        Add noise to the input image
        Args:
            img_path (str): The path to the input image
        Returns:
            PIL.Image.Image: The image with added noise
        """
        img = Image.open(img_path)
        
        # Convert the image to numpy array
        img_arr = np.array(img)

        # Generate Gaussian noise
        noise = np.random.normal(0, 25, img_arr.shape).astype(np.uint8)

        # Add the noise to the image
        noisy_img_array = img_arr + noise

        # Ensure the noisy image array values are within the valid range (0-255)
        noisy_img_array = np.clip(noisy_img_array, 0, 255)

        # Convert the noisy image array back to an image
        return Image.fromarray(noisy_img_array)
        
if __name__ == "__main__":
    input_folder = r"data\VN_traffic_sign_frames_video\Frames-Video for YOLO\Vietnam_video_traffic_sign\test\images"
    output_folder = r"test_resize_data"
    data_augment = DataAugment(input_folder, output_folder)
    data_augment.process_images(data_augment.add_noise)
