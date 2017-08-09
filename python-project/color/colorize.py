from PIL import Image, ImageDraw

# Square distance between 2 colors
def distance2(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

color_to_change = (0, 0, 255)

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
        if distance2(color_to_change, input_pixels[x, y]) < 230 ** 2:
            r = int(r * .5)
            g = int(g * 1.25)
            b = int(b * .5)
        draw.point((x, y), (r, g, b))

output_image.save("output.png")
