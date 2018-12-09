# Filtering

A lot of image processing algorithms rely on the convolution between a kernel (typicaly a 3x3 or 5x5 matrix) and an image. This may sound scary to some of you but that's not as difficult as it sounds:

Let's take a 3x3 matrix as our kernel. For each pixel, the filter multiplies the current pixel value and the other 8 surrounding pixels by the kernel corresponding value. Then it adds the result to get the value of the current pixel. Let's see an example:

![Matrix convolution](convolution.png)

In this example, the value of each pixel is equal to the double of the pixel that was located above it (e.g. 92 = 46 x 2).

# Blur

A simple blur can be done using this kernel: 

```math
\frac{1}{9}
\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}
```

This is called the Box Blur. Each pixel is computed as the average of the surrounding pixels.

And here is the kernel for the Gaussian Blur:

```math
\frac{1}{256}
\begin{bmatrix}
1 &  4 &  6 &  4 & 1 \\
4 & 16 & 24 & 16 & 4 \\
6 & 24 & 36 & 24 & 6 \\
4 & 16 & 24 & 16 & 4 \\
1 &  4 &  6 &  4 & 1 
\end{bmatrix}
```
As you can see, it's a weighted mean of the surrounding pixels that gives more weight to the pixel near the current pixel. This kind of filter is also called a low-pass filter.

@[Blur]({"stubs": ["edge/blur.py"], "command": "sh -c 'cp lena256.png input.png && python3 edge/blur.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

# Sharpening

The details of an image can be emphasized by using a high-pass filter:

```math
\begin{bmatrix}
0 & -0.5 & 0 \\
-0.5 & 3 & -0.5 \\
0 & -0.5 & 0
\end{bmatrix}
```

In this kernel, the pixel is boosted when the neighbor pixels are different.

@[Sharpening]({"stubs": ["edge/high-pass.py"], "command": "sh -c 'cp face.png input.png && python3 edge/high-pass.py && echo \"TECHIO> open -s /project/target/ index_512.html\"'"})

This filter can also be improved by applying the transformation only when the pixel is dark enough.

Another approach, called unsharp mask, consist in substracting from the original image a mask created using a low-pass filter. Basically, sharpening is realized by removed the blurry part of the image: $`sharpened = original + (original − blurred) × amount.`$

@[Unsharp Mask]({"stubs": ["edge/unsharp-mask.py"], "command": "sh -c 'cp face.png input.png && python3 edge/unsharp-mask.py && echo \"TECHIO> open -s /project/target/ index_512.html\"'"})

# Edge detection

There are multiple ways to do edge detection. We will present the Sobel Operator here.

The Sobel Operator uses two kernels (one for each direction): $`
K_x =
\begin{bmatrix}
-1 & 0 & 1 \\
-2 & 0 & 2 \\
-1 & 0 & 1
\end{bmatrix}
`$ and $`
K_y =
\begin{bmatrix}
-1 & -2 & -1 \\
 0 &  0 &  0 \\
 1 &  2 &  1
\end{bmatrix}
`$.

We compute the convolution between the image (converted in black and white) and the two kernels separately. That gives us, for each pixel, the values $`mag_x`$ and $`mag_y`$. The value of the current pixel is set at $`\sqrt{mag_x^2 + mag_y^2}`$.

@[Sobel operator]({"stubs": ["edge/sobel.py"], "command": "sh -c 'cp lena.png input.png && python3 edge/sobel.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})
