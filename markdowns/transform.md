# Crop

Let's start with a very simple operation: cropping. Cropping is the action to cut a part of the image to reframe it.

In order to crop an image, we need to copy in a new image the pixels we want to keep.  Let `origin` be the coordinate of upper-left corner and `end` the coordinate of the bottom-right corner. The pixel at coordinate `(x, y)` in the new image is equal to the pixel located at coordinate `(x + origin.x, y + origin.y)` in the old image.

@[Crop]({"stubs": ["crop/crop.py"], "command": "sh -c 'cp lena.png input.png && python3 crop/crop.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

# Scale

Scaling is used to change the size of the image. It can be a scale down or up. There are several methods available to interpolate the pixels. We will use the simplest possible algorithm: Nearest Neighbor. Feel free to implement other algorithms such as the Bilinear algorithm, Box sampling, Fourier transform...

To compute the rescaled image, we need the ratio for both horizontal and vertical axes: `x_ratio = old_img.x / new_img.x` and `y_ratio = old_img.y / new_img.y`. The pixel at coordinate `(x, y)` in the new image is equal to the pixel that is located at coordinate `(floor(x * x_ratio), floor(y * y_ratio))`.

@[Scale]({"stubs": ["crop/scale.py"], "command": "sh -c 'cp lena.png input.png && python3 crop/scale.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

# Flip

# Rotate
