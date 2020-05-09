import sys
from PIL import Image


class ImageConverter():
    """
      Convert Pillow Object
    """

    def __init__(self, img_obj):
        self.img_obj = img_obj

    def __repr__(self):
        return self.img_obj

    def resize_image_obj(self, new_width):
        """Resize image object with given width"""
        img_width, img_height = self.img_obj.size
        aspect_ratio = img_height/img_width
        new_height = aspect_ratio * new_width * 0.5
        self.img_obj = self.img_obj.resize((new_width, int(new_height)))

    def convert_to_greyscale(self):
        """Converts image object to greyscale"""
        self.img_obj = self.img_obj.convert('L')

    def get_pixel_info(self):
        """Returns image data"""
        return self.img_obj.getdata()


class AsciiGenerator():
    """
      Modify pixel list to chars
    """

    def __init__(self, pixel_list):
        self.pixel_list = pixel_list

    def get_chars(self):
        """Returns special characters that appear instead of pixels"""
        return [".", "&", "+", "1", "$", "*", "!", ":", ".", "[", "]", "{", "}"]

    def get_char_from_pixel(self):
        """Converts pixel values to special characters"""
        chars = self.get_chars()
        pixel_chars = [chars[pixel//30] for pixel in self.pixel_list]
        return ''.join(pixel_chars)

    def get_ascii_image(self, console_width):
        """Returns a ASCII image of the given width"""
        pixel_chars = self.get_char_from_pixel()
        char_pixels_count = len(pixel_chars)
        ascii_image = [pixel_chars[index:index + console_width]
                       for index in range(0, char_pixels_count, console_width)]
        return "\n".join(ascii_image)


def convert_img_to_ascii(image_path, width):
    """
    Converts image from path to ASCII string
    """
    img = Image.open(image_path)
    img_conv = ImageConverter(img)
    img_conv.resize_image_obj(width)
    img_conv.convert_to_greyscale()
    pixel_info = img_conv.get_pixel_info()
    return AsciiGenerator(pixel_info).get_ascii_image(width)


if __name__ == '__main__':

    CONSOLE_WIDTH = 100
    image_path = sys.argv[1]
    print(convert_img_to_ascii(image_path, CONSOLE_WIDTH))
