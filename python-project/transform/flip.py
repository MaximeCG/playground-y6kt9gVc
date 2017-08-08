from PIL import Image, ImageDraw

# Load image:
input_image = Image.open("input.png")
input_pixels = input_image.load()

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Copy pixels
for x in range(output_image.width):
    for y in range(output_image.height):
        xp = input_image.width - x - 1
        draw.point((x, y), input_pixels[xp, y])

output_image.save("output.png")
