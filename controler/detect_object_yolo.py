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


def run_tracker_in_thread(filename: str, model, file_index):
    """
    Deject object in a sample video file using YOLOv8 model

    - filename: The path to the video file or the webcam/external
    camera source.
    - model: The file path to the YOLOv8 model.
    - file_index: An argument to specify the count of the
    file being processed.
    """

    video = cv2.VideoCapture(filename)  # Read the video file

    while True:
        ret, frame = video.read()  # Read the video frames

        # Exit the loop if no more frames in either video
        if not ret:
            break

        # Track objects in frames if available
        results = model.track(frame, persist=True)
        res_plotted = results[0].plot()
        cv2.imshow("Detect Object", res_plotted)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # Release video sources
    video.release()


def main():
    # Path to the video file
    video_file = r"video\video-YOLO.mp4"
    # Load the best weight of the YOLOv8 pre-trained model
    model = load_model(r"notebook\yolo-training-model-for-video\best.pt")
    tracker = threading.Thread(target=run_tracker_in_thread,
                               args=(video_file, model, 1),
                               daemon=True)
    tracker.start()
    tracker.join()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
