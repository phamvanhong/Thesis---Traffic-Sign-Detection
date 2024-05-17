from chitra.image import Chitra
import matplotlib.pyplot as plt

# Đường dẫn đến file annotation
annotation_file_path = r'data\VN_traffic_sign_frames_video\Frames-Video for YOLO\Vietnam_video_traffic_sign\test\labels\image_524.txt'

# Đường dẫn đến ảnh
img_path = r'data\VN_traffic_sign_frames_video\Frames-Video for YOLO\Vietnam_video_traffic_sign\test\images\image_524.jpg'

# Kích thước ảnh
image_width = 1280
image_height = 720

# Đọc file annotation
with open(annotation_file_path, 'r') as file:
    lines = file.readlines()

# Lưu trữ các bounding box và nhãn
bboxes = []
labels = []

# Xử lý từng dòng trong file annotation
for line in lines:
    # Tách dòng thành các phần tử
    elements = line.strip().split()

    # Lấy nhãn và annotation YOLO
    label = elements[0]
    yolo_annotation = list(map(float, elements[1:]))

    # Chuyển đổi annotation YOLO sang định dạng chuẩn
    center_x = yolo_annotation[0] * image_width
    center_y = yolo_annotation[1] * image_height
    box_width = yolo_annotation[2] * image_width
    box_height = yolo_annotation[3] * image_height

    top_left_x = center_x - box_width / 2
    top_left_y = center_y - box_height / 2
    bottom_right_x = center_x + box_width / 2
    bottom_right_y = center_y + box_height / 2

    # Định dạng chuẩn
    standard_annotation = [top_left_x, top_left_y, bottom_right_x, bottom_right_y]

    # Thêm bounding box và nhãn vào danh sách tương ứng
    bboxes.append(standard_annotation)
    labels.append(label)

# Tạo đối tượng Chitra với các bounding box và nhãn
image = Chitra(img_path, bboxes, labels)

# Thay đổi kích thước ảnh cùng với bounding box
#image.resize_image_with_bbox((640, 640))

# In bounding box đã thay đổi kích thước
print('Rescaled bboxes:', image.bboxes)

# Hiển thị ảnh với bounding box đã thay đổi kích thước
plt.imshow(image.draw_boxes())
plt.show()
