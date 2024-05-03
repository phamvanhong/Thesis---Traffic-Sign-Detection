import cv2
from ultralytics import YOLO
import threading


def load_model(model_name):
    """Load pre-trained YOLOv8 model with the best weights file

    Args:
        model_name (_type_): path to the best weights file
    """
    model = YOLO(model_name)  # Load YOLOv8 model with the best weights file
    return model


def detect_object(video_path: str, model: YOLO):
    """
    Detect objects in a video using the YOLOv8 model
    Args:
        video_path (str): path to the video file
        model (YOLO): YOLOv8 model
    
    """
    cap = cv2.VideoCapture(video_path)

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
            cv2.imshow("YOLOv8 Detection", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()

def main():
    # Path to the video file
    video_file = r"video\video-YOLO.mp4"
    # Load the best weight of the YOLOv8 pre-trained model
    model = load_model(r"notebook\yolo-training-model-for-video\64epoch_batch16\best.pt")
    detect_object(video_file, model)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
