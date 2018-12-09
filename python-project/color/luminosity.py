from PIL import Image, ImageDraw

# Change this:
luminosity = 80

# Load image:
input_image = Image.open("input.png")
input_pixels = input_image.load()

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Generate image
for x in range(output_image.width):
    for y in range(output_image.height):
        r, g, b = input_pixels[x, y]
        r = int(r + luminosity)
        g = int(g + luminosity)
        b = int(b + luminosity)
        draw.point((x, y), (r, g, b))

output_image.save("output.png")
