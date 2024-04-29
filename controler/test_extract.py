import cv2
import os

def extract_frame(video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get the total number of frames in the video
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Convert each frame to an image and save it
    for i in range(frame_count):
        ret, frame = video.read()
        if ret:
            image_path = os.path.join(output_folder, f"image{i}.jpg")
            cv2.imwrite(image_path, frame)

if __name__ == "__main__":
    video_path = "video2_RCNN.mp4"
    output_folder = "VN_traffic_sign_vid_data/Video for R-CNN/frames"
    extract_frame(video_path, output_folder)
