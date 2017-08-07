from PIL import Image, ImageDraw
from math import floor

# Load image:
input_image = Image.open("input.png")
input_pixels = input_image.load()

new_size = (300, 300)

# Create output image
output_image = Image.new("RGB", new_size)
draw = ImageDraw.Draw(output_image)

x_scale = input_image.width / output_image.width
y_scale = input_image.height / output_image.height

# Copy pixels
for x in range(output_image.width):
    for y in range(output_image.height):
        xp, yp = floor(x * x_scale), floor(y * y_scale)
        draw.point((x, y), input_pixels[xp, yp])

output_image.save("output.png")
