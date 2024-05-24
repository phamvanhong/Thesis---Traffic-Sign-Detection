import sys
sys.path.append(r"E:\Traffic_Sign_Detection Thesis\Thesis---Traffic-Sign-Detection")
from src.common.constans import *
from src.common.configs import *
import cv2
from ultralytics import YOLO


class  Detection:
    def __init__(self, model: str, video: str):
        """
        Initialize the Detection class with the model and video file
        Args:
            model (str): The pre-trained model file
            video (str): The video file to be processed
        """
        self.model = model
        self.video = video
    
    def load(self):
        """
        Load pre-trained model with the best weights file
        """
        model = YOLO(self.model)
        return model
    
    def detect(self):
        """
        Detect objects in a video using the YOLOv8 model
        """
        model = self.load()
        cap = cv2.VideoCapture(self.video)

        # Loop through the video frames
        while cap.isOpened():
            # Read a frame from the video
            success, frame = cap.read()

            if success:
                # Run YOLOv8 inference on the frame
                results = model(frame)

                # Visualize the results on the frame
                annotated_frame = results[0].plot()

                # Display the annotated frame
                cv2.imshow(YOLOV8_DETECTION, annotated_frame)

                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord(Q):
                    break
            else:
                # Break the loop if the end of the video is reached
                break

        # Release the video capture object and close the display window
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Path to the video file
    video_file = r"data\video\test video\test_video.mp4"
    # Load the best weight of the YOLOv8 pre-trained model
    model = r"notebook\yolo-training-model-for-video\Baseline weight\Small\best.pt"
    detection = Detection(model, video_file)
    detection.detect()