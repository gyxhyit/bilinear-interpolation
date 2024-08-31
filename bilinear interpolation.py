import numpy as np
from PIL import Image


def double_linear(image_path, output_path, scale):
    img = np.array(Image.open(image_path))
    width, height, _ = img.shape
    n_width = int(width * scale)
    n_height = int(height * scale)
    n_img = np.zeros((n_width, n_height, 3))

    for k in range(3):
        for i in range(n_width):
            for j in range(n_height):
                src_x = i / scale
                src_y = j / scale
                src_x_0 = int(np.floor(src_x))
                src_y_0 = int(np.floor(src_y))
                src_x_1 = min(src_x_0 + 1, width - 1)
                src_y_1 = min(src_y_0 + 1, height - 1)

                value0 = (src_x_1 - src_x) * img[src_x_0, src_y_0, k] + (src_x - src_x_0) * img[src_x_1, src_y_0, k]
                value1 = (src_x_1 - src_x) * img[src_x_0, src_y_1, k] + (src_x - src_x_0) * img[src_x_1, src_y_1, k]
                n_img[i, j, k] = int((src_y_1 - src_y) * value0 + (src_y - src_y_0) * value1)

    result_img = Image.fromarray(np.uint8(n_img))
    result_img.save(output_path)


# Example usage:
default_image_path = 'C:/Users/admin/Desktop/999.jpg'
default_output_path = 'default_output_path.jpg'
scale_factor = 2

double_linear(default_image_path, default_output_path, scale_factor)