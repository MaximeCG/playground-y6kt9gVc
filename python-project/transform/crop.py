from PIL import Image, ImageDraw

# Load image:
input_image = Image.open("input.png")
input_pixels = input_image.load()

# Cropped area
origin = (130, 150)
end = (400, 320)

# Create output image
output_image = Image.new("RGB", (end[0] - origin[0], end[1] - origin[1]))
draw = ImageDraw.Draw(output_image)

# Copy pixels
for x in range(output_image.width):
    for y in range(output_image.height):
        xp, yp = x + origin[0], y + origin[1]
        draw.point((x, y), input_pixels[xp, yp])

output_image.save("output.png")
