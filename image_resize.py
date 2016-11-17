from PIL import Image
import argparse
import os


def resize_image(path_to_original, input_width, input_height, input_scale):
    image = get_image(path_to_original)
    if input_width is not None or input_height is not None:
        width_new, height_new = get_calculated_width_height_dimensions(image, input_width, input_height)
    elif input_scale is not None:
        width_new, height_new = get_calculated_scale_dimensions(image, input_scale)
    return image.resize((int(width_new), int(height_new)), Image.ANTIALIAS)


def save_new_image(path_to_result, image, image_name):
    result_width, result_height = image.size
    image_name = image_name.replace(".", "_{0}x{1}.".format(result_width, result_height))
    path_to_result = "{0}\{1}".format(path_to_result, image_name)
    image.save(path_to_result)
    print("New image created and saved in {}".format(path_to_result))


def get_image(path_to_original):
    try:
        return Image.open(path_to_original)
    except IOError:
        print("cannot convert", path_to_original)


def get_calculated_width_height_dimensions(image, orig_width, orig_height):
    original_width, original_height = image.size
    if orig_width is None:
        width_new = float(orig_height) * (original_width / original_height)
        return width_new, float(orig_height)
    elif orig_height is None:
        height_new = float(orig_width) * (original_height / original_width)
        return float(orig_width), height_new
    else:
        return float(orig_width), float(orig_height)


def get_calculated_scale_dimensions(image, scale):
    scale = float(scale)
    width_new, height_new = image.size
    width_new *= scale
    height_new *= scale
    return width_new, height_new


def get_path_to_image(image_path):
    if not os.path.exists(image_path):
        print("Image '{}' is not exists!".format(image_path))
        exit()
    return image_path


def get_path_to_result_folder(result_path, original_path):
    if result_path is None:
        return original_path
    return result_path


def check_input_params(input_width, input_height, input_scale):
    if input_scale is None and (input_width is not None or input_height is not None):
        return None
    elif input_scale and (input_width is not None or input_height is not None):
        print("Width and height can't be used with scale params!")
        exit()


def get_command_line_arguments():
    parser = argparse.ArgumentParser(description='Image resize parameters.')
    parser.add_argument('-image', help='Path to image.', required=True)
    parser.add_argument('-width', help='Width to be changed.', required=False)
    parser.add_argument('-height', help='Height to be changed.', required=False)
    parser.add_argument('-scale', help='Scale. Can\'t be used if width or height are defined.', required=False)
    parser.add_argument('-output', help='Path where new file will be saved. '
                                        'By default file will be saved near the image path.', required=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = get_command_line_arguments()
    path_to_original_img = get_path_to_image(args.image)
    original_dir_name, original_image_name = os.path.split(path_to_original_img)
    width = args.width
    height = args.height
    scale = args.scale
    path_to_result_img = get_path_to_result_folder(args.output, original_dir_name)
    check_input_params(width, height, scale)
    result_image = resize_image(path_to_original_img, width, height, scale)
    save_new_image(path_to_result_img, result_image, original_image_name)
