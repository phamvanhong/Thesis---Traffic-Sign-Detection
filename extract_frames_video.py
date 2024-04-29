import cv2
import os


def get_frames(video_path: str, output_folder: str) -> None:
    """Extract frames from a video and save them in a folder

    Args:
        video_path (str): path to the video file
        output_folder (str): out folder to save the frames
    """
    cap = cv2.VideoCapture(video_path)
    i = 0

    # set number of frames to skip
    frame_skip = 1

    # a variable to keep track of the frame to be saved
    frame_count = 0

    # create if not have output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i > frame_skip - 1:
            frame_count += 1
            filename = os.path.join(output_folder, f'image_{
                                    frame_count * frame_skip}.jpg')
            cv2.imwrite(filename, frame)
            i = 0
            continue
        i += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # set video path and output folder (video 2 and video 3)
    video_path = "data/VN_traffic_sign_vid_data/sample videos/video2_RCNN.mp4"
    output_folder = "data/VN_traffic_sign_vid_data/Video for R-CNN/frame"
    get_frames(video_path, output_folder)
