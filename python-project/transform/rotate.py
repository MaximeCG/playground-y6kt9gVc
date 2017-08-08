from PIL import Image, ImageDraw
from math import sin, cos, pi


# Load image:
input_image = Image.open("input.png")
input_pixels = input_image.load()

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

angle = pi / 3  # angle in radian
center_x = input_image.width / 2
center_y = input_image.height / 2

# Copy pixels
for x in range(input_image.width):
    for y in range(input_image.height):
        # Compute coordinate in input image
        xp = int((x - center_x) * cos(angle) - (y - center_y) * sin(angle) + center_x)
        yp = int((x - center_x) * sin(angle) + (y - center_y) * cos(angle) + center_y)
        if 0 <= xp < input_image.width and 0 <= yp < input_image.height:
            draw.point((x, y), input_pixels[xp, yp])

output_image.save("output.png")
