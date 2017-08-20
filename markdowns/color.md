# Luminosity

Changing the luminosity of a picture in a RGB mode can be done by adding a constant to each color component. However, this is a very simplified algorithm: the perceived luminosity has not an easy definition and there are several ways to estimate the luminosity of a pixel. Note that it is also possible to change from RGB to HSL to modify the luminosity easily.

@[]({"stubs": ["color/luminosity.py"], "command": "sh -c 'cp lena.png input.png && python3 color/luminosity.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

# Contrast

The contrast is the difference in brightness (or color) that makes the objects in a picture distinguishable. The intensity histogram of an image is the distribution of pixel luminance for an image. In order to improve the contrast, we can use a linear normalization of the intensity histogram:

$`I_N=(I-\text{Imin})\frac{255}{\text{Imax}-\text{Imin}}`$, where $`I_N`$ is the normalized pixel intensity, $`\text{Imin}`$ and $`\text{Imax}`$ are the minimum and maximum intensity (before normalization).

@[]({"stubs": ["color/contrast.py"], "command": "sh -c 'cp lena.png input.png && python3 color/contrast.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

# Colorize

In the previous example, we saw how to adjust the color of the pixels. This can be used to change the color balance for instance. In the next example, we detect the pixels whose color is close to blue (0, 0, 255) by computing a distance, and we reduce the value of the red and blue components and increase the green component.

@[]({"stubs": ["color/colorize.py"], "command": "sh -c 'cp lena.png input.png && python3 color/colorize.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

