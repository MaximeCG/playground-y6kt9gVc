from PIL import Image, ImageDraw
from math import sqrt

# Load image:
inputImage = Image.open("input.png")
inputPixels = inputImage.load()

# Box Blur kernel
box_kernel = [[1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9]]

gaussian_kernel = [[1 / 256,  4  / 256,  6 / 256,   4 / 256, 1 / 256]
                   [4 / 256,  16 / 256, 24 / 256,  16 / 256, 4 / 256]
                   [6 / 256,  24 / 256, 36 / 256,  24 / 256, 6 / 256]
                   [4 / 256,  16 / 256, 24 / 256,  16 / 256, 4 / 256]
                   [1 / 256,  4  / 256,  6 / 256,   4 / 256, 1 / 256]]

kernel = box_kernel

# Create output image
outputImage = Image.new("RGB", inputImage.size)
draw = ImageDraw.Draw(outputImage)

# Compute convolution between intensity and kernels
for x in range(1, inputImage.width - 1):
    for y in range(1, inputImage.height - 1):
        acc = [0, 0 , 0]
        for a in range(len(kernel)):
            for b in range(len(kernel)):
                xn = x + a - 1
                yn = y + b - 1
                pixel = inputPixels[xn, yn]
                acc[0] += pixel[0] * kernel[a][b]
                acc[1] += pixel[1] * kernel[a][b]
                acc[2] += pixel[2] * kernel[a][b]

        draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))
    
outputImage.save("output.png")
