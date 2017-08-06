from PIL import Image, ImageDraw
from math import sqrt

# Load image:
inputImage = Image.open("input.png")
inputPixels = inputImage.load()

# Calculate pixel intensity as the average of red, green and blue colors.
intensity = [[sum(inputPixels[x, y]) / 3 for y in range(inputImage.height)] for x in range(inputImage.width)]

# Sobel kernels
kernelx = [[-1, 0, 1],
           [-2, 0, 2],
           [-1, 0, 1]]
kernely = [[-1, -2, -1],
           [0, 0, 0],
           [1, 2, 1]]

# Create output image
outputImage = Image.new("RGB", inputImage.size)
draw = ImageDraw.Draw(outputImage)

# Compute convolution between intensity and kernels
for x in range(1, inputImage.width - 1):
    for y in range(1, inputImage.height - 1):
        magx, magy = 0, 0
        for a in range(3):
            for b in range(3):
                xn = x + a - 1
                yn = y + b - 1
                magx += intensity[xn][yn] * kernelx[a][b]
                magy += intensity[xn][yn] * kernely[a][b]

        # Draw in black and white the magnitude
        color = int(sqrt(magx**2 + magy**2))
        draw.point((x, y), (color, color, color))
    
outputImage.save("output.png")
