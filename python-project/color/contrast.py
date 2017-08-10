from PIL import Image, ImageDraw

# Square distance between 2 colors
def distance2(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

# Change this:
luminosity = 80

# Load image:
input_image = Image.open("input.png")
input_pixels = input_image.load()

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Find minimum and maximum luminosity
imin = 255
imax = 0
for x in range(input_image.width):
    for y in range(input_image.height):
        r, g, b = input_pixels[x, y]
        i = (r + g + b) / 3
        imin = min(imin, i)
        imax = max(imax, i)

# Generate image
for x in range(output_image.width):
    for y in range(output_image.height):
        r, g, b = input_pixels[x, y]
        # Current luminosity
        i = (r + g + b) / 3
        # New luminosity
        ip = 255 * (i - imin) / (imax - imin)
        r = int(r * ip / i)
        g = int(g * ip / i)
        b = int(b * ip / i)
        draw.point((x, y), (r, g, b))

output_image.save("output.png")
