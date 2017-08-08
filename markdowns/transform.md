# Crop

Let's start with a very simple operation: cropping. Cropping is the action to cut a part of the image to reframe it.

In order to crop an image, we need to copy in a new image the pixels we want to keep.  Let `origin` be the coordinate of upper-left corner and `end` the coordinate of the bottom-right corner. The pixel at coordinate `(x, y)` in the new image is equal to the pixel located at coordinate `(x + origin.x, y + origin.y)` in the old image.

@[Crop]({"stubs": ["transform/crop.py"], "command": "sh -c 'cp lena.png input.png && python3 transform/crop.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

# Scale

Scaling is used to change the size of the image. It can be a scale down or up. There are several methods available to interpolate the pixels. We will use the simplest possible algorithm: Nearest Neighbor. Feel free to implement other algorithms such as the Bilinear algorithm, Box sampling, Fourier transform...

To compute the rescaled image, we need the ratio for both horizontal and vertical axes: `x_ratio = old_img.x / new_img.x` and `y_ratio = old_img.y / new_img.y`. The pixel at coordinate `(x, y)` in the new image is equal to the pixel that is located at coordinate `(floor(x * x_ratio), floor(y * y_ratio))`.

@[Scale]({"stubs": ["transform/scale.py"], "command": "sh -c 'cp lena.png input.png && python3 transform/scale.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

# Flip

A flip (mirror effect) is done by reversing the pixels horizontally or vertically. For instance, for an horizontal flip, the pixel situated at coordinate (x, y) will be situated at coordinate (width - x - 1, y) in the new image.

@[Flip]({"stubs": ["transform/flip.py"], "command": "sh -c 'cp lena.png input.png && python3 transform/flip.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

# Rotate

The algorithm used for a rotation is similar to a flip: to compute the new image, we iterate over all the pixels and print the corresponding pixel from the source image.

The point situated at the coordinates (x, y) in the new image is equal to the point (xp, yp) in the input image:
```
xp = x * cos(angle) - y * sin(angle)
yp = x * sin(angle) + y * cos(angle)
```
If (xp, yp) is out of the input image, it is ignored (black pixel).

This can be used to do a rotation, however, the center of the rotation will be at coordinate (0, 0). In order to change the coordinates of the center of the rotation, we need to shift the coordinates before the rotation and after the rotation:

```
xp = (x - center_x) * cos(angle) - (y - center_y) * sin(angle) + center_x
yp = (x - center_x) * sin(angle) + (y - center_y) * cos(angle) + center_y
```

@[Rotate]({"stubs": ["transform/rotate.py"], "command": "sh -c 'cp lena.png input.png && python3 transform/rotate.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})
