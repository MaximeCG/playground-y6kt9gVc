# Filtering

A lot of image processing algorithms rely on the convolution between a kernel (typicaly a 3x3 or 5x5 matrix) and an image. This may sound scary to some of you but that's not as difficult as it sounds:

Let's take a 3x3 matrix as our kernel. For each pixel, the filter multiplies the current pixel value and the other 8 surrounding pixels by the kernel corresponding value. Then it adds the result to get the value of the current pixel. That's all. Let's see an example:

![Matrix convolution](convolution.png)

## Edge detection

@[Sobel operator]({"stubs": ["edge/sobel.py"], "command": "sh -c 'cp lena.png input.png && python3 edge/sobel.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})
