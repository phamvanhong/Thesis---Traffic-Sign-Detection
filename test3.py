from PIL import Image
import os

def resize_images(img_folder, output_folder, new_size=(640, 640)):
    # Tạo thư mục đầu ra nếu nó không tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lặp qua tất cả các file trong thư mục hình ảnh
    for filename in os.listdir(img_folder):
        # Kiểm tra nếu đó là file hình ảnh
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Tạo đường dẫn đầy đủ đến file hình ảnh
            img_path = os.path.join(img_folder, filename)

            # Mở hình ảnh
            img = Image.open(img_path)

            # Thay đổi kích thước hình ảnh
            resized_img = img.resize(new_size)

            # Tạo đường dẫn đầy đủ đến file hình ảnh đầu ra
            output_img_path = os.path.join(output_folder, filename)

            # Lưu hình ảnh đã thay đổi kích thước
            resized_img.save(output_img_path)

# Sử dụng hàm
input_folder = r"data\VN_traffic_sign_frames_video\Frames-Video for YOLO\Vietnam_video_traffic_sign\test\images"
output_folder = r"test_resize_data"
resize_images(input_folder, output_folder, new_size=(640, 640))
