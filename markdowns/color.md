# Luminosity

Changing the luminosity of a picture in a RGB mode can be done by multiplying the colors by a factor or by adding a constant. However, this is a very simplified algorithm: the perceived luminosity has not an easy definition and there are several ways to estimate the luminosity of a pixel. Note that it is also possible to change from RGB to HSL to modify the luminosity easily.

@[Scale]({"stubs": ["color/luminosity.py"], "command": "sh -c 'cp lena.png input.png && python3 color/luminosity.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

# Colorize

In the previous example, we saw how to adjust the color of the pixels. This can be used to change the color balance for instance. In the next example, we detect the pixels whose color is close to blue (0, 0, 255) by computing a distance, and we reduce the value of the red and blue components and increase the green component.

@[Scale]({"stubs": ["color/colorize.py"], "command": "sh -c 'cp lena.png input.png && python3 color/colorize.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

