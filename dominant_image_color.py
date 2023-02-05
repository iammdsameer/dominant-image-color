from collections import Counter
from PIL import Image

def get_color(path_to_image_file):
    # Open the image
    with Image.open(path_to_image_file) as img:
        # Convert the image to RGB format if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')
        # Get the pixel data
        pixels = img.getdata()
        # Count the number of times each color appears
        color_counts = Counter(pixels)
        # Get the most frequent color
        most_frequent = color_counts.most_common(1)[0][0]
        # Convert the RGB color to hex code
        hex_code = '#{:02x}{:02x}{:02x}'.format(*most_frequent)
        return hex_code