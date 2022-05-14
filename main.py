from tkinter import filedialog
import numpy as np
import webbrowser
from PIL import Image
from check_pixel import check_pixel


LINE_SPACING_CORRECTION = 3


def combine_pixel(start_row, start_column, step, image):
    """Combine pixels on images that would create large ascii art."""
    total_pixels = 0
    for rows in range(0, step * 3):
        for columns in range(0, step):
            try:
                total_pixels += image[start_row + rows, start_column + columns]
            except IndexError:
                total_pixels += 0
    return total_pixels / ((step * 3) * step)


def turn_ascii(image):
    """Take an image and convert it to ascii art; create and open a text document with the art."""
    ascii_art_list = []
    basic_ascii_char = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]
    fancy_ascii_char = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`'. '''

    prompt = input('Would you like fancy (large and using more characters) or basic ascii art?\n'
                   'Basic art tends to render better on smaller sizes.\n'
                   'Enter "fancy" or "basic": ')
    if prompt == 'fancy':
        characters = fancy_ascii_char
    else:
        characters = basic_ascii_char

    file = Image.open(image)
    image = file.convert('L')
    gray_image = np.array(image)

    img_width = len(gray_image[0])
    img_height = len(gray_image)

    size_prompt = input(f'Do you want a full sized ascii image? (In this case {img_width} by {img_height} pixels.\n'
                        f'If not, we will reduce the image size so it is easier to see and copy.\n'
                        f'Type "yes" or "no": ')

    # create full sized ascii art
    if size_prompt == 'yes' or img_width < 80:
        for row in range(0, img_height, LINE_SPACING_CORRECTION):
            new_list = []
            for column in range(0, img_width):
                pixel = gray_image[row, column]
                check_pixel(pixel, new_list, characters)
            ascii_art_list.append(new_list)
    else:
        # combine pixels and print smaller ascii art
        step = round(img_width / 80)
        for row in range(0, img_height, step * LINE_SPACING_CORRECTION):
            new_list = []
            for column in range(0, img_width, step):
                pixel = combine_pixel(row, column, step, gray_image)
                check_pixel(pixel, new_list, characters)
            ascii_art_list.append(new_list)

    ascii_art = ""
    for row_list in ascii_art_list:
        ascii_art += "".join(row_list)
        ascii_art += "\n"

    return ascii_art


image_name = filedialog.askopenfilename(title="Select an image")
new_ascii = turn_ascii(image_name)

with open(f"{image_name}.txt", "w") as new_file:
    new_file.write(new_ascii)

webbrowser.open(f"{image_name}.txt")
