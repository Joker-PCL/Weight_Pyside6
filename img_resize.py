import os
from PIL import Image

def crop_center(image, target_width, target_height):
    width, height = image.size
    left = (width - target_width) / 2
    top = (height - target_height) / 2
    right = (width + target_width) / 2
    bottom = (height + target_height) / 2

    return image.crop((left, top, right, bottom))

def resize_to_square(image_path, output_path, size):
    image = Image.open(image_path)
    width, height = image.size

    if width == height:
        image = image.resize((size, size))
    elif width > height:
        image = crop_center(image, height, height)
        image = image.resize((size, size))
    else:
        image = crop_center(image, width, width)
        image = image.resize((size, size))

    image.save(output_path)

def process_images_in_folder(folder_path, size):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                input_image_path = os.path.join(root, file)
                output_image_path = os.path.join(root, file)
                resize_to_square(input_image_path, output_image_path, size)
                print(f"Resized image saved to: {output_image_path}")

# Path to your main folder
main_folder_path = r"Product"
resize_size = 500  # Example size

# Process all images in all subfolders
process_images_in_folder(main_folder_path, resize_size)
